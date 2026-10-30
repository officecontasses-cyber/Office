# Fechamento contábil mensal
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: skill `.claude/skills/fechamento-contabil-dominio` (commit 078216c, 27/10/2026); teste completo com o cliente 238 em 26 e 27/10/2026

## Como acionar
Na conversa: **"fechamento NNN MM/AAAA"** (ex.: "fechamento 238 09/2026"). A skill `fechamento-contabil-dominio`
conduz, etapa por etapa, para Simples, Presumido e Real.

## Quando
Depois que o fiscal libera a competência (GATILHO da Controle_Fiscal ou da SIMPLES 2026; ver
`06 Sistemas e integrações/Planilhas de controle.md`).

## As 7 etapas
1. **Documentos:** extratos (CSV de preferência), comprovantes pagos, situação fiscal (e-CAC), certidões, relatórios do Domínio. Ao fim, oferecer marcar "Em andamento" no artefato.
2. **Mapa contábil do cliente** (`MAPA CONTABIL NNN.xlsx`): como o cliente classifica; regras confirmadas pelo colaborador.
3. **Bancos:** conciliação e importação. Mês já lançado vira conferência. Aplicações conferidas por título.
4. **Integrações** fiscal, folha e patrimônio, com o link do manual em cada pedido. Procurar lançamento manual que duplica nota já integrada.
5. **Conciliação conta a conta** (`CONCILIACAO NNN MM-AAAA.xlsx`). Saldo antigo de tributo cruzado com o SIEG.
6. **Tributos do regime.** Presumido: o fiscal apura e envia, a contabilidade confere. Real: a contabilidade refaz o acumulado mês a mês com o razão atual e libera a apuração ao fiscal.
7. **Encerramento:** pendências por responsável, mapa atualizado, artefato gravado (com autorização) e e-mail ao Gian.

## Arquivos de cada competência
Em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}` do cliente: `CONCILIACAO BANCARIA`, `IMPORTACAO`, `AJUSTES`
(se houver) e `CONCILIACAO` (abas Contas, Resultado, Rodadas, Tributos, Pendências). O mapa fica em
`{ano}/005_CONTABIL RELATORIOS/`. O Claude entrega no chat; a pessoa salva.

## Situação da skill
Testada no 238 (Lucro Real) em modo teste. Faltam os testes do 016 (Presumido) e de um cliente do Simples
antes de ir para a `main`.
