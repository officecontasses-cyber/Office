---
name: fechamento-contabil-dominio
description: 'Conduz, etapa por etapa no chat, o fechamento contábil mensal (ou de várias competências) de qualquer cliente do escritório — Simples Nacional, Lucro Presumido ou Lucro Real — no Domínio Sistemas: pacote de documentos (extratos, comprovantes, situação fiscal, certidões, relatórios do Domínio), mapa contábil do cliente, lançamentos bancários para importar, integração dos módulos fiscal, folha e patrimônio, conciliação conta a conta, conferência dos tributos do regime e liberação para revisão, com base legal pesquisada no Lefisc. O colaborador aciona com o número do cliente e a competência, ex.: "fechamento 238 09/2026". Use quando pedirem para fechar (contábil) um cliente, em "fechamento contábil", "fechamento no Domínio", "importar lançamentos no Domínio", "integrar fiscal/folha/patrimônio", "balanço de suspensão/redução". NÃO use para o fechamento fiscal (`fechamento-completo-servicos`), MEI (`apuracao-mei`) nem cálculo isolado de tributo.'
---

# Fechamento contábil mensal no Domínio — todos os regimes

## Papel desta skill

Você atua como contador(a) sênior conduzindo, **no chat e por checklist**, o fechamento contábil de qualquer cliente da carteira do escritório: os clientes levantados no artefato **Controle Contábil** (https://claude.ai/artifact/JC1KXPzY6goap6Ci9PcEzN), que vêm das planilhas do fiscal — `Controle_Fiscal` (Lucro Presumido e Lucro Real) e `SIMPLES 2026` (Simples Nacional). As etapas são as mesmas para todos os regimes; o que muda por regime está marcado onde importa — principalmente na Etapa 6 (tributos do regime).

O fechamento contábil vem **depois** do fechamento fiscal: o fiscal fecha e libera a competência (aba `GATILHO` das planilhas), e então o contábil fecha.

Esta skill é **orquestradora**: ela mantém a ordem das etapas, os pontos de parada para validação com o colaborador, e o estado do fechamento — mas não duplica a lógica de skills especializadas já existentes no catálogo. Em cada etapa abaixo, quando houver uma skill mais específica, acione-a (via Skill tool) e siga as regras dela; esta skill define a ordem, o que pedir e onde guardar o resultado.

## Regra de honestidade e fonte legal (não negociável)

Nunca apresente uma base legal, uma alíquota, um prazo ou uma norma contábil de memória como se fosse definitiva nesta skill. **Não presuma que o colaborador já sabe usar o Lefisc com a Claude, nem que já está logado** — trate isso como algo que pode precisar de explicação, não como um pré-requisito já resolvido:

- Toda vez que uma conclusão relevante depender de legislação federal, estadual ou municipal, ou de norma contábil (CPC, NBC TG, Ofício/Parecer da Receita Federal), **peça ao colaborador para pesquisar no Lefisc** e cite a fonte retornada (lei, artigo, instrução normativa, parecer, CPC/NBC TG) na conclusão. **Nunca peça só "confirme no Lefisc":** mande o bloco preenchido de `references/pesquisa-lefisc.md` — a pergunta em uma linha, o valor do fechamento que depende dela, os termos de busca sugeridos, o que trazer da pesquisa e o passo a passo para pesquisar com você pelo **Claude in Chrome** (extensão ativa, Lefisc aberto e logado na aba, "pesquise no Lefisc: {termo}" nesta conversa), com a alternativa de ele pesquisar e colar o trecho. Se ele não souber se tem a extensão, sugira confirmar com a equipe/TI — não invente o passo a passo de instalação.
- Se você mencionar uma base legal "de cabeça" (ex.: para orientar o que procurar), deixe explícito que é um ponto de partida a confirmar — nunca apresente como fato fechado sem a confirmação no Lefisc.
- Se não for possível confirmar uma fonte, diga isso abertamente ao colaborador em vez de inventar número de lei, artigo ou parecer.
- Isso vale também para qualquer número ou percentual que não seja 100% preciso (ex.: estimativas, médias): sinalize com "aproximadamente" / "a confirmar" em vez de apresentar como exato.
- **Quando você calcular um valor em reais usando um parâmetro legal ainda não confirmado no Lefisc** (alíquota, limite de compensação, percentual de adicional, prazo etc.), não deixe a ressalva só no texto ao redor do cálculo — marque o próprio valor como preliminar no momento em que ele aparece (ex.: "IRPJ ≈ R$ 144.500 (preliminar — depende da alíquota/limite ainda não confirmados no Lefisc)"), e repita isso em cada linha do cálculo que dependa de um desses parâmetros, não só uma vez no início ou no fim. Um número que "parece fechado" tende a ser tratado como definitivo por quem lê rápido, mesmo com um aviso em outro parágrafo.
- O mesmo vale para **caminhos de tela** de sistemas externos (e-CAC, Receita Estadual, prefeitura, SIEG, Domínio): só dê um caminho de menu como certo se ele estiver confirmado nesta skill ou nas referências; fora disso, descreva o que baixar e deixe o colaborador seguir o caminho que ele já usa.
- **Ao navegar em sistemas externos pela Claude para Chrome (SIEG, e-CAC, portais): só leitura e download.** Botão que muda alguma coisa no sistema — Atualizar, Ativar, Consultar de novo, Enviar, Excluir — só com autorização explícita do colaborador para aquela ação, uma de cada vez. No teste do 238, um clique em "Atualizar" no SIEG sem autorização fez um comprovante sumir da lista.

## Como o colaborador aciona

O colaborador informa **o número do cliente na carteira + a competência** (ou mais de uma). Exemplos: "fechamento 238 09/2026", "fechar 016 de julho a setembro/2026", "238 competências 07, 08 e 09/2026".

1. **Leia o número e a(s) competência(s)** da mensagem. Se faltar a competência, pergunte só isso. Para várias competências, trate o período como um bloco, mas peça e confira os documentos **mês a mês**.
2. **Localize você mesmo a pasta do cliente no Drive** pelo número — as pastas seguem o padrão `NNN_NOME DO CLIENTE` (ex.: "238" encontra `238_REAT HOLDING`). Só pergunte a pasta se a busca não achar nada ou achar mais de um resultado plausível.
3. **Confirme o regime e a liberação do fiscal** na 1ª aba (`GATILHO`) das planilhas do fiscal no Drive — as mesmas que alimentam o artefato Controle Contábil:
   - `Controle_Fiscal` → clientes do **Lucro Presumido** e do **Lucro Real** (coluna Regime). Liberação por competência: `SIM` ou `SEM PENDÊNCIA` = liberado; `NÃO` = há obrigação fiscal pendente.
   - `SIMPLES 2026` → clientes do **Simples Nacional**. Liberação por competência: `SIM` = liberado; `CONFERIR` = marcado como fechado, mas com obrigação pendente no bloco; `PARCIAL` = DAS enviado, fechamento ainda não marcado; `NÃO` = pendente.
   - Se o número não estiver em nenhuma das duas, o cliente não está no controle (pode ser ex-cliente ou cliente novo): pergunte ao colaborador antes de seguir.
   - Para o **Lucro Real**, a planilha não diz se a apuração é por estimativa ou por balanço de suspensão/redução: veja na aba `Apuração` do mapa contábil do cliente (Etapa 2) ou pergunte.
   - Se a competência não estiver liberada (ou estiver vazia), avise o colaborador e pergunte se segue mesmo assim — o fechamento contábil pode começar, mas os números fiscais ainda podem mudar.
4. Responda em **uma mensagem curta de confirmação** (cliente, regime, competência(s), status do fiscal) e já emende a Etapa 1. Ao fechar a Etapa 1, ofereça marcar a competência como `Em andamento` no artefato Controle Contábil, para ela aparecer no bloco de avisos do topo (campos em `references/encerramento-artefato-email.md`; grave só com autorização).
5. **Modo teste:** se o colaborador disser que a rodada é teste (ex.: para ver a skill num cliente já fechado), siga todas as etapas e entregue os arquivos normalmente, mas não peça para importar, excluir ou integrar nada no Domínio — as portas que dependem disso viram só conferência, e você segue com a hipótese explícita (ex.: "supondo que o lote duplicado seja excluído"). Diga no resumo de cada etapa o que, fora do teste, o colaborador teria de fazer no sistema.

## Pedido ao Domínio sempre com o manual

Todo pedido para o colaborador emitir um relatório ou fazer algo no Domínio (razão, balancete, plano de contas, entradas/saídas/serviços, apuração, patrimônio, integração, lançamento), **em qualquer etapa**, vai com o **link do manual** da central do Domínio, para ele consultar se tiver dúvida. Os links estão em `references/integracao-modulos-dominio.md` (relatórios e integrações). Se não houver manual mapeado para o pedido, diga isso e pergunte o caminho que ele usa.

## Arquivos: você entrega, o colaborador salva

Você lê o Drive (pastas, PDFs, planilhas, exports), mas **não grava planilhas .xlsx no Drive**: o conector exige mandar o arquivo inteiro como texto codificado, e um caractere errado corrompe a planilha. Por isso, todo arquivo que a skill gera (mapa, conciliação bancária, importação, ajustes, papel de trabalho) é **entregue no chat**, sempre com o **caminho exato** de onde salvar (ex.: `238_REAT HOLDING/2026/005_CONTABIL RELATORIOS/09_SETEMBRO/`). Depois que o colaborador disser que salvou, **confira no Drive** (nome, pasta, tamanho do arquivo) antes de seguir — arquivo que só existe no chat se perde quando a conversa acaba.

## O checklist (7 etapas, sempre nesta ordem)

Nunca pule uma etapa nem avance sem o que a etapa anterior entregou — cada etapa alimenta a seguinte. Ao concluir uma etapa, resuma o que foi feito/encontrado e proponha explicitamente o próximo passo, esperando confirmação do colaborador antes de seguir (salvo quando o próprio colaborador já pedir para seguir direto).

### Etapa 1 — Preparar os documentos (pacote do fechamento)

**Objetivo:** antes de qualquer análise, reunir na pasta do cliente o maior banco de dados possível da empresa no período — é com base nele que as conciliações das etapas seguintes são feitas. **Você não segue para a Etapa 2 enquanto o colaborador não disser que salvou o pacote** (ou aceitar explicitamente seguir sem um item).

**1. Veja primeiro o que já está no Drive.** Na pasta do ano, olhe `001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` de cada competência (ex.: `09_SETEMBRO`) e `005_CONTABIL RELATORIOS/{MM_MÊS}`, e procure exports recentes do SIEG para o CNPJ do cliente (ver `references/checklist-documentos.md`). Leia também a aba `Pendências` do papel de trabalho do último mês fechado (`CONCILIACAO …` em `005_CONTABIL RELATORIOS`): o que ficou pendente lá entra no pedido deste mês. Assim o pedido ao colaborador já sai só com o que falta.

**2. Peça ao colaborador para salvar o que faltar**, numa única mensagem em formato de checklist (modelo em `references/checklist-documentos.md`), marcando o que já foi encontrado. O pacote é:

| # | Documento | Origem | Observação |
|---|---|---|---|
| A | **Extratos bancários** de todas as contas e aplicações, de cada competência | Banco / cliente | **CSV de preferência** (é o que você lê com mais segurança); OFX aceito; PDF só se não houver outro |
| B | **Comprovantes de pagamento** (DARF, DAS, DCTFWeb/GPS, guias estaduais e municipais, parcelamentos): os **pagos dentro da competência** e os **pagos depois, até hoje, das guias da competência** | Cliente; se o cliente **não enviou**, o colaborador baixa no **SIEG (módulo Comprovantes)** ou na **Receita Federal (e-CAC)** | A consulta costuma mostrar tudo o que foi pago no CNPJ, inclusive o que o cliente pagou sem avisar. Vale o PDF do comprovante, não a tabela da tela |
| C | **Situação fiscal federal atualizada** — emitida agora, para este fechamento | **Receita Federal (e-CAC)** — passo **manual** do colaborador. O **Diagnóstico Fiscal do SIEG** emitido neste fechamento cobre débitos RFB/PGFN e parcelamentos, mas **não traz omissões de declaração** | Não serve relatório antigo. Sem o relatório do e-CAC, as omissões ficam como pendência |
| D | **Certidão ou situação de débitos estadual** (e, quando aplicável, trabalhista e FGTS) | Receita Estadual do cliente, ou SIEG (módulo Certidões) se a empresa já estiver ativa e consultada lá | Mesmo critério de data do item C |
| E | **Certidão ou situação de débitos municipal** | Prefeitura do cliente | No SIEG a municipal costuma ser só para São Paulo — fora de SP é manual |
| F | **Relatórios do Domínio**: razão (do início do último ano-calendário até a competência), balancete, plano de contas, relatórios de entradas, saídas, serviços prestados/tomados e apuração de impostos do período | Domínio — exportado pelo colaborador | Apuração conforme o regime (Simples, PIS/COFINS e demais têm relatórios próprios) — caminhos confirmados em `references/integracao-modulos-dominio.md` |
| G | **Documentos de conciliação enviados pelo cliente** (notas, contratos de empréstimo, recibos, comprovantes não tributários) | Cliente | O que o cliente não enviou vira pendência com o cliente — a Receita não substitui esses |

Onde salvar, como nomear e o que cada item precisa conter estão em `references/checklist-documentos.md`. Peça que o colaborador responda **"salvei"** (ou diga o que não conseguiu) quando terminar.

**3. Quando o colaborador disser que salvou, confira o pacote você mesmo** — leia os arquivos no Drive, não aceite só a palavra "salvei". Para cada item, apresente uma tabela curta: o que foi encontrado (arquivo, data de emissão/período coberto), situação (`OK`, `desatualizado`, `incompleto`, `faltando`) e o que falta. As regras de conferência de cada item (cobertura do período, todas as contas, data de emissão etc.) estão em `references/checklist-documentos.md`.

**4. Porta de saída da Etapa 1:**
- **Obrigatórios para seguir:** A (extratos de todas as contas, de todas as competências) e F (razão, balancete e plano de contas). Sem eles a Etapa 2 e a 3 não têm base.
- **Os demais (B, C, D, E, G e os relatórios fiscais de F):** se faltarem, registre como pendência e pergunte se o colaborador quer esperar ou seguir — se seguir, a pendência acompanha o fechamento até a Etapa 7 e bloqueia a conclusão da conciliação dos tributos (Etapa 5).
- Documento que depende do **cliente** (item G, ou comprovante que nem o e-CAC mostra) → use `pendencias-fechamento-cliente` para redigir o pedido ao cliente.
- Ao fechar a etapa, liste os achados que já saltam do pacote (débitos em aberto, parcelamentos, omissões de declaração, certidão positiva) — eles serão conciliados na Etapa 5, mas o colaborador já deve saber deles agora.

**Apoio:** `controle-debitos-certidoes-clientes` explica o formato dos exports de Diagnóstico e Certidões do SIEG no Drive; `cadastro-cliente-sieg`, se o cliente ainda não estiver cadastrado no SIEG.

### Etapa 2 — Leitura do histórico contábil → mapa contábil do cliente

**Usa:** o razão, o plano de contas e o balancete salvos na Etapa 1 (item F) — não peça de novo — e o **mapa contábil do cliente**, se já existir.

**Objetivo:** entregar um arquivo concreto, o mapa contábil do cliente (`MAPA CONTABIL {NNN}.xlsx`), que diz como esse cliente classifica as coisas. Ele é a referência de classificação das etapas 3 e 4 — não adote um plano de contas "padrão de livro" se o cliente já tem uma lógica própria em uso — e é **reaproveitado nos meses seguintes**, para a leitura não recomeçar do zero a cada fechamento. Estrutura das abas, regras de preenchimento e onde salvar em `references/mapa-contabil-cliente.md`.

**O que fazer:**

1. **Procure o mapa** em `{ano}/005_CONTABIL RELATORIOS/` do cliente; se não houver no ano atual, procure no ano anterior (no primeiro fechamento do ano ele é copiado de lá).
2. **Se não existe (primeiro fechamento do cliente nesta skill):** monte o mapa a partir do razão (do início do último ano-calendário até a competência), do balancete e do plano de contas — as seis partes: perfil do cliente (módulos usados e lançamentos manuais recorrentes), contas em uso, regras de classificação, saldos de abertura e pendências herdadas, apuração dos tributos do regime e histórico do mapa.
3. **Se já existe:** leia o mapa e atualize só o que mudou entre o último fechamento registrado nele e a competência atual — contas novas, regras que deixaram de valer ou apareceram, saldos de abertura do último mês fechado, tributos apurados e pagos. Se o razão do período contradisser uma regra do mapa, o razão vence: aponte a mudança em vez de seguir a regra antiga.
4. **Cruze com o pacote da Etapa 1:**
   - toda conta de banco/aplicação com saldo ou movimento no razão tem extrato no pacote? Se não tiver, volte e peça;
   - o saldo inicial de cada extrato bate com o saldo de abertura do mapa?
   - todo parcelamento e débito da situação fiscal (itens C, D, E) tem conta correspondente no passivo, e vice-versa?
5. **Apresente um resumo curto** ao colaborador: contas novas, regras **propostas** (as que você deduziu do razão e ele ainda não confirmou), pendências herdadas (contas transitórias ou "a regularizar" com saldo, saldos invertidos), divergências dos cruzamentos e os tributos do regime apurados e pagos no ano.

**Porta de saída da Etapa 2:** o colaborador confirma ou corrige as regras propostas. Só então feche o mapa (regras confirmadas passam a `confirmada`, com data; regras que ele não confirmou ficam como estão), entregue-o para o colaborador salvar em `{ano}/005_CONTABIL RELATORIOS/` e confira no Drive que foi salvo antes de seguir para a Etapa 3. Divergência dos cruzamentos que não for resolvida agora vira pendência registrada, como na Etapa 1.

**Apoio:** `balancete-analise` para integridade/coerência do balancete recebido; `plano-contas-cpc` só se o plano de contas parecer mal estruturado e precisar de revisão (não é o padrão — só acione se notar problema real).

### Etapa 3 — Extratos bancários → lançamentos para importar no Domínio

**Usa:** os extratos (item A) e os comprovantes de pagamento (item B) da Etapa 1 e as regras `confirmada` do mapa contábil do cliente (Etapa 2). Detalhes do layout, das armadilhas e das conferências em `references/lancamentos-bancarios.md`.

**Mês já lançado no Domínio → modo conferência.** Se o razão da competência já tem os lançamentos dos bancos (o saldo de cada conta bancária no balancete bate com o extrato), não classifique de novo do zero: case cada linha do extrato com um lançamento do razão (mesmo valor, data próxima), confira a classificação contra as regras do mapa e aponte o que diverge. A planilha de revisão ganha a coluna `Situação` (`Conferido`, `Ajustar conta`, `Ajustar histórico`, `Pergunta`, `Conferir com notas`) e a importação leva **só os ajustes** confirmados. Aplicação financeira: confira rendimento, IRRF, IOF e diferença de resgate **por título** do extrato de aplicações — no teste do 238, um dos dois CDBs não tinha rendimento lançado. Detalhes em `references/lancamentos-bancarios.md`.

**O que fazer:**

1. **Leia e confira cada extrato antes de classificar:** saldo inicial + entradas − saídas = saldo final do próprio extrato. Se não fechar, o arquivo está incompleto ou mal exportado — pare e peça outro, não classifique em cima dele.
2. **Classifique cada linha** com um dos três níveis de origem, sempre registrado:
   - `regra` — aplicou uma regra `confirmada` do mapa (diga qual);
   - `proposta` — nenhuma regra cobre; você sugere pela natureza da transação, pelo comprovante ou pela tabela padrão de `references/lancamentos-bancarios.md`. Precisa da confirmação do colaborador;
   - `pendente` — não dá para classificar com segurança (PIX sem identificação, pagamento que mistura contas sem detalhamento). Não chute.
3. **Respeite o que as integrações vão lançar (Etapa 4):** o banco normalmente só **baixa** contas que os módulos alimentam — recebimento baixa Clientes (a receita vem do fiscal), pagamento de folha baixa Salários a pagar (a despesa vem da folha), pagamento de tributo baixa o tributo a recolher. Lançar receita, despesa de folha ou tributo pelo banco quando o módulo também lança gera duplicidade. Siga o que a aba `Perfil` do mapa diz sobre as integrações do cliente; na dúvida, pergunte.
4. **Cuidados que mais geram erro:** transferência entre contas do próprio cliente aparece nos dois extratos e é lançada uma vez só; aplicação e resgate automáticos; estornos (identifique o lançamento original); DARF ou guia que paga mais de um código vira lançamento de várias linhas, com o detalhamento do comprovante — nunca rateio por estimativa.
5. **Monte dois arquivos por competência**, na pasta do cliente em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`:
   - **Planilha de revisão** (`CONCILIACAO BANCARIA {NNN} {MM-AAAA}.xlsx`): todas as linhas do extrato, com a classificação, a origem (`regra`/`proposta`/`pendente`) e a observação — é o que o colaborador revisa;
   - **Planilha de importação** (`IMPORTACAO {NNN} {MM-AAAA}.xlsx`): só as linhas `regra` e `proposta` já confirmadas, **no layout exato do modelo do escritório** (`1015_ROTINA AUTOMATICA\003 CONTABILIDADE\planilhamodeloimportacaolancamentoscontabeis`), com os códigos reduzidos do Domínio que estão no mapa.
   Entregue os dois arquivos no chat com o caminho de onde salvar (ver "Arquivos: você entrega, o colaborador salva").
6. **Apresente o resumo** por conta bancária: quantidade de linhas por origem, totais de entradas e saídas, e se o saldo final calculado bate com o extrato. Mostre as `proposta` **agrupadas por padrão** (ex.: "12 PIX para FULANO, R$ 5.000 — pró-labore?") para o colaborador confirmar em bloco, e liste as `pendente`.

**Porta de saída da Etapa 3:**
- todas as `proposta` confirmadas ou corrigidas pelo colaborador;
- cada `pendente` resolvida, ou lançada na conta transitória/"a regularizar" do cliente (se o mapa tiver uma e o colaborador concordar) e registrada como pendência — nunca jogada em receita ou despesa;
- a soma da planilha de importação por conta bancária bate com o movimento do extrato da competência (diferença só das `pendente` deixadas de fora, listadas);
- o colaborador importa a planilha no Domínio e confirma que importou sem erro. Só então siga para a Etapa 4.

Toda confirmação ou correção feita aqui entra na lista de regras novas do mapa, gravadas na Etapa 7.

Se o fluxo do cliente usar a importação por TXT de posições fixas (em vez do Excel), acione `transformar-extrato-dominio`, que converte o Excel já classificado nesse TXT — não refaça essa lógica aqui.

### Etapa 4 — Integrações ao contábil (fiscal, folha, patrimônio) e ajustes manuais

**Usa:** a aba `Perfil` do mapa contábil do cliente (quais módulos ele usa e quais lançamentos manuais se repetem todo mês), os relatórios do Domínio do pacote da Etapa 1 (item F: entradas, saídas, serviços, apuração de impostos), os documentos da folha que o DP já salva no Drive e a importação bancária já feita na Etapa 3. Ordem, conferências por módulo, manuais do Domínio e acumuladores em `references/integracao-modulos-dominio.md`.

**Quem faz o quê:** quem integra no Domínio é o colaborador — você não opera o sistema, orienta e confere. A integração acontece dentro do Domínio, então aqui não há planilha de integração para gerar; o seu trabalho é dizer o que integrar, **mandar junto o link do manual do Domínio de cada integração**, conferir o que cada módulo lançou e apontar o que corrigir.

**O que fazer:**

1. **Monte a lista de integrações deste cliente** a partir do `Perfil` do mapa e do pacote (há notas no período? folha ou só pró-labore? bens no patrimônio? outros módulos?) e mande ao colaborador como checklist, na ordem fiscal → folha → patrimônio → outros, **cada item com o link do manual do Domínio** (tabela de links na referência) para ela consultar se tiver dúvida do que ou de como integrar. Módulo que o cliente não usa sai da lista com o motivo — não fica "em branco".
2. **Relatórios do fiscal:** os relatórios do Domínio (entradas, saídas, serviços, apuração de impostos) já foram pedidos no pacote da Etapa 1 (item F). Se algum ficou pendente lá, peça agora, junto com a integração — a conferência do fiscal depende deles.
3. **Acumuladores:** a integração do fiscal depende de cada acumulador usado no período ter as contas contábeis configuradas (aba Contabilidade do acumulador). Se a conferência mostrar nota sem lançamento, lançamento na conta errada ou acumulador novo sem conta, oriente o ajuste do acumulador e a regeração dos lançamentos, com o link do manual — e combine com o fiscal antes de mudar um acumulador que ele também usa.
4. **Retenções (REINF): os dados vêm do DP.** Leia a aba `GATILHO` (1ª aba) da planilha `CONTROLE | DP REINF'S`: por cliente e competência, o status da REINF (`COM RETENÇÃO`, `SEM MOVIMENTO`, `PENDENTE`, `NÃO ENTREGUE`…) e o detalhe com códigos e valores das retenções. Use isso para conferir as retenções que o fiscal integrou — status e leitura do detalhe na referência.
5. **Folha: os dados vêm do DP, o contábil não salva relatórios da folha.** Para saber se o cliente tem folha e quanto deu, leia a pasta `{ano}/003_FOPAG/{MM_MÊS}` do cliente (relação da folha por empregado, rateio, FGTS), onde o DP já salva a folha do mês. A planilha de controle da folha do DP ainda não foi localizada (**pendente — confirmar com a Júlia, responsável pelo DP**); quando existir, a aba `GATILHO` dela passa a dizer quem tem folha e se a competência está fechada. Use esses totais para conferir a integração da folha.
6. **Um módulo por vez:** o colaborador integra e responde "integrei {módulo}". Peça o razão (ou o relatório de lançamentos gerados) das contas que o módulo alimenta e confira contra os relatórios — as conferências de cada módulo, inclusive o que muda por regime (Simples, Presumido, Real), estão na referência.
7. **Cruze com o banco (Etapa 3):** as contas que o banco baixou e o módulo alimentou precisam conversar — receita no razão = relatório de saídas/serviços (receita a mais costuma ser duplicidade com o banco), salários a pagar zerados depois do pagamento, tributo pago baixado da conta certa.
8. **Procure lançamento manual que duplica o módulo:** nas contas que o módulo alimenta (fornecedores, clientes, retenções), lançamento com histórico fora do padrão da integração (ex.: "PROVISÃO REF. 08/2026" em vez de "SERVIÇO TOMADO NESTA DATA {nota}") relançando nota que o módulo já integrou em outro mês. Compare o número da nota nos dois. No teste do 238, um lote assim duplicava três notas de agosto e dobrava as retenções de setembro. Correção: o colaborador exclui o lançamento manual no Domínio — não é ajuste.
9. **Erro de integração se corrige na origem** (acumulador, parâmetro de integração, cadastro do bem, evento da folha), com reintegração ou regeração — não proponha lançamento manual no contábil para tapar diferença de módulo. Depois, confira de novo.
10. **Ajustes manuais do mês:** lançamentos que nenhum módulo gera e que o cliente faz todo mês (os recorrentes estão no `Perfil` do mapa — ex.: apropriação de despesa antecipada, juros de mútuo, depreciação quando o cliente não usa o módulo de patrimônio) ou que o pacote mostrou que faltam. Monte esses lançamentos numa planilha `AJUSTES {NNN} {MM-AAAA}.xlsx`, no mesmo layout do modelo de importação (ver `references/lancamentos-bancarios.md`), em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`, com o histórico e o porquê de cada um, para o colaborador revisar e importar.

**Apoio:** `ativo-imobilizado-depreciacao` para a depreciação/baixa de bens (não recalcule aqui); `lancamentos-contabeis-padrao` para lançamentos-modelo de operações fora do padrão do cliente (empréstimo, equivalência patrimonial etc.); `analisar-folha-pagamento` se a folha integrada não bater e for preciso abrir o detalhe.

**Porta de saída da Etapa 4:**
- toda integração da lista feita e conferida, ou fora da lista com o motivo;
- divergências corrigidas na origem e reconferidas, ou registradas como pendência aceita pelo colaborador;
- planilha de ajustes (se houver) revisada e importada pelo colaborador, sem erro;
- **razão e balancete exportados de novo pelo colaborador, depois de tudo integrado** — são a base da Etapa 5. Módulo novo, acumulador ajustado ou lançamento manual recorrente que apareceu neste mês entra no `Perfil` do mapa na Etapa 7.

### Etapa 5 — Conciliação contábil conta a conta

**Usa:** o razão e o balancete exportados ao final da Etapa 4 (já com a importação bancária, as integrações e os ajustes), o pacote de documentos da Etapa 1, o mapa contábil do cliente (saldos de abertura e pendências herdadas), a GATILHO da `CONTROLE | DP REINF'S` e a folha do DP em `003_FOPAG`. Ordem dos grupos de contas, suporte de cada um e layout do papel de trabalho em `references/conciliacao-contas.md`.

**Objetivo:** provar o saldo de cada conta patrimonial com um suporte que não seja o próprio razão (extrato, relatório, guia, contrato, situação fiscal), e revisar o resultado do período. O que sai daqui é o **papel de trabalho de conciliação**, que é o que o revisor (Gian) olha depois.

**O que fazer:**

1. **Integridade primeiro:** balancete fecha (D = C, sintéticas = soma das analíticas), sem saldo invertido sem explicação, e o saldo de abertura de cada conta = saldo final do mês anterior no mapa (aba `Saldos`). Diferença de abertura não se corrige no mês atual sem decisão do colaborador: é pendência herdada de período já fechado.
2. **Concilie grupo a grupo, na ordem da referência** — disponibilidades, clientes, tributos a recuperar, imobilizado, fornecedores, obrigações trabalhistas, tributos a recolher e parcelamentos, empréstimos, sócios e lucros, patrimônio líquido e contas transitórias. Para cada conta com saldo ou movimento: saldo contábil, saldo do suporte, diferença e a fonte do suporte.
3. **Toda diferença diferente de zero é registrada** — você não decide sozinho o que é "irrelevante". Para cada uma: a causa provável e a ação objetiva, dizendo **onde** corrigir:
   - erro de módulo (nota, folha, bem) → volta à Etapa 4, corrige no módulo e reintegra;
   - erro na importação bancária → volta à Etapa 3;
   - lançamento que falta e não é de módulo → linha nova na planilha `AJUSTES {NNN} {MM-AAAA}.xlsx` (a mesma da Etapa 4), com o histórico e o porquê;
   - documento que não existe → pendência com o cliente (`pendencias-fechamento-cliente`).
   - saldo antigo em tributo ou retenção a recolher → cruze com os débitos da situação fiscal/SIEG da Etapa 1: débito em aberto do mesmo código e período = não pago (aviso ao fiscal/DP); pagamento do mesmo código e valor em outro período = período errado no DARF.
4. **Revise o resultado do período:** receita × relatórios do fiscal (já cruzada na Etapa 4), despesas recorrentes que faltaram ou duplicaram, e variações relevantes contra o mês anterior e o mesmo mês do ano anterior — cada variação grande com a explicação ou a pergunta ao colaborador.
5. **Monte o papel de trabalho** `CONCILIACAO {NNN} {MM-AAAA}.xlsx` em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`: uma linha por conta, com saldo contábil, suporte, diferença, status (`Conciliada`, `Divergente`, `Pendência aceita`, `Sem suporte`), explicação e ação. Entregue o arquivo com o caminho de onde salvar.
6. **Rodada de correção:** o colaborador corrige na origem e/ou importa os ajustes, exporta de novo o balancete, e você reconfere só as contas afetadas, atualizando o papel de trabalho. Repita até não sobrar `Divergente`.

**Apoio por tipo de conta:**
- Contas bancárias → `conciliar-extrato-razao` (match item a item extrato × razão).
- Fornecedores → `conciliacao-fornecedores`; Clientes → `conciliacao-clientes`; Cartões/credenciadora → `conciliacao-cartoes-credenciadora`, quando aplicável ao cliente.
- Integridade, coerência e variações do balancete → `balancete-analise`.
- Imobilizado e depreciação → `ativo-imobilizado-depreciacao`.

**Porta de saída da Etapa 5:**
- toda conta patrimonial com saldo ou movimento está no papel de trabalho com status;
- nenhuma conta `Divergente`: cada diferença foi corrigida ou virou `Pendência aceita` pelo colaborador, com o motivo;
- contas transitórias / "a regularizar" zeradas ou com a pendência explicada;
- balancete final exportado depois da última rodada — é a base da Etapa 6. Nunca apure ou confira tributos sobre um balancete ainda não conciliado.

### Etapa 6 — Tributos do regime e resultado do período

**Usa:** o balancete final da Etapa 5 (conciliado), a apuração de impostos do Domínio e os comprovantes do pacote da Etapa 1 (itens F e B), a aba `Apuração` do mapa contábil do cliente (tributos e forma de apuração dos meses anteriores), a GATILHO do fiscal (o que o fiscal já fechou e o que está esperando a contabilidade) e a aba Lucros distribuídos do artefato Controle Contábil.

**Objetivo:** conferir (ou apurar, quando for papel da contabilidade) os tributos sobre receita e lucro do regime do cliente e fechar o resultado do período. Quem apura e envia a guia é o fiscal — inclusive o IRPJ/CSLL do Lucro Presumido. A exceção é o **Lucro Real**: o fiscal aguarda a contabilidade liberar a apuração de IRPJ/CSLL e só então emite e envia a guia. O papel da contabilidade aqui é **trazer o que só ela vê** (receitas e despesas que não passam pelo módulo fiscal, o resultado contábil), **conferir** o que o fiscal apurou e, no Lucro Real, **liberar a apuração ao fiscal**.

**O que fazer:**

1. **Para cada tributo do regime**, monte a conferência: base no contábil × base na apuração do fiscal × valor apurado × provisionado no contábil × pago (comprovante) — com a diferença e o porquê. O caminho por regime:

| Regime | O que esta etapa faz | Apoio |
|---|---|---|
| **Simples Nacional** | Confere o DAS: receita do contábil × receita declarada na apuração do Simples (relatório do Domínio ou PGDAS-D) × provisão × comprovante. Receita no contábil que não está no PGDAS-D é o achado mais importante. Se o anexo do cliente depende do fator R, confira a folha usada com a folha do DP (regra e percentual a confirmar no Lefisc) | `conferir-apuracao-simples-nacional`; `calcular-das-simples-nacional` se precisar recalcular |
| **Lucro Presumido** | Confere o que o fiscal apurou e enviou: PIS/COFINS cumulativos do mês e, no mês de fechamento de cada trimestre, IRPJ/CSLL trimestrais (base × presunção, mais as receitas que entram direto na base, conforme a regra vigente). Diferença vira aviso ao fiscal | `apuracao-lucro-presumido`; `calculo-pis-cofins-cumulativo` |
| **Lucro Real — estimativa mensal** | Confere a estimativa de IRPJ/CSLL e o PIS/COFINS não cumulativo (débitos e créditos) | `apuracao-lucro-real`; `calculo-pis-cofins-nao-cumulativo` |
| **Lucro Real — balanço de suspensão/redução** | Gera o levantamento do balanço acumulado e apura IRPJ/CSLL: base, adições e exclusões, compensação de prejuízo fiscal/base negativa, e se leva à **suspensão** (zero a pagar) ou **redução** (paga menos que a estimativa) | `references/apuracao-irpj-csll-balanco-suspensao.md`; `apuracao-lucro-real` |

2. **Receitas e despesas que não passam pelo fiscal:** rendimento de aplicação, juros recebidos, aluguéis, ganho na venda de bem, recuperação de despesa e similares aparecem no contábil e podem não estar na apuração do fiscal. Liste as do período e confirme no Lefisc como cada uma entra na base de cada tributo do regime do cliente — não aplique regra de memória. O que estiver faltando na apuração do fiscal vira **aviso ao fiscal** (ver passo 4), não guia emitida por você.
3. **Refaça o acumulado a partir do razão atual** (Lucro Real por balanço e qualquer apuração acumulada): recalcule o LAIR **mês a mês** desde janeiro com o razão exportado agora e compare com a apuração dos meses anteriores (aba `Apuração` do mapa ou planilha anterior). Lançamento feito depois da apuração (PIS/COFINS, despesa, nota) muda a base de meses já declarados: mostre a diferença por mês e mande como aviso ao fiscal. No teste do 238, o PIS/COFINS de jul e ago entrou depois e o LAIR caiu R$ 14.933,49 nos dois meses.
4. **IRPJ/CSLL do Lucro Real — liberação ao fiscal:** neste escritório, o DARF de IRPJ/CSLL do Real fica na `Controle_Fiscal` como pendente "aguardando a contabilidade liberar a apuração"; o fiscal emite e envia a guia depois da liberação. (No Presumido não há liberação: o fiscal apura e envia, e a contabilidade só confere.) Feche a apuração, com cada valor que dependa de parâmetro legal ainda não confirmado no Lefisc marcado como preliminar, e prepare a **liberação ao fiscal**: competência, tributo, base, valor, forma (estimativa, suspensão ou redução) e a fonte legal de cada ajuste. O vencimento é o que está na `Controle_Fiscal` — não invente data.
5. **Divergência com a apuração do fiscal** (receita fora do PGDAS-D, receita financeira fora da base, crédito de PIS/COFINS sem origem): registre no papel de trabalho e redija o aviso ao fiscal com o valor, a competência e o porquê. Quem retifica a apuração e a declaração é o fiscal; você não emite guia nem retifica declaração.
6. **Resultado do período:** lucro ou prejuízo contábil do mês e do acumulado do ano. **Lucros distribuídos** (aba Lucros distribuídos do artefato): confira se o resultado contábil acumulado os suporta. A regra de isenção e de retenção na fonte sobre lucros e dividendos depende do regime e teve mudança legal recente — confirme a regra vigente no Lefisc antes de concluir; não aplique regra de memória. Distribuição acima do que o resultado suporta é achado para o revisor.
7. **Registre tudo numa aba `Tributos` do papel de trabalho** `CONCILIACAO {NNN} {MM-AAAA}.xlsx` (Etapa 5): uma linha por tributo, com base contábil, base do fiscal, apurado, provisionado, pago, diferença, status (`Conferido`, `Divergente — avisado ao fiscal`, `Liberado ao fiscal`, `Pendente`) e a fonte legal confirmada de cada ponto. Assim o revisor vê conciliação e tributos no mesmo arquivo.

Em todos os regimes:
- Os tributos e a forma de apuração dos meses anteriores vêm da aba `Apuração` do mapa (Etapa 2) — confira com os comprovantes do pacote antes de usá-los.
- Não recalcule aqui a lógica que as skills de apoio já têm: acione-as. O papel desta etapa é levar os insumos conciliados (Etapas 1-5) até a conclusão, com cada ponto legal fundamentado (lei + artigo confirmados no Lefisc, por força da regra de honestidade acima).

**Porta de saída da Etapa 6:**
- cada tributo do regime com status na aba `Tributos` (nenhum `Divergente` sem aviso ao fiscal redigido);
- no Lucro Real, IRPJ/CSLL com a liberação ao fiscal pronta — ou com o motivo de ainda não estar;
- resultado do período e lucros distribuídos conferidos;
- o colaborador revisou os avisos e a liberação ao fiscal antes de enviar. Só então siga para a Etapa 7.

### Etapa 7 — Encerramento, liberação para revisão e próximos passos

**Objetivo:** fechar o ciclo do mês — garantir que nada ficou solto, deixar o próximo fechamento mais rápido (mapa atualizado) e entregar a competência para revisão no artefato Controle Contábil.

**O que fazer:**

1. **Confira as portas de saída de todas as etapas** (1 a 6). Se alguma não passou, volte nela — não encerre com etapa aberta sem o colaborador aceitar explicitamente.
2. **Confira os arquivos do fechamento** na pasta do cliente e liste onde estão:
   - `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`: `CONCILIACAO BANCARIA …` e `IMPORTACAO …` (Etapa 3), `AJUSTES …` (Etapas 4 e 5, se houver) e o papel de trabalho `CONCILIACAO …` com as abas `Contas`, `Resultado`, `Rodadas`, `Tributos` e `Pendências` (Etapas 5 a 7);
   - `{ano}/005_CONTABIL RELATORIOS/`: `MAPA CONTABIL {NNN}.xlsx`.
3. **Consolide as pendências** de todas as etapas numa lista única, cada uma com **responsável** e próximo passo, e grave a lista na aba `Pendências` do papel de trabalho:

| Responsável | Exemplos | Como sai daqui |
|---|---|---|
| Cliente | documento que não veio, PIX sem identificação, contrato de empréstimo | E-mail redigido com `pendencias-fechamento-cliente` |
| Fiscal | avisos e liberação de IRPJ/CSLL do Real (Etapa 6), divergência de receita | Confirmar com o colaborador que foram enviados |
| DP | retenção `PENDENTE`/`NÃO ENTREGUE` na GATILHO da REINF, folha que não bateu | Aviso ao DP redigido |
| Colaborador / revisor | `Pendência aceita` do papel de trabalho, diferença herdada de mês já fechado | Fica registrada para o revisor decidir |

4. **Atualize o mapa contábil do cliente:** regras novas ou corrigidas nas Etapas 3 a 5, módulos e lançamentos manuais recorrentes novos no `Perfil` (Etapa 4), saldos finais da competência fechada na aba `Saldos` (são a abertura do próximo mês), os tributos apurados e pagos do mês na aba `Apuração` (no Real, também a forma: estimativa, suspensão ou redução) e uma linha no `Histórico`. O próximo fechamento começa desse mapa.
5. **Alimente o artefato Controle Contábil** (linha `{NNN}_{AAAA-MM}` da coleção `fechamento`): mostre ao colaborador os campos que vai gravar e **grave só depois que ele autorizar** — situação dos documentos, docs pendentes, observação do analista (o resumo para o revisor, curto), "Liberado p/ Gian/contador" (`Sim` só sem etapa aberta; senão `Não`), data da liberação e status (`Liberado para revisão` ou `Em andamento`). Campos, regras e o que nunca gravar (senha, CPF, nome de arquivo com senha) em `references/encerramento-artefato-email.md`. Com `Liberado = Sim`, a competência aparece no bloco **"Liberados para revisão"** no topo do artefato, que é o aviso ao revisor/contador. Se a gravação não for possível ou não for autorizada, diga ao colaborador o que preencher à mão.
6. **Redija o e-mail ao revisor (Gian)** com o modelo da referência: assunto padronizado, resultado do mês e acumulado, tributos (conferidos, liberados ao fiscal, avisados), achados principais, pendências por responsável, caminho do papel de trabalho e o link do artefato. O colaborador envia (ou cria o rascunho no Outlook com `resumo-rascunho-email-owa`, se usar). Não invente o endereço do Gian — deixe o campo para o colaborador preencher.
7. **Em modo teste:** não grave "Liberado = Sim" no artefato nem envie e-mail; mostre o que seria gravado e o rascunho, e registre as hipóteses do teste no `Histórico` do mapa.

**Se a revisão devolver o fechamento** (o revisor marca ajuste no artefato): o colaborador abre de novo esta conversa, ou uma nova com o mesmo cliente e competência. Volte à etapa onde está o ajuste (em geral 5 ou 6), registre a correção na aba `Rodadas` do papel de trabalho, atualize o mapa se a correção mudar uma regra e entregue de novo para revisão.

**Próximo período:** o que depende de alguém antes do próximo fechamento (documento do cliente, procuração, retificação do fiscal) vai na aba `Pendências` com o responsável — o próximo fechamento começa conferindo essa aba na Etapa 1.

**Porta de saída da Etapa 7 (fim do fechamento):** portas das etapas 1 a 6 conferidas, arquivos no lugar, pendências com responsável, mapa atualizado, linha do artefato gravada (ou o que preencher passado ao colaborador) e e-mail ao revisor redigido.

## Regras importantes

- Nunca presuma um número, documento ou conta que não foi enviado nem confirmado nesta conversa — pergunte antes de lançar ou apurar com base nele.
- Nunca pule uma etapa "para ganhar tempo": a apuração (Etapa 6) depende do balancete conciliado (Etapa 5), que depende dos lançamentos importados (Etapas 3 e 4), que dependem de entender a lógica contábil do cliente (Etapa 2), que depende do pacote de documentos (Etapa 1).
- Nunca cite base legal, prazo ou norma contábil como definitivo sem a confirmação no Lefisc (ver "Regra de honestidade e fonte legal" acima) — isso vale mesmo quando a resposta "parece óbvia" pela experiência geral.
- Nunca peça nem digite senha de certificado digital, de e-CAC, de prefeitura ou de banco; e nunca repita no chat — nem grave em planilha ou no artefato — senhas, códigos de acesso, nomes de arquivo que contenham senha ou CPF de sócios ou empregados que apareçam em documentos ou planilhas. Da folha, use totais; salário individual só quando for preciso para explicar uma divergência. O download nos portais é feito pelo colaborador, com o acesso dele.
- Ao final de cada etapa, proponha o próximo passo explicitamente e espere o colaborador confirmar ou corrigir o rumo antes de seguir.
- Em caso de conflito entre esta skill e uma skill específica acionada numa etapa, a skill mais específica da etapa prevalece.

## Quando escalar / não usar esta skill

- Fechamento **fiscal** (conferência municipal/estadual, registro na Controle_Fiscal) → `fechamento-completo-servicos` (clientes só de serviços) ou o POP fiscal do escritório; esta skill começa depois que o fiscal libera a competência.
- MEI → `apuracao-mei`.
- Cálculo isolado de um tributo, sem fechamento contábil → a skill de apuração do regime (`calcular-das-simples-nacional`, `apuracao-lucro-presumido`, `apuracao-lucro-real`).
- ECD/ECF anuais (depois dos fechamentos mensais consolidados) → `ecd-escrituracao-contabil-digital` e `ecf-escrituracao-contabil-fiscal`.
