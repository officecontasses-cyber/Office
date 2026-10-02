/**
 * incluirClienteBelemSet2026.gs — inclui o cliente novo 265 (BELEM BRASIL HOLDING) na Controle_Fiscal:
 *   1) uma linha em Cadastro_Clientes;
 *   2) o bloco de obrigações na aba Set2026 (competência 09/2026, a primeira da empresa).
 *
 * Dados (fonte: contrato social registrado na JUCISRS em 30/09/2026, NIRE 43212412791, e proposta
 * comercial de 04/08/2026, ambos na pasta do cliente no Drive):
 *   - BELEM BRASIL ARQUITETURA E PARTICIPACOES LTDA (nome registrado), Porto Alegre/RS, bairro Belém Novo.
 *   - Objeto: serviços de arquitetura; holding de instituições não financeiras; aluguel de imóveis próprios;
 *     compra e venda de imóveis próprios. Início das atividades: 08/09/2026.
 *   - Lucro Presumido, sem empregados; sócios-administradores Marcelo Michelon Cornetet e Mariangela Conte Cornetet.
 *   - CNPJ 69.405.790/0001-91 (lido do nome do arquivo do certificado A1; os dígitos verificadores conferem).
 *
 * O que NÃO está preenchido de propósito (a Fernanda confirma com o Cartão CNPJ, que ainda não está na pasta):
 *   CNAE principal e secundários. O contrato não traz CNAE, só o objeto social.
 *
 * Bloco da Set2026: cópia do bloco do cliente 2 (RF CONSULTORIA: Presumido, Porto Alegre, aluguel de imóveis),
 * que tem CERTIFICADO DIGITAL, REINF, SERVIÇOS TOMADOS/PRESTADOS, RECEITA ALUGUEIS, GUIA ISSQN,
 * DECLARAÇÃO PREFEITURA, DARF PIS/COFINS/IRPJ/CSLL e SPED CONTRIBUIÇÕES. Data, Valor, Status e Fechamento
 * ficam em branco: nenhum status é definido aqui (só pela fila Atualizações, com confirmação da Fernanda).
 *
 * Idempotente: se o 265 já existir em cada aba, aquela parte é pulada. Só escreve nas abas Cadastro_Clientes e Set2026.
 * Depende de _ultimaLinhaDadosSet2026_ e _avisoSet2026_ (arquivo criarAbaSet2026).
 *
 * Depois de rodar incluirClienteBelemSet2026(), rode verificarClienteBelemSet2026() e definirPrazosSet2026().
 */

const BELEM265 = {
  ABA_SET: 'Set2026',
  ABA_CAD: 'Cadastro_Clientes',
  NUM: 265,
  MODELO: 2,                       // cliente usado como modelo do bloco
  EMPRESA: 'BELEM BRASIL HOLDING',
  CNPJ: '69405790000191',
  ULTIMA_COL: 14,                  // A..N na Set2026
  COL_NUM: 3, COL_OBRIG: 5,
  COLS_LIMPAR: [6, 7, 8, 11, 14],  // F Data, G Valor, H Status, K Observações, N Fechamento
  CADASTRO: {
    cidade: 'PORTO ALEGRE / RS',
    cnaePrincipal: 'A CONFIRMAR (Cartão CNPJ)',
    cnaeSecundarios: 'A CONFIRMAR — objeto: serviços de arquitetura; holding; aluguel e compra e venda de imóveis próprios',
    socios: 'MARCELO MICHELON CORNETET (Sócio-Administrador); MARIANGELA CONTE CORNETET (Sócia-Administradora)',
    regime: 'Lucro Presumido',
    portalNacional: 'PENDENTE DE CADASTRO',
    icms: 'NÃO',
    ie: 'Isento / N/A'
  },
  OBS: {
    'CERTIFICADO DIGITAL': 'Cliente novo (início das atividades em 08/09/2026). Certificado A1 (.pfx) na pasta CERTIFICADOS do cliente; senha com o Gian.',
    'RECEITA ALUGUEIS': 'Receita projetada de R$ 15.000/mês (proposta de 04/08/2026). Pedir os contratos de locação.',
    'GUIA ISSQN': 'Cliente novo: confirmar a inscrição municipal e o acesso ao DecWeb antes da 1ª declaração.',
    'DECLARAÇÃO PREFEITURA': 'Cliente novo: confirmar a inscrição municipal e o acesso ao DecWeb antes da 1ª declaração.',
    'DARF IRPJ': 'Lucro Presumido, apuração trimestral. 1º trimestre da empresa: 3º tri/2026 (atividades desde 08/09/2026).',
    'DARF CSLL': 'Lucro Presumido, apuração trimestral. 1º trimestre da empresa: 3º tri/2026 (atividades desde 08/09/2026).'
  }
};

