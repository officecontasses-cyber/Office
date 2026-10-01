/**
 * definirPrazosSet2026.gs — preenche a coluna Prazo (I) da aba Set2026 com os vencimentos de 09/2026.
 *
 * Regras (competência 09/2026):
 *  - Prazo por obrigação (nome exato da coluna E), igual para todos os clientes: REINF 15/10;
 *    DARF PIS e COFINS 23/10 (25/10 é domingo, antecipa); DARF IRPJ, CSLL e REFIS 30/10.
 *  - Obrigações estaduais só para clientes do RS (coluna A termina em /RS): GIA RS e SPED ICMS 15/10
 *    (Lefisc); Guia ICMS 13/10 (12/10 é feriado, prorroga). Cliente de outra UF não recebe a data do RS.
 *  - Guia ISSQN e Declaração Prefeitura: prazo por município (coluna A). Porto Alegre 09/10 (dia 10
 *    cai no sábado, antecipa); São Leopoldo 15/10. Município fora da lista fica em branco.
 *  - Não mexe em SPED CONTRIBUIÇÕES (já tem fórmula, 16/11/2026).
 *  - Linhas internas (Serviços Tomados/Prestados, Entradas, Saídas, Receita Aluguéis/Tributável),
 *    Certificado Digital e linhas com status "Não se aplica" ficam sem prazo.
 *
 * Só escreve na coluna I da Set2026, e só nas linhas que têm prazo definido. "Dias p/ Vencer" (J)
 * já calcula a partir de I. Para incluir um município novo, acrescente em POR_MUNICIPIO_ISS e
 * execute de novo (o script pode ser repetido sem efeito colateral).
 *
 * Depende de _ultimaLinhaDadosSet2026_ e _avisoSet2026_ (arquivo criarAbaSet2026).
 */

const PRAZOS_SET2026 = {
  ABA: 'Set2026',
  COL_MUN: 1, COL_NUM: 3, COL_OBRIG: 5, COL_STATUS: 8, COL_PRAZO: 9,
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
  const sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(C.ABA);
  if (!sh) { _avisoSet2026_('Aba ' + C.ABA + ' não encontrada. Nada foi alterado.'); return; }

  const n = _ultimaLinhaDadosSet2026_(sh) - 1;
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

  Object.keys(porData).forEach(function (chave) {
    const p = chave.split('-').map(Number);
    const rl = sh.getRangeList(porData[chave]);
    rl.setValue(new Date(p[0], p[1] - 1, p[2]));
    rl.setNumberFormat('dd/mm/yyyy');
  });
  SpreadsheetApp.flush();

  const porDia = Object.keys(porData).sort().map(function (k) {
    const p = k.split('-'); return ('0' + p[2]).slice(-2) + '/' + ('0' + p[1]).slice(-2) + ': ' + porData[k].length;
  }).join(' | ');
  _avisoSet2026_('Prazos gravados em ' + aplicadas + ' linhas.\nPor data: ' + porDia +
    '\nISS sem prazo (município não cadastrado): ' + (Object.keys(semPrazoMun).length ? JSON.stringify(semPrazoMun) : 'nenhum') +
    '\nPuladas por UF: ' + (Object.keys(foraUf).length ? JSON.stringify(foraUf) : 'nenhuma') +
    '\nRode verificarPrazosSet2026() para conferir.');
}

/** Conferência (somente leitura). */
function verificarPrazosSet2026() {
  const C = PRAZOS_SET2026;
  const sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(C.ABA);
  if (!sh) { _avisoSet2026_('Aba ' + C.ABA + ' não encontrada.'); return; }
  const n = _ultimaLinhaDadosSet2026_(sh) - 1;
  const v = sh.getRange(2, 1, n, 10).getDisplayValues();
  const problemas = [];
  const porObr = {};
  const internas = ['SERVICOS TOMADOS', 'SERVICOS PRESTADOS', 'ENTRADAS', 'SAIDAS', 'RECEITA ALUGUEIS', 'RECEITA TRIBUTAVEL', 'CERTIFICADO DIGITAL'];

  v.forEach(function (l, i) {
    const o = _normSet2026_(l[C.COL_OBRIG - 1]);
    const prazo = l[C.COL_PRAZO - 1], dias = l[9];
    const st = _normSet2026_(l[C.COL_STATUS - 1]);
    if (prazo.charAt(0) === '#' || dias.charAt(0) === '#') problemas.push('Erro em Prazo/Dias na linha ' + (i + 2));
    if (prazo !== '' && !/^\d{2}\/\d{2}\/\d{4}$/.test(prazo)) problemas.push('Prazo fora do formato de data na linha ' + (i + 2) + ': ' + prazo);
    if (prazo !== '' && (st === 'NAO SE APLICA' || st === 'NA')) problemas.push('Linha ' + (i + 2) + ' é "Não se aplica" e tem prazo');
    if (prazo !== '' && internas.some(function (x) { return o.indexOf(x) === 0; })) problemas.push('Linha interna com prazo na linha ' + (i + 2) + ' (' + l[C.COL_OBRIG - 1] + ')');
    if (prazo !== '') {
      const k = String(l[C.COL_OBRIG - 1]).trim();
      (porObr[k] = porObr[k] || {})[prazo] = (porObr[k][prazo] || 0) + 1;
    }
  });

  const resumo = Object.keys(porObr).sort().map(function (k) { return k + ' ' + JSON.stringify(porObr[k]); }).join('\n');
  _avisoSet2026_(resumo + (problemas.length ? '\nPROBLEMAS:\n- ' + problemas.slice(0, 15).join('\n- ') : '\nSem problemas encontrados.'));
}

function _normSet2026_(s) {
  return String(s).trim().toUpperCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
}
