/**
 * definirPrazosSet2026.gs — preenche a coluna Prazo (I) da aba Set2026 com os vencimentos de 09/2026,
 * no formato de texto com contagem regressiva usado em Jul/Ago e mantido pelo atualizarPrazos():
 *   "23/10/2026 · 22 dias"   (futuro)      "13/09/2026 · Vencido há 16 dias"   (vencido)
 *
 * Regras (competência 09/2026):
 *  - Prazo por obrigação (nome exato da coluna E): REINF 15/10; DARF PIS e COFINS 23/10 (25/10 é
 *    domingo, antecipa); DARF IRPJ, CSLL e REFIS 30/10.
 *  - Obrigações estaduais só para clientes do RS (coluna A termina em /RS): GIA RS e SPED ICMS 15/10
 *    (Lefisc); Guia ICMS 13/10 (12/10 é feriado, prorroga). Outra UF não recebe a data do RS.
 *  - Guia ISSQN e Declaração Prefeitura: prazo por município (coluna A). Porto Alegre 09/10 (dia 10
 *    cai no sábado, antecipa); São Leopoldo 15/10. Município fora da lista fica em branco.
 *  - Não mexe em SPED CONTRIBUIÇÕES (16/11/2026, já está na planilha).
 *  - Linhas internas, Certificado Digital e status "Não se aplica" ficam sem prazo.
 *
 * "Dias p/ Vencer" (J): fórmula que lê a data dos 10 primeiros caracteres do texto do Prazo. A sintaxe da
 * fórmula depende da configuração regional da planilha, então o script testa variantes na primeira linha
 * e só aplica a que devolver o número esperado. Se nenhuma servir, deixa a coluna vazia (a contagem já
 * está no texto do Prazo).
 *
 * As datas são calculadas no fuso da planilha. Só escreve nas colunas I e J da Set2026.
 * Pode ser repetido sem efeito colateral. Depende de _ultimaLinhaDadosSet2026_ e _avisoSet2026_
 * (arquivo criarAbaSet2026).
 */

const PRAZOS_SET2026 = {
  ABA: 'Set2026',
  COL_MUN: 1, COL_NUM: 3, COL_OBRIG: 5, COL_STATUS: 8, COL_PRAZO: 9, COL_DIAS: 10,
  // d = [ano, mês, dia]; uf = restringe à UF indicada.
  POR_OBRIGACAO: {
    'REINF':                      { d: [2026, 10, 15] },
    'DARF PIS':                   { d: [2026, 10, 23] },
    'DARF COFINS':                { d: [2026, 10, 23] },
    'DARF IRPJ':                  { d: [2026, 10, 30] },
    'DARF CSLL':                  { d: [2026, 10, 30] },
    'DARF REFIS':                 { d: [2026, 10, 30] },
    'GIA RS':                     { d: [2026, 10, 15], uf: 'RS' },
    'SPED ICMS':                  { d: [2026, 10, 15], uf: 'RS' },
    'SPED ICMS - Envio arquivo':  { d: [2026, 10, 15], uf: 'RS' },
    'SPED ICMS (Recibo)':         { d: [2026, 10, 15], uf: 'RS' },
    'GUIA ICMS':                  { d: [2026, 10, 13], uf: 'RS' }
  },
  OBRIGACOES_ISS: ['GUIA ISSQN', 'DECLARAÇÃO PREFEITURA'],
  POR_MUNICIPIO_ISS: {
    'PORTO ALEGRE/RS': [2026, 10, 9],
    'SÃO LEOPOLDO/RS': [2026, 10, 15]
  }
};

