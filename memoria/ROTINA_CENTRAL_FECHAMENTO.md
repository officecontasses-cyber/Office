# Rotina única da Central: G-Click + Controle_Fiscal + memória

Criada em 30/10/2026 a pedido da Fernanda ("monta a rotina única que cruza as três fontes").
Substitui as duas rotinas separadas de sincronização (G-Click 06:40 e planilha 06:45), que foram desativadas.
Agendada em `trig_016a6Uq5MEeC9DsgWUzLUsmJ` (06:45, seg a sex), **presa à conversa `session_01CWgCcTwyysvFaLyxrhSeXZ`**, porque só lá existem
ao mesmo tempo o conector do Google Sheets, o repositório com a `memoria/` e o acesso de rede à API do G-Click.

**Se esta conversa for arquivada, a rotina para.** O plano B é reativar `trig_016AfnLdRkGsJMffKFTxvRad`
(G-Click em sessão nova, que não depende de conector) e refazer o cruzamento à mão.

Painel: https://claude.ai/artifact/PYPKFYQgT9VNni3pZwg8G7

## Regras que valem para toda a rotina

- **G-Click: só leitura.** Apenas GET. Nunca POST, PUT, PATCH nem DELETE. O que precisa ser escrito lá sai
  como lista de ação no painel e como prompt para a extensão do Chrome.
- **Não escrever na Controle_Fiscal.** Toda atualização de status vai pela aba `Atualizações`, conforme o `CLAUDE.md`.
  Esta rotina **não** grava na fila: ela só lê a planilha e reporta divergência.
- **Não inventar.** Nenhum prazo, valor, cliente ou ato sem a fonte na mão. Não enviar nada a ninguém.
- **Escrita no painel sempre com `if_version`**, pelo `ArtifactData`, em `batch`. Nunca republicar a página.
- Nunca mexer em documento de origem `manual` nem no campo `notas` e `comando` (são da Fernanda), nem desmarcar passo.
- CNPJ só com números, buscado em `memoria/CNPJS_CLIENTES.md`.

## Etapa 1 — memória (antes de qualquer leitura de dado)

1. `git -C /home/user/Office fetch origin main && git rebase origin/main` (a `main` tem outras sessões gravando).
2. Ler `CLAUDE.md`, `memoria/PENDENCIAS.md` (as entradas dos últimos 3 dias) e `memoria/CNPJS_CLIENTES.md`.
3. Para cada cliente que aparecer como divergência na etapa 5, ler o dossiê `memoria/CLIENTE_NNN_*.md` antes de
   classificar. **Decisão já registrada na memória vence a aparência do dado.** Exemplos reais:
   - 133 RFL (`87828430000184`): prejuízo fiscal no 3ºTRIM, IRPJ e CSLL `Sem movimento` de propósito.
   - 197 ASBBM (`05164750000112`): IRPJ e CSLL `Não se aplica` (IN RFB 1.700/2017, art. 13), mas **há COFINS de 4%
     sobre receita financeira devida e em atraso**, e a ASBBM não tem tarefa de COFINS/PIS no G-Click.
   - Grupo Tacom (138, 248, 263): o federal é entregue pela matriz, que não é cliente. A falta de linhas de DARF,
     REINF e SPED Contribuições nesses três **não é falha do controle**.

## Etapa 2 — G-Click pela API

Base `https://api.gclick.com.br`. O proxy do ambiente injeta o Authorization: não chamar `/oauth/token` e não
mandar cabeçalho. Se vier 401, 403 ou host bloqueado, **parar sem gravar** e dizer o código no resumo.

- `GET /tarefas?categoria=Obrigacao&responsaveisIds=109763&size=100&page=N` com:
  - `dataVencimentoInicio` = hoje − 60 dias e `dataVencimentoFim` = hoje + 90 dias, **para a análise**;
  - os documentos do painel só são criados para o intervalo hoje − 30 a hoje + 30, para a lista não virar infinita.
