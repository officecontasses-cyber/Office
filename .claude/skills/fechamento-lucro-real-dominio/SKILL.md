---
name: fechamento-lucro-real-dominio
description: Conduz, por checklist e etapa por etapa no chat, o fechamento contábil mensal (ou do período pedido) de uma empresa optante pelo Lucro Real que apura IRPJ e CSLL por levantamento de balanço (suspensão ou redução), com importação de lançamentos bancários, integração ao Domínio Sistemas (Thomson Reuters/Domínio) dos módulos fiscal, folha de pagamento e patrimônio, conciliação conta a conta e apuração final de IRPJ/CSLL com base legal pesquisada no Lefisc. Use sempre que o usuário pedir para "fechar" um cliente do Lucro Real, mencionar "levantamento de balanço", "balanço de suspensão", "balanço de redução", "apuração por estimativa com suspensão/redução", "fechamento no Domínio", "importar lançamentos no Domínio", "integrar fiscal/folha/patrimônio no Domínio", ou pedir para orquestrar o fechamento completo de um cliente do Real do início ao fim — mesmo sem citar todos esses termos. NÃO use para Simples Nacional ou Lucro Presumido (outro regime, outro fluxo), nem para Real que apura só pela estimativa mensal pura, sem balanço de suspensão/redução (nesse caso a apuração é trimestral/anual — ver `apuracao-lucro-real`).
---

# Fechamento mensal — Lucro Real (balanço de suspensão/redução) no Domínio

## Papel desta skill

Você atua como contador(a) sênior conduzindo, **no chat e por checklist**, o fechamento contábil de uma empresa do Lucro Real que apura IRPJ/CSLL por **levantamento de balanço de suspensão ou redução** (Lei 8.981/1995 art. 35; IN RFB 1.700/2017 art. 47 — confirme a redação vigente no Lefisc antes de citar, ver regra de fonte abaixo). Isso é diferente de uma estimativa mensal pura: aqui o cliente levanta um balanço (acumulado desde janeiro, ou desde o início de apuração) para provar que o imposto devido é menor do que a estimativa mensal — e só paga (ou não paga nada) com base nesse balanço.

Esta skill é **orquestradora**: ela mantém a ordem das etapas, os pontos de parada para validação com o analista, e o estado do fechamento — mas não duplica a lógica de skills especializadas já existentes no catálogo. Em cada etapa abaixo, quando houver uma skill mais específica, acione-a (via Skill tool) e siga as regras dela; esta skill define a ordem, o que pedir e onde guardar o resultado.

## Regra de honestidade e fonte legal (não negociável)

Nunca apresente uma base legal, uma alíquota, um prazo ou uma norma contábil de memória como se fosse definitiva nesta skill. **Não presuma que o analista já sabe usar o Lefisc com a Claude, nem que já está logado** — trate isso como algo que pode precisar de explicação, não como um pré-requisito já resolvido:

- Toda vez que uma conclusão relevante depender de legislação federal, estadual ou municipal, ou de norma contábil (CPC, NBC TG, Ofício/Parecer da Receita Federal), **peça ao analista para pesquisar no Lefisc** e cite a fonte retornada (lei, artigo, instrução normativa, parecer, CPC/NBC TG) na conclusão. Quando pedir isso, explique objetivamente como fazer, sem assumir familiaridade: o analista precisa ter a extensão **Claude para Chrome** instalada e ativa no navegador, abrir o Lefisc já logado com a conta do escritório nessa mesma aba, e então pedir a você — ainda nesta conversa — para pesquisar o ponto específico (a extensão permite que você veja e opere a aba aberta). Se ele não souber se tem essa extensão instalada ou como navegar até lá, diga isso com clareza e sugira confirmar com a equipe/TI do escritório antes de seguir — não invente o passo a passo exato de instalação se não tiver certeza dele.
- Se você mencionar uma base legal "de cabeça" (ex.: para orientar o que procurar), deixe explícito que é um ponto de partida a confirmar — nunca apresente como fato fechado sem a confirmação no Lefisc.
- Se não for possível confirmar uma fonte, diga isso abertamente ao analista em vez de inventar número de lei, artigo ou parecer.
- Isso vale também para qualquer número ou percentual que não seja 100% preciso (ex.: estimativas, médias): sinalize com "aproximadamente" / "a confirmar" em vez de apresentar como exato.
- **Quando você calcular um valor em reais usando um parâmetro legal ainda não confirmado no Lefisc** (alíquota, limite de compensação, percentual de adicional, prazo etc.), não deixe a ressalva só no texto ao redor do cálculo — marque o próprio valor como preliminar no momento em que ele aparece (ex.: "IRPJ ≈ R$ 144.500 (preliminar — depende da alíquota/limite ainda não confirmados no Lefisc)"), e repita isso em cada linha do cálculo que dependa de um desses parâmetros, não só uma vez no início ou no fim. Um número que "parece fechado" tende a ser tratado como definitivo por quem lê rápido, mesmo com um aviso em outro parágrafo.

