# Checklist de documentos por etapa e tabela de classificação de extrato

Use este arquivo como apoio das Etapas 1-3 do `SKILL.md`. Ele não substitui o julgamento sobre o histórico
real do cliente (Etapa 1) — é um ponto de partida para quando o histórico do razão não decidir sozinho
como classificar um lançamento novo.

## Onde pedir para o analista procurar

Quando um documento não tiver sido enviado na conversa, peça ao analista para indicar:
- Se está salvo no **Drive do cliente** (peça o nome/código da pasta, já que a estrutura de pastas varia
  de cliente para cliente) — nunca assuma um caminho de pasta sem confirmação.
- Ou se ele vai **baixar diretamente** (ex.: do portal da Receita Federal, do internet banking, do
  Domínio) e enviar na conversa.

Nunca presuma que um documento "deve existir" e siga sem ele — se a etapa depende dele, pare e peça.

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

## Checklist de saída da Etapa 2

- [ ] Saldo inicial da planilha de importação = saldo inicial do extrato de cada conta
- [ ] Todo lançamento do extrato tem uma linha classificada (conta débito e conta crédito)
- [ ] Lançamentos sem classificação clara estão marcados como pendência, não "chutados"
- [ ] Planilha salva em `Meu Drive\1015_ROTINA AUTOMATICA\003 CONTABILIDADE\planilhamodeloimportacaolancamentoscontabeis`
