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

## Manuais do Domínio para mandar ao colaborador

Mande o link junto com cada integração pedida, para o colaborador consultar se tiver dúvida do que ou de
como integrar. São soluções da central de suporte do Domínio encontradas por busca; **os títulos abaixo
vêm do índice da busca — não foi possível abrir as páginas para conferir o conteúdo**. Se um link não
corresponder ao título, avise e troque aqui.

| Integração / assunto | Solução na central do Domínio |
|---|---|
| Fiscal → Contábil: configurar a integração contábil | [Como configurar integração contábil? (881)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=881) |
| Fiscal: cadastrar acumulador (abas Impostos e Contabilidade) | [Como cadastrar um acumulador? (1156)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=1156) |
| Fiscal: lançamento não gerado ou errado, contas no acumulador, regerar, fornecedor/cliente duplicado | [Perguntas e Respostas – Integração Contábil Escrita Fiscal (5551)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=5551) |
| Fiscal: integração dos impostos calculados | [Como configurar integração contábil dos impostos calculados? (231)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=231) |
| Fiscal: integração dos impostos lançados por nota | [Como configurar a integração contábil dos impostos lançados… (2846)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=2846) |
| Fiscal: integração de serviços prestados | [Como configurar a integração contábil de Serviços Prestados? (10185)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=10185) |
| Fiscal: integração e baixa de tributos federais | [Como configurar integração contábil e baixar tributos federais… (6703)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=6703) |
| Folha → Contábil: configurar e gerar a integração | [Como configurar e gerar Integração Contábil? (822)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=822) |
| Folha: copiar configuração da integração entre empresas | [Exportar integração contábil do módulo folha (4497)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=4497) |
| Folha: integração por colaborador | [Como fazer Integração Contábil por colaborador? (9272)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=9272) |
| Folha: integração por centro de custo com rateio | [Como configurar Integração por Centro de Custo com Rateio… (3566)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=3566) |
| Patrimônio: integração da baixa de bens | [Como configurar a integração contábil da baixa de Bens? (3522)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=3522) |
| Contabilidade: lançamento contábil manual | [Como fazer Lançamento Contábil? (1278)](https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=1278) |
| Apuração de impostos (relatórios) | Solução nº 1998 — ver abaixo |

Para a geração da integração do **patrimônio** (depreciação do período), a busca não trouxe um título
específico confirmado: oriente pelo caminho geral (gerar lançamentos contábeis nos parâmetros do módulo,
conta patrimonial no cadastro do bem, processo de integração contábil da competência) e peça ao
colaborador para conferir na central do Domínio.

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

**Acumuladores.** Cada acumulador define como um tipo de documento fiscal é escriturado; a aba
Contabilidade dele traz as contas contábeis dos lançamentos. Antes ou durante a integração:
- todo acumulador usado no período (inclusive um criado no mês) tem as contas contábeis preenchidas,
  coerentes com as contas do mapa do cliente;
- nota sem lançamento, ou lançamento em conta errada, quase sempre é acumulador sem conta ou com conta
  errada: ajuste o acumulador e regere os lançamentos (solução 5551), em vez de corrigir no contábil;
- o acumulador é configuração do módulo fiscal: combine com o fiscal antes de alterar um acumulador que
  ele também usa, e registre o ajuste no `Perfil` do mapa (Etapa 7).

Conferir em todos os regimes:
- Receita do razão no período = relatório de saídas + serviços prestados (sem notas faltando, duplicadas
  ou canceladas lançadas). Receita **acima** do relatório depois da Etapa 3 costuma ser duplicidade com o
  banco (recebimento lançado como receita em vez de baixa de Clientes).
- Entradas integradas = relatório de entradas + serviços tomados, nas contas que o mapa mostra.
- Retenções (ISS, IRRF, PIS/COFINS/CSLL, INSS) = relatório de retenções (`Relatórios > Acompanhamentos >
  Retenções`): retidas pelo cliente como tomador em obrigação a recolher; retidas dele como prestador em
  tributo a compensar/recuperar, não em despesa.
- Retenções federais × controle da REINF do DP (ver "Retenções — controle do DP" abaixo).

**Retenções — controle do DP (`CONTROLE | DP REINF'S`, aba `GATILHO`).** A 1ª aba da planilha resume,
por cliente (Nº) e competência (colunas `01.2026` … `12.2026`), o que o DP registrou nas abas mensais
(`MOD GERAL MM.AAAA`; em fevereiro, `REINFS 02.2026` e `SIMPLES NACIONAL 02.2026`):