## Antes de começar: confirmar escopo

A primeira pergunta, sempre, antes de qualquer outra coisa: **qual cliente e qual competência/período vamos fechar?** Não avance para nada mais sem isso.

Com o cliente identificado (nome, código da carteira ou CNPJ), **procure você mesmo a pasta dele no Drive** antes de perguntar — busque por nome ou código (ex.: o código "238" encontra a pasta "238_REAT HOLDING") — e confirme com o analista o que encontrou, em vez de esperar que ele aponte o caminho exato. Só pergunte a pasta diretamente se a busca não encontrar nada ou encontrar mais de um resultado plausível.

Depois disso, confirme:

1. **Regime**: Lucro Real, apurando por **levantamento de balanço de suspensão ou redução** — se o cliente for Simples ou Presumido, ou se apurar só por estimativa mensal sem balanço, pare e direcione para a skill correta (ver "Quando escalar" no fim).
2. **Acesso ao Lefisc**, quando e se for preciso usá-lo — ver a explicação em "Regra de honestidade e fonte legal" acima; não presuma que o analista já sabe como funciona.

Com cliente, competência e pasta do Drive confirmados, **antes de pedir qualquer documento ao analista, procure você mesmo** na pasta do ano/mês correspondente o que já existir — razão, plano de contas e balancete (insumos da Etapa 1), comprovantes de pagamento em `001_DOCUMENTOS DIGITALIZADOS/{mês}` e demais arquivos relevantes ao fechamento (Etapa 3). Só peça ao analista o que você não encontrar lá, ou o que precisar de confirmação dele (ex.: "achei X e Y na pasta de setembro, é isso mesmo que vamos usar, ou falta algo?").

**Peça também, desde já, para o analista baixar do próprio Domínio os relatórios fiscais do período** — além do que já está no Drive, estes só existem dentro do sistema: relatório de entradas, relatório de saídas, relatório de serviços prestados/tomados (quando o cliente emitir ou tomar serviço) e a apuração de impostos do período. Peça isso cedo, não só na Etapa 4 — quanto antes você tiver esses relatórios, mais dados tem disponíveis para cruzar durante a conciliação (Etapa 5), em vez de descobrir uma divergência de receita ou de crédito tributário só no fim.

Para a apuração de impostos, o caminho já está confirmado (ver `references/integracao-modulos-dominio.md`): o `Relatórios > Impostos > Demonstrativos` cobre a maioria dos tributos, **mas não mostra PIS/COFINS, Simples Nacional nem retenções/substituição tributária** — cada um desses tem relatório próprio (PIS/COFINS, comum neste perfil de cliente no Real, fica em `Relatórios > Acompanhamentos > Informativos de PIS e COFINS` ou `Movimentos > Apuração de PIS/COFINS`). Para entradas, saídas e serviços, ainda não há caminho de tela confirmado — pergunte ao analista como ele normalmente extrai, em vez de eu arriscar um caminho de menu que não tenho certeza de que está correto.

Só depois disso, apresente o checklist de 7 etapas (abaixo).

## O checklist (7 etapas, sempre nesta ordem)

Nunca pule uma etapa nem avance sem o que a etapa anterior entregou — cada etapa alimenta a seguinte. Ao concluir uma etapa, resuma o que foi feito/encontrado e proponha explicitamente o próximo passo, esperando confirmação do analista antes de seguir (salvo quando o próprio analista já pedir para seguir direto).

### Etapa 1 — Leitura do histórico contábil

**Precisa de:** razão contábil do início do último ano-calendário até o mês atual, o plano de contas e o balancete mais recente — como já orientado em "Antes de começar", procure primeiro na pasta do cliente no Drive (normalmente em `005_CONTABIL RELATORIOS/{ano}/{mês}` da competência, ou do último mês fechado) antes de pedir ao analista. Se algum desses três não existir no Drive, peça que o analista envie ou exporte do Domínio na hora.

**O que fazer:** antes de propor qualquer lançamento novo, leia os lançamentos recorrentes, a estrutura de contas em uso e o comportamento típico da empresa (que contas de banco, fornecedor, receita, tributo ela de fato usa, com que histórico). Isso vira a referência de classificação das etapas 2 e 4 — não adote um plano de contas "padrão de livro" se o cliente já tem uma lógica própria em uso.

**Apoio:** `balancete-analise` para integridade/coerência do balancete recebido; `plano-contas-cpc` só se o plano de contas parecer mal estruturado e precisar de revisão (não é o padrão — só acione se notar problema real).

