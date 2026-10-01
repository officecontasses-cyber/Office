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
