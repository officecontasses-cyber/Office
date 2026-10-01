/**
 * criarAbaSet2026.gs — cria a aba de competência 09/2026 (Set2026) na Controle_Fiscal.
 *
 * O que faz
 *  - Copia a aba Ago2026 inteira (layout, larguras, painel congelado, formatação condicional,
 *    lista de feriados da coluna P) para uma aba nova chamada Set2026, posicionada à esquerda.
 *  - Mantém as colunas estruturais: A Município/UF, B CNPJ, C Nº, D Empresa, E Obrigação,
 *    L Contribuinte ICMS, M Regime Tributário.
 *  - Zera as colunas de movimento: F Data, G Valor, H Status, K Observações, N Fechamento Concluído?.
 *    Exceção: a Observação da linha CERTIFICADO DIGITAL é fixa por cliente e é mantida.
 *  - Recria Prazo (I) e Dias p/ Vencer (J) com fórmula em todas as linhas. O prazo só aparece na
 *    linha SPED CONTRIBUIÇÕES: 10º dia útil do 2º mês seguinte à competência (09/2026 -> novembro),
 *    descontados os feriados de P2:P8. Resultado esperado: 16/11/2026.
 *
 * O que NÃO faz
 *  - Não toca em Ago2026, Jul2026, Atualizações nem Cadastro_Clientes.
 *  - Não define nenhum Status. As linhas nascem em branco e passam a Pendente/Enviado/etc. pelo
 *    pipeline normal (aba Atualizações + processarAtualizacoes), com confirmação da Fernanda.
 *  - Não cria linhas novas (por exemplo DARF IRPJ/CSLL trimestral dos clientes Presumido).
 *    A estrutura é idêntica à de Ago2026.
 *
 * Segurança: se Set2026 já existir, o script para sem alterar nada.
 *
 * Como usar: colar no editor do Apps Script da Controle_Fiscal, executar criarAbaSet2026()
 * e depois verificarAbaSet2026() para conferir.
 */

const SET2026 = {
  ORIGEM: 'Ago2026',
  DESTINO: 'Set2026',
  ANO: 2026,
  MES_COMPETENCIA: 9,            // 09/2026
  COL_FERIADOS_RANGE: '$P$2:$P$8',
  COLS_LIMPAR: [6, 7, 8, 14],    // F Data, G Valor, H Status, N Fechamento Concluído?
  COL_OBS: 11,                   // K Observações
  COL_OBRIGACAO: 5,              // E
  COL_NUM: 3,                    // C
  COL_PRAZO: 9,                  // I
  COL_DIAS: 10,                  // J
  OBRIGACAO_FIXA_OBS: 'CERTIFICADO DIGITAL',
  OBRIGACAO_SPED: 'SPED CONTRIBUIÇÕES'
};