- Paginar até `last: true`.
- Abertas: status `A`, `S`, `P`, `Q`, `E`. Fechadas: `C`, `F`, `D`, `X`, `O`. `D` é dispensada.
  O significado de `E` nunca foi confirmado na documentação: tratar como aberta e dizer isso quando aparecer.
- Para cada aberta, `GET /tarefas/{id}/atividades` e montar `resumo` em até 160 caracteres
  ("Etapas a, b feitas; falta: c, d"). **A atividade que pede e-mail ou envio ao cliente é ação de verdade:
  marcar a tarefa como "não dispensar, não concluir".**
- `GET /tarefas/{id}` dá erro 500: não usar.
- Link da tarefa: id `"<coid>.<eveId>"` → `https://app.gclick.com.br/coListar.do?obj=coevento&coid=<coid>&eveId=<eveId>&empId=4715`

## Etapa 3 — planilha Controle_Fiscal

Planilha `1gYVmH-N6YXPOmcOKJRqbmXprjCUVuad_mPZFU-yhstE`.

1. `get_spreadsheet` com `fields` `sheets.properties.sheetId` e `sheets.properties.title` para achar as abas de mês.
2. Ler as **duas abas de mês mais recentes**, range `A1:I<fim>`. Colunas: Município/UF | CNPJ | Nº | Empresa |
   Obrigação | Data | Valor | Status | Prazo.
3. Linha aberta = Status `Pendente` ou `Em andamento`. Resolvida = `Enviado`, `Importado`, `Compensado`, `Retido`,
   `Sem Recolhimento (Retenção Integral)`, `Não se aplica`, `Sem movimento`, `Confirmado`.
4. CNPJ da planilha vem sem zero à esquerda às vezes: normalizar com `zfill(14)`.
5. Competência: `Set2026` = `2026-09`, `Ago2026` = `2026-08`.
6. Link da linha: `https://docs.google.com/spreadsheets/d/<id>/edit#gid=<gid>&range=A<linha>:K<linha>`

## Etapa 4 — cobertura: o que o G-Click já cobre

Uma linha da planilha está **coberta** quando existe tarefa no G-Click com o mesmo CNPJ, a mesma competência e
obrigação equivalente. Equivalências confirmadas:

| Planilha | G-Click |
|---|---|
| DARF PIS, DARF COFINS | COFINS / PIS |
| DARF IRPJ, DARF CSLL | nome contendo IRPJ (LP Trimestral, LP 3 Cotas, LR Mensal) |
| REINF | EFD Reinf - (Ativo) |
| SPED CONTRIBUIÇÕES | EFD Contribuições |
| GUIA ISSQN, DECLARAÇÃO PREFEITURA | ISSQN, DAM, DecWeb, ISSQN - <município> |
| GUIA ICMS | ICMS |
| GIA RS, SPED ICMS | EFD ICMS/IPI, EFD ICMS/IPI + Gia Mensal |
| DARF REFIS | REFIS |

**Nunca cobertas pelo G-Click** (são só da planilha, e é por isso que a planilha continua): SERVIÇOS TOMADOS,
SERVIÇOS PRESTADOS, ENTRADAS, SAÍDAS, RECEITA ALUGUEIS, RECEITA TRIBUTÁVEL, CERTIFICADO DIGITAL.

## Etapa 5 — classificar e montar as listas

Para cada tarefa **aberta** no G-Click, olhar o que a planilha diz das linhas equivalentes:

| Situação na planilha | Classificação |
|---|---|
| Todas `Sem movimento`, `Retido`, `Sem Recolhimento` ou `Não se aplica` | **dispensar** |
| Todas `Enviado`, `Importado`, `Compensado` ou `Confirmado` | **concluir**, se a etapa 6 achar o comprovante |
| Misturado, vazio, ou sem linha na planilha | **verificar** |
| Checklist pede e-mail ou envio ao cliente | **ação de verdade**: fora das duas listas |