| Valor | Significado | O que o contábil faz |
|---|---|---|
| `COM RETENÇÃO` | Houve retenção e a REINF foi enviada | Conferir as retenções do razão com o detalhe |
| `COM RETENÇÃO — NÃO ENVIADO` | Houve retenção, envio não marcado | Conferir e avisar o DP |
| `PENDENTE` / `PENDENTE (COM RETENÇÃO)` | O DP ainda não concluiu | Os valores podem mudar — registrar pendência |
| `NÃO ENTREGUE` | Marcado como não entregue | Avisar o DP; registrar pendência |
| `SEM MOVIMENTO` | Sem retenção no mês | Retenção no contábil nessa competência é divergência a explicar |
| `ENVIADO` / `SEM STATUS` | Enviado sem marcação de retenção / linha sem status | Conferir na aba do mês |
| vazio | Cliente não está na aba do mês | Normal para quem não tem REINF |

As colunas `Detalhe MM/AAAA` trazem o texto do DP (códigos de receita e valores, ex.: "IRRF (Cód. Rec.
170806): R$ 83,61"). Quando o detalhe disser "VALORES AO LADO", os valores estão num quadro à direita
na aba do mês (colunas H:I ou I:J): leia a aba do mês nesse caso. Os valores do detalhe são o que o DP
digitou — confira com os comprovantes do pacote da Etapa 1 antes de tratá-los como definitivos.

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

**De onde vêm os dados da folha — o contábil não salva relatórios da folha:**
- **Planilha de controle da folha do DP, aba `GATILHO`** — **pendente**: a planilha que o DP usa para
  controlar a folha ainda não foi localizada (a `CONTROLE | DP REINF'S` controla só a REINF); confirmar
  com a Júlia, responsável pelo DP. Quando existir, a aba `GATILHO` dela diz por cliente se há folha
  (funcionários / só pró-labore / não) e se a folha da competência está fechada; registre aqui o nome
  da planilha e as colunas. Até lá, use o Drive e o `Perfil` do mapa.
- **Pasta do cliente `{ano}/003_FOPAG/{MM_MÊS}`**, onde o DP salva a folha do mês. Nos clientes vistos,
  ela tem "Relação da Folha por Empregado {MMAAAA}" (.xls e .pdf), "Rateio Folha por Empregado
  {MMAAAA}", "FGTS {MMAAAA}" e "Detalhes Trabalhadores FGTS {MMAAAA}" — os nomes podem variar por
  cliente. Leia os totais (proventos, descontos, líquido, INSS, IRRF, FGTS); não repita no chat dados
  pessoais de empregados.
- Pasta `003_FOPAG` vazia para a competência de um cliente que tem folha: pergunte ao DP antes de
  integrar — a folha pode ainda não estar fechada.

Conferir após a integração:
- Total líquido da folha integrada = líquido da relação da folha do DP = o que foi pago no extrato
  (cruza com a Etapa 3): depois do pagamento, salários e pró-labore a pagar ficam zerados (ou com o saldo
  que se explica).
- Encargos patronais e provisões (férias/13º) foram gerados, não só o líquido; FGTS do razão = guia de
  FGTS do DP. No Simples, a parte patronal depende do anexo (há anexos em que o INSS patronal é recolhido
  fora do DAS) — confirme no `Perfil`/com o colaborador em vez de presumir.
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

- [ ] Lista de integrações do cliente enviada ao colaborador, com o link do manual de cada uma (e o
  motivo de cada módulo fora da lista)
- [ ] Relatórios do fiscal do item F da Etapa 1 disponíveis (pedidos agora, se tinham ficado pendentes)
- [ ] Acumuladores do período com contas contábeis; ajustes combinados com o fiscal
- [ ] Fiscal integrado e conferido: receita = saídas + serviços, entradas, retenções (inclusive × GATILHO
  da REINF do DP) e tributos do regime
- [ ] Folha integrada e conferida com os dados do DP (controle da folha / `003_FOPAG`): líquido bate com
  o banco, encargos, FGTS e provisões gerados
- [ ] Patrimônio integrado e conferido (bens do período cadastrados antes da geração, depreciação plausível)
- [ ] Qualquer outro módulo usado pelo cliente também integrado
- [ ] Divergências corrigidas no módulo e reconferidas, ou registradas como pendência aceita
- [ ] Planilha de ajustes (se houver) revisada e importada sem erro
- [ ] Razão e balancete exportados de novo, depois de tudo integrado (base da Etapa 5)
