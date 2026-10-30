# Google Drive — mapa das pastas administrativas
Atualizado em: 30/10/2026 · por: Claude Code (sessão na nuvem)
Fontes: leitura do Drive de officecont.asses@gmail.com em 30/10/2026 (só o primeiro nível de cada pasta; conteúdo lido apenas no `CLAUDE.md` da 1015). Contagens são aproximadas: a listagem do Drive pagina de forma irregular.

## Regra
O Drive é só leitura para a montagem da base. Nada é criado, movido, renomeado ou apagado lá sem pedido expresso (ver regra 10 do `LEIA-ME.md`). Este arquivo só descreve onde as coisas estão.

## Estrutura geral da raiz ("O meu disco")
- Pastas de clientes ativos: `NNN_NOME` (cerca de 70). Dentro de cada uma: `AAAA/` (por ano), com `001_DOCUMENTOS DIGITALIZADOS`, `002_FISCAL`, `003_FOPAG`, `004_DECLARAÇÕES`, `005_CONTABIL RELATORIOS`, `008_NOTAS FISCAIS` e outras; `CADASTRO` e `ANOS ANTERIORES` ao lado do ano.
- Pastas administrativas `1000` a `1023` e algumas sem número (lista abaixo).
- Uma planilha solta na raiz: `GATILHO_DP_REINF`.

## Estrutura de um cliente em 2026 (conferida nos clientes 205 e 261)
- `2026/002_FISCAL/001_FEDERAIS | 002_MUNICIPAIS | 003_ESTADUAIS`, cada uma com subpastas de mês `01_JANEIRO` a `12_DEZEMBRO`.
- `2026/004_DECLARAÇÕES/` com: `001_DEC PREF`, `002_SPED CONTRIBUICOES MENSAL`, `003_SPED FISCAL ICMS MENSAL`, `004_MIT`, `005_ GIA MENSAL` (o nome tem um espaço depois do `_`), `006_NOTA FISCAL GAÚCHA`, `007_SEDIF`, `008_DCTF WEB`, `009_REINF`, `010_ESOCIAL`, `011_DEFIS`; cada uma com subpastas de mês.
- `2026/008_NOTAS FISCAIS/` com subpastas de mês.
- Não conferi todos os clientes: pelo menos o cliente 227 (Progest) não tem a pasta `2026`.

## Pastas administrativas
| Pasta | O que tem (primeiro nível) | Observação |
|---|---|---|
| `1000_INATIVAS` | 51 pastas de clientes inativos | Não aberto por dentro |
| `1001_PLANILHAS E FORMULARIOS` | Pastas `FISCAL`, `CONTABILIDADE`, `MODELOS - USO INTERNO`, `PASSO A PASSOS_FISCAL_CONTÁBIL`, `LEGISLAÇÃO`; planilhas de 2021 e `INATIVAS.xlsx` | Subpastas não abertas |
| `1002_GIAN` | Pastas de 2020 a 2025, `A PAGAMENTOS BB`, `DIVERSOS`, `CURSO MAPEANDO PROCESSOS CONTABEIS`, `Teste Gian`; PDFs de rescisão | Não aberto por dentro |
| `1003_IMPOSTO DE RENDA PF` | `IRPF 2017` a `IRPF 2026`; 2 arquivos | |
| `1004_SUPPORTIT` | ~49 arquivos técnicos (logs, executáveis `grive`, backups `.CMP`) e `Office 2013` | Aparenta material técnico antigo; não aberto |
| `1006_DIRF`, `1007_DMED`, `1008_DIMOB` | Arquivos de declaração de 2016 a 2021 | |
| `1009_SERVIÇOS EXTRAS` | `EVERTON L M RIBEIRO EIRELI`, `IRISAT` | Não aberto |
| `1010_COMUNICAÇÕES` | Comunicados, tutorial de NFS-e padrão nacional, orientação contábil (imobilizado), `Officecont_passo_retencoes.html` | |
| `1011_ARQUIVOS REINF` | `2025`, `2026` | |
| `1012_PASTAS SOLTAS` | `DIVERSOS`, `001_FISCAL x DP`, `JULIA`, `FISCAL`, `CAMILA`; 3 controles marcados `[ANTIGO]` | Pastas pessoais não vistas por dentro |
| `1013_IMPLATAÇÃO G-CLICK` | 4 planilhas de dados cadastrais (Omie.G-Click) | |
| `1014_ARQUIVOS SOLTOS` | ~96 itens, quase todos planilhas Google (`GATILHO_SIMPLES_2026`, `SIMPLES 2026`, `PARCELAMENTOS`, balanços de suspensão da REAT) e a pasta `Kit_Modelo_Manual_Officecont` | Há nomes repetidos (ex.: `GATILHO_SIMPLES_2026` em duplicidade) |
| `1015_ROTINA AUTOMATICA` | `001 FECHAMENTO FISCAL`, `002 FISCAL CAMILA`, `003 CONTABILIDADE`, `SIMPLES NACIONAL`, `CLAUDE.md` | Ver abaixo |
| `1020_PROCESSOS IRPF` | 5 pastas de pessoas, com data | |
| `1021_MEIS` | 3 pastas de pessoas | |
| `1022_EMPRESAS EM CONSTITUIÇÃO` | 9 pastas (REMAX Moderna, Belém Holding, Zenith Paracuru, Ipanema Lar de Idosos, Nadal Incorporações, Dizi Snacks, Tacom Projetos POA, Blower, Giatech) | |
| `1023_CONTROLE DE CERTIDÕES` | Zips de certidões e diagnósticos de carteira (jul e ago/2026); extratos da Tacom (Palhoça) | |
| `REFORMA TRIBUTÁRIA` | 6 arquivos (Resolução CGSN 186/2026, comunicado do Simples, exclusões da base IBS/CBS) | |
| `NOTAS IMPORTAÇÃO SITTAX`, `PROSPERE BPO`, `DBSeller`, `04613222` | Poucas pastas ou 1 arquivo cada | Não abertos |

