# Checklist de documentos por etapa e tabela de classificação de extrato

Use este arquivo como apoio das Etapas 1-3 do `SKILL.md`. Ele não substitui o julgamento sobre o histórico
real do cliente (Etapa 1) — é um ponto de partida para quando o histórico do razão não decidir sozinho
como classificar um lançamento novo.

## Onde procurar antes de perguntar

Com o cliente e a competência confirmados (ver "Antes de começar" no `SKILL.md`), procure você mesmo na
pasta do cliente no Drive antes de pedir qualquer coisa ao analista. A estrutura típica de um cliente
deste perfil, dentro da pasta do ano, costuma ter (confirme com o que encontrar, não assuma que todo
cliente tem exatamente isso):

- `001_DOCUMENTOS DIGITALIZADOS/{mês}` — comprovantes de pagamento digitalizados (Etapa 3).
- `002_FISCAL` — documentos do módulo fiscal.
- `004_DECLARAÇÕES` — declarações entregues.
- `005_CONTABIL RELATORIOS/{mês}` — razão, balancete e planilhas de fechamento já geradas (Etapa 1 e
  saída das Etapas 2 e 4).
- `006_SPED CONTABIL ANUAL` — ECD, quando aplicável.
- Uma pasta de `CADASTRO` (fora da pasta do ano) com certidões/situação fiscal e dados cadastrais.

Só depois de checar essas pastas, peça ao analista para indicar onde está (ou enviar) o que você não
encontrou. Nunca presuma que um documento "deve existir" e siga sem ele — se a etapa depende dele e você
não achou nem no Drive nem na conversa, pare e peça.

## Checklist por etapa

### Etapa 1 — Histórico contábil
- [ ] Razão contábil do início do último ano-calendário até o mês atual
- [ ] Plano de contas
- [ ] Balancete mais recente

### Etapa 2 — Extratos bancários
- [ ] Extrato de **cada** conta bancária/aplicação do período (CSV preferencialmente; PDF ou outro formato legível aceito)
- [ ] Saldo inicial de cada conta, para conferência de abertura

### Etapa 3 — Documentos e comprovantes
- [ ] Comprovantes de pagamentos federais do período (DARF, GPS, guias de parcelamento)
- [ ] Situação fiscal da empresa junto à Receita Federal (certidão/extrato — para conciliar parcelamentos
  e débitos ativos; não assumir "sem parcelamento" sem checar)
- [ ] Documentos estaduais aplicáveis ao cliente (guias, declarações, SPED quando houver)
- [ ] Documentos municipais aplicáveis ao cliente (ISS, declarações)
- [ ] Qualquer outro comprovante que o cliente já tenha enviado e ainda não esteja lançado

## Tabela de classificação padrão de extrato bancário (quando o histórico do cliente não decidir)

Esta tabela é um ponto de partida genérico, não uma regra fixa — sempre prefira a lógica que o próprio
razão do cliente já usa (Etapa 1). Use-a só quando aparecer um tipo de lançamento sem precedente claro no
histórico, e sinalize ao analista que a classificação é uma proposta a confirmar, não um fato.

| Lançamento no extrato              | Lançamento contábil sugerido                              |
|-------------------------------------|-------------------------------------------------------------|
| Recebimento de cliente (PIX/depósito/boleto) | D Banco / C Clientes a receber |
| PIX recebido sem identificação      | D Banco / C conta de obrigações a regularizar (investigar antes de confirmar) |
| Pagamento a fornecedor              | D Fornecedores / C Banco |
| Tarifa bancária                     | D Despesa com tarifas / C Banco |
| IOF                                 | D Despesa com IOF / C Banco |
| Juros/rendimento de aplicação       | D Banco / C Receita financeira |
| Parcela de empréstimo (principal + juros) | D Empréstimos (principal) + D Despesa financeira (juros) / C Banco |
| Pagamento de folha (líquido)        | D Salários a pagar / C Banco |
| Pagamento de tributo                | D Tributo a recolher (conta específica) / C Banco |
| Estorno                             | Lançamento inverso do original — identificar o lançamento estornado antes de lançar |
| Compensação de cheque               | Baixa de "cheques emitidos pendentes" |

**Nunca** classifique um PIX recebido sem identificação direto como receita — pode ser empréstimo de
sócio, devolução ou adiantamento; sinalize como pendência de identificação se o histórico do cliente não
esclarecer.

**A mesma contraparte pode exigir contas diferentes dependendo do valor.** Já se confirmou na prática que
um Pix para a mesma pessoa (ex.: um sócio) pode ser um mútuo num valor e pró-labore em outro — não
classifique só pelo nome de quem recebe/envia; confira se o valor bate com algum saldo ou padrão já
conhecido daquela conta específica antes de decidir.

**Lançamento que mistura mais de um tributo/conta no mesmo pagamento (ex.: um DARF que paga IRPJ e CSLL
juntos, ou uma guia que soma PIS e COFINS) não deve ter o valor dividido por estimativa.** Se a fonte que
você está lendo (razão resumido por conta, por exemplo) não mostrar como o valor se divide entre as
contas, marque como pendência e peça para conferir o detalhe no Domínio ou no comprovante — não invente a
proporção.

## Checklist de saída da Etapa 2

- [ ] Saldo inicial da planilha de importação = saldo inicial do extrato de cada conta
- [ ] Todo lançamento do extrato tem uma linha classificada (conta débito e conta crédito)
- [ ] Lançamentos sem classificação clara, ou com mais de uma contrapartida não detalhada, estão
  marcados como pendência, não "chutados"
- [ ] Planilha final salva na pasta do cliente, em `005_CONTABIL RELATORIOS/{ano}/{mês}` (não no modelo
  genérico do escritório em `1015_ROTINA AUTOMATICA\003 CONTABILIDADE`, que é só o template de partida)