function definirPrazosSet2026() {
  const C = PRAZOS_SET2026;
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName(C.ABA);
  if (!sh) { _avisoSet2026_('Aba ' + C.ABA + ' não encontrada. Nada foi alterado.'); return; }
  const tz = ss.getSpreadsheetTimeZone();
  const hoje = _hojeSet2026_(tz);

  const ultima = _ultimaLinhaDadosSet2026_(sh);
  const n = ultima - 1;
  const v = sh.getRange(2, 1, n, C.COL_PRAZO).getValues();

  const porObr = {};
  Object.keys(C.POR_OBRIGACAO).forEach(function (k) { porObr[_normSet2026_(k)] = C.POR_OBRIGACAO[k]; });
  const iss = C.OBRIGACOES_ISS.map(_normSet2026_);
  const porMun = {};
  Object.keys(C.POR_MUNICIPIO_ISS).forEach(function (k) { porMun[_normSet2026_(k)] = C.POR_MUNICIPIO_ISS[k]; });

  const porData = {};          // 'a-m-d' -> ['I5', 'I9', ...]
  const semPrazoMun = {};      // município -> nº de linhas ISS sem prazo
  const foraUf = {};           // obrigação -> nº de linhas puladas por UF
  let aplicadas = 0;

  v.forEach(function (l, i) {
    const o = _normSet2026_(l[C.COL_OBRIG - 1]);
    const st = _normSet2026_(l[C.COL_STATUS - 1]);
    if (st === 'NAO SE APLICA' || st === 'NA') return;
    const mun = String(l[C.COL_MUN - 1]).trim();
    let d = null;

    if (porObr[o]) {
      const r = porObr[o];
      if (r.uf && !new RegExp('/' + r.uf + '$').test(_normSet2026_(mun))) {
        foraUf[l[C.COL_OBRIG - 1]] = (foraUf[l[C.COL_OBRIG - 1]] || 0) + 1;
        return;
      }
      d = r.d;
    } else if (iss.indexOf(o) >= 0) {
      d = porMun[_normSet2026_(mun)] || null;
      if (!d) { semPrazoMun[mun] = (semPrazoMun[mun] || 0) + 1; return; }
    }
    if (!d) return;
    const chave = d.join('-');
    (porData[chave] = porData[chave] || []).push('I' + (i + 2));
    aplicadas++;
  });

  // Prazo (I): texto "dd/mm/aaaa · N dias". Formato de texto primeiro, para o Sheets não reinterpretar.
  Object.keys(porData).forEach(function (chave) {
    const p = chave.split('-').map(Number);
    const rl = sh.getRangeList(porData[chave]);
    rl.setNumberFormat('@');
    rl.setValue(_textoPrazoSet2026_(p, hoje));
  });
  SpreadsheetApp.flush();

  // Dias p/ Vencer (J): fórmula que lê a data do texto. Testa sintaxes na primeira linha com prazo.
  let msgDias = 'sem linhas com prazo';
  const chaves = Object.keys(porData).sort();
  if (chaves.length) {
    const p0 = chaves[0].split('-').map(Number);
    const linhaTeste = parseInt(porData[chaves[0]][0].slice(1), 10);
    const esperado = _diasEntreSet2026_(p0, hoje);
    msgDias = _aplicarDiasSet2026_(sh, ultima, linhaTeste, esperado);
  }

  const porDia = chaves.map(function (k) {
    const p = k.split('-'); return ('0' + p[2]).slice(-2) + '/' + ('0' + p[1]).slice(-2) + ': ' + porData[k].length;
  }).join(' | ');
  _avisoSet2026_('Prazos gravados em ' + aplicadas + ' linhas (hoje = ' + hoje.d + '/' + hoje.m + '/' + hoje.y + ').\nPor data: ' + porDia +
    '\nDias p/ Vencer: ' + msgDias +
    '\nISS sem prazo (município não cadastrado): ' + (Object.keys(semPrazoMun).length ? JSON.stringify(semPrazoMun) : 'nenhum') +
    '\nPuladas por UF: ' + (Object.keys(foraUf).length ? JSON.stringify(foraUf) : 'nenhuma') +
    '\nRode verificarPrazosSet2026() para conferir.');
}

function _aplicarDiasSet2026_(sh, ultima, linhaTeste, esperado) {
  const C = PRAZOS_SET2026;
  const n = ultima - 1;
  const EN = { IF: 'IF', NUM: 'ISNUMBER', DV: 'DATEVALUE', LEFT: 'LEFT', TODAY: 'TODAY' };
  const PT = { IF: 'SE', NUM: 'ÉNÚM', DV: 'DATA.VALOR', LEFT: 'ESQUERDA', TODAY: 'HOJE' };
  const variantes = [
    { nome: 'EN vírgula', F: EN, s: ',' },
    { nome: 'EN ponto e vírgula', F: EN, s: ';' },
    { nome: 'PT-BR ponto e vírgula', F: PT, s: ';' }
  ];
  const f = function (v, r) {
    const F = v.F, s = v.s, c = '$I' + r;
    return '=' + F.IF + '(' + c + '=""' + s + '""' + s + '(' + F.IF + '(' + F.NUM + '(' + c + ')' + s + c + s +
      F.DV + '(' + F.LEFT + '(' + c + s + '10)))-' + F.TODAY + '()))';
  };
  const cel = sh.getRange(linhaTeste, C.COL_DIAS);
  const log = [];
  for (let k = 0; k < variantes.length; k++) {
    const v = variantes[k];
    try {
      cel.setFormula(f(v, linhaTeste));
      SpreadsheetApp.flush();
      const disp = cel.getDisplayValue();
      log.push(v.nome + ' -> ' + disp);
      if (disp === String(esperado)) {
        const F = [];
        for (let r = 2; r <= ultima; r++) F.push([f(v, r)]);
        sh.getRange(2, C.COL_DIAS, n, 1).setFormulas(F).setNumberFormat('0');
        SpreadsheetApp.flush();
        return 'fórmula aplicada (variante "' + v.nome + '")';
      }
    } catch (e) {
      log.push(v.nome + ' -> erro ' + e.message);
    }
  }
  sh.getRange(2, C.COL_DIAS, n, 1).clearContent();
  return 'nenhuma fórmula funcionou, coluna deixada vazia (a contagem está no texto do Prazo). Testes: ' + log.join(' | ');
}

