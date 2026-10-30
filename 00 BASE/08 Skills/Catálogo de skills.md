# Catálogo de skills
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: repositório `officecontasses-cyber/office`; lista de skills da conta claude.ai disponível nesta sessão (30/10/2026)

## Skill do repositório
| Skill | Para que serve | Cópia mestra | Instalada em |
|---|---|---|---|
| `fechamento-contabil-dominio` | Fechamento contábil mensal de todos os regimes no Domínio (7 etapas) | `.claude/skills/fechamento-contabil-dominio` neste repositório | claude.ai (upload do zip pela responsável, versão de 27/10/2026) e branch `claude/keen-fermi-g7xibd` |

A cópia mestra fica em `.claude/skills` e não em `08 Skills`: é a pasta que o Claude Code carrega
sozinho. Duplicar aqui criaria duas versões. Toda mudança: editar no repositório, gerar o zip e subir no
claude.ai, nessa ordem.

## Skills da conta claude.ai (instaladas na conta; cópia mestra fora deste repositório)
Ligadas ao fechamento contábil e fiscal:
- **Fiscal:** `fechamento-completo-servicos`, `conferencia-xml-prefeitura-dominio`, `conciliacao-notas-dominio-estado`, `registro-obrigacoes-icms-rs`, `registro-municipal-declaracao-issqn`, `analisar-retencoes-portal-nacional`, `conciliacao-retencoes-servicos-tomados`, `retencoes-tributarias-tomador`, `efd-reinf`, `dctfweb`, `upload-envio-guias-gclick`, `concluir-tarefas-gclick`, `cadastro-cliente-gclick`, `cadastro-cliente-sieg`, `controle-debitos-certidoes-clientes`.
- **Apuração:** `apuracao-lucro-real`, `apuracao-lucro-presumido`, `calcular-das-simples-nacional`, `conferir-apuracao-simples-nacional`, `calculo-pis-cofins-nao-cumulativo`, `calculo-pis-cofins-cumulativo`, `apuracao-mei`.
- **Contábil:** `conciliar-extrato-razao`, `conciliacao-fornecedores`, `conciliacao-clientes`, `conciliacao-cartoes-credenciadora`, `balancete-analise`, `ativo-imobilizado-depreciacao`, `lancamentos-contabeis-padrao`, `pendencias-fechamento-cliente`, `transformar-extrato-dominio`, `zeramento-dominio`, `ecd-escrituracao-contabil-digital`, `ecf-escrituracao-contabil-fiscal`.
- **DP:** `folha-pagamento-mensal`, `analisar-folha-pagamento`, `esocial-eventos-periodicos`, `fgts-guia-recolhimento`.
- **Apoio:** `resumo-rascunho-email-owa` (rascunho no Outlook web), `docx`, `xlsx`, `pdf`.

Esta lista registra nome e área; o que cada uma faz está na descrição da própria skill no claude.ai.
Quando uma skill da conta for alterada, registrar aqui a data.
