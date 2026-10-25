# Lançamentos bancários para importar no Domínio (Etapa 3)

Apoia a Etapa 3 do `SKILL.md`: dos extratos da Etapa 1 até a planilha de importação do Domínio.

## Layout da planilha de importação (modelo do escritório)

Modelo: `Meu Drive\1015_ROTINA AUTOMATICA\003 CONTABILIDADE\planilhamodeloimportacaolancamentoscontabeis.xlsx`
(aba `Planilha1`). A planilha de importação de cada cliente usa **exatamente** este cabeçalho, nesta
ordem — não renomeie, não reordene e não acrescente colunas:

| Coluna | Conteúdo |
|---|---|
| Data | Data do lançamento (data do movimento no extrato) |
| Cód. Conta Debito | Código reduzido da conta no Domínio (o mesmo da coluna "Código Domínio" do mapa) |
| Cód. Conta Credito | idem |
| Valor | Valor positivo, com ponto como separador decimal (como no modelo: `5000.00`) |
| Cód. Histórico | Código de histórico padrão do Domínio, se o cliente usar; pode ficar vazio |
| Complemento Histórico | Texto do histórico (siga o histórico padrão do mapa; se não houver, use a descrição do extrato, sem dados pessoais) |
| Inicia Lote | Ver abaixo |
| Código Matriz/Filial | Só se o cliente tiver filial no Domínio; senão vazio |
| Centro de Custo Débito / Crédito | Só se o cliente usar centro de custo; senão vazio |

**Lançamento simples (uma conta a débito, uma a crédito):** uma linha com as duas contas preenchidas
(no modelo: `1/10/2026 | 8 | 5 | 5000.00 | | DEPOSITO C/C | 854`).

**Lançamento com várias linhas** (ex.: um DARF que paga IRPJ e CSLL; uma parcela de empréstimo com
principal e juros): no modelo, a primeira linha do lote tem só uma das contas e a coluna `Inicia Lote`
preenchida; as linhas seguintes do mesmo lote têm só a outra conta e `Inicia Lote` vazio (no modelo:
crédito 245 de 100.000,00 com `Inicia Lote` = 99, seguido de débitos 5 e 55 de 10.000,00 e 90.000,00).
O total a débito e a crédito de cada lote precisa fechar.

**O que ainda não está confirmado:** o significado exato do valor em `Inicia Lote` (no modelo aparecem
99 e 854 — pode ser número do lote ou só um marcador) e se o Domínio exige algum formato de data
específico. No primeiro uso com um cliente, peça ao colaborador para importar e confirmar que o Domínio
aceitou; se ele souber a regra, registre-a aqui em vez de manter a dúvida.

## Planilha de revisão

`CONCILIACAO BANCARIA {NNN} {MM-AAAA}.xlsx`, uma aba por conta bancária, uma linha por movimento do
extrato:

| Coluna | Conteúdo |
|---|---|
| Data | Do extrato |
| Descrição no extrato | Como veio do banco |
| Valor | Com sinal (entrada +, saída −) |
| Conta débito | Código Domínio + nome |
| Conta crédito | Código Domínio + nome |
| Histórico | O que vai para a importação |
| Origem | `regra` (com o nº/descrição da regra do mapa) · `proposta` · `pendente` |
| Observação | Comprovante usado, motivo da pendência, regra nova a gravar no mapa |

No rodapé de cada aba: saldo inicial, total de entradas, total de saídas, saldo final calculado, saldo
final do extrato e diferença (tem que ser zero).

## Armadilhas mais comuns

- **Receita ou despesa lançada duas vezes.** Se o módulo fiscal integra a receita (D Clientes /
  C Receita), o recebimento no banco é D Banco / C Clientes — não C Receita. O mesmo para folha (a
  despesa vem do módulo de folha; o banco baixa Salários a pagar) e tributos (a apuração gera o tributo
  a recolher; o banco o baixa). Siga o que o mapa mostra que o cliente faz: há clientes em que a receita
  é lançada pelo banco porque não há integração fiscal — nesse caso, é o mapa que diz.
- **Transferência entre contas do próprio cliente.** Aparece como saída num extrato e entrada no outro.
  Lance uma vez só (D banco de destino / C banco de origem) e marque a outra linha como "contrapartida
  da transferência" na revisão.
- **Aplicação e resgate automáticos.** Muitos bancos aplicam e resgatam sozinhos todo dia. Agrupe por
  dia quando o cliente fizer assim (veja o mapa), ou lance um a um — mas nunca deixe de fora, senão o
  saldo da aplicação não fecha.
- **Estorno.** Identifique o lançamento original antes de lançar o inverso; estorno sem original no
  período é pendência.
- **Pagamento que mistura mais de um tributo ou conta.** Use o detalhamento do comprovante (item B da
  Etapa 1) e monte um lote de várias linhas; sem detalhamento, é `pendente` — nunca rateio por
  estimativa.
- **Mesma contraparte, contas diferentes.** Já se confirmou na prática que um PIX para o mesmo sócio pode
  ser pró-labore num valor e mútuo em outro: confira a condição da regra do mapa, não só o nome.
- **PIX recebido sem identificação.** Nunca direto em receita — pode ser empréstimo de sócio, devolução
  ou adiantamento. É `pendente` até o colaborador ou o cliente identificar.

## Tabela de classificação padrão (só quando nenhuma regra do mapa cobrir)

Ponto de partida genérico, não regra fixa: sempre prefira as regras `confirmada` do mapa contábil do
cliente. O que sair desta tabela é `proposta` e precisa da confirmação do colaborador.

| Lançamento no extrato              | Lançamento contábil sugerido                              |
|-------------------------------------|-------------------------------------------------------------|
| Recebimento de cliente (PIX/depósito/boleto) | D Banco / C Clientes a receber |
| PIX recebido sem identificação      | `pendente` — se o colaborador decidir lançar já, D Banco / C conta transitória "a regularizar" do cliente |
| Pagamento a fornecedor              | D Fornecedores / C Banco |
| Tarifa bancária                     | D Despesa com tarifas / C Banco |
| IOF                                 | D Despesa com IOF / C Banco |
| Juros/rendimento de aplicação       | D Banco (ou Aplicação) / C Receita financeira |
| Parcela de empréstimo (principal + juros) | Lote: D Empréstimos (principal) + D Despesa financeira (juros) / C Banco |
| Pagamento de folha (líquido)        | D Salários a pagar / C Banco |
| Pagamento de tributo                | D Tributo a recolher (conta específica) / C Banco |
| Estorno                             | Lançamento inverso do original — identificar o original antes de lançar |
| Compensação de cheque               | Baixa de "cheques emitidos pendentes" |

## Checklist de saída da Etapa 3

- [ ] Cada extrato fecha sozinho: saldo inicial + entradas − saídas = saldo final
- [ ] Saldo inicial de cada extrato = saldo de abertura do mapa (aba `Saldos`)
- [ ] Toda linha do extrato está na planilha de revisão com origem `regra`, `proposta` ou `pendente`
- [ ] Nenhuma `proposta` sem confirmação do colaborador na planilha de importação
- [ ] `pendente` resolvidas ou lançadas na transitória com a pendência registrada
- [ ] Transferências entre contas do cliente lançadas uma vez só
- [ ] Cada lote de várias linhas fecha débito = crédito
- [ ] Soma da planilha de importação por conta bancária = movimento do extrato (menos as `pendente`
  deixadas de fora, listadas)
- [ ] Planilha de importação no layout exato do modelo, salva em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`
  do cliente (não na pasta do modelo, que é só o template)
- [ ] Colaborador importou no Domínio e confirmou que não houve erro
