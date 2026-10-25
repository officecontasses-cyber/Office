# Integração dos módulos ao contábil no Domínio — ordem e pontos de conferência

Este arquivo apoia a Etapa 4 do `SKILL.md`. Ele descreve a lógica geral de por que cada módulo precisa
ser integrado antes do contábil e o que conferir em cada um — **não é uma transcrição do manual de
integração do Domínio**, que o colaborador deve ter disponível no próprio sistema ou no suporte Thomson
Reuters/Domínio. Sempre que uma tela, campo ou nome de rotina específico do Domínio estiver em jogo,
peça ao colaborador para confirmar na tela real do sistema (ou no manual dele) em vez de aceitar como certo
um nome de tela ou campo citado de memória — nomes de rotina mudam entre versões do sistema.

## Relatórios pedidos já na Etapa 1 (não só na hora de integrar)

Estes relatórios do Domínio já são pedidos no pacote da Etapa 1 do `SKILL.md` (item F), não só quando
chegar nesta etapa — eles dão mais dados para cruzar na conciliação (Etapa 5) e ajudam a pegar erro de integração
antes dele virar pendência no fim:

- **Relatório de entradas** (notas de compra/aquisição do período).
- **Relatório de saídas** (notas de venda/faturamento do período).
- **Relatório de serviços prestados e tomados**, quando o cliente emitir ou tomar nota de serviço.
- **Apuração de impostos do período** — ver o caminho confirmado abaixo, que varia por tributo.

Para entradas, saídas e serviços, ainda não há um caminho de tela confirmado — pergunte ao colaborador como
ele normalmente extrai esses relatórios no sistema dele, em vez de aceitar um caminho de menu citado de
memória, ou peça que ele consulte a central de suporte do Domínio (suporte.dominioatendimento.com).

### Apuração de impostos — caminho confirmado (central de suporte do Domínio, solução nº 1998)

**Demonstrativo de impostos (uso geral)**: `Relatórios > Impostos > Demonstrativos` — define a
competência inicial/final, seleciona os impostos desejados (ou o botão "Todos"), o detalhamento em
"Opções" e a ordem (Data ou Documento), e confirma em "OK".

**Atenção — este demonstrativo geral NÃO mostra os impostos abaixo**, porque cada um tem relatório
próprio no sistema:

| Imposto | Onde está o demonstrativo específico |
|---|---|
| 44 — Simples Nacional | `Relatórios > Impostos > Simples Nacional` |
| 4, 5, 17, 19 — PIS e COFINS (cumulativo ou não-cumulativo) | `Relatórios > Acompanhamentos > Informativos de PIS e COFINS`; para conferência detalhada de créditos e débitos (EFD-Contribuições): `Movimentos > Apuração de PIS/COFINS` |
| 38, 67, 68 — Retenções e substituição tributária (inclusive retenção de órgão público) | `Relatórios > Acompanhamentos > Retenções` |

Um cliente que apure PIS/COFINS (Lucro Presumido, no cumulativo, ou Lucro Real, no não cumulativo) **não
vai aparecer no Demonstrativo geral** — use o caminho de PIS/COFINS acima para esse tributo
especificamente. Essa tabela vem de uma fonte confirmada (central de suporte oficial do Domínio); mesmo
assim, confirme com o colaborador se a versão/plano do Domínio da empresa segue a mesma nomenclatura de
menu, já que o sistema pode variar por módulo contratado.

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
  Etapa 5 (conciliação de tributos a recolher), junto com os comprovantes e a situação fiscal do pacote
  da Etapa 1.
- Créditos de PIS/COFINS/ICMS reconhecidos nas entradas estão de fato lançados nas contas de tributos a
  recuperar, não direto em despesa.

### 2. Folha de pagamento → Contábil
Alimenta: despesa de salários, encargos patronais (INSS, FGTS), provisões (férias, 13º quando aplicável),
retenções a recolher (INSS, IRRF, FGTS).

Conferir após a integração:
- Total líquido da folha integrada = total que de fato será pago/foi pago no extrato bancário (cruza com
  a Etapa 3) — nunca deixar passar pela conciliação sem bater.
- Encargos patronais e provisões (férias/13º) foram gerados, não só o líquido da folha.
- Retenções de terceiros (INSS, IRRF) estão em conta de obrigação a recolher, com o valor que será pago
  no vencimento.

### 3. Patrimônio (ativo imobilizado) → Contábil
Alimenta: depreciação do período, baixas/altas de bens.

Conferir após a integração:
- Toda aquisição e baixa de bem do período (identificada nos documentos do cliente do pacote da Etapa 1) está
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