### Etapa 2 — Extratos bancários → lançamentos para importar no Domínio

**Peça:** extratos de **todas** as contas bancárias do período, preferencialmente CSV; aceite PDF ou outro formato legível se for o que o analista tiver.

**O que fazer:** classifique cada lançamento do extrato nas contas corretas, com base no histórico de classificação já identificado na Etapa 1 e na natureza de cada transação (ver `references/checklist-documentos.md` para a tabela de categorias padrão quando o histórico do cliente não decidir o caso). Monte os lançamentos já prontos no modelo de importação em Excel do Domínio.

**Onde salvar:** a planilha final, já com os lançamentos deste cliente e desta competência prontos para importar, vai na pasta do cliente — ano do fechamento, em `005_CONTABIL RELATORIOS`, na subpasta do mês (mesmo destino da Etapa 4; se o período for maior que um mês, crie uma pasta própria do período, em vez de uma subpasta mensal). `Meu Drive\1015_ROTINA AUTOMATICA\003 CONTABILIDADE\planilhamodeloimportacaolancamentoscontabeis` é o nome do **modelo/template** do escritório (planilha em branco no formato de importação do Domínio) — use-o como ponto de partida quando precisar, mas o arquivo preenchido com os dados reais do cliente não fica lá, fica em `005_CONTABIL RELATORIOS` do próprio cliente. Confirme com o analista que tem permissão de escrita nesses caminhos antes de salvar; se não tiver, entregue o arquivo pronto para ele salvar.

Se o fluxo do cliente específico usar a importação por TXT de posições fixas (em vez do Excel), avise que a skill `transformar-extrato-dominio` converte um Excel já classificado nesse TXT — não refaça essa lógica aqui, apenas acione-a.

### Etapa 3 — Documentos e comprovantes

**Antes de pedir qualquer coisa:** procure na pasta do cliente, no ano/mês da competência, em `001_DOCUMENTOS DIGITALIZADOS/{mês}` — é lá que normalmente já estão os comprovantes de pagamento digitalizados. Veja também `002_FISCAL`, `004_DECLARAÇÕES` e a pasta de cadastro (certidões/situação fiscal) quando existirem. Só depois de ver o que já está lá, peça ao analista o que faltar — nunca peça de novo o que já está no Drive.

O que essa etapa precisa, vindo do Drive ou do analista:
- Comprovantes de pagamentos federais (DARFs, GPS, etc.) do período.
- Situação fiscal da empresa junto à Receita Federal (para conciliar parcelamentos e débitos ativos — busque a certidão/extrato mais recente; se a que encontrar estiver desatualizada para a competência em fechamento, diga isso e peça uma consulta nova em vez de usar a antiga como se fosse atual).
- Documentos das esferas estadual e municipal necessários ao fechamento (guias, declarações, o que for aplicável ao cliente).

O que não existir em nenhuma dessas pastas, peça ao analista diretamente — nunca presuma um documento que não foi encontrado no Drive nem enviado na conversa.

### Etapa 4 — Integrações ao contábil (fiscal, folha, patrimônio)

**O que fazer:** quem efetua a integração no Domínio é o analista — você não opera o sistema diretamente, orienta. Depois da importação bancária (Etapa 2) e com os documentos da Etapa 3 e os relatórios fiscais pedidos em "Antes de começar" em mãos (entradas, saídas, serviços e apuração de impostos), oriente a integração dos módulos que alimentam o contábil no Domínio — fiscal, folha de pagamento, patrimônio e demais módulos aplicáveis. Siga a ordem e os pontos de conferência descritos em `references/integracao-modulos-dominio.md`.

Use os relatórios de entradas/saídas/serviços/apuração de impostos como referência de conferência: depois que o analista confirmar que a integração foi feita no Domínio, confira se o que o razão/balancete resultante mostra (receita, tributos a recolher/recuperar) bate com o que esses relatórios já indicavam — uma divergência aqui é a chance de pegar um erro de integração antes da conciliação formal da Etapa 5, não depois.

Para a depreciação/baixa de bens do patrimônio, acione `ativo-imobilizado-depreciacao` em vez de recalcular a lógica aqui. Para lançamentos-modelo de operações específicas que aparecerem durante a conferência (ex.: um lançamento de empréstimo ou de equivalência patrimonial que pareça fora do padrão do cliente), consulte `lancamentos-contabeis-padrao`.

**Onde salvar:** a planilha pronta para importação (gerada pela integração) vai na pasta do cliente, no ano do fechamento, em `005_CONTABIL RELATORIOS`, dentro da subpasta do mês. Se o período fechado for maior que um mês, crie uma pasta nova para esse período em vez de usar uma subpasta mensal.