/** Conferência (somente leitura). */
function verificarPrazosSet2026() {
  const C = PRAZOS_SET2026;
  const sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(C.ABA);
  if (!sh) { _avisoSet2026_('Aba ' + C.ABA + ' não encontrada.'); return; }
  const n = _ultimaLinhaDadosSet2026_(sh) - 1;
  const v = sh.getRange(2, 1, n, C.COL_DIAS).getDisplayValues();
  const problemas = [];
  const porObr = {};
  const internas = ['SERVICOS TOMADOS', 'SERVICOS PRESTADOS', 'ENTRADAS', 'SAIDAS', 'RECEITA ALUGUEIS', 'RECEITA TRIBUTAVEL', 'CERTIFICADO DIGITAL'];
  const formato = /^\d{2}\/\d{2}\/\d{4} · (Vencido há )?\d+ dias?$/;

  v.forEach(function (l, i) {
    const o = _normSet2026_(l[C.COL_OBRIG - 1]);
    const prazo = l[C.COL_PRAZO - 1], dias = l[C.COL_DIAS - 1];
    const st = _normSet2026_(l[C.COL_STATUS - 1]);
    if (prazo.charAt(0) === '#' || dias.charAt(0) === '#') problemas.push('Erro em Prazo/Dias na linha ' + (i + 2));
    if (prazo !== '' && !formato.test(prazo)) problemas.push('Prazo fora do formato na linha ' + (i + 2) + ': ' + prazo);
    if (prazo !== '' && dias !== '' && !/^-?\d+$/.test(dias)) problemas.push('Dias p/ Vencer não numérico na linha ' + (i + 2) + ': ' + dias);
    if (prazo !== '' && (st === 'NAO SE APLICA' || st === 'NA')) problemas.push('Linha ' + (i + 2) + ' é "Não se aplica" e tem prazo');
    if (prazo !== '' && internas.some(function (x) { return o.indexOf(x) === 0; })) problemas.push('Linha interna com prazo na linha ' + (i + 2) + ' (' + l[C.COL_OBRIG - 1] + ')');
    if (prazo !== '') {
      const k = String(l[C.COL_OBRIG - 1]).trim();
      const dt = prazo.slice(0, 10);
      (porObr[k] = porObr[k] || {})[dt] = (porObr[k][dt] || 0) + 1;
    }
  });

  const resumo = Object.keys(porObr).sort().map(function (k) { return k + ' ' + JSON.stringify(porObr[k]); }).join('\n');
  _avisoSet2026_(resumo + (problemas.length ? '\nPROBLEMAS:\n- ' + problemas.slice(0, 15).join('\n- ') : '\nSem problemas encontrados.'));
}

function _hojeSet2026_(tz) {
  const p = Utilities.formatDate(new Date(), tz, 'yyyy-M-d').split('-').map(Number);
  return { y: p[0], m: p[1], d: p[2] };
}

function _diasEntreSet2026_(p, hoje) {
  return Math.round((Date.UTC(p[0], p[1] - 1, p[2]) - Date.UTC(hoje.y, hoje.m - 1, hoje.d)) / 86400000);
}

function _textoPrazoSet2026_(p, hoje) {
  const dias = _diasEntreSet2026_(p, hoje);
  const dd = ('0' + p[2]).slice(-2) + '/' + ('0' + p[1]).slice(-2) + '/' + p[0];
  return dias >= 0 ? dd + ' · ' + dias + ' dias' : dd + ' · Vencido há ' + (-dias) + ' dias';
}

function _normSet2026_(s) {
  return String(s).trim().toUpperCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
}