## `1015_ROTINA AUTOMATICA` em detalhe
- `001 FECHAMENTO FISCAL/001_FECHAMENTO FISCAL/07_JULHO`, `08_AGOSTO`, `09_SETEMBRO`: material do fechamento fiscal, com subpastas numeradas de origem (`001 ARQUIVOS REINF`, `002 ARQUIVOS MUNICIPAIS`, `003 ARQUIVOS PORTAL NACIONAL`, `004 ARQUIVOS ICMS`, `005 ARQUIVOS CONFERÊNCIAS`, `006 XML PORTAL NACIONAL`, `007 ARQUIVOS SIEG`, `008 ARQUIVOS DOMÍNIO`, `009 IMPOSTOS FEDERAIS`, `010 EFD CONTRIBUIÇÕES`). Em 05/10/2026 os arquivos de julho e agosto foram movidos para as pastas dos clientes; ficaram os pendentes (Tacom, itens sem cliente, conferências) e os logs `LOG_REALOCACAO_...` em cada mês.
- `001 FECHAMENTO FISCAL` também tem `ARQUIVOS EXTENSÃO - CODE - CLAUDE` e `SOLTOS-CONTROLES`.
- `002 FISCAL CAMILA`: pasta `.claude`, `ROBO PORTAL NACIONAL`, `ROBO DECWEB - PORTO ALEGRE`.
- `003 CONTABILIDADE`: `fechamento-contabil-dominio.zip` (skill) e `planilhamodeloimportacaolancamentoscontabeis.xlsx`.
- `SIMPLES NACIONAL`: subpastas `2025` e `2026`.

## O `CLAUDE.md` da `1015_ROTINA AUTOMATICA`
Atualizado em 29/10/2026 (Drive). É uma cópia do modelo de repositório único de outro escritório: o título diz "Repositório único da Fernanda Poleto (Terceirizza)" e aponta a base para `Clientes Contabilidade\999 ROTINAS AUTOMÁTICAS\003 CODE FERNANDA\00 BASE`, caminho que não existe neste Drive. Não foi alterado. Pendente: a pessoa decidir se é modelo ou se deve ser adaptado. A base deste escritório está neste repositório git.

## O que ainda não foi visto
- Interior de `1000`, `1001`, `1002`, `1009`, `1012` (pastas pessoais), `1022`, `DBSeller`, `PROSPERE BPO`, `SITTAX`.
- Quais planilhas de controle estão em uso (só a pessoa sabe).
