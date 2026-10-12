/**
 * corrigirCnpjSet2026.gs — corrige a coluna B (CNPJ) da aba Set2026 da Controle_Fiscal.
 *
 * Problema (auditoria de 12/10/2026): na Set2026 e na Ago2026 os CNPJs estavam gravados como NÚMERO
 * ("General"), e cinco perderam o zero à esquerda (13 dígitos): 26 Raldi, 71 Conte, 138 Tacom Sistemas FL RS,
 * 197 ASBBM e 263 Tacom Projetos FL RS. Ao completar o zero, os dígitos verificadores conferem e batem com a
 * aba Cadastro_Clientes.
 *
 * O que faz (só na coluna B da aba configurada em CNPJ_FIX.ABAS):
 *   1) lê o CNPJ de cada linha; se for número (ou texto com menos de 14 dígitos), completa com zeros à esquerda
 *      até 14 dígitos;
 *   2) só grava quando o CNPJ completado tem dígitos verificadores VÁLIDOS; senão deixa como está e avisa;
 *   3) grava como TEXTO (formato '@'), com os 14 dígitos sem pontuação (mesmo padrão da Cadastro_Clientes e do
 *      script do cliente 265);
 *   4) não mexe em células com fórmula nem em outras colunas; compara com Cadastro_Clientes e apenas avisa
 *      divergência (não altera).
 *
 * Uso: rode verificarCnpjSet2026() para ver o que seria corrigido (não grava nada) e depois corrigirCnpjSet2026().
 * Idempotente: rodar de novo não muda nada. Para a Ago2026, troque ABAS por ['Set2026', 'Ago2026'].
 *
 * Depois de rodar, para as abas dos próximos meses, deixe a coluna B da aba modelo com formato "Texto simples".
 */

const CNPJ_FIX = {
  ABAS: ['Set2026'],
  ABA_CAD: 'Cadastro_Clientes',
  COL_CNPJ: 2,   // B
  COL_NUM: 3,    // C (Nº do cliente na aba do mês)
  PRIMEIRA_LINHA: 2
};

function verificarCnpjSet2026() { return _cnpjFix_(false); }
function corrigirCnpjSet2026() { return _cnpjFix_(true); }

function _cnpjDvOk_(s) {
  if (!/^\d{14}$/.test(s)) return false;
  const d = s.split('').map(Number);
  function dig(base, pesos) {
    let soma = 0;
    for (let i = 0; i < pesos.length; i++) soma += base[i] * pesos[i];
    const r = soma % 11;
    return r < 2 ? 0 : 11 - r;
  }
  const p1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
  const p2 = [6].concat(p1);
  const d1 = dig(d, p1);
  const d2 = dig(d.slice(0, 12).concat([d1]), p2);
  return d[12] === d1 && d[13] === d2;
}

function _cnpjFix_(gravar) {
  const C = CNPJ_FIX;
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const msgs = [];

  // cadastro: Nº -> CNPJ (14 dígitos)
  const cad = {};
  const shCad = ss.getSheetByName(C.ABA_CAD);
  if (shCad && shCad.getLastRow() >= 2) {
    shCad.getRange(2, 1, shCad.getLastRow() - 1, 3).getValues().forEach(function (l) {
      const n = parseInt(l[0], 10);
      if (!isNaN(n)) cad[n] = String(l[2]).replace(/\D/g, '').padStart(14, '0');
    });
  }

  C.ABAS.forEach(function (nome) {
    const sh = ss.getSheetByName(nome);
    if (!sh) { msgs.push(nome + ': aba não encontrada.'); return; }
    const ultima = sh.getLastRow();
    if (ultima < C.PRIMEIRA_LINHA) { msgs.push(nome + ': sem linhas.'); return; }
    const qtd = ultima - C.PRIMEIRA_LINHA + 1;
    const rngB = sh.getRange(C.PRIMEIRA_LINHA, C.COL_CNPJ, qtd, 1);
    const valores = rngB.getValues();
    const formulas = rngB.getFormulas();
    const nums = sh.getRange(C.PRIMEIRA_LINHA, C.COL_NUM, qtd, 1).getValues();

    let corrigidos = 0, jaTexto = 0, avisos = [];
    const mudar = [];                                          // {linha, valor}
    valores.forEach(function (l, i) {
      const v = l[0];
      if (formulas[i][0]) return;                              // fórmula: não mexe
      if (v === '' || v === null) return;
      const bruto = (typeof v === 'number') ? String(Math.round(v)) : String(v).replace(/\D/g, '');
      const completo = bruto.padStart(14, '0');
      const cliente = parseInt(nums[i][0], 10);
      if (!_cnpjDvOk_(completo)) {
        avisos.push('linha ' + (i + C.PRIMEIRA_LINHA) + ' (cliente ' + cliente + '): CNPJ "' + v + '" inválido mesmo completando zeros. Mantido.');
        return;
      }
      if (!isNaN(cliente) && cad[cliente] && cad[cliente] !== completo) {
        avisos.push('linha ' + (i + C.PRIMEIRA_LINHA) + ' (cliente ' + cliente + '): CNPJ ' + completo + ' diferente do cadastro (' + cad[cliente] + '). Não alterado se já estiver igual ao texto atual.');
      }
      if (typeof v === 'number' || bruto.length !== 14 || String(v) !== completo) {
        corrigidos++;
        mudar.push({ linha: i + C.PRIMEIRA_LINHA, valor: completo });
      } else {
        jaTexto++;
      }
    });

    msgs.push(nome + ': ' + corrigidos + ' linha(s) a corrigir, ' + jaTexto + ' já corretas como texto.');
    avisos.forEach(function (a) { msgs.push('  ' + nome + ' ' + a); });

    if (gravar && corrigidos > 0) {
      mudar.forEach(function (m) {
        sh.getRange(m.linha, C.COL_CNPJ).setNumberFormat('@').setValue(m.valor);   // texto, 14 dígitos
      });
      msgs.push(nome + ': ' + mudar.length + ' célula(s) da coluna B gravada(s) como texto.');
    } else if (!gravar) {
      msgs.push(nome + ': modo verificação, nada foi gravado.');
    }
  });

  const texto = msgs.join('\n');
  Logger.log(texto);
  try { SpreadsheetApp.getUi().alert(texto); } catch (e) { /* execução sem interface */ }
  return texto;
}