function criarAbaSet2026() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  if (ss.getSheetByName(SET2026.DESTINO)) {
    _avisoSet2026_('A aba ' + SET2026.DESTINO + ' já existe. Nada foi alterado.');
    return;
  }
  const origem = ss.getSheetByName(SET2026.ORIGEM);
  if (!origem) {
    _avisoSet2026_('Aba de origem ' + SET2026.ORIGEM + ' não encontrada. Nada foi alterado.');
    return;
  }

  // 1) Copia a aba inteira (formatação, larguras, painel congelado, formatação condicional, feriados).
  const destino = origem.copyTo(ss);
  destino.setName(SET2026.DESTINO);
  ss.setActiveSheet(destino);
  ss.moveActiveSheet(1);

  // 2) Descobre a última linha de dados pela coluna Nº.
  const ultima = _ultimaLinhaDadosSet2026_(destino);
  if (ultima < 2) throw new Error('Nenhuma linha de dados encontrada em ' + SET2026.ORIGEM);
  const n = ultima - 1;

  // 3) Zera as colunas de movimento (mantém formatação).
  SET2026.COLS_LIMPAR.forEach(function (c) {
    destino.getRange(2, c, n, 1).clearContent();
  });

  // 4) Observações: zera, exceto a linha fixa de CERTIFICADO DIGITAL.
  const obrig = destino.getRange(2, SET2026.COL_OBRIGACAO, n, 1).getValues();
  const obsAtual = destino.getRange(2, SET2026.COL_OBS, n, 1).getValues();
  const obsNova = obsAtual.map(function (linha, i) {
    return [String(obrig[i][0]).trim() === SET2026.OBRIGACAO_FIXA_OBS ? linha[0] : ''];
  });
  destino.getRange(2, SET2026.COL_OBS, n, 1).setValues(obsNova);

  // 5) Prazo (I) e Dias p/ Vencer (J) por fórmula em todas as linhas.
  //    10º dia útil do 2º mês seguinte: DATE(ano, mesCompetencia + 2, 1) - 1 é o último dia do mês anterior.
  const baseSped = 'DATE(' + SET2026.ANO + ',' + (SET2026.MES_COMPETENCIA + 2) + ',1)-1';
  const fPrazo = [];
  const fDias = [];
  for (let r = 2; r <= ultima; r++) {
    fPrazo.push(['=IF(AND($E' + r + '="' + SET2026.OBRIGACAO_SPED + '",$H' + r + '<>"NÃO SE APLICA"),' +
      'WORKDAY.INTL(' + baseSped + ',10,1,' + SET2026.COL_FERIADOS_RANGE + '),"")']);
    fDias.push(['=IF($I' + r + '="","",$I' + r + '-TODAY())']);
  }
  destino.getRange(2, SET2026.COL_PRAZO, n, 1).setFormulas(fPrazo).setNumberFormat('dd/mm/yyyy');
  destino.getRange(2, SET2026.COL_DIAS, n, 1).setFormulas(fDias).setNumberFormat('0');

  SpreadsheetApp.flush();
  _avisoSet2026_('Aba ' + SET2026.DESTINO + ' criada a partir de ' + SET2026.ORIGEM + ': ' + n +
    ' linhas, status em branco. Rode verificarAbaSet2026() para conferir.');
}

/** Conferência pós-criação (somente leitura). Resultado no Logger e em alerta. */
function verificarAbaSet2026() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const o = ss.getSheetByName(SET2026.ORIGEM);
  const d = ss.getSheetByName(SET2026.DESTINO);
  if (!o || !d) { _avisoSet2026_('Falta a aba ' + (o ? SET2026.DESTINO : SET2026.ORIGEM) + '.'); return; }

  const uo = _ultimaLinhaDadosSet2026_(o);
  const ud = _ultimaLinhaDadosSet2026_(d);
  const problemas = [];
  if (uo !== ud) problemas.push('Quantidade de linhas difere: ' + SET2026.ORIGEM + '=' + (uo - 1) + ', ' + SET2026.DESTINO + '=' + (ud - 1));

  const n = Math.min(uo, ud) - 1;
  const estruturais = [1, 2, 3, 4, 5, 12, 13]; // A B C D E L M
  estruturais.forEach(function (c) {
    const vo = o.getRange(2, c, n, 1).getValues();
    const vd = d.getRange(2, c, n, 1).getValues();
    for (let i = 0; i < n; i++) {
      if (String(vo[i][0]) !== String(vd[i][0])) { problemas.push('Coluna ' + c + ' linha ' + (i + 2) + ' difere'); break; }
    }
  });

  [6, 7, 8, 14].forEach(function (c) {
    const preenchidas = d.getRange(2, c, n, 1).getValues().filter(function (x) { return x[0] !== ''; }).length;
    if (preenchidas) problemas.push('Coluna ' + c + ' ainda tem ' + preenchidas + ' células preenchidas');
  });

  const vals = d.getRange(2, 1, n, SET2026.COL_DIAS).getDisplayValues();
  const sped = vals.filter(function (l) { return l[SET2026.COL_OBRIGACAO - 1] === SET2026.OBRIGACAO_SPED; });
  const prazos = {};
  sped.forEach(function (l) { prazos[l[SET2026.COL_PRAZO - 1]] = (prazos[l[SET2026.COL_PRAZO - 1]] || 0) + 1; });
  const erros = vals.filter(function (l) { return String(l[SET2026.COL_PRAZO - 1]).indexOf('#') === 0 || String(l[SET2026.COL_DIAS - 1]).indexOf('#') === 0; }).length;
  if (erros) problemas.push(erros + ' linhas com erro em Prazo/Dias');

  const clientes = {};
  d.getRange(2, SET2026.COL_NUM, n, 1).getValues().forEach(function (x) { clientes[parseInt(x[0], 10)] = true; });

  const msg = 'Linhas: ' + n + ' | Clientes: ' + Object.keys(clientes).length +
    ' | Linhas SPED: ' + sped.length + ' | Prazos SPED: ' + JSON.stringify(prazos) +
    (problemas.length ? '\nPROBLEMAS:\n- ' + problemas.join('\n- ') : '\nSem problemas encontrados.');
  Logger.log(msg);
  _avisoSet2026_(msg);
}

