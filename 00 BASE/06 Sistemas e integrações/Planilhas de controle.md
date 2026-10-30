# Planilhas de controle (Google Drive)
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: leitura das planilhas em 25 a 30/10/2026; skill `fechamento-contabil-dominio` (SKILL.md e referências)

As planilhas ficam no Drive e não são alteradas pelo Claude. A **1ª aba de cada uma é a `GATILHO`**:
a exportação do Drive lê a primeira aba visível, por isso a GATILHO precisa ficar em primeiro.

| Planilha | O que controla | GATILHO |
|---|---|---|
| `Controle_Fiscal` | Obrigações fiscais mensais dos clientes do Presumido e do Real (abas `Jul2026`, `Ago2026`, `Set2026`…; `Cadastro_Clientes`; `Atualizações`) | Por cliente e competência: `SIM` ou `SEM PENDÊNCIA` = liberado; `NÃO` = obrigação pendente |
| `SIMPLES 2026` | Fechamento fiscal do Simples Nacional | `SIM` = liberado; `CONFERIR` = fechado com obrigação pendente; `PARCIAL` = DAS enviado, sem fechamento marcado; `NÃO` = pendente |
| `CONTROLE \| DP REINF'S` | REINF por cliente (abas `MOD GERAL MM.AAAA`; em fev também `SIMPLES NACIONAL 02.2026`) | Status (`COM RETENÇÃO`, `SEM MOVIMENTO`, `PENDENTE`, `NÃO ENTREGUE`…) e o detalhe com códigos e valores retidos |
| `DIST LUCROS 2026` | Lucros distribuídos | Alimenta a aba Lucros distribuídos do artefato Controle Contábil |
| `Clientes LP.LR` e `Clientes Simples` | Cadastro da carteira por regime | — |

## Regras de leitura
- Aba de mês nova da DP REINF'S precisa seguir o nome `MOD GERAL MM.AAAA` para entrar na GATILHO.
- No Google Sheets, `COUNTIF` sobre `INDIRECT` com erro devolve 0: cada ramo da fórmula da GATILHO é
  protegido com `IF(ISNUMBER(...), ..., NA())`.
- `Clientes Simples` e `SIMPLES 2026` têm senhas e CPFs: nunca copiar esses campos.
- No Lucro Real, o DARF de IRPJ/CSLL fica na Controle_Fiscal como "aguardando a contabilidade liberar a
  apuração"; no Presumido o fiscal apura e envia sem liberação da contabilidade.

## Pendente
- Planilha de controle da **folha** do DP: ainda não localizada (perguntar à Júlia). Ver `HANDOFF.md`.
