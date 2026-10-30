# Artefato Controle Contábil Mensal
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: artefato https://claude.ai/artifact/JC1KXPzY6goap6Ci9PcEzN (versão 7, 27/10/2026); referência da skill `fechamento-contabil-dominio/references/encerramento-artefato-email.md`

## Para que serve
Painel do fechamento contábil de todos os clientes (Simples, Presumido e Real): liberação do fiscal,
documentos no Drive, situação do fechamento, lucros distribuídos, obrigações anuais e prioridades do Gian.

## Onde e quem
- Link: https://claude.ai/artifact/JC1KXPzY6goap6Ci9PcEzN
- Proprietária: Officecont (officecont.asses@gmail.com). Acesso geral: "qualquer pessoa com o link".
- **Quem entra só pelo link vê, mas não grava.** Para editar (ex.: o Gian classificar prioridades),
  convidar o e-mail em Compartilhar › Convidar pessoas e abrir logado no Claude. A aba Prioridades avisa
  quando a pessoa está em somente leitura.
- Visual: fundo sempre claro (sem modo escuro), uma cor de destaque, cor só nos estados.

## Abas
Prioridades (Gian) · Fechamento · Lucros distribuídos · Obrigações anuais · Alertas · Cadastro · Como usar.
No topo, antes das abas, o bloco **Avisos do fechamento**: "Liberados para revisão" e "Em andamento",
com botão Abrir, e "Aprovados recentes".

## Banco de dados (coleções)
`clientes` (71 em 30/10/2026), `fechamento` (um documento por cliente e competência, id `NNN_AAAA-MM`),
`lucros`, `anuais`, `alertas`, `meta`.

Campos do fechamento que o analista ou a skill preenchem: `docsSituacao`, `docsPendentes`,
`obsAnalista`, `liberadoRevisao`, `dataLiberacao`, `status`, `atualizadoEm`. O revisor preenche
`obsContador`, `dataRevisao` e marca `Aprovado`. `liberadoFiscal`/`statusFiscal` vêm do GATILHO das
planilhas fiscais; `docsDrive*` vem da leitura do Drive.

## Regras
- A skill grava só com autorização, mostrando os campos antes.
- Nunca gravar senha, CPF ou nome de arquivo com senha (limpeza feita em 27/10/2026 em 12 linhas do 238 e do 255).
- Observação de um cliente nunca reaproveita texto de outro (erro corrigido em 27/10/2026: o 002, Presumido,
  tinha recebido a nota do 238 sobre LALUR).
