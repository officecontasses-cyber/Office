/**
 * atualizarReinfDP.gs — atualiza a planilha "CONTROLE | DP REINF'S" a partir de uma fila colada em TSV,
 * no mesmo modelo da fila "Atualizações" da Controle_Fiscal. Instalar no Apps Script da planilha do DP.
 *
 * Como usar (todo mês):
 *  1. Rodar prepararAbaAtualizacoesReinf() uma vez: cria a aba "Atualizações REINF" com o cabeçalho.
 *  2. Colar o TSV (sem cabeçalho) na aba, a partir da linha 2. Colunas (8):
 *       A Nº | B aba | C Status | D Observação | E Detalhe | F Rótulo caixa | G Valor caixa | H Processado (deixar em branco)
 *     - B aba: nome exato da aba de destino, p.ex. "MOD GERAL 09.2026".
 *     - C Status vai para a coluna D da aba de destino (Enviado, Pendente...). Vazio = não mexe.
 *     - D Observação vai para a coluna E (Sem movimento / COM RETENÇÃO). Vazio = não mexe.
 *     - E Detalhe vai para a coluna F. O texto "\n" vira quebra de linha. Se começar com "+", acrescenta
 *       ao texto que já existe na célula (em nova linha) em vez de substituir.
 *     - F e G (opcionais): preenchem a caixa de valores ao lado (rótulo na coluna H, valor na coluna I da
 *       aba de destino), p.ex. rótulo "COD 6190 COSIRF S/SERVIÇOS" e valor 1534,82. A linha da caixa é
 *       achada pelo texto do rótulo; sem rótulo igual, avisa e não escreve.
 *  3. Rodar processarAtualizacoesReinf(). Cada linha é marcada em H (OK, já preenchido, não encontrada...).
 *
 * Regras de segurança:
 *  - A linha do cliente é achada pelo Nº (coluna A) com Obrigação (coluna C) começando por "REINF".
 *    Cliente sem linha na aba: só é criado no fim da lista se CRIAR_LINHA_SE_NAO_EXISTIR = true.
 *  - Não sobrescreve célula já preenchida (exceto modelo vazio, como "IRRF (Cód. Rec. 170806): R$ ");
 *    nesse caso marca "Já preenchido" em H. FORCAR_SOBRESCRITA = true libera a troca.
 *  - Não mexe nas colunas B, C e G (o "ok" do DP) da aba de destino.
 *  - Pode ser repetido: linha com H preenchido não é processada de novo.
 */

const REINF_DP = {
  ABA_FILA: 'Atualizações REINF',
  CABECALHO: ['Nº', 'aba', 'Status', 'Observação', 'Detalhe', 'Rótulo caixa', 'Valor caixa', 'Processado'],
  // colunas da aba de destino (1 = A)
  D_NUM: 1, D_EMPRESA: 2, D_OBRIG: 3, D_STATUS: 4, D_OBS: 5, D_DET: 6, D_ROTULO: 8, D_VALOR: 9,
  CRIAR_LINHA_SE_NAO_EXISTIR: false,
  FORCAR_SOBRESCRITA: false,
  FORMATO_VALOR: '"R$" #,##0.00'
};

function prepararAbaAtualizacoesReinf() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(REINF_DP.ABA_FILA);
  if (!sh) sh = ss.insertSheet(REINF_DP.ABA_FILA);
  sh.getRange(1, 1, 1, REINF_DP.CABECALHO.length).setValues([REINF_DP.CABECALHO]).setFontWeight('bold');
  sh.setFrozenRows(1);
  sh.getRange(2, 1, 1000, 5).setNumberFormat('@');          // texto: não deixa "1/10" virar data
  sh.getRange(2, 6, 1000, 1).setNumberFormat('@');
  SpreadsheetApp.getUi().alert('Aba "' + REINF_DP.ABA_FILA + '" pronta. Cole o TSV a partir da linha 2 e rode processarAtualizacoesReinf().');
}

