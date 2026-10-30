# Snapshot 30/10/2026 (sexta): fechamento fiscal 09/2026

Versão completa: `memoria/PENDENCIAS.md` e dossiês `memoria/CLIENTE_NNN_*.md`. Snapshot anterior: `PENDENCIAS_E_RESOLVIDOS_2026-10-29.md`.
**Hoje é o vencimento do IRPJ/CSLL do 3º trimestre.** Todas as guias foram entregues aos clientes até 29/10; o que resta é pagamento, que é do cliente.

## Situação do fechamento de 09/2026
| Bloco | Situação |
|---|---|
| IRPJ/CSLL 3º trimestre | **Fechado** — nenhuma linha `Pendente` ou `Em andamento` na Set2026 |
| PIS/COFINS 09/2026 | Fechado, menos o 197 (COFINS 4% a decidir) e o pagamento do 126 |
| ISSQN e declarações municipais | Fechados |
| REINF | Fechada |
| **SPED Contribuições 09/2026** | **Não começou** — ~25 linhas `Pendente`, prazo 16/11; pasta `010 EFD CONTRIBUIÇÕES` de setembro vazia no Drive |
| Conciliações do Domínio | Abertas em 126, 152, 177, 238, 248, 258, 261, 263, 264 |

## Guias do 3º trimestre entregues em 29/10
| Nº | Cliente | CNPJ | DARF | Total |
|---|---|---|---|---|
| 247 | Porto Mais Alegre | 53290951000109 | 07.16.26302.4034482-1 | 4.309,37 |
| 71 | Conte Arquitetura | 08307701000180 | 07.16.26302.4311001-5 | 174.386,85 |
| 186 | Lopes & Nadal | 28516249000173 | 07.16.26302.4584488-1 | 2.337,93 |
| 261 | Giatech | 64866011000131 | 07.16.26301.2705806-1 | 2.801,71 (refeita em 28/10) |
| 238 | REAT Holding | 49252432000189 | 07.16.26301.0615789-3 | 795,57 (28/10) |

## Vencido, esperando decisão de terceiro
| Nº | Cliente | O quê | Desde |
|---|---|---|---|
| 197 | ASBBM (05164750000112) | **COFINS 4% sobre receita financeira: R$ 163,60 em 2026** (abril 116,15; 3º trim 42,51), nenhuma paga. E-mail ao Gian enviado em 29/10 | vencimentos mensais |
| 238 | REAT Holding | DARFs de abr, mai e jun: **9.405,48**, pagamento não confirmado | — |
| 126 | Tatsch & Leite (10914420000137) | Guia de PIS/COFINS reemitida em 27/10 por **4.118,90**, pagamento não confirmado | venceu 23/10 |

## Com prazo
| Prazo | Nº | O quê |
|---|---|---|
| 31/10 (sáb) | 238 | Balancete de setembro no Livro Diário; relatório de débitos de 06/2026 à cliente |
| 03/11 | 197 | Consulta formal ao Lefisc (cota de outubro esgotada) |
| 09/11 | 261 | Pagamento da NF de outubro da Giatech, com abatimento de 340,00 |
| 13/11 | 71 | **Certificado A1 da Conte vence** — sem ele o Portal Nacional não roda |
| 16/11 | todos | **SPED Contribuições 09/2026**, ~25 clientes |

## Aguardando terceiros
| Nº | O quê |
|---|---|
| 133 | Balancete/LALUR do 3º trimestre por escrito (apuração é da contabilidade, não do fiscal) |
| 126 | Resposta do Gian sobre a taxa de fiscalização anual (e-mail enviado 29/10) |
| 197 | Resposta do Gian sobre a COFINS; criar a obrigação de PIS/COFINS no perfil do G-Click |
| 261 | DARF e R-4020 da Betha; número e valor da NF de outubro |
| 227 | CNPJ do cliente, que não está na aba `Cadastro_Clientes` |

