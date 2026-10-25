# Pacote de documentos (Etapa 1)

Use este arquivo como apoio da Etapa 1 (preparar os documentos) do `SKILL.md`. A classificação dos
extratos (Etapa 3) está em `references/lancamentos-bancarios.md`.

## Onde procurar antes de pedir

Com o cliente e a competência confirmados (ver "Como o colaborador aciona" no `SKILL.md`), procure você
mesmo na pasta do cliente no Drive antes de pedir qualquer coisa. A estrutura típica de um cliente deste
perfil, dentro da pasta do ano, costuma ter (confirme com o que encontrar, não assuma que todo cliente
tem exatamente isso):

- `001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` (ex.: `09_SETEMBRO`) — documentos do cliente: extratos,
  comprovantes de pagamento, documentos de conciliação.
- `002_FISCAL` — documentos do módulo fiscal.
- `004_DECLARAÇÕES` — declarações entregues.
- `005_CONTABIL RELATORIOS/{MM_MÊS}` — razão, balancete e planilhas de fechamento já geradas.
- `006_SPED CONTABIL ANUAL` — ECD, quando aplicável.
- Uma pasta de `CADASTRO` (fora da pasta do ano) com cartão CNPJ, contrato social e certidões antigas.

Já se viu no Drive cliente guardando documento de um mês na pasta de outro mês, ou só em
`008_NOTAS FISCAIS`. Se não achar na pasta do mês, olhe as vizinhas antes de dar como faltando — e, se
achar fora do lugar, diga onde estava.

**Exports do SIEG:** procure no Drive pelo CNPJ do cliente. Os exports seguem o padrão
`Diagnostico_<CNPJ>.pdf` (débito federal RFB/PGFN) e `<CNPJ>_Certidao_<Esfera>.pdf` (Estadual,
Trabalhista, FGTS e, só para São Paulo, Municipal), agrupados em pastas `RAZÃO SOCIAL (CNPJ)` — formato
descrito na skill `controle-debitos-certidoes-clientes`. Use só se a data de emissão for recente (ver
regras de conferência abaixo).

## Pacote da Etapa 1 — onde salvar

| Item | Onde salvar |
|---|---|
| A. Extratos bancários | `{ano}/001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` de cada competência |
| B. Comprovantes de pagamento (cliente ou e-CAC) | `{ano}/001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` |
| C. Situação fiscal federal | `{ano}/001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` da última competência do fechamento |
| D. Certidão/situação de débitos estadual | idem C |
| E. Certidão/situação de débitos municipal | idem C |
| F. Relatórios do Domínio | `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}` |
| G. Documentos de conciliação do cliente | `{ano}/001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` |

Nome do arquivo é livre — você lê o conteúdo —, mas peça que o colaborador ponha a **data de emissão** no
nome dos itens C, D e E (ex.: `SITUACAO FISCAL RFB 25-10-2026.pdf`): é o que mostra, de relance, que o
relatório foi atualizado para este fechamento.

## Mensagem-modelo ao colaborador (início da Etapa 1)

Adapte ao que você já encontrou no Drive (✅ = já está lá, com o nome do arquivo; ⬜ = falta salvar).
Uma mensagem só, curta, sem repetir explicações que o colaborador já conhece:

> **Etapa 1 — Preparar os documentos · {NNN} {CLIENTE} · {competência(s)}**
> Antes de seguir, salve na pasta do cliente o que está com ⬜:
>
> **Banco** — em `001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}`
> ⬜ Extratos de todas as contas e aplicações ({lista de contas do razão, se já souber}) — CSV de preferência
>
> **Receita Federal (e-CAC)**
> ⬜ Relatório de situação fiscal emitido hoje
> ⬜ Comprovantes de pagamento do período — o cliente não enviou {ou: enviou só X}
>
> **Estado e município**
> ⬜ Certidão ou situação de débitos estadual
> ⬜ Certidão ou situação de débitos municipal
>
> **Domínio** — em `005_CONTABIL RELATORIOS/{MM_MÊS}`
> ⬜ Razão (desde jan/{ano anterior}), balancete, plano de contas
> ⬜ Entradas, saídas, serviços prestados/tomados e apuração de impostos do período
>
> **Do cliente** — o que tiver para conciliação (contratos, notas, recibos)
>
> Me responda **"salvei"** quando terminar, ou diga o que não conseguiu baixar.

