/**
 * inserirIrpjCsllTrimestralSet2026.gs — insere as linhas DARF IRPJ e DARF CSLL (3º trimestre/2026)
 * na aba Set2026 para os clientes Lucro Presumido.
 *
 * Padrão seguido: o mesmo dos clientes Lucro Real (133 e 238), com as duas linhas logo abaixo de
 * DARF COFINS e antes de SPED CONTRIBUIÇÕES, na ordem DARF IRPJ, DARF CSLL.
 *
 * Cada linha nova é cópia da linha DARF COFINS do cliente (Município, CNPJ, Nº, Empresa, ICMS, Regime,
 * formatação e fórmulas de Prazo/Dias); muda só a Obrigação. Data, Valor, Status, Observações e
 * Fechamento ficam em branco.
 *
 * Fora do escopo por padrão (sem linha DARF COFINS na planilha): 138, 152, 248, 263.
 * Ajuste EXCLUIR_CLIENTES se quiser outro recorte.
 *
 * Idempotente: cliente que já tem DARF IRPJ ou DARF CSLL é ignorado. Só altera a aba Set2026.
 * Depende de _ultimaLinhaDadosSet2026_ e _avisoSet2026_ (arquivo criarAbaSet2026).
 */

const IRPJCSLL_SET2026 = {
  ABA: 'Set2026',
  REGIME: 'Lucro Presumido',
  EXCLUIR_CLIENTES: [138, 152, 248, 263],
  ANCORA: 'DARF COFINS',
  NOVAS: ['DARF IRPJ', 'DARF CSLL'],
  COL_NUM: 3, COL_OBRIG: 5, COL_REGIME: 13,
  ULTIMA_COL: 14,
  COLS_LIMPAR: [6, 7, 8, 11, 14]   // F Data, G Valor, H Status, K Observações, N Fechamento
};

function inserirIrpjCsllTrimestralSet2026() {
  const C = IRPJCSLL_SET2026;
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName(C.ABA);
  if (!sh) { _avisoSet2026_('Aba ' + C.ABA + ' não encontrada. Nada foi alterado.'); return; }

  const ultima = _ultimaLinhaDadosSet2026_(sh);
  const vals = sh.getRange(2, 1, ultima - 1, C.ULTIMA_COL).getValues();

  const jaTem = {};
  vals.forEach(function (l) {
    const o = String(l[C.COL_OBRIG - 1]).trim();
    if (o === C.NOVAS[0] || o === C.NOVAS[1]) jaTem[parseInt(l[C.COL_NUM - 1], 10)] = true;
  });

  const alvos = [];
  vals.forEach(function (l, i) {
    const cli = parseInt(l[C.COL_NUM - 1], 10);
    if (String(l[C.COL_OBRIG - 1]).trim() !== C.ANCORA) return;
    if (String(l[C.COL_REGIME - 1]).trim() !== C.REGIME) return;
    if (jaTem[cli] || C.EXCLUIR_CLIENTES.indexOf(cli) >= 0) return;
    alvos.push({ linha: i + 2, cli: cli });
  });

  if (!alvos.length) { _avisoSet2026_('Nada a inserir: nenhum cliente elegível sem DARF IRPJ/CSLL.'); return; }

  // De baixo para cima, para não deslocar as linhas ainda não processadas.
  for (let k = alvos.length - 1; k >= 0; k--) {
    const r = alvos[k].linha;
    sh.insertRowsAfter(r, C.NOVAS.length);
    const origem = sh.getRange(r, 1, 1, C.ULTIMA_COL);
    for (let j = 0; j < C.NOVAS.length; j++) {
      const dest = r + 1 + j;
      origem.copyTo(sh.getRange(dest, 1, 1, C.ULTIMA_COL));
      sh.getRange(dest, C.COL_OBRIG).setValue(C.NOVAS[j]);
      C.COLS_LIMPAR.forEach(function (c) { sh.getRange(dest, c).clearContent(); });
    }
  }
  SpreadsheetApp.flush();

  const lista = alvos.map(function (a) { return a.cli; }).reverse().join(', ');
  _avisoSet2026_('Inseridas ' + (alvos.length * C.NOVAS.length) + ' linhas (' + C.NOVAS.join(' + ') + ') para ' +
    alvos.length + ' clientes: ' + lista + '.\nRode verificarIrpjCsllSet2026() para conferir.');
}

/** Conferência (somente leitura). */
function verificarIrpjCsllSet2026() {
  const C = IRPJCSLL_SET2026;
  const sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(C.ABA);
  if (!sh) { _avisoSet2026_('Aba ' + C.ABA + ' não encontrada.'); return; }
  const ultima = _ultimaLinhaDadosSet2026_(sh);
  const n = ultima - 1;
  const v = sh.getRange(2, 1, n, C.ULTIMA_COL).getDisplayValues();
  const problemas = [];
  const porCliente = {};

  v.forEach(function (l, i) {
    const cli = parseInt(l[C.COL_NUM - 1], 10);
    (porCliente[cli] = porCliente[cli] || []).push({ o: String(l[C.COL_OBRIG - 1]).trim(), l: l, linha: i + 2 });
    if (l[8].charAt(0) === '#' || l[9].charAt(0) === '#') problemas.push('Erro em Prazo/Dias na linha ' + (i + 2));
  });

  let comBloco = 0;
  Object.keys(porCliente).forEach(function (k) {
    const obs = porCliente[k].map(function (x) { return x.o; });
    const iI = obs.indexOf(C.NOVAS[0]), iC = obs.indexOf(C.NOVAS[1]);
    if (iI < 0 && iC < 0) return;
    comBloco++;
    if (iI < 0 || iC < 0) problemas.push('Cliente ' + k + ': falta ' + (iI < 0 ? C.NOVAS[0] : C.NOVAS[1]));
    else if (iC !== iI + 1) problemas.push('Cliente ' + k + ': IRPJ e CSLL não estão em sequência');
    if (obs.filter(function (o) { return o === C.NOVAS[0]; }).length > 1) problemas.push('Cliente ' + k + ': DARF IRPJ duplicada');
    [iI, iC].forEach(function (ix) {
      if (ix < 0) return;
      const x = porCliente[k][ix];
      [5, 6, 7, 10, 13].forEach(function (c) { if (x.l[c] !== '') problemas.push('Cliente ' + k + ' linha ' + x.linha + ': coluna ' + (c + 1) + ' preenchida'); });
    });
  });

  const msg = 'Linhas: ' + n + ' | Clientes: ' + Object.keys(porCliente).length + ' | Clientes com IRPJ/CSLL: ' + comBloco +
    (problemas.length ? '\nPROBLEMAS:\n- ' + problemas.slice(0, 15).join('\n- ') : '\nSem problemas encontrados.');
  _avisoSet2026_(msg);
}