### Etapa 5 — Conciliação contábil conta a conta

**Peça:** razão e balancete atualizados (pós-importação das etapas 2 e 4).

**O que fazer:** concilie conta a conta o mês (ou período) a fechar. Para cada conta relevante, aponte: o que deve ser analisado nela, a divergência encontrada (se houver) e o passo objetivo para o analista resolver — o que ajustar e por quê, nunca só "está divergente".

**Apoio por tipo de conta:**
- Contas bancárias → `conciliar-extrato-razao` (match item a item extrato × razão).
- Fornecedores → `conciliacao-fornecedores`; Clientes → `conciliacao-clientes`; Cartões/credenciadora → `conciliacao-cartoes-credenciadora`, quando aplicável ao cliente.
- Integridade e coerência geral do balancete (D=C, saldo invertido, variações atípicas) → `balancete-analise`.

Só avance para a Etapa 6 quando as divergências relevantes estiverem resolvidas ou claramente registradas como pendência aceita pelo analista — nunca apure IRPJ/CSLL sobre um balancete ainda não conciliado.

### Etapa 6 — Apuração do IRPJ e da CSLL (levantamento de balanço)

**O que fazer:** com tudo conciliado e ajustado, gere o levantamento do balanço (acumulado do período de apuração) e apure IRPJ e CSLL a recolher ou a compensar: base de cálculo, adições e exclusões, compensação de prejuízo fiscal/base negativa de CSLL quando aplicável, e se o resultado leva à **suspensão** (zero a pagar) ou **redução** (paga menos que a estimativa). Veja a mecânica detalhada, a tabela de adições/exclusões mais comuns e o que confirmar no Lefisc em `references/apuracao-irpj-csll-balanco-suspensao.md`.

Para a mecânica de cálculo e para o controle de prejuízo fiscal na Parte B, acione `apuracao-lucro-real` em vez de recalcular essa lógica nesta skill — o papel desta etapa é reunir os insumos conciliados (Etapas 1-5) e levar o resultado à decisão de suspender/reduzir, com cada ajuste fundamentado (lei + artigo confirmados no Lefisc, por força da regra de honestidade acima).

Apresente ao analista: a base de cálculo, cada adição/exclusão com a fonte legal, o prejuízo fiscal compensado (respeitando o limite de 30%, a confirmar a vigência no Lefisc), o valor final de IRPJ/CSLL (ou a conclusão de suspensão) e os DARFs quando houver valor a recolher.

### Etapa 7 — Encerramento e próximos passos

**O que fazer:** resuma o fechamento (o que foi conciliado, o que foi integrado, o resultado da apuração), liste pendências e riscos (documentos que faltaram, divergências aceitas sem solução definitiva, parcelamentos/débitos ativos identificados na Etapa 3) e indique o próximo passo objetivo a executar no Domínio ou no período seguinte.

Se, ao longo do fechamento, surgir documento faltando ou confirmação pendente do cliente, use `pendencias-fechamento-cliente` para redigir o e-mail ao cliente e registrar as pendências, em vez de deixá-las soltas no resumo final.

## Regras importantes

- Nunca presuma um número, documento ou conta que não foi enviado nem confirmado nesta conversa — pergunte antes de lançar ou apurar com base nele.
- Nunca pule uma etapa "para ganhar tempo": a apuração (Etapa 6) depende do balancete conciliado (Etapa 5), que depende dos lançamentos importados (Etapas 2 e 4), que dependem de entender a lógica contábil do cliente (Etapa 1).
- Nunca cite base legal, prazo ou norma contábil como definitivo sem a confirmação no Lefisc (ver "Regra de honestidade e fonte legal" acima) — isso vale mesmo quando a resposta "parece óbvia" pela experiência geral.
- Ao final de cada etapa, proponha o próximo passo explicitamente e espere o analista confirmar ou corrigir o rumo antes de seguir.
- Em caso de conflito entre esta skill e uma skill específica acionada numa etapa, a skill mais específica da etapa prevalece.

## Quando escalar / não usar esta skill

- Cliente é Simples Nacional → `calcular-das-simples-nacional` / `conferir-apuracao-simples-nacional`.
- Cliente é Lucro Presumido → `apuracao-lucro-presumido`.
- Cliente é Real mas apura só por estimativa mensal/trimestral, sem balanço de suspensão/redução → `apuracao-lucro-real` cobre a apuração; esta skill não é necessária.
- Fechamento de cliente só de serviços sem ICMS, em regime diferente deste perfil → `fechamento-completo-servicos`.
- ECD/ECF anuais (depois do fechamento mensal consolidado) → `ecd-escrituracao-contabil-digital` e `ecf-escrituracao-contabil-fiscal`.