function incluirClienteBelemSet2026() {
  const C = BELEM265;
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const msgs = [];

  // ---------- 1) Cadastro_Clientes ----------
  const cad = ss.getSheetByName(C.ABA_CAD);
  if (!cad) {
    msgs.push('Aba ' + C.ABA_CAD + ' não encontrada: cadastro NÃO incluído.');
  } else {
    const n = cad.getLastRow();
    const col = n > 1 ? cad.getRange(2, 1, n - 1, 1).getValues() : [];
    let ultima = 1, jaTem = false;
    col.forEach(function (l, i) {
      if (String(l[0]).trim() !== '') ultima = i + 2;
      if (parseInt(String(l[0]).replace(/\D/g, ''), 10) === C.NUM) jaTem = true;
    });
    if (jaTem) {
      msgs.push('Cadastro: o cliente ' + C.NUM + ' já existe, nada incluído.');
    } else {
      const dest = ultima + 1;
      if (dest > cad.getMaxRows()) cad.insertRowsAfter(cad.getMaxRows(), 1);
      cad.getRange(ultima, 1, 1, 11).copyTo(cad.getRange(dest, 1, 1, 11), SpreadsheetApp.CopyPasteType.PASTE_FORMAT, false);
      const k = C.CADASTRO;
      cad.getRange(dest, 1, 1, 3).setNumberFormat('@');
      cad.getRange(dest, 1, 1, 11).setValues([[
        String(C.NUM), C.EMPRESA, C.CNPJ, k.cidade, k.cnaePrincipal, k.cnaeSecundarios,
        k.socios, k.regime, k.portalNacional, k.icms, k.ie
      ]]);
      msgs.push('Cadastro: cliente ' + C.NUM + ' incluído na linha ' + dest + '.');
    }
  }

  // ---------- 2) Set2026 ----------
  const sh = ss.getSheetByName(C.ABA_SET);
  if (!sh) {
    msgs.push('Aba ' + C.ABA_SET + ' não encontrada: obrigações NÃO incluídas.');
  } else {
    const ultima = _ultimaLinhaDadosSet2026_(sh);
    const vals = sh.getRange(2, 1, ultima - 1, C.ULTIMA_COL).getValues();
    const nums = vals.map(function (l) { return parseInt(l[C.COL_NUM - 1], 10); });
    if (nums.indexOf(C.NUM) >= 0) {
      msgs.push('Set2026: o cliente ' + C.NUM + ' já tem linhas, nada incluído.');
    } else {
      const linhasModelo = [];
      nums.forEach(function (n, i) { if (n === C.MODELO) linhasModelo.push(i + 2); });
      if (!linhasModelo.length) {
        msgs.push('Set2026: não achei o bloco do cliente modelo (' + C.MODELO + '). Obrigações NÃO incluídas.');
      } else {
        const ini = linhasModelo[0], qtd = linhasModelo.length;
        if (linhasModelo[qtd - 1] - ini + 1 !== qtd) {
          msgs.push('Set2026: o bloco do cliente modelo (' + C.MODELO + ') não é contínuo. Obrigações NÃO incluídas.');
        } else {
          if (ultima + qtd > sh.getMaxRows()) sh.insertRowsAfter(sh.getMaxRows(), ultima + qtd - sh.getMaxRows());
          const origem = sh.getRange(ini, 1, qtd, C.ULTIMA_COL);
          const destino = sh.getRange(ultima + 1, 1, qtd, C.ULTIMA_COL);
          origem.copyTo(destino);
          for (let j = 0; j < qtd; j++) {
            const r = ultima + 1 + j;
            sh.getRange(r, 2).setNumberFormat('@').setValue(C.CNPJ);
            sh.getRange(r, C.COL_NUM).setValue(C.NUM);
            sh.getRange(r, 4).setValue(C.EMPRESA);
            C.COLS_LIMPAR.forEach(function (c) { sh.getRange(r, c).clearContent(); });
            const obrig = String(sh.getRange(r, C.COL_OBRIG).getValue()).trim();
            if (C.OBS[obrig]) sh.getRange(r, 11).setValue(C.OBS[obrig]);
          }
          SpreadsheetApp.flush();
          msgs.push('Set2026: ' + qtd + ' linhas incluídas (linhas ' + (ultima + 1) + ' a ' + (ultima + qtd) + ').');
        }
      }
    }
  }

  msgs.push('Agora rode verificarClienteBelemSet2026() e depois definirPrazosSet2026().');
  _avisoSet2026_(msgs.join('\n'));
}

