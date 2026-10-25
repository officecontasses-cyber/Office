# Mapa contábil do cliente (Etapa 2)

Apoia a Etapa 2 do `SKILL.md` e é atualizado na Etapa 7. O mapa é um arquivo por cliente que registra
como aquele cliente classifica as coisas na contabilidade, para a leitura do histórico não recomeçar do
zero a cada fechamento.

## Onde fica e como se chama

- Arquivo: `MAPA CONTABIL {NNN}.xlsx` (ex.: `MAPA CONTABIL 238.xlsx`).
- Local: pasta do cliente, `{ano}/005_CONTABIL RELATORIOS/` — na raiz da pasta, não dentro da subpasta
  do mês, porque vale para o ano inteiro.
- Primeiro fechamento do ano: copie o mapa da pasta do ano anterior para a do ano atual e siga dali;
  não comece um mapa novo se já existir um do ano anterior.
- Confirme com o colaborador que você tem permissão de escrita na pasta antes de salvar; se não tiver,
  entregue o arquivo pronto para ele salvar.

## Abas e colunas

### 1. `Perfil` — como o cliente é contabilizado

Duas tabelas na mesma aba.

**Módulos e características**

| Item | Valor | Observação |
|---|---|---|
| Regime | Simples Nacional · Lucro Presumido · Lucro Real (estimativa ou balanço) | Da aba `GATILHO` do fiscal |
| Integração fiscal no Domínio | Sim · Não | Se não, a receita e os tributos entram por outro caminho (ex.: pelo banco) — diga qual |
| Contribuinte de ICMS | Sim · Não · Baixada | |
| Presta / toma serviço (ISS) | Presta · Toma · Ambos · Não | |
| Folha | Funcionários · Só pró-labore · Não | |
| Patrimônio no módulo do Domínio | Sim · Não | Se não, a depreciação (quando houver bens) é lançamento manual |
| Outros módulos integrados | Ex.: contas a pagar/receber | |

**Lançamentos manuais recorrentes** (os que nenhum módulo gera e o cliente faz todo mês)

| Descrição | Conta débito | Conta crédito | Valor ou critério | Origem | Status |
|---|---|---|---|---|---|

Mesmas regras de status das `Regras` (`proposta` até o colaborador confirmar; `inativa` em vez de apagar).

### 2. `Contas` — contas em uso

| Coluna | Conteúdo |
|---|---|
| Código Domínio | Código reduzido da conta, como aparece no razão |
| Classificação | Classificação completa da conta |
| Nome | Nome da conta |
| Grupo | Banco · Aplicação · Cliente · Fornecedor · Tributo a recolher · Tributo a recuperar · Empréstimo/financiamento · Sócio · Receita · Despesa · Transitória · Outro |
| Detalhe | Para banco/aplicação: banco, agência e conta (sem dados de acesso); para sócio: nome do sócio e natureza (pró-labore, lucros, mútuo) |
| Último movimento | Última competência com lançamento nessa conta |
| Observação | O que for útil para classificar (ex.: "conta usada só para tarifas do Banco X") |

Liste só contas com saldo ou movimento no período lido — o plano de contas inteiro já está no Domínio.

### 3. `Regras` — regras de classificação

| Coluna | Conteúdo |
|---|---|
| Padrão no extrato | Contraparte e/ou trecho do histórico bancário (ex.: "PIX ENVIADO FULANO", "TARIFA PACOTE") |
| Condição | Faixa de valor, periodicidade ou outra condição que mude a conta (ex.: "R$ 5.000 todo dia 5"; "demais valores") |
| Conta débito | Código Domínio |
| Conta crédito | Código Domínio |
| Histórico padrão | Histórico que o cliente usa no razão para esse lançamento |
| Origem | De onde a regra saiu: competências e número de ocorrências no razão (ex.: "razão jan–set/2026, 9 lançamentos") ou "definida pelo colaborador" |
| Status | `proposta` (deduzida do razão, ainda não confirmada) · `confirmada` (com data e quem confirmou) · `inativa` (deixou de valer — manter a linha, não apagar) |

Regras práticas:
- **Nunca marque `confirmada` sem o colaborador confirmar** — regra deduzida do razão nasce `proposta`.
- A mesma contraparte pode ter mais de uma regra, separadas pela condição: um Pix para o mesmo sócio
  pode ser pró-labore num valor e mútuo em outro (caso já confirmado na prática).
