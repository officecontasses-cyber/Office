# Integração dos módulos ao contábil no Domínio — ordem e pontos de conferência

Este arquivo apoia a Etapa 4 do `SKILL.md`. Ele descreve a lógica geral de por que cada módulo precisa
ser integrado antes do contábil e o que conferir em cada um — **não é uma transcrição do manual de
integração do Domínio**, que o analista deve ter disponível no próprio sistema ou no suporte Thomson
Reuters/Domínio. Sempre que uma tela, campo ou nome de rotina específico do Domínio estiver em jogo,
peça ao analista para confirmar na tela real do sistema (ou no manual dele) em vez de aceitar como certo
um nome de tela ou campo citado de memória — nomes de rotina mudam entre versões do sistema.

## Relatórios a pedir antes de começar (não só na hora de integrar)

Peça estes relatórios do Domínio desde "Antes de começar" no `SKILL.md`, não só quando chegar nesta
etapa — eles dão mais dados para cruzar na conciliação (Etapa 5) e ajudam a pegar erro de integração
antes dele virar pendência no fim:

- **Relatório de entradas** (notas de compra/aquisição do período).
- **Relatório de saídas** (notas de venda/faturamento do período).
- **Relatório de serviços prestados e tomados**, quando o cliente emitir ou tomar nota de serviço.
- **Apuração de impostos do período** (demonstrativo de PIS/COFINS e, quando aplicável ao cliente,
  ICMS/ISS).

Não tenho um manual confiável do Domínio com o caminho exato de tela para gerar cada um — pergunte ao
analista como ele normalmente extrai esses relatórios no sistema dele, em vez de aceitar um caminho de
menu citado de memória.

## Por que a ordem importa

Os módulos fiscal, folha de pagamento e patrimônio geram lançamentos que **alimentam** o contábil — se o
contábil for fechado antes de todos eles serem integrados, o balancete fica incompleto e qualquer
conciliação ou apuração feita em cima dele (Etapas 5 e 6) vai estar errada. A ordem sugerida abaixo evita
reprocessamento: cada módulo depende de dados que o anterior já consolidou.

## Ordem sugerida e o que conferir

### 1. Fiscal → Contábil
Alimenta: receita bruta, tributos sobre venda (ICMS, PIS/COFINS, ISS conforme o caso), tributos a
recuperar nas compras.

Conferir após a integração:
- Total de notas de saída do período integrado = total apurado no módulo fiscal do Domínio para o mesmo
  período (sem notas faltando nem duplicadas).
- Tributos a recolher gerados no fiscal batem com o que será pago (ou já foi pago) — isso alimenta a
  Etapa 3 (situação fiscal) e a Etapa 5 (conciliação de tributos a recolher).
- Créditos de PIS/COFINS/ICMS reconhecidos nas entradas estão de fato lançados nas contas de tributos a
  recuperar, não direto em despesa.

### 2. Folha de pagamento → Contábil
Alimenta: despesa de salários, encargos patronais (INSS, FGTS), provisões (férias, 13º quando aplicável),
retenções a recolher (INSS, IRRF, FGTS).

Conferir após a integração:
- Total líquido da folha integrada = total que de fato será pago/foi pago no extrato bancário (cruza com
  a Etapa 2) — nunca deixar passar pela conciliação sem bater.
- Encargos patronais e provisões (férias/13º) foram gerados, não só o líquido da folha.
- Retenções de terceiros (INSS, IRRF) estão em conta de obrigação a recolher, com o valor que será pago
  no vencimento.

### 3. Patrimônio (ativo imobilizado) → Contábil
Alimenta: depreciação do período, baixas/altas de bens.

Conferir após a integração:
- Toda aquisição e baixa de bem do período (identificada na Etapa 3, pelos comprovantes do cliente) está
  cadastrada no módulo de patrimônio antes de gerar a depreciação — bem cadastrado depois da geração fica
  de fora do cálculo do mês.
- O valor de depreciação gerado é coerente com o que a skill `ativo-imobilizado-depreciacao` calcularia
  para os mesmos bens (use-a para o cálculo em si; aqui só se confere se o Domínio gerou algo plausível).

### 4. Outros módulos que alimentem o contábil (quando aplicável ao cliente)
Ex.: contas a pagar/receber, se o cliente operar com esses módulos separados do fiscal. Confira, para
qualquer módulo adicional, se ele já foi integrado **antes** de declarar a Etapa 4 concluída — um módulo
esquecido é a causa mais comum de divergência só descoberta na conciliação (Etapa 5).

## Checklist de saída da Etapa 4

- [ ] Fiscal integrado e conferido (saída/entrada, tributos)
- [ ] Folha integrada e conferida (líquido bate com o banco, encargos e provisões geradas)
- [ ] Patrimônio integrado e conferido (bens do período cadastrados antes da geração, depreciação plausível)
- [ ] Qualquer outro módulo usado pelo cliente também integrado
- [ ] Planilha/arquivo de integração salvo na pasta do cliente, ano do fechamento, em
  `005_CONTABIL RELATORIOS`, subpasta do mês (ou pasta própria do período, se maior que um mês)