## A revisar no pós-fechamento
- **261:** protocolo de Serviços Tomados de Novo Hamburgo a refazer (4 notas, 1.058,95); lançar a CSLL retida de 340,00 na NFS-e 10 quando chegar o comprovante; IBS/CBS.
- **197:** IRRF das aplicações não pode estar em "IRRF a Recuperar" no Domínio (entidade isenta lança direto no resultado); ECF 2026 com forma de tributação 9 – Isenta; rever a ECF 2024 entregue em Lucro Presumido e a CSLL de 41,42 paga como LP em 2025.
- **238:** apuração do Lucro Real precisa bater no Domínio (estimativa de setembro veio do balanço de redução, rodada 9).
- **247:** saldo credor de IRPJ de 2.994,33 — origem não documentada e PER/DCOMP a confirmar; revisar no 4º trimestre.
- **186:** conferir os 653,00/6,51 do resgate de 31/07 quando sair o informe anual do Bradesco.

## Resolvido em 29/10
- **126:** a diferença de 1.516,78 na COFINS **não era erro**: compensação via PERDCOMP 002 (562,22) e 003 (954,56), créditos de 01/2025, transmitidos em 17/10. 4.609,87 − 1.516,78 = 3.093,09.
- **248:** não possui ICMS → GUIA ICMS `Não se aplica`, encerrando a divergência com o G-Click.
- **152:** tarefa "Confirmações - Retenções" é para dispensar no G-Click.
- **133:** prejuízo fiscal no trimestre → sem guia.
- **197:** CSLL de 95,64 não é devida (IN 1.700/2017, art. 13 §1º).
- **Grupo Tacom:** o federal é entregue pela matriz, que não é cliente do escritório; 138, 248 e 263 só têm municipal e estadual.

## Alertas
- **Senha em texto aberto** num e-mail de 04/03/2026 ("Cadastro e-mail contribuinte", Novo Hamburgo): trocar e apagar.
- **Certificado A1 do 71 vence em 13/11.**

## Rotina única da Central — rodada das 06:45 (30/10/2026)
- G-Click (API, só GET): 775 tarefas na janela 31/08–28/01, **462 abertas**. Planilha Controle_Fiscal: **sem mudança** desde 29/10 (Set2026 43 e Ago2026 64 linhas abertas).
- **Resolvido hoje no G-Click:** 155 MANIERI E OLIVEIRA (`17333275000140`) — COFINS/PIS (4.9160) e CSLL e IRPJ LP Trimestral (4.9166) **concluídas**. Vencidas em aberto: de 8 para **7**. **Nada vence hoje em aberto** (as 27 tarefas de IRPJ/CSLL de 30/10 estão todas `C` ou `D`).
- **Lista de concluir: 5 tarefas** — 018 CC&D (`93309631000178`) COFINS/PIS; 248 TACOM PROJETOS FL SC (`01005845002003`) EFD ICMS/IPI; 152 CRBM5 (`13738204000176`) EFD Reinf; 138 TACOM SISTEMAS FL RS (`08196752000262`) e 257 B2B SOLUCOES (`30839235000132`) EFD ICMS/IPI + GIA.
- **Ação de verdade, fora da lista:** 152 CRBM5 Confirmações - Retenções (envio ao CRBIO) e 126 TATSCH & LEITE (`10914420000137`) taxa de fiscalização anual (e-mail ao Gian enviado em 29/10, aguardando resposta).
- **`E` decifrado:** cotas 2 e 3 do IRPJ/CSLL do 126, venc. 30/11 e 31/12, com `dataConclusao` 17/10 — tarefa já trabalhada à espera do mês da cota. Não é pendência.
- **227 PROGEST: CNPJ `45087762000105`** (obtido pela API, confere com a planilha).
- **197 ASBBM (`05164750000112`) segue sem COFINS/PIS cadastrado no G-Click** — não aparece entre os 27 clientes de 25/11.
- **Alerta de controle:** a coluna `Prazo` da Set2026 está congelada em 26/10; a contagem regressiva está 4 dias atrasada.