## Regras de conferência do pacote (depois do "salvei")

Leia os arquivos; não aceite só a confirmação. Para cada item:

**A. Extratos bancários**
- Há um extrato para **cada** conta bancária e de aplicação que aparece no razão/balancete com saldo ou
  movimento no período — compare a lista de contas, não só a quantidade de arquivos.
- Cada extrato cobre do primeiro ao último dia de cada competência (sem buraco de dias).
- O saldo inicial do extrato bate com o saldo final do mês anterior no razão, quando o mês anterior já
  está fechado. Se não bater, aponte agora — é divergência de abertura, não da competência atual.
- Formato: CSV/OFX lido sem erro. Se só houver PDF, aceite, mas avise que a leitura é menos segura e
  confira os totais com mais cuidado.

**B. Comprovantes de pagamento**
- Para cada tributo que aparece na apuração de impostos (item F) com vencimento no período, há um
  comprovante — liste o que foi apurado e não tem comprovante, e o que tem comprovante e não foi apurado
  (pode ser parcelamento, multa ou pagamento de outra competência).
- DARF que paga mais de um código (ex.: IRPJ e CSLL juntos) vem com o detalhamento por código; se não
  vier, é pendência — não divida por estimativa.

**C, D, E. Situação fiscal federal, estadual e municipal**
- Data de emissão **posterior ao fim da última competência** do fechamento e de agora, durante este
  fechamento. Relatório mais antigo que isso é `desatualizado` — peça para emitir de novo, não use como
  se fosse atual.
- Registre o que cada um mostra: débitos em aberto (tributo, competência, valor), parcelamentos ativos,
  omissões de declaração, certidão negativa / positiva / positiva com efeitos de negativa. Isso vira
  insumo direto da Etapa 5.
- Export do SIEG (Diagnóstico federal, certidão estadual) pode complementar ou substituir D quando
  estiver dentro desse critério de data; o relatório de situação fiscal da Receita (C) continua sendo
  emitido pelo colaborador no e-CAC.

**F. Relatórios do Domínio**
- Razão do início do último ano-calendário até a competência; balancete da última competência; plano
  de contas.
- Relatórios fiscais (entradas, saídas, serviços, apuração de impostos) do mesmo período do fechamento.
- Se um relatório fiscal vier de período diferente do fechamento, aponte — é erro comum de filtro na
  exportação.

**G. Documentos do cliente**
- Não há regra fixa: liste o que veio. O que for necessário para conciliar e não veio, vira pendência
  com o cliente (`pendencias-fechamento-cliente`).

**Dados sensíveis:** relatórios e certidões podem trazer CPF de sócios e outros dados pessoais. Use só o
que for necessário para o fechamento e não repita no chat dados pessoais nem credenciais.

## Formato da resposta de conferência

Uma tabela por competência (ou uma única, se o período for curto):

| Item | Arquivo encontrado | Período / emissão | Situação | O que falta |
|---|---|---|---|---|

Depois da tabela: os achados que já saltam do pacote (débitos, parcelamentos, certidão positiva), as
pendências e a pergunta objetiva: "Sigo para a Etapa 2 com essas pendências registradas, ou você vai
salvar {X} antes?".

## SIEG: o que já ajuda hoje e rotina em desenho

**Hoje (sem rotina nova):** se o escritório já exportou do SIEG para o Drive o Diagnóstico federal e as
certidões do CNPJ, use esses arquivos como complemento do pacote, respeitando o critério de data acima. O
SIEG Docs Fiscais também guarda os XML de NF-e/CT-e/NFS-e do cliente, que servem para conferir os
relatórios de entradas, saídas e serviços do Domínio.

**Em desenho (ainda não implementado — não prometa ao colaborador como se existisse):** uma rotina para
baixar do SIEG, por CNPJ, o Diagnóstico, as certidões e os XML do período direto para a pasta do
cliente, reduzindo o passo manual da Etapa 1. Enquanto ela não existir, o pacote é montado como descrito
acima.