Também apontar, como **divergência**:
- tarefa dispensada (`D`) no G-Click com a linha `Pendente` na planilha, e o contrário;
- linha aberta na planilha, não coberta e sem tarefa no G-Click, quando não for escrituração;
- cliente com tributo devido e **sem a obrigação cadastrada** no G-Click (o caso da ASBBM);
- status que não sei interpretar (`E`).

## Etapa 6 — Drive: o comprovante existe?

Antes de mandar concluir, conferir se há comprovante em
`001 FECHAMENTO FISCAL / 001_FECHAMENTO FISCAL / <MM_MÊS da competência>`, nas subpastas por tipo
(009 IMPOSTOS FEDERAIS para DARF, 001 ARQUIVOS REINF, 002 ARQUIVOS MUNICIPAIS, 004 ARQUIVOS ICMS,
010 EFD CONTRIBUIÇÕES). Nome no padrão `codigo_Cliente_Municipio_09.2026_Documento.pdf`; não existe arquivo com
"DARF" no nome (são `PIS-COFINS` e `IRPJ-CSLL 3ºTRIM`). Só metadados: **não abrir PDF**.
Compensação não gera guia: ausência de arquivo aí não impede concluir, mas tem de ser dito.

## Etapa 7 — gravar no painel

1. Documentos `gclick` em `pendencias`, agrupados por (obrigacao.id, dataVencimento), id `gc-<obrId>-<AAAAMMDD>`,
   um passo por tarefa com `t`, `ok`, `empresa`, `cnpj`, `comp` (AAAA-MM), `obrigacao`, `gclickId`, `resumo`, `url`.
   Chave nova cria; chave existente atualiza só `t`, `cnpj`, `comp`, `resumo`, `url` e acrescenta passo novo.
   Passo cuja tarefa fechou ou saiu da busca vira `ok: true`; todos `ok` → `concluida`.
   **Nunca** alterar titulo, prazo, prioridade, situacao, notas, comando nem desmarcar passo.
2. Documentos `planilha`: só as linhas abertas **não cobertas**, agrupadas por aba + grupo + prazo.
   Passo que saiu das linhas abertas vira `ok: true`, dizendo se foi resolvido na planilha ou passou para o G-Click.
3. As três listas de ação, como documentos de origem `manual` com id fixo, atualizados no lugar:
   `gclick-<comp>-dispensar`, `gclick-<comp>-concluir`, `fechamento-<comp>-divergencias`.
   Item que saiu da lista vira passo `ok: true` com o motivo; nunca apagar o documento.
4. `meudia/hoje`, só o campo `fontes`: "G-Click (API)", "Planilha Controle_Fiscal" e "Drive (comprovantes)",
   cada um com `status` e `obs` dizendo quantos e a hora da leitura.

## Etapa 8 — gravar na memória e no Drive

1. Acrescentar uma entrada em `memoria/PENDENCIAS.md` com a data, o que mudou e as divergências novas.
2. Atualizar `memoria/PENDENCIAS_E_RESOLVIDOS_<hoje>.md` (criar se não existir, no lugar se existir).
3. Commit e push na `main`, com `fetch` e `rebase` antes, porque há outras sessões gravando.
4. O snapshot do Drive o conector não sobrescreve: entregar o trecho em bloco de código para a Fernanda colar.

## Etapa 9 — responder

No formato do `CLAUDE.md`: linha de situação, painel de status com no máximo 6 linhas, números só em tabela,
"O que eu fiz" separado de "O que depende de você", e terminar em `→ Próximo passo` com os comandos em bloco.
Dizer sempre: tarefas abertas lidas, linhas abertas na planilha, quantas cobertas, quantas a dispensar, quantas a
concluir, divergências novas, e erros. Se alguma fonte falhar, dizer qual e seguir com as outras.