function _ultimaLinhaDadosSet2026_(sheet) {
  const vals = sheet.getRange(2, SET2026.COL_NUM, Math.max(sheet.getMaxRows() - 1, 1), 1).getValues();
  let ultima = 1;
  for (let i = 0; i < vals.length; i++) {
    if (vals[i][0] !== '' && vals[i][0] !== null) ultima = i + 2;
  }
  return ultima;
}

function _avisoSet2026_(msg) {
  Logger.log(msg);
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) { /* execução sem interface */ }
}

/**
 * Corrige Prazo (I) e Dias p/ Vencer (J) da Set2026 quando as fórmulas gravadas por
 * criarAbaSet2026() resultam em #ERROR! (suspeita: sintaxe de fórmula x configuração regional).
 * Testa variantes de sintaxe na primeira linha SPED e só aplica a que calcular certo
 * (16/11/2026 para a competência 09/2026). Se nenhuma funcionar, grava a data como valor fixo.
 * Mexe apenas nas colunas I e J da Set2026.
 */
function corrigirPrazosSet2026() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const d = ss.getSheetByName(SET2026.DESTINO);
  if (!d) { _avisoSet2026_('Aba ' + SET2026.DESTINO + ' não encontrada.'); return; }
  const ultima = _ultimaLinhaDadosSet2026_(d);
  const n = ultima - 1;
  const obrig = d.getRange(2, SET2026.COL_OBRIGACAO, n, 1).getValues();
  let r0 = 0;
  for (let i = 0; i < n; i++) {
    if (String(obrig[i][0]).trim() === SET2026.OBRIGACAO_SPED) { r0 = i + 2; break; }
  }
  if (!r0) { _avisoSet2026_('Nenhuma linha SPED CONTRIBUIÇÕES encontrada.'); return; }

  const tz = ss.getSpreadsheetTimeZone();
  const mesSped = SET2026.MES_COMPETENCIA + 2;
  const feriados = d.getRange(2, 16, 7, 1).getValues()
    .filter(function (x) { return x[0] instanceof Date; })
    .map(function (x) { return Utilities.formatDate(x[0], tz, 'yyyy-MM-dd'); });
  const alvo = _decimoDiaUtilSet2026_(SET2026.ANO, mesSped, feriados, tz);

  const EN = { IF: 'IF', AND: 'AND', WD: 'WORKDAY.INTL', DATE: 'DATE', TODAY: 'TODAY' };
  const PT = { IF: 'SE', AND: 'E', WD: 'DIATRABALHO.INTL', DATE: 'DATA', TODAY: 'HOJE' };
  const variantes = [
    { nome: 'EN ponto e vírgula', F: EN, s: ';' },
    { nome: 'PT-BR ponto e vírgula', F: PT, s: ';' },
    { nome: 'EN vírgula', F: EN, s: ',' }
  ];
  const fI = function (v, r) {
    const F = v.F, s = v.s;
    return '=' + F.IF + '(' + F.AND + '($E' + r + '="' + SET2026.OBRIGACAO_SPED + '"' + s + '$H' + r + '<>"NÃO SE APLICA")' + s +
      F.WD + '(' + F.DATE + '(' + SET2026.ANO + s + mesSped + s + '1)-1' + s + '10' + s + '1' + s + SET2026.COL_FERIADOS_RANGE + ')' + s + '"")';
  };
  const fJ = function (v, r) {
    return '=' + v.F.IF + '($I' + r + '=""' + v.s + '""' + v.s + '$I' + r + '-' + v.F.TODAY + '())';
  };
  const ehData = function (x) { return /^\d{2}\/\d{2}\/\d{4}$/.test(x); };
  const celI = d.getRange(r0, SET2026.COL_PRAZO);
  const celJ = d.getRange(r0, SET2026.COL_DIAS);
  const log = ['Linha de teste: ' + r0 + ' | esperado: ' + alvo];

  // 1) Tenta fórmulas.
  for (let k = 0; k < variantes.length; k++) {
    const v = variantes[k];
    try {
      celI.setFormula(fI(v, r0)).setNumberFormat('dd/mm/yyyy');
      celJ.setFormula(fJ(v, r0)).setNumberFormat('0');
      SpreadsheetApp.flush();
      const di = celI.getDisplayValue(), dj = celJ.getDisplayValue();
      log.push(v.nome + ': I=' + di + ' J=' + dj);
      if (ehData(di) && di === alvo && dj.charAt(0) !== '#') {
        const FI = [], FJ = [];
        for (let r = 2; r <= ultima; r++) { FI.push([fI(v, r)]); FJ.push([fJ(v, r)]); }
        d.getRange(2, SET2026.COL_PRAZO, n, 1).setFormulas(FI).setNumberFormat('dd/mm/yyyy');
        d.getRange(2, SET2026.COL_DIAS, n, 1).setFormulas(FJ).setNumberFormat('0');
        SpreadsheetApp.flush();
        _avisoSet2026_('Corrigido com a variante "' + v.nome + '". Prazo SPED = ' + alvo + '.\n' + log.join('\n'));
        return;
      }
    } catch (e) {
      log.push(v.nome + ': erro ' + e.message);
    }
  }

  // 2) Fallback: Prazo como data fixa nas linhas SPED; Dias p/ Vencer por fórmula, se alguma variante servir.
  const partes = alvo.split('/');
  const dataAlvo = new Date(parseInt(partes[2], 10), parseInt(partes[1], 10) - 1, parseInt(partes[0], 10));
  const hAtual = d.getRange(2, 8, n, 1).getValues();
  const vI = [];
  for (let i = 0; i < n; i++) {
    const ehSped = String(obrig[i][0]).trim() === SET2026.OBRIGACAO_SPED;
    const na = String(hAtual[i][0]).toUpperCase() === 'NÃO SE APLICA';
    vI.push([ehSped && !na ? dataAlvo : '']);
  }
  d.getRange(2, SET2026.COL_PRAZO, n, 1).setValues(vI).setNumberFormat('dd/mm/yyyy');
  let jOk = null;
  for (let k = 0; k < variantes.length && !jOk; k++) {
    const v = variantes[k];
    try {
      celJ.setFormula(fJ(v, r0)).setNumberFormat('0');
      SpreadsheetApp.flush();
      if (celJ.getDisplayValue().charAt(0) !== '#') jOk = v;
    } catch (e) { log.push('J ' + v.nome + ': erro ' + e.message); }
  }
  if (jOk) {
    const FJ = [];
    for (let r = 2; r <= ultima; r++) FJ.push([fJ(jOk, r)]);
    d.getRange(2, SET2026.COL_DIAS, n, 1).setFormulas(FJ).setNumberFormat('0');
  } else {
    d.getRange(2, SET2026.COL_DIAS, n, 1).clearContent();
  }
  SpreadsheetApp.flush();
  _avisoSet2026_('Nenhuma fórmula de Prazo funcionou. Prazo gravado como data fixa (' + alvo + '). Dias p/ Vencer: ' +
    (jOk ? 'fórmula "' + jOk.nome + '"' : 'vazio') + '.\n' + log.join('\n'));
}

/** 10º dia útil do mês (mes 1-12), descontados feriados no formato yyyy-MM-dd. Retorna dd/MM/yyyy. */
function _decimoDiaUtilSet2026_(ano, mes, feriados, tz) {
  let d = new Date(ano, mes - 1, 1, 12, 0, 0);
  let cont = 0;
  while (true) {
    const dow = d.getDay();
    const iso = Utilities.formatDate(d, tz, 'yyyy-MM-dd');
    if (dow !== 0 && dow !== 6 && feriados.indexOf(iso) === -1) cont++;
    if (cont === 10) return Utilities.formatDate(d, tz, 'dd/MM/yyyy');
    d = new Date(d.getFullYear(), d.getMonth(), d.getDate() + 1, 12, 0, 0);
  }
}