/** Conferência (somente leitura). */
function verificarClienteBelemSet2026() {
  const C = BELEM265;
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const problemas = [], resumo = [];

  const cad = ss.getSheetByName(C.ABA_CAD);
  if (cad) {
    const v = cad.getDataRange().getDisplayValues();
    const l = v.filter(function (x, i) { return i > 0 && parseInt(String(x[0]).replace(/\D/g, ''), 10) === C.NUM; });
    if (l.length !== 1) problemas.push('Cadastro: esperado 1 linha do cliente ' + C.NUM + ', achei ' + l.length + '.');
    else {
      resumo.push('Cadastro: ' + l[0][1] + ' | CNPJ ' + l[0][2] + ' | ' + l[0][7]);
      if (l[0][2] !== C.CNPJ) problemas.push('Cadastro: CNPJ diferente do esperado.');
    }
  } else problemas.push('Aba ' + C.ABA_CAD + ' não encontrada.');

  const sh = ss.getSheetByName(C.ABA_SET);
  if (sh) {
    const ultima = _ultimaLinhaDadosSet2026_(sh);
    const v = sh.getRange(2, 1, ultima - 1, C.ULTIMA_COL).getDisplayValues();
    const mod = v.filter(function (l) { return parseInt(l[C.COL_NUM - 1], 10) === C.MODELO; }).map(function (l) { return l[C.COL_OBRIG - 1].trim(); });
    const novo = v.filter(function (l) { return parseInt(l[C.COL_NUM - 1], 10) === C.NUM; });
    const obs = novo.map(function (l) { return l[C.COL_OBRIG - 1].trim(); });
    if (obs.join('|') !== mod.join('|')) problemas.push('Set2026: as obrigações do 265 não são iguais às do modelo (' + C.MODELO + ').');
    novo.forEach(function (l, i) {
      [5, 6, 7, 13].forEach(function (c) { if (l[c] !== '') problemas.push('Set2026: ' + obs[i] + ' tem a coluna ' + (c + 1) + ' preenchida (deveria estar em branco).'); });
      if (l[8].charAt(0) === '#' || l[9].charAt(0) === '#') problemas.push('Set2026: erro em Prazo/Dias na linha de ' + obs[i] + '.');
      if (l[1] !== C.CNPJ) problemas.push('Set2026: CNPJ errado na linha de ' + obs[i] + '.');
    });
    resumo.push('Set2026: ' + novo.length + ' linhas do cliente ' + C.NUM + ' (' + obs.join(', ') + ').');
  } else problemas.push('Aba ' + C.ABA_SET + ' não encontrada.');

  _avisoSet2026_(resumo.join('\n') + (problemas.length ? '\nPROBLEMAS:\n- ' + problemas.join('\n- ') : '\nSem problemas encontrados.'));
}