- Pagamento que mistura mais de um tributo ou conta (ex.: DARF de IRPJ + CSLL) não ganha regra de
  rateio fixo: a regra aponta para o comprovante da Etapa 1, que traz o detalhamento por código.
- Quando o razão do mês contradisser uma regra `confirmada`, não siga a regra: aponte a mudança e
  pergunte se a regra deve ficar `inativa` ou ganhar uma condição nova.

### 4. `Saldos` — saldos de abertura e pendências herdadas

| Coluna | Conteúdo |
|---|---|
| Competência | Último mês fechado (ex.: 2026-08) |
| Código Domínio | Conta |
| Saldo final | Valor com sinal ou natureza (D/C) |
| Alerta | `invertido` (saldo contrário à natureza da conta) · `transitória com saldo` · `a regularizar com saldo` · `sem movimento há N meses com saldo` · vazio |
| Observação | Origem conhecida da pendência, se houver |

Na Etapa 2, o saldo final do último mês fechado é a abertura da competência atual: confira contra o
saldo inicial de cada extrato. Na Etapa 7, grave os saldos finais da competência que acabou de fechar.

### 5. `Apuração` — tributos do regime

Uma linha por competência e tributo (formato longo, para servir a qualquer regime).

| Coluna | Conteúdo |
|---|---|
| Competência | Mês (ou trimestre, para IRPJ/CSLL do Presumido) |
| Regime | Simples Nacional · Lucro Presumido · Lucro Real |
| Forma de apuração | Só no Real: Estimativa · Suspensão · Redução (vazio se ainda não apurado) |
| Tributo | Ex.: DAS · PIS · COFINS · IRPJ · CSLL |
| Valor apurado | Valor da apuração (Domínio/PGDAS-D) |
| Valor pago | Valor pago, com o comprovante de onde saiu |
| Fonte | Conta do razão e/ou comprovante da Etapa 1 |
| Observação | Ex.: "pago em atraso com multa", "compensado via PER/DCOMP" — só o que estiver documentado |

Preencha com o que estiver no razão, na apuração e nos comprovantes; não presuma pagamento que não
aparece em nenhum deles. No Lucro Real, saldo de prejuízo fiscal e base negativa **não** vêm do razão
(estão na Parte B do LALUR/e-Lalur) — se o colaborador informar, registre na observação com a fonte; se
não, deixe em branco e trate na Etapa 6.

### 6. `Histórico` — o que mudou no mapa

| Coluna | Conteúdo |
|---|---|
| Data | Data da alteração |
| Fechamento | Competência(s) do fechamento em que a alteração foi feita |
| Alteração | O que mudou (ex.: "2 regras novas confirmadas; conta 1.1.1.05 incluída") |
| Confirmado por | Nome do colaborador que confirmou |

## Montagem no primeiro fechamento

1. Leia o razão do início do último ano-calendário até a competência, o balancete e o plano de contas
   (pacote da Etapa 1).
2. Preencha o `Perfil` com o que o razão mostra (contas alimentadas por integração fiscal, de folha,
   de patrimônio; lançamentos manuais que se repetem) e confirme com o colaborador o que o razão não
   deixar claro. Liste as contas com saldo ou movimento (aba `Contas`).
3. Para contas de banco e aplicação, agrupe as contrapartidas recorrentes por histórico/contraparte e
   valor: o que se repete vira regra `proposta`, com a origem (competências e quantidade).
4. Grave os saldos finais do último mês fechado e marque os alertas (aba `Saldos`).
5. Levante os tributos do regime apurados e pagos no ano (no Real, também a forma de apuração de cada
   mês), se o razão e os comprovantes permitirem identificar (aba `Apuração`).
6. Apresente o resumo ao colaborador e só salve as regras como `confirmada` depois da resposta dele.

## Atualização nos meses seguintes

1. Leia o mapa e veja no `Histórico` qual foi o último fechamento registrado.
2. Leia no razão só os meses entre esse fechamento e a competência atual.
3. Atualize: mudanças de perfil (aba `Perfil`), contas novas (aba `Contas`), regras novas ou contrariadas (aba `Regras`), saldos de
   abertura (aba `Saldos`), tributos do período (aba `Apuração`).
4. Apresente ao colaborador só o que mudou — não repita o mapa inteiro.

## Dados sensíveis

O mapa pode ter nome de sócios e dados bancários (banco, agência, conta), porque são necessários para
classificar. **Nunca** inclua CPF, senhas, códigos de acesso ou tokens bancários.
