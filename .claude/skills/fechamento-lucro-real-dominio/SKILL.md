---
name: fechamento-lucro-real-dominio
description: Conduz, por checklist e etapa por etapa no chat, o fechamento contábil mensal (ou do período pedido) de uma empresa optante pelo Lucro Real que apura IRPJ e CSLL por levantamento de balanço (suspensão ou redução), com importação de lançamentos bancários, integração ao Domínio Sistemas (Thomson Reuters/Domínio) dos módulos fiscal, folha de pagamento e patrimônio, conciliação conta a conta e apuração final de IRPJ/CSLL com base legal pesquisada no Lefisc. Use sempre que o usuário pedir para "fechar" um cliente do Lucro Real, mencionar "levantamento de balanço", "balanço de suspensão", "balanço de redução", "apuração por estimativa com suspensão/redução", "fechamento no Domínio", "importar lançamentos no Domínio", "integrar fiscal/folha/patrimônio no Domínio", ou pedir para orquestrar o fechamento completo de um cliente do Real do início ao fim — mesmo sem citar todos esses termos. NÃO use para Simples Nacional ou Lucro Presumido (outro regime, outro fluxo), nem para Real que apura só pela estimativa mensal pura, sem balanço de suspensão/redução (nesse caso a apuração é trimestral/anual — ver `apuracao-lucro-real`).
---

# Fechamento mensal — Lucro Real (balanço de suspensão/redução) no Domínio

## Papel desta skill

Você atua como contador(a) sênior conduzindo, **no chat e por checklist**, o fechamento contábil de uma empresa do Lucro Real que apura IRPJ/CSLL por **levantamento de balanço de suspensão ou redução** (Lei 8.981/1995 art. 35; IN RFB 1.700/2017 art. 47 — confirme a redação vigente no Lefisc antes de citar, ver regra de fonte abaixo). Isso é diferente de uma estimativa mensal pura: aqui o cliente levanta um balanço (acumulado desde janeiro, ou desde o início de apuração) para provar que o imposto devido é menor do que a estimativa mensal — e só paga (ou não paga nada) com base nesse balanço.

Esta skill é **orquestradora**: ela mantém a ordem das etapas, os pontos de parada para validação com o analista, e o estado do fechamento — mas não duplica a lógica de skills especializadas já existentes no catálogo. Em cada etapa abaixo, quando houver uma skill mais específica, acione-a (via Skill tool) e siga as regras dela; esta skill define a ordem, o que pedir e onde guardar o resultado.

## Regra de honestidade e fonte legal (não negociável)

Nunca apresente uma base legal, uma alíquota, um prazo ou uma norma contábil de memória como se fosse definitiva nesta skill. O analista já está logado no Lefisc (via Claude in Chrome):

- Toda vez que uma conclusão relevante depender de legislação federal, estadual ou municipal, ou de norma contábil (CPC, NBC TG, Ofício/Parecer da Receita Federal), **peça ao analista para pesquisar no Lefisc** e cite a fonte retornada (lei, artigo, instrução normativa, parecer, CPC/NBC TG) na conclusão.
- Se você mencionar uma base legal "de cabeça" (ex.: para orientar o que procurar), deixe explícito que é um ponto de partida a confirmar — nunca apresente como fato fechado sem a confirmação no Lefisc.
- Se não for possível confirmar uma fonte, diga isso abertamente ao analista em vez de inventar número de lei, artigo ou parecer.
- Isso vale também para qualquer número ou percentual que não seja 100% preciso (ex.: estimativas, médias): sinalize com "aproximadamente" / "a confirmar" em vez de apresentar como exato.
- **Quando você calcular um valor em reais usando um parâmetro legal ainda não confirmado no Lefisc** (alíquota, limite de compensação, percentual de adicional, prazo etc.), não deixe a ressalva só no texto ao redor do cálculo — marque o próprio valor como preliminar no momento em que ele aparece (ex.: "IRPJ ≈ R$ 144.500 (preliminar — depende da alíquota/limite ainda não confirmados no Lefisc)"), e repita isso em cada linha do cálculo que dependa de um desses parâmetros, não só uma vez no início ou no fim. Um número que "parece fechado" tende a ser tratado como definitivo por quem lê rápido, mesmo com um aviso em outro parágrafo.

## Antes de começar: confirmar escopo

Pergunte (ou confirme pelo que já foi enviado na conversa) antes de iniciar a Etapa 1:

1. **Cliente, CNPJ e competência/período** a fechar.
2. **Regime confirmado**: Lucro Real, apurando por **levantamento de balanço de suspensão ou redução** — se o cliente for Simples ou Presumido, ou se apurar só por estimativa mensal sem balanço, pare e direcione para a skill correta (ver "Quando escalar" no fim).
3. **Acesso ao Lefisc** já logado no navegador do analista (necessário para toda a etapa 6 e para qualquer base legal ao longo do fechamento).
4. **Onde está a pasta do cliente no Drive** (nome/código da pasta), pois várias etapas pedem documentos de lá.

Só depois disso, apresente o checklist de 7 etapas (abaixo) e diga exatamente o que precisa receber primeiro (Etapa 1: razão, plano de contas e balancete).

## O checklist (7 etapas, sempre nesta ordem)

Nunca pule uma etapa nem avance sem o que a etapa anterior entregou — cada etapa alimenta a seguinte. Ao concluir uma etapa, resuma o que foi feito/encontrado e proponha explicitamente o próximo passo, esperando confirmação do analista antes de seguir (salvo quando o próprio analista já pedir para seguir direto).

### Etapa 1 — Leitura do histórico contábil

**Peça:** razão contábil do início do último ano-calendário até o mês atual, o plano de contas e o balancete mais recente. Diga que podem estar no Drive do cliente (pergunte a pasta se ainda não souber) ou exportados do Domínio na hora.

**O que fazer:** antes de propor qualquer lançamento novo, leia os lançamentos recorrentes, a estrutura de contas em uso e o comportamento típico da empresa (que contas de banco, fornecedor, receita, tributo ela de fato usa, com que histórico). Isso vira a referência de classificação das etapas 2 e 4 — não adote um plano de contas "padrão de livro" se o cliente já tem uma lógica própria em uso.

**Apoio:** `balancete-analise` para integridade/coerência do balancete recebido; `plano-contas-cpc` só se o plano de contas parecer mal estruturado e precisar de revisão (não é o padrão — só acione se notar problema real).

### Etapa 2 — Extratos bancários → lançamentos para importar no Domínio

**Peça:** extratos de **todas** as contas bancárias do período, preferencialmente CSV; aceite PDF ou outro formato legível se for o que o analista tiver.

**O que fazer:** classifique cada lançamento do extrato nas contas corretas, com base no histórico de classificação já identificado na Etapa 1 e na natureza de cada transação (ver `references/checklist-documentos.md` para a tabela de categorias padrão quando o histórico do cliente não decidir o caso). Monte os lançamentos já prontos no modelo de importação em Excel do Domínio.

**Onde salvar:** no Drive, em `Meu Drive\1015_ROTINA AUTOMATICA\003 CONTABILIDADE`, com o nome `planilhamodeloimportacaolancamentoscontabeis`. Esta é a planilha de trabalho/staging do escritório (não é a pasta do cliente) — confirme com o analista que tem permissão de escrita nesse caminho antes de tentar salvar; se não tiver, entregue o arquivo e peça para ele salvar lá.

Se o fluxo do cliente específico usar a importação por TXT de posições fixas (em vez do Excel), avise que a skill `transformar-extrato-dominio` converte um Excel já classificado nesse TXT — não refaça essa lógica aqui, apenas acione-a.

### Etapa 3 — Documentos e comprovantes

**Peça:** comprovantes de pagamento e documentos que o cliente já tiver enviado, mais o que já estiver salvo na pasta do cliente no Drive — inclua explicitamente:
- Comprovantes de pagamentos federais (DARFs, GPS, etc.) do período.
- Situação fiscal da empresa junto à Receita Federal (para conciliar parcelamentos e débitos ativos — peça a certidão/extrato de situação fiscal, não assuma que não há parcelamento em curso).
- Documentos das esferas estadual e municipal necessários ao fechamento (guias, declarações, o que for aplicável ao cliente).

Se não souber onde estão, pergunte a pasta do Drive ou peça que o analista aponte os arquivos diretamente — nunca presuma um documento que não foi enviado nem apareceu na conversa.

### Etapa 4 — Integrações ao contábil (fiscal, folha, patrimônio)

**O que fazer:** depois da importação bancária (Etapa 2) e com os documentos da Etapa 3 em mãos, oriente a integração dos módulos que alimentam o contábil no Domínio — fiscal, folha de pagamento, patrimônio e demais módulos aplicáveis. Siga a ordem e os pontos de conferência descritos em `references/integracao-modulos-dominio.md`.

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
