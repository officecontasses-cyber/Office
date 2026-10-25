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
conciliação ou apuração feita em cima dele (Etapas 5 e 6) vai estar errada. A ordem abaixo evita
reprocessamento: cada módulo depende de dados que o anterior já consolidou.

## Antes de integrar: a lista de módulos do cliente

Monte a lista a partir da aba `Perfil` do mapa contábil do cliente e confirme com o pacote da Etapa 1:
houve nota de entrada/saída/serviço no período? Há folha ou só pró-labore? O cliente tem bens no módulo
de patrimônio? Usa algum outro módulo? Cliente sem integração fiscal (receita e tributos entram por
outro caminho) também precisa estar marcado no `Perfil` — senão o fiscal parece "esquecido".

## Ordem e o que conferir em cada módulo

Depois de cada integração, peça o razão (ou o relatório de lançamentos gerados) das contas que o módulo
alimenta e confira com os relatórios do pacote da Etapa 1. Diferença encontrada se corrige **no módulo**,
com reintegração — não com lançamento manual no contábil.

### 1. Fiscal → Contábil
Alimenta: receita bruta, tributos sobre receita e compras, tributos a recuperar, retenções.

Conferir em todos os regimes:
- Receita do razão no período = relatório de saídas + serviços prestados (sem notas faltando, duplicadas
  ou canceladas lançadas). Receita **acima** do relatório depois da Etapa 3 costuma ser duplicidade com o
  banco (recebimento lançado como receita em vez de baixa de Clientes).
- Entradas integradas = relatório de entradas + serviços tomados, nas contas que o mapa mostra.
- Retenções (ISS, IRRF, PIS/COFINS/CSLL, INSS) = relatório de retenções (`Relatórios > Acompanhamentos >
  Retenções`): retidas pelo cliente como tomador em obrigação a recolher; retidas dele como prestador em
  tributo a compensar/recuperar, não em despesa.

Conferir conforme o regime:

| Regime | O que o fiscal precisa ter gerado no contábil |
|---|---|
| **Simples Nacional** | Simples a recolher = relatório do Simples (`Relatórios > Impostos > Simples Nacional`) da competência. Não há crédito de PIS/COFINS a recuperar nas compras — se aparecer, a integração está configurada errada |
| **Lucro Presumido** | PIS/COFINS cumulativos a recolher = informativo de PIS/COFINS (sem créditos nas compras); ISS e ICMS conforme a atividade. IRPJ/CSLL trimestrais: se o cliente apura no módulo fiscal do Domínio, a provisão entra nos meses de fechamento de trimestre — confira com a apuração; se não, ficam para a Etapa 6 |
| **Lucro Real** | PIS/COFINS não cumulativos: débitos sobre a receita **e** créditos sobre as compras em tributos a recuperar (não direto em despesa) = `Movimentos > Apuração de PIS/COFINS`. ICMS e ISS conforme a atividade. IRPJ/CSLL ficam para a Etapa 6 |

Os tributos gerados no fiscal alimentam a conciliação de tributos a recolher da Etapa 5, junto com os
comprovantes e a situação fiscal do pacote da Etapa 1.

### 2. Folha de pagamento → Contábil
Alimenta: despesa de salários e pró-labore, encargos patronais (INSS, FGTS), provisões (férias, 13º
quando aplicável), retenções a recolher (INSS, IRRF).

Conferir após a integração:
- Total líquido da folha integrada = o que foi pago no extrato (cruza com a Etapa 3): depois do
  pagamento, salários e pró-labore a pagar ficam zerados (ou com o saldo que se explica).
- Encargos patronais e provisões (férias/13º) foram gerados, não só o líquido da folha. No Simples, a
  parte patronal depende do anexo (há anexos em que o INSS patronal é recolhido fora do DAS) — confirme
  no `Perfil`/com o colaborador em vez de presumir.
- Retenções (INSS, IRRF) estão em obrigação a recolher, com o valor que será pago no vencimento.
- Cliente só com pró-labore: o módulo gera o pró-labore e o INSS/IRRF retidos — confira só isso.

### 3. Patrimônio (ativo imobilizado) → Contábil
Alimenta: depreciação do período, baixas/altas de bens.

Conferir após a integração:
- Toda aquisição e baixa de bem do período (identificada no pacote da Etapa 1 ou na importação bancária
  da Etapa 3) está cadastrada no módulo antes de gerar a depreciação — bem cadastrado depois da geração
  fica de fora do cálculo do mês.
- O valor de depreciação gerado é coerente com o que a skill `ativo-imobilizado-depreciacao` calcularia
  para os mesmos bens (use-a para o cálculo em si; aqui só se confere se o Domínio gerou algo plausível).
- Cliente com bens e sem módulo de patrimônio: a depreciação vira lançamento manual recorrente do
  `Perfil` e entra na planilha de ajustes.

### 4. Outros módulos que alimentem o contábil (quando aplicável ao cliente)
Ex.: contas a pagar/receber, se o cliente operar com esses módulos separados do fiscal. Confira, para
qualquer módulo adicional, se ele já foi integrado **antes** de declarar a Etapa 4 concluída — um módulo
esquecido é a causa mais comum de divergência só descoberta na conciliação (Etapa 5).

## Ajustes manuais

O que nenhum módulo gera entra na planilha `AJUSTES {NNN} {MM-AAAA}.xlsx`, no mesmo layout do modelo de
importação (`references/lancamentos-bancarios.md`), em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`:

- os lançamentos manuais recorrentes do `Perfil` do mapa (apropriações mensais, juros de mútuo,
  depreciação sem módulo etc.);
- o que o pacote da Etapa 1 mostrou que falta e não é de módulo (ex.: parcelamento novo da situação
  fiscal ainda não registrado no passivo).

Cada linha com o histórico e, na planilha de revisão do colaborador, o porquê. Nunca use ajuste manual
para cobrir diferença de integração.

## Checklist de saída da Etapa 4

- [ ] Lista de módulos do cliente montada (com o motivo de cada módulo fora da lista)
- [ ] Fiscal integrado e conferido: receita = saídas + serviços, entradas, retenções e tributos do regime
- [ ] Folha integrada e conferida (líquido bate com o banco, encargos e provisões gerados)
- [ ] Patrimônio integrado e conferido (bens do período cadastrados antes da geração, depreciação plausível)
- [ ] Qualquer outro módulo usado pelo cliente também integrado
- [ ] Divergências corrigidas no módulo e reconferidas, ou registradas como pendência aceita
- [ ] Planilha de ajustes (se houver) revisada e importada sem erro
- [ ] Razão e balancete exportados de novo, depois de tudo integrado (base da Etapa 5)
