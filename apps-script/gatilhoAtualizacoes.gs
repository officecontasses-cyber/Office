/**
 * Processa a fila da aba "Atualizações" sozinho, sem precisar rodar processarAtualizacoes() à mão.
 *
 * Uso (uma vez): cole este arquivo no Apps Script da Controle_Fiscal (Extensões > Apps Script > + > Script),
 * salve, escolha a função instalarGatilhoAtualizacoes e clique em Executar (autorize quando pedir).
 * Depois disso, a cada 5 minutos o script olha a fila e, se houver linha nova sem "Processado",
 * chama o processarAtualizacoes() que já existe na planilha.
 *
 * Para desligar: rode removerGatilhoAtualizacoes().
 */
var NOME_ABA_FILA = 'Atualizações';
var COLUNA_PROCESSADO = 7; // Nº | aba | Obrigação | Status | Valor | Observações | Processado

function instalarGatilhoAtualizacoes() {
  removerGatilhoAtualizacoes();
  ScriptApp.newTrigger('processarAtualizacoesAutomatico').timeBased().everyMinutes(5).create();
}

function removerGatilhoAtualizacoes() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'processarAtualizacoesAutomatico') ScriptApp.deleteTrigger(t);
  });
}

function processarAtualizacoesAutomatico() {
  var trava = LockService.getScriptLock();
  if (!trava.tryLock(30000)) return; // outra execução em andamento
  try {
    var aba = SpreadsheetApp.getActive().getSheetByName(NOME_ABA_FILA);
    if (!aba || aba.getLastRow() < 2) return;
    var linhas = aba.getRange(2, 1, aba.getLastRow() - 1, COLUNA_PROCESSADO).getValues();
    var temNova = linhas.some(function (l) {
      return String(l[0]).trim() !== '' && String(l[COLUNA_PROCESSADO - 1]).trim() === '';
    });
    if (temNova) processarAtualizacoes();
  } finally {
    trava.releaseLock();
  }
}
