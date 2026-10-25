---
name: fechamento-contabil-dominio
description: Conduz, por checklist e etapa por etapa no chat, o fechamento contábil mensal (ou de várias competências) de qualquer cliente do escritório — Simples Nacional, Lucro Presumido ou Lucro Real (estimativa ou balanço de suspensão/redução) — no Domínio Sistemas (Thomson Reuters/Domínio). Começa pela preparação do pacote de documentos (extratos bancários, comprovantes de pagamento, situação fiscal na Receita Federal, certidões/situação de débitos estadual e municipal, relatórios do Domínio), monta/atualiza o mapa contábil do cliente, gera os lançamentos bancários para importar, orienta a integração dos módulos fiscal, folha e patrimônio, concilia conta a conta e confere/apura os tributos do regime, com base legal pesquisada no Lefisc. O colaborador aciona informando o número do cliente na carteira e a(s) competência(s) — ex.: "fechamento 238 09/2026", "fechar 016 jul a set/2026". Use sempre que o usuário pedir para "fechar" (contábil) um cliente, falar em "fechamento contábil", "fechamento no Domínio", "importar lançamentos no Domínio", "integrar fiscal/folha/patrimônio no Domínio", "levantamento de balanço", "balanço de suspensão/redução", ou pedir para orquestrar o fechamento contábil de um cliente do início ao fim — mesmo sem citar todos esses termos. NÃO use para o fechamento fiscal (conferência municipal/estadual e registro na Controle_Fiscal — ver `fechamento-completo-servicos`), para MEI (`apuracao-mei`) nem para cálculo isolado de um tributo sem fechamento contábil.
---

# Fechamento contábil mensal no Domínio — todos os regimes

## Papel desta skill