function processarAtualizacoesReinf() {
  const C = REINF_DP;
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const fila = ss.getSheetByName(C.ABA_FILA);
  if (!fila) { _reinfAviso_('Aba "' + C.ABA_FILA + '" não existe. Rode prepararAbaAtualizacoesReinf() primeiro.'); return; }
  const ultima = fila.getLastRow();
  if (ultima < 2) { _reinfAviso_('Fila vazia.'); return; }

  const dados = fila.getRange(2, 1, ultima - 1, C.CABECALHO.length).getValues();
  const agora = Utilities.formatDate(new Date(), ss.getSpreadsheetTimeZone(), 'dd/MM/yyyy HH:mm');
  const resumo = { ok: 0, ja: 0, naoAchou: 0, erro: 0 };

  dados.forEach(function (lin, i) {
    const linhaFila = i + 2;
    const marca = String(lin[7] || '').trim();
    const num = String(lin[0] || '').trim().replace(/^0+/, '');
    if (marca || !num) return;                                  // já processada ou linha em branco

    const nomeAba = String(lin[1] || '').trim();
    const sh = ss.getSheetByName(nomeAba);
    if (!sh) { fila.getRange(linhaFila, 8).setValue('ERRO: aba "' + nomeAba + '" não existe'); resumo.erro++; return; }

    let linhaDest = _reinfAcharLinha_(sh, num);
    if (!linhaDest) {
      if (C.CRIAR_LINHA_SE_NAO_EXISTIR) linhaDest = _reinfCriarLinha_(sh, num);
      else { fila.getRange(linhaFila, 8).setValue('Cliente ' + num + ' sem linha REINF na aba (nada gravado)'); resumo.naoAchou++; return; }
    }

    const msgs = [];
    let barrou = false;
    const status = String(lin[2] || '').trim();
    const obs = String(lin[3] || '').trim();
    const det = String(lin[4] || '').replace(/\\n/g, '\n');
    if (status) barrou = _reinfGravar_(sh.getRange(linhaDest, C.D_STATUS), status, msgs, 'Status') || barrou;
    if (obs) barrou = _reinfGravar_(sh.getRange(linhaDest, C.D_OBS), obs, msgs, 'Observação') || barrou;
    if (String(lin[4] || '').trim()) {
      const cel = sh.getRange(linhaDest, C.D_DET);
      if (det.charAt(0) === '+') {
        const atual = String(cel.getValue() || '').trim();
        const novo = det.substring(1).trim();
        if (atual.indexOf(novo) === -1) cel.setValue(atual ? atual + '\n' + novo : novo);
        msgs.push('Detalhe acrescentado');
      } else {
        barrou = _reinfGravar_(cel, det, msgs, 'Detalhe') || barrou;
      }
    }
    const rotulo = String(lin[5] || '').trim();
    if (rotulo) {
      const lr = _reinfAcharRotulo_(sh, rotulo);
      if (!lr) { msgs.push('rótulo "' + rotulo + '" não achado'); barrou = true; }
      else {
        const v = lin[6];
        const num2 = (typeof v === 'number') ? v : parseFloat(String(v).replace(/[^\d,.-]/g, '').replace(/\./g, '').replace(',', '.'));
        const cel = sh.getRange(lr, C.D_VALOR);
        if (isNaN(num2)) { msgs.push('valor inválido para "' + rotulo + '"'); barrou = true; }
        else if (!_reinfPodeSobrescrever_(cel.getValue()) && Math.abs(_reinfNumero_(cel.getValue()) - num2) > 0.004) {
          msgs.push('caixa "' + rotulo + '" já tem ' + cel.getDisplayValue()); barrou = true;
        } else { cel.setValue(num2).setNumberFormat(C.FORMATO_VALOR); msgs.push('caixa "' + rotulo + '" ok'); }
      }
    }
    fila.getRange(linhaFila, 8).setValue((barrou ? 'Parcial/Já preenchido: ' : 'OK ') + agora + ' — ' + msgs.join('; '));
    if (barrou) resumo.ja++; else resumo.ok++;
  });

  _reinfAviso_('Fila processada.\nOK: ' + resumo.ok + '\nJá preenchido/parcial: ' + resumo.ja +
               '\nCliente sem linha na aba: ' + resumo.naoAchou + '\nErro: ' + resumo.erro +
               '\nVeja a coluna H da aba "' + C.ABA_FILA + '".');
}

// ---------------------------------------------------------------- auxiliares

function _reinfAcharLinha_(sh, num) {
  const C = REINF_DP;
  const ultima = sh.getLastRow();
  if (ultima < 2) return 0;
  const v = sh.getRange(2, 1, ultima - 1, 3).getValues();
  for (let i = 0; i < v.length; i++) {
    const n = String(v[i][0]).trim().replace(/^0+/, '').replace(/\.0$/, '');
    if (n === num && String(v[i][2]).trim().toUpperCase().indexOf('REINF') === 0) return i + 2;
  }
  return 0;
}

function _reinfCriarLinha_(sh, num) {
  const C = REINF_DP;
  const v = sh.getRange(1, 1, Math.max(sh.getLastRow(), 2), 1).getValues();
  let ult = 1;
  for (let i = 0; i < v.length; i++) if (String(v[i][0]).trim() !== '') ult = i + 1;
  const nova = ult + 1;
  sh.getRange(nova, C.D_NUM).setValue(Number(num));
  sh.getRange(nova, C.D_OBRIG).setValue('REINF');
  return nova;
}

function _reinfAcharRotulo_(sh, rotulo) {
  const C = REINF_DP;
  const ultima = sh.getLastRow();
  if (ultima < 2) return 0;
  const alvo = _reinfNorm_(rotulo);
  const v = sh.getRange(2, C.D_ROTULO, ultima - 1, 1).getValues();
  for (let i = 0; i < v.length; i++) if (_reinfNorm_(v[i][0]) === alvo) return i + 2;
  return 0;
}

function _reinfNorm_(s) { return String(s || '').replace(/\s+/g, ' ').trim().toUpperCase(); }

function _reinfNumero_(v) {
  if (typeof v === 'number') return v;
  const n = parseFloat(String(v || '').replace(/[^\d,.-]/g, '').replace(/\./g, '').replace(',', '.'));
  return isNaN(n) ? 0 : n;
}

// vazio ou modelo sem valor ("... R$ ") pode ser trocado sem pergunta
function _reinfPodeSobrescrever_(atual) {
  if (REINF_DP.FORCAR_SOBRESCRITA) return true;
  const t = String(atual === null || atual === undefined ? '' : atual).trim();
  if (t === '') return true;
  const semModelo = t.split('\n').every(function (l) { return /R\$\s*$/.test(l.trim()) || l.trim() === ''; });
  return semModelo;
}

// devolve true quando NÃO gravou (célula já preenchida com outro valor)
function _reinfGravar_(cel, valor, msgs, nome) {
  const atual = String(cel.getValue() === null ? '' : cel.getValue()).trim();
  if (atual === String(valor).trim()) { msgs.push(nome + ' já estava igual'); return false; }
  if (_reinfPodeSobrescrever_(atual)) { cel.setValue(valor); msgs.push(nome + ' gravado'); return false; }
  msgs.push(nome + ' já preenchido ("' + atual.substring(0, 40) + '")');
  return true;
}

function _reinfAviso_(texto) {
  try { SpreadsheetApp.getUi().alert(texto); } catch (e) { Logger.log(texto); }
}
