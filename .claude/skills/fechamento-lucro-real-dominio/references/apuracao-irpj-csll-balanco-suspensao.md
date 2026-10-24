# Apuração de IRPJ/CSLL por levantamento de balanço — suspensão ou redução

Apoia a Etapa 6 do `SKILL.md`. Esta skill não recalcula a mecânica completa de LALUR/prejuízo fiscal —
isso é papel da skill `apuracao-lucro-real`, que deve ser acionada aqui. O que este arquivo cobre é a
lógica específica de **por que** se levanta um balanço para suspender ou reduzir o pagamento mensal, e o
checklist de insumos que as Etapas 1-5 precisam ter entregado antes de chegar aqui.

**Toda referência legal abaixo é um ponto de partida para pesquisa, não uma citação pronta.** Antes de
apresentar qualquer base legal ao analista como conclusão do fechamento, peça a ele para confirmar no
Lefisc o texto vigente (a lei pode ter sido alterada desde o conhecimento usado para montar este
material) e cite a fonte retornada — nunca a fonte "de memória" listada aqui.

## A lógica da suspensão/redução

Uma empresa do Lucro Real Anual recolhe, por padrão, uma **estimativa mensal** de IRPJ/CSLL (receita do
mês × percentual de presunção, nos mesmos percentuais do Lucro Presumido, com a alíquota de IRPJ/CSLL por
cima). Em vez de pagar essa estimativa todo mês, a empresa pode **levantar um balanço acumulado** (desde
janeiro, ou desde o início de apuração) e demonstrar que:

- O imposto devido pelo balanço acumulado é **menor** que a soma das estimativas já pagas no ano até
  aquele mês → a empresa pode **reduzir** o valor a pagar no mês (ou até os meses seguintes, até o fim do
  ano, se continuar demonstrando pelo balanço).
- O imposto devido pelo balanço acumulado é **zero ou negativo** (prejuízo fiscal/base negativa no
  acumulado) → a empresa pode **suspender** o pagamento do mês.

Pedir ao analista para confirmar no Lefisc, antes de citar como definitivo: o fundamento legal vigente
para a possibilidade de suspensão/redução por balanço (historicamente associado à Lei 8.981/1995 art. 35
e à IN RFB 1.700/2017 art. 47, mas confirme a redação e eventuais atualizações normativas atuais), e
qualquer exigência formal de **livro-caixa/balanço transcrito no Diário** até a data do vencimento do
tributo do mês em questão — essa exigência formal é frequentemente o ponto que gera autuação quando não
cumprida no prazo, então vale confirmar o prazo exato vigente no Lefisc antes de orientar o cliente.

## Insumos que as etapas anteriores precisam ter entregado

Antes de iniciar esta etapa, confirme que você já tem (se faltar algo, volte à etapa correspondente — não
avance com dado presumido):

- [ ] Balancete acumulado do período (desde o início do ano/apuração até o mês do balanço), já conciliado
  na Etapa 5 — não um balancete "de passagem" ainda com pendência relevante aberta.
- [ ] LAIR (resultado contábil antes de IR/CSLL) do acumulado.
- [ ] Soma das estimativas mensais já pagas no ano até o mês anterior (para comparar com o valor apurado
  pelo balanço).
- [ ] Saldo de prejuízo fiscal acumulado (Parte B do LALUR) e de base negativa de CSLL, se houver.
- [ ] Qualquer adição/exclusão específica do período (ver tabela de pontos de atenção abaixo) com o
  documento que a comprova (NF, ata, comprovante).

## Pontos de atenção mais comuns na Parte A (adições/exclusões) — verificar aplicabilidade e fonte no Lefisc

Esta lista é só um roteiro de perguntas a fazer sobre o período fechado — não assuma que algum destes
itens se aplica ao cliente sem evidência real na documentação recebida nas Etapas 1-3.

**Adições a verificar** (despesas contábeis que costumam não ser dedutíveis — confirmar fundamento e
vigência no Lefisc antes de tratar como certo):
- Multas de natureza punitiva (não as de natureza compensatória/moratória)
- Provisões não expressamente autorizadas pela legislação fiscal
- Resultado negativo de equivalência patrimonial
- Doações sem amparo em incentivo fiscal reconhecido
- Despesas com brindes
- Juros sobre capital próprio (JCP) pago/creditado acima do limite legal
- Tributos com exigibilidade suspensa sem o depósito judicial correspondente

**Exclusões a verificar**:
- Reversão de provisão que havia sido adicionada em período anterior
- Resultado positivo de equivalência patrimonial em controlada/coligada no Brasil
- Dividendos recebidos de outra pessoa jurídica no Brasil
- Depreciação fiscal acelerada (quando a contábil for mais lenta que a fiscalmente admitida) — confirme
  se o cliente tem essa opção formalizada

## Prejuízo fiscal e base negativa de CSLL

Historicamente, a compensação de prejuízo fiscal/base negativa em cada período é limitada a um percentual
do lucro líquido ajustado do próprio período (a trava de 30% é a mais conhecida) — confirme no Lefisc se
esse limite e o percentual continuam vigentes exatamente assim antes de aplicar. A skill
`apuracao-lucro-real` mantém o controle de saldo por ano de origem (Parte B) — não recrie esse controle
aqui, peça o saldo atualizado a ela.

## O que apresentar ao analista ao final da Etapa 6

1. Base de cálculo do balanço acumulado (LAIR + adições − exclusões).
2. Cada adição/exclusão aplicada, com a fonte legal confirmada no Lefisc.
3. Prejuízo fiscal/base negativa compensado no período, respeitando o limite vigente confirmado.
4. Conclusão: suspensão (zero a pagar) ou redução (valor menor que a estimativa), com o comparativo
   contra a soma das estimativas já pagas no ano.
5. DARF pronto (código, valor, vencimento) quando houver valor a recolher.
6. Alerta explícito se identificar que a formalidade exigida (ex.: transcrição do balanço no Diário até o
   vencimento) ainda não foi cumprida — isso é risco a reportar na Etapa 7, não algo a assumir resolvido.