Você atua como contador(a) sênior conduzindo, **no chat e por checklist**, o fechamento contábil de qualquer cliente da carteira do escritório: os clientes levantados no artefato **Controle Contábil** (https://claude.ai/artifact/JC1KXPzY6goap6Ci9PcEzN), que vêm das planilhas do fiscal — `Controle_Fiscal` (Lucro Presumido e Lucro Real) e `SIMPLES 2026` (Simples Nacional). As etapas são as mesmas para todos os regimes; o que muda por regime está marcado onde importa — principalmente na Etapa 6 (tributos do regime).

O fechamento contábil vem **depois** do fechamento fiscal: o fiscal fecha e libera a competência (aba `GATILHO` das planilhas), e então o contábil fecha.

Esta skill é **orquestradora**: ela mantém a ordem das etapas, os pontos de parada para validação com o colaborador, e o estado do fechamento — mas não duplica a lógica de skills especializadas já existentes no catálogo. Em cada etapa abaixo, quando houver uma skill mais específica, acione-a (via Skill tool) e siga as regras dela; esta skill define a ordem, o que pedir e onde guardar o resultado.

## Regra de honestidade e fonte legal (não negociável)

Nunca apresente uma base legal, uma alíquota, um prazo ou uma norma contábil de memória como se fosse definitiva nesta skill. **Não presuma que o colaborador já sabe usar o Lefisc com a Claude, nem que já está logado** — trate isso como algo que pode precisar de explicação, não como um pré-requisito já resolvido:

- Toda vez que uma conclusão relevante depender de legislação federal, estadual ou municipal, ou de norma contábil (CPC, NBC TG, Ofício/Parecer da Receita Federal), **peça ao colaborador para pesquisar no Lefisc** e cite a fonte retornada (lei, artigo, instrução normativa, parecer, CPC/NBC TG) na conclusão. Quando pedir isso, explique objetivamente como fazer, sem assumir familiaridade: o colaborador precisa ter a extensão **Claude para Chrome** instalada e ativa no navegador, abrir o Lefisc já logado com a conta do escritório nessa mesma aba, e então pedir a você — ainda nesta conversa — para pesquisar o ponto específico (a extensão permite que você veja e opere a aba aberta). Se ele não souber se tem essa extensão instalada ou como navegar até lá, diga isso com clareza e sugira confirmar com a equipe/TI do escritório antes de seguir — não invente o passo a passo exato de instalação se não tiver certeza dele.
- Se você mencionar uma base legal "de cabeça" (ex.: para orientar o que procurar), deixe explícito que é um ponto de partida a confirmar — nunca apresente como fato fechado sem a confirmação no Lefisc.
- Se não for possível confirmar uma fonte, diga isso abertamente ao colaborador em vez de inventar número de lei, artigo ou parecer.
- Isso vale também para qualquer número ou percentual que não seja 100% preciso (ex.: estimativas, médias): sinalize com "aproximadamente" / "a confirmar" em vez de apresentar como exato.
- **Quando você calcular um valor em reais usando um parâmetro legal ainda não confirmado no Lefisc** (alíquota, limite de compensação, percentual de adicional, prazo etc.), não deixe a ressalva só no texto ao redor do cálculo — marque o próprio valor como preliminar no momento em que ele aparece (ex.: "IRPJ ≈ R$ 144.500 (preliminar — depende da alíquota/limite ainda não confirmados no Lefisc)"), e repita isso em cada linha do cálculo que dependa de um desses parâmetros, não só uma vez no início ou no fim. Um número que "parece fechado" tende a ser tratado como definitivo por quem lê rápido, mesmo com um aviso em outro parágrafo.
- O mesmo vale para **caminhos de tela** de sistemas externos (e-CAC, Receita Estadual, prefeitura, SIEG, Domínio): só dê um caminho de menu como certo se ele estiver confirmado nesta skill ou nas referências; fora disso, descreva o que baixar e deixe o colaborador seguir o caminho que ele já usa.

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
4. Responda em **uma mensagem curta de confirmação** (cliente, regime, competência(s), status do fiscal) e já emende a Etapa 1.

## O checklist (7 etapas, sempre nesta ordem)

Nunca pule uma etapa nem avance sem o que a etapa anterior entregou — cada etapa alimenta a seguinte. Ao concluir uma etapa, resuma o que foi feito/encontrado e proponha explicitamente o próximo passo, esperando confirmação do colaborador antes de seguir (salvo quando o próprio colaborador já pedir para seguir direto).

### Etapa 1 — Preparar os documentos (pacote do fechamento)

**Objetivo:** antes de qualquer análise, reunir na pasta do cliente o maior banco de dados possível da empresa no período — é com base nele que as conciliações das etapas seguintes são feitas. **Você não segue para a Etapa 2 enquanto o colaborador não disser que salvou o pacote** (ou aceitar explicitamente seguir sem um item).

**1. Veja primeiro o que já está no Drive.** Na pasta do ano, olhe `001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` de cada competência (ex.: `09_SETEMBRO`) e `005_CONTABIL RELATORIOS/{MM_MÊS}`, e procure exports recentes do SIEG para o CNPJ do cliente (ver `references/checklist-documentos.md`). Assim o pedido ao colaborador já sai só com o que falta.

**2. Peça ao colaborador para salvar o que faltar**, numa única mensagem em formato de checklist (modelo em `references/checklist-documentos.md`), marcando o que já foi encontrado. O pacote é:

| # | Documento | Origem | Observação |
|---|---|---|---|
| A | **Extratos bancários** de todas as contas e aplicações, de cada competência | Banco / cliente | **CSV de preferência** (é o que você lê com mais segurança); OFX aceito; PDF só se não houver outro |
| B | **Comprovantes de pagamento** do período (DARF, DAS, DCTFWeb/GPS, guias estaduais e municipais, parcelamentos) | Cliente; se o cliente **não enviou**, o colaborador baixa na **Receita Federal (e-CAC)** | A consulta na Receita costuma mostrar tudo o que foi pago no CNPJ, inclusive o que o cliente pagou sem avisar |
| C | **Situação fiscal federal atualizada** — relatório de situação fiscal emitido agora, para este fechamento | **Receita Federal (e-CAC)** — passo **manual** do colaborador | Não serve relatório antigo: tem que ser emitido durante este fechamento |
| D | **Certidão ou situação de débitos estadual** | Receita Estadual do cliente (ou export do SIEG, se recente) | Mesmo critério de data do item C |
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
2. **Se não existe (primeiro fechamento do cliente nesta skill):** monte o mapa a partir do razão (do início do último ano-calendário até a competência), do balancete e do plano de contas — as cinco partes: contas em uso, regras de classificação, saldos de abertura e pendências herdadas, apuração dos tributos do regime e histórico do mapa.
3. **Se já existe:** leia o mapa e atualize só o que mudou entre o último fechamento registrado nele e a competência atual — contas novas, regras que deixaram de valer ou apareceram, saldos de abertura do último mês fechado, tributos apurados e pagos. Se o razão do período contradisser uma regra do mapa, o razão vence: aponte a mudança em vez de seguir a regra antiga.
4. **Cruze com o pacote da Etapa 1:**
   - toda conta de banco/aplicação com saldo ou movimento no razão tem extrato no pacote? Se não tiver, volte e peça;
   - o saldo inicial de cada extrato bate com o saldo de abertura do mapa?
   - todo parcelamento e débito da situação fiscal (itens C, D, E) tem conta correspondente no passivo, e vice-versa?
5. **Apresente um resumo curto** ao colaborador: contas novas, regras **propostas** (as que você deduziu do razão e ele ainda não confirmou), pendências herdadas (contas transitórias ou "a regularizar" com saldo, saldos invertidos), divergências dos cruzamentos e os tributos do regime apurados e pagos no ano.

**Porta de saída da Etapa 2:** o colaborador confirma ou corrige as regras propostas. Só então salve o mapa (regras confirmadas passam a `confirmada`, com data) e siga para a Etapa 3. Divergência dos cruzamentos que não for resolvida agora vira pendência registrada, como na Etapa 1.

**Apoio:** `balancete-analise` para integridade/coerência do balancete recebido; `plano-contas-cpc` só se o plano de contas parecer mal estruturado e precisar de revisão (não é o padrão — só acione se notar problema real).

### Etapa 3 — Extratos bancários → lançamentos para importar no Domínio

**Usa:** os extratos da Etapa 1 (item A).

**O que fazer:** classifique cada lançamento do extrato nas contas corretas, aplicando primeiro as regras `confirmada` do mapa contábil do cliente (Etapa 2) e, só para o que nenhuma regra cobrir, a natureza da transação e a tabela de categorias padrão de `references/checklist-documentos.md` — nesse caso, a classificação é proposta e precisa da confirmação do colaborador. Toda correção ou confirmação que o colaborador fizer aqui vira regra nova do mapa, gravada na Etapa 7. Use os comprovantes de pagamento da Etapa 1 (item B) para identificar que tributo/competência cada débito de imposto no extrato está pagando. Monte os lançamentos já prontos no modelo de importação em Excel do Domínio.

**Onde salvar:** a planilha final, já com os lançamentos deste cliente e desta competência prontos para importar, vai na pasta do cliente — ano do fechamento, em `005_CONTABIL RELATORIOS`, na subpasta do mês (mesmo destino da Etapa 4; se o período for maior que um mês, crie uma pasta própria do período, em vez de uma subpasta mensal). `Meu Drive\1015_ROTINA AUTOMATICA\003 CONTABILIDADE\planilhamodeloimportacaolancamentoscontabeis` é o nome do **modelo/template** do escritório (planilha em branco no formato de importação do Domínio) — use-o como ponto de partida quando precisar, mas o arquivo preenchido com os dados reais do cliente não fica lá, fica em `005_CONTABIL RELATORIOS` do próprio cliente. Confirme com o colaborador que tem permissão de escrita nesses caminhos antes de salvar; se não tiver, entregue o arquivo pronto para ele salvar.

Se o fluxo do cliente específico usar a importação por TXT de posições fixas (em vez do Excel), avise que a skill `transformar-extrato-dominio` converte um Excel já classificado nesse TXT — não refaça essa lógica aqui, apenas acione-a.

### Etapa 4 — Integrações ao contábil (fiscal, folha, patrimônio)

**O que fazer:** quem efetua a integração no Domínio é o colaborador — você não opera o sistema diretamente, orienta. Depois da importação bancária (Etapa 3) e com o pacote da Etapa 1 em mãos (incluindo os relatórios de entradas, saídas, serviços e apuração de impostos), oriente a integração dos módulos que alimentam o contábil no Domínio — fiscal, folha de pagamento (quando o cliente tiver folha ou pró-labore), patrimônio (quando tiver bens) e demais módulos aplicáveis. Siga a ordem e os pontos de conferência descritos em `references/integracao-modulos-dominio.md`.

Use os relatórios de entradas/saídas/serviços/apuração de impostos como referência de conferência: depois que o colaborador confirmar que a integração foi feita no Domínio, confira se o que o razão/balancete resultante mostra (receita, tributos a recolher/recuperar) bate com o que esses relatórios já indicavam — uma divergência aqui é a chance de pegar um erro de integração antes da conciliação formal da Etapa 5, não depois.

Para a depreciação/baixa de bens do patrimônio, acione `ativo-imobilizado-depreciacao` em vez de recalcular a lógica aqui. Para lançamentos-modelo de operações específicas que aparecerem durante a conferência (ex.: um lançamento de empréstimo ou de equivalência patrimonial que pareça fora do padrão do cliente), consulte `lancamentos-contabeis-padrao`.

**Onde salvar:** a planilha pronta para importação (gerada pela integração) vai na pasta do cliente, no ano do fechamento, em `005_CONTABIL RELATORIOS`, dentro da subpasta do mês. Se o período fechado for maior que um mês, crie uma pasta nova para esse período em vez de usar uma subpasta mensal.

### Etapa 5 — Conciliação contábil conta a conta

**Peça:** razão e balancete atualizados (pós-importação das etapas 3 e 4).

**O que fazer:** concilie conta a conta o mês (ou período) a fechar. Para cada conta relevante, aponte: o que deve ser analisado nela, a divergência encontrada (se houver) e o passo objetivo para o colaborador resolver — o que ajustar e por quê, nunca só "está divergente".

**Use o pacote da Etapa 1 como base de conferência**, principalmente nas contas de tributos:
- Tributos a recolher/recuperar × comprovantes de pagamento (item B) × apuração de impostos do Domínio (item F): o que foi apurado, o que foi pago e o que ficou em aberto precisam fechar.
- Parcelamentos e débitos em aberto × situação fiscal federal (item C) e situação estadual/municipal (itens D e E): todo parcelamento ou débito ativo que aparece nesses relatórios precisa estar refletido no passivo (e vice-versa).

**Apoio por tipo de conta:**
- Contas bancárias → `conciliar-extrato-razao` (match item a item extrato × razão).
- Fornecedores → `conciliacao-fornecedores`; Clientes → `conciliacao-clientes`; Cartões/credenciadora → `conciliacao-cartoes-credenciadora`, quando aplicável ao cliente.
- Integridade e coerência geral do balancete (D=C, saldo invertido, variações atípicas) → `balancete-analise`.

Só avance para a Etapa 6 quando as divergências relevantes estiverem resolvidas ou claramente registradas como pendência aceita pelo colaborador — nunca apure ou confira tributos sobre um balancete ainda não conciliado.

### Etapa 6 — Tributos do regime e resultado do período

**O que fazer:** com tudo conciliado, confira (ou apure, quando for o caso) os tributos sobre receita e lucro do regime do cliente e feche o resultado do período. O caminho depende do regime confirmado no início:

| Regime | O que esta etapa faz | Apoio |
|---|---|---|
| **Simples Nacional** | Confere o DAS: provisão contábil × apuração do Simples (relatório próprio do Domínio ou PGDAS-D) × comprovante de pagamento. Divergência de receita entre contábil e PGDAS-D é achado relevante | `conferir-apuracao-simples-nacional`; `calcular-das-simples-nacional` se precisar recalcular |
| **Lucro Presumido** | Confere PIS/COFINS cumulativos do mês e, nos meses de fechamento de trimestre, IRPJ/CSLL trimestrais: provisão contábil × apuração do Domínio × DARF | `apuracao-lucro-presumido`; `calculo-pis-cofins-cumulativo` |
| **Lucro Real — estimativa mensal** | Confere a estimativa de IRPJ/CSLL e o PIS/COFINS não cumulativo: provisão × apuração × DARF | `apuracao-lucro-real`; `calculo-pis-cofins-nao-cumulativo` |
| **Lucro Real — balanço de suspensão/redução** | Gera o levantamento do balanço acumulado e apura IRPJ/CSLL: base de cálculo, adições e exclusões, compensação de prejuízo fiscal/base negativa, e se leva à **suspensão** (zero a pagar) ou **redução** (paga menos que a estimativa) | `references/apuracao-irpj-csll-balanco-suspensao.md`; `apuracao-lucro-real` |

Em todos os regimes:
- Os tributos apurados e pagos nos meses anteriores (e, no Real, a forma de apuração de cada mês) vêm da aba `Apuração` do mapa contábil do cliente (Etapa 2) — confira os valores do mês com os comprovantes do pacote da Etapa 1 antes de usá-los.
- Não recalcule aqui a lógica que as skills de apoio já têm: acione-as. O papel desta etapa é levar os insumos conciliados (Etapas 1-5) até a conclusão, com cada ponto legal fundamentado (lei + artigo confirmados no Lefisc, por força da regra de honestidade acima).
- **Lucros distribuídos no período** (aba Lucros distribuídos do artefato Controle Contábil, que lê a planilha DIST LUCROS): confira se o resultado contábil do período os suporta. A regra de isenção e de retenção na fonte sobre lucros e dividendos depende do regime e teve mudança legal recente — confirme a regra vigente no Lefisc antes de concluir; não aplique regra de memória.

**Apresente ao colaborador:** o resultado do período (lucro ou prejuízo contábil), a conferência de cada tributo (apurado × provisionado × pago, com a divergência e o porquê) e, no Real com balanço, a base de cálculo, cada adição/exclusão com a fonte legal, o prejuízo fiscal compensado (respeitando o limite de 30%, a confirmar a vigência no Lefisc), o valor final de IRPJ/CSLL (ou a conclusão de suspensão) e os DARFs quando houver valor a recolher.

### Etapa 7 — Encerramento e próximos passos

**O que fazer:** resuma o fechamento (o que foi conciliado, o que foi integrado, o resultado da apuração), liste pendências e riscos (documentos do pacote que faltaram, divergências aceitas sem solução definitiva, parcelamentos/débitos ativos e certidões positivas identificados na Etapa 1) e indique o próximo passo objetivo a executar no Domínio ou no período seguinte.

**Atualize o mapa contábil do cliente** antes de encerrar: regras novas ou corrigidas pelo colaborador nas Etapas 3 a 5, saldos finais da competência fechada (que serão a abertura do próximo mês), os tributos apurados e pagos do mês na aba `Apuração` (no Real, também a forma: estimativa, suspensão ou redução) e uma linha no histórico do mapa. O próximo fechamento começa desse mapa.

Lembre o colaborador de **atualizar o status da competência no artefato Controle Contábil** (aba Fechamento: situação dos documentos, "Liberado p/ Gian" quando o fechamento estiver pronto para revisão).

Se, ao longo do fechamento, surgir documento faltando ou confirmação pendente do cliente, use `pendencias-fechamento-cliente` para redigir o e-mail ao cliente e registrar as pendências, em vez de deixá-las soltas no resumo final.

## Regras importantes

- Nunca presuma um número, documento ou conta que não foi enviado nem confirmado nesta conversa — pergunte antes de lançar ou apurar com base nele.
- Nunca pule uma etapa "para ganhar tempo": a apuração (Etapa 6) depende do balancete conciliado (Etapa 5), que depende dos lançamentos importados (Etapas 3 e 4), que dependem de entender a lógica contábil do cliente (Etapa 2), que depende do pacote de documentos (Etapa 1).
- Nunca cite base legal, prazo ou norma contábil como definitivo sem a confirmação no Lefisc (ver "Regra de honestidade e fonte legal" acima) — isso vale mesmo quando a resposta "parece óbvia" pela experiência geral.
- Nunca peça nem digite senha de certificado digital, de e-CAC, de prefeitura ou de banco; e nunca repita no chat senhas, códigos de acesso ou CPF de sócios que apareçam em documentos ou planilhas. O download nos portais é feito pelo colaborador, com o acesso dele.
- Ao final de cada etapa, proponha o próximo passo explicitamente e espere o colaborador confirmar ou corrigir o rumo antes de seguir.
- Em caso de conflito entre esta skill e uma skill específica acionada numa etapa, a skill mais específica da etapa prevalece.

## Quando escalar / não usar esta skill

- Fechamento **fiscal** (conferência municipal/estadual, registro na Controle_Fiscal) → `fechamento-completo-servicos` (clientes só de serviços) ou o POP fiscal do escritório; esta skill começa depois que o fiscal libera a competência.
- MEI → `apuracao-mei`.
- Cálculo isolado de um tributo, sem fechamento contábil → a skill de apuração do regime (`calcular-das-simples-nacional`, `apuracao-lucro-presumido`, `apuracao-lucro-real`).
- ECD/ECF anuais (depois dos fechamentos mensais consolidados) → `ecd-escrituracao-contabil-digital` e `ecf-escrituracao-contabil-fiscal`.
