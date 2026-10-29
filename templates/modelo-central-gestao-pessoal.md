# MODELO — Central de gestão pessoal (painel único no Claude)

Modelo para montar, em **outra conta** e com **outras fontes**, um painel no estilo da "Central da Fernanda": um artefato do Claude com banco de dados próprio que junta o dia, as tarefas, as atualizações do setor, o acompanhamento de outra área e o recado semanal ao time. Nada é enviado sozinho: o painel organiza, rascunha e deixa pronto para a pessoa aprovar.

Como usar este modelo:
1. Preencha a **Ficha de configuração** (seção 1).
2. Cole a ficha e a seção 2 numa conversa do Claude (Claude Code ou Cowork, na conta de destino) e peça: "monte o painel conforme este modelo".
3. Crie as rotinas com os **prompts-modelo** da seção 4, trocando os `{{campos}}`.
4. Use o **checklist** da seção 7 para validar.

Tudo entre `{{ }}` é para substituir. Seções marcadas como *(opcional)* podem ser puladas.

---

## 1. Ficha de configuração (preencher)

| Campo | Valor |
|---|---|
| Nome do painel | `{{NOME_DO_PAINEL}}` (ex.: "Central da Ana") |
| Dono / conta | `{{NOME}}` · `{{EMAIL_DA_CONTA}}` |
| Empresa / setor | `{{EMPRESA}}` · `{{SETOR}}` |
| Fuso / idioma | `{{FUSO}}` · português do Brasil |
| Fonte de tarefas atual (de onde importar) | `{{EX.: Microsoft To Do, Google Tarefas, Trello, planilha}}` |
| Sistema de tarefas da equipe (para sincronizar) | `{{EX.: G-Click, Asana, Jira, Monday — e como exportar: API, JSON, CSV}}` |
| Link padrão de uma tarefa nesse sistema | `{{EX.: https://sistema/tarefas/<id>}}` |
| E-mail a ler (só leitura) | `{{EX.: Gmail da conta}}` |
| Agenda(s) | principal `{{EMAIL}}` · pessoal compartilhada `{{CALENDAR_ID}}` *(opcional)* |
| Planilha de controle *(opcional)* | `{{ID_DA_PLANILHA}}` · aba/padrão `{{EX.: CONTROLE MM.AAAA}}` · colunas `{{...}}` |
| Painel de outra área para acompanhar *(opcional)* | `{{URL}}` · dono `{{NOME}}` · compartilhado com a conta? `{{sim/não}}` |
| Radar de atualizações *(opcional)* | tema `{{EX.: tributário, trabalhista, regulatório}}` · esferas `{{...}}` · carteira/base para cruzar `{{...}}` |
| Quem aprova avisos | `{{NOME / CARGO}}` |
| Grupo do recado semanal *(opcional)* | `{{NOME DO GRUPO}}` · dia/hora `{{EX.: segunda 9h}}` · reuniões a citar `{{EX.: títulos que contêm "Check in"}}` |
| Mensageria para análise *(opcional)* | `{{EX.: Digisac via API, só leitura}}` |
| Identidade visual | cores `{{...}}` · fontes `{{...}}` · logo/marca no topo? `{{sim/não}}` |
| Regras que nunca podem ser quebradas | `{{EX.: não enviar nada sem aprovação; não excluir e-mail de vez; não clicar em painéis de terceiros}}` |

---

## 2. Especificação do painel

### 2.1 Abas (ordem sugerida)
1. **Meu dia** — o painel sempre abre aqui.
2. **Tarefas** — lista única.
3. **Radar** *(opcional)*.
4. **{{ÁREA ACOMPANHADA}}** *(opcional)*.
5. **Recado da semana** *(opcional)*.

### 2.2 Meu dia
- **Resumo do dia** (recolhido, abre ao clicar).
- **Por onde começar**: 3 a 5 itens, cada um com "por quê".
- **Agora — vence hoje ou atrasado**.
- **Agenda do dia**: compromissos reais. Eventos de dia inteiro ou "livre" ficam fora, exceto os da lista de avisos (`config/agenda`).
- **Semana à frente** (recolhido).
- **Caixa de entrada** espelhada: cada conversa com pedido, leitura sugerida, rascunho de resposta, decisão e fila de ação no e-mail.
- **De onde veio** (recolhido): uma linha por fonte, dizendo se deu certo.
- **Ao vivo**: cada linha é cruzada com a tarefa correspondente (por número ou título). Concluída some; prorrogada sai de "Agora" e de "Semana" conforme a nova data. Linha com tarefa do sistema mostra "abrir ↗".

### 2.3 Tarefas
- Resumo por prazo: Atrasadas · Hoje · Próximos 7 dias · Mais adiante · Sem data · Concluídas.
- Filtros: busca, responsável e origem (Todas · Minhas · {{SISTEMA}}).
- Cada item tem prazo, cliente, prioridade, situação (aberta/andamento/aguardando), passos marcáveis, anotação e "repetir a cada N dias" (ao concluir, cria a próxima).
- Ações por item: adiar 1 dia, adiar 1 semana, próxima segunda, excluir (com confirmação).
- Itens do sistema mostram etiqueta e "Abrir no {{SISTEMA}} ↗". Itens agrupados (mesma obrigação, vários clientes) têm um passo e um link por cliente.

### 2.4 Caixa de entrada (dentro de Meu dia)
- **O que fazer**: Resolvido ✓ · Respondi · Virar tarefa · Deleguei · Aguardando resposta · Nada a fazer. Só registram a decisão; Resolvido também põe na fila de "ler e arquivar".
- **No e-mail**: Ler e arquivar · Só arquivar · Apagar (lixeira, em vermelho). Põem na **fila**, com etiqueta escolhida.
- A fila **só é executada no chat**, quando a pessoa pede "executa a fila". Nenhuma rotina mexe no e-mail.

### 2.5 Radar *(opcional)*
- No topo, o alinhamento com `{{QUEM APROVA}}`: um **bloco por assunto**. Cada bloco tem:
  - em cima, recolhido, "o que o radar mapeou";
  - embaixo, as mensagens para a diretoria e para comercial/marketing;
  - os botões Copiar · Marcar como enviado · Descartar, mais "{{QUEM APROVA}} aprovou".
- Bloco enviado ou descartado recolhe. Categorias: pra decidir · em andamento · informativo · só acompanhar.
- Lista completa recolhida, com "Descartar do radar" e a seção "Descartados" para restaurar.

### 2.6 Área acompanhada *(opcional)*
- Resumo do andamento: número grande, barra de progresso e grupos por situação, recolhidos.
- Botão para abrir o painel original.
- O resumo é atualizado **sob pedido no chat**.

### 2.7 Recado da semana *(opcional)*
- O rascunho chega no dia e hora configurados.
- Fluxo: revisar e editar → Aprovar → "Copiar e abrir no WhatsApp" → escolher o grupo → colar → Marcar como enviada.
- O histórico das semanas anteriores fica recolhido.

### 2.8 Layout
- Abrir sempre em Meu dia. **Texto longo sempre recolhido**; à vista, só o que pede ação.
- Destrutivos em vermelho; concluído em verde.
- Cores e fontes conforme a ficha. Funcionar no celular, com tema claro e escuro.

---

## 3. Banco de dados do artefato (capability `db`)

| Coleção | Conteúdo | Quem escreve |
|---|---|---|
| `pendencias` | `titulo, cliente, responsavel, prazo, prioridade, situacao, passos[{t,ok}], notas, recorrenciaDias, concluida, concluidaEm, origem, criadoEm, atualizadoEm` + (do sistema) `sistemaIds[], links[{t,url}]` | página, chat, rotina de sincronização |
| `meudia/hoje` | `data, modo, resumo, ordem[], agora[], agenda[], semana[], fontes{}` | rotina Meu dia |
| `emails/<threadId>` | conteúdo (`assunto, de, quando, quandoISO, naoLida, nMsgs, link, cliente, prazo, grupo, pedido, sugestao, etiquetaSugerida, rascunho, pendenciaTitulo, inbox`) + da pessoa (`decisao, decisaoEm, nota, etiqueta, acao, acaoEm, acaoFeita, acaoErro`) | rotina (só conteúdo) · página e chat (campos da pessoa) |
| `radar` | `titulo, esfera, orgao, uf, municipio, oQueMuda, baseLegal, fonte, confirmado, prazo, clientes[], pautaMarketing, rascunhoMkt, avisoDiretoria, aprovadoDiretoria, enviadoMkt, data` | rotina Radar |
| `radar_dir` | camada da pessoa: `categoria, ordem, titulo, texto, enviadoKaEm, descartadoKaEm, descartadoRadarEm, motivoDescarte, respostas` | página e chat (separada para a rotina não sobrescrever) |
| `mensagens/semana-AAAA-MM-DD` | `data, titulo, destino, status, texto, observacao, aprovadaEm, enviadaEm` | rotina Recado · página |
| `config/agenda` | `avisosIncluir[], avisosExcluir[], contexto{}` | chat |
| `config/paineis` | `{{area}}: {titulo, dono, url, obs, resumo{...}}` | chat |

Regra geral: toda escrita usa `if_version`, para nunca sobrescrever um clique da pessoa. Nenhum dado fica embutido no HTML.

---

## 4. Prompts-modelo das rotinas

Cada rotina roda numa sessão nova e sem memória, então o prompt tem de ser completo. Troque os `{{campos}}`.

### 4.1 Sincronizar tarefas do sistema da equipe
- **Quando:** `{{EX.: seg e sex 8h30}}`.
- **Onde roda:** tarefa agendada do Claude Code (desktop).

> Sincronize as tarefas de `{{SISTEMA}}` de `{{NOME}}` com o painel `{{URL_DO_ARTEFATO}}`, coleção `pendencias`, só pela ferramenta ArtifactData (não republique a página).
> Fonte: `{{COMO OBTER: arquivo JSON do dia em <pasta>, ou API <endpoint>}}`. Se faltar, `{{EX.: rode a tarefa X}}`; se ainda faltar, pare e avise — não use dado velho.
> Use só as tarefas de `{{NOME}}` (vencidas, de hoje e dos próximos 7 dias).
> Novas: crie com `origem: "{{SISTEMA}}"`, `sistemaIds` e `links` (`{{LINK PADRÃO}}`). Quando houver 2 ou mais com o mesmo nome e vencimento, agrupe numa só, com um passo e um link por cliente.
> Existentes: não altere título, prazo, notas nem passos da pessoa. Se o vencimento mudou, só anote.
> Sumiu da lista: marque o passo (agrupada) ou conclua com a nota "saiu da lista do {{SISTEMA}}". Nunca exclua.
> Grave com batch e `if_version`. Termine com um resumo curto. Não envie nada a ninguém.

### 4.2 Meu dia (briefing da manhã)
- **Quando:** `{{EX.: seg a sex 6h50}}`.
- **Onde roda:** rotina do Cowork ou agendada.

> Monte o briefing da manhã de `{{NOME}}` e grave no painel `{{URL}}`. Segunda = varredura completa; terça a sexta = só o que mudou e o que vence em 7 dias.
> Fontes, nesta ordem:
> 1) `pendencias` (não concluídas);
> 2) `radar` *(se houver)*;
> 3) `{{SISTEMA}}`, via `{{arquivo/API}}`, conferindo a data de geração;
> 4) planilha `{{ID}}`, aba `{{padrão}}`, colunas `{{...}}` *(se houver)*;
> 5) agenda `{{EMAIL}}` + `{{CALENDAR_ID pessoal}}`, eventos de hoje, sem os de dia inteiro ou "livre", exceto os de `config/agenda`;
> 6) e-mail, caixa inteira, SÓ LEITURA.
> Grave `meudia/hoje` (resumo, ordem 3–5 com "porque", agora, agenda, semana, fontes) e `emails/<threadId>` só com os campos de conteúdo. Nunca toque em `decisao, nota, etiqueta, acao, acaoFeita`. Limpeza: apague docs cuja conversa saiu da caixa de entrada, exceto os que têm fila pendente.
> Não invente prazo, valor nem cliente. Não envie nada para fora.

### 4.3 Radar de atualizações *(opcional)*
- **Quando:** `{{EX.: seg a sex 8h40}}`.

> Pesquise novidades de `{{TEMA}}` nas esferas `{{...}}` publicadas nos últimos `{{N}}` dias e prazos que vencem em `{{N}}` dias. Cruze com a carteira `{{FONTE DA CARTEIRA}}`.
> Para cada item, grave em `radar`: o que muda, base legal, fonte oficial (`confirmado: false` se não achar o ato), prazo e clientes atingidos. Quando couber, inclua uma sugestão de pauta e um rascunho para o marketing, e um pedido de aprovação para `{{QUEM APROVA}}`.
> Não altere `radar_dir`. Atualize `radar_meta/status` com a data da rodada e uma observação curta. Não envie nada.

### 4.4 Recado semanal *(opcional)*
- **Quando:** `{{EX.: seg 8h}}`.

> Rascunhe o bom-dia de `{{DIA}}` para o grupo `{{GRUPO}}` e grave em `mensagens/semana-AAAA-MM-DD` com `status: "rascunho"`. Não sobrescreva se já estiver aprovada ou enviada.
> Use as reuniões de hoje cujo título contém `{{"Check in"}}` (horário + link do Meet), os feriados até a próxima semana e até 3 prazos do radar.
> Varie a abertura em relação às semanas anteriores. No máximo 2 emojis. Não cite clientes nem valores. Não envie nada.

### 4.5 Comandos no chat (sem rotina)
- **"executa a fila"**: executa no e-mail as ações de `emails` com `acao` preenchida e `acaoFeita` vazia (ler, etiquetar, arquivar ou mandar para a lixeira) e grava `acaoFeita` ou `acaoErro`.
- **"atualiza {{área}}"**: lê o painel da área (pelo navegador da pessoa, só leitura e sem clicar) e troca o resumo em `config/paineis`.
- **"revisa as tarefas"**: revisão pelo painel e pelo que está registrado, sem varrer o e-mail.

---

## 5. Montagem em ordem

1. Na conta de destino, peça ao Claude o artefato com `db`, conforme as seções 2 e 3. Publique-o e guarde a URL.
2. Importe as tarefas atuais (`{{FONTE ATUAL}}`) para `pendencias`.
3. Configure o acesso às fontes:
   - conectores de e-mail, agenda, Drive e planilhas;
   - compartilhe a agenda pessoal com a conta do trabalho, só leitura;
   - peça para compartilharem o painel da área com a conta.
4. Crie a sincronização do sistema (4.1) e teste com "rodar agora": não pode duplicar nada.
5. Crie o Meu dia (4.2), rode um teste e confira "De onde veio".
6. *(Opcional)* Radar (4.3) e Recado (4.4).
7. Registre na memória do projeto: URL do painel, coleções, regras (seção 1) e comandos (4.5).

---

## 6. Limites conhecidos (para não perder tempo)

- **Rotinas criadas no Cowork:** o prompt só se edita pelo Cowork. Pela API, seria preciso reenviar a configuração inteira.
- **Painel de outra pessoa:**
  - não abre dentro do artefato, por bloqueio do claude.ai;
  - só dá para ler dados dele se estiver compartilhado com a conta;
  - sem compartilhamento, a leitura é pelo navegador da pessoa, sob pedido;
  - uma rotina que use o navegador logado sozinha tende a ser bloqueada pela proteção do Claude.
- **WhatsApp:**
  - não abre direto num grupo sem o link de convite, que só administrador gera;
  - não há envio em grupo por API;
  - o texto enviado por link pode perder emojis no app de desktop. Fluxo: copiar e colar.
- **Botão na página não chama o chat:** a página só registra o pedido, e a ação acontece quando a pessoa pede no chat.
- **Repetição "última quinta do mês":** o painel repete por N dias, então confira a data ao concluir.

---

## 7. Checklist de validação

- [ ] O painel abre em Meu dia, no celular e no computador, nos temas claro e escuro.
- [ ] Concluir uma tarefa recorrente cria a próxima.
- [ ] Prorrogar uma tarefa tira ela do "Agora" sem esperar o briefing.
- [ ] A sincronização rodada duas vezes seguidas não duplica nada.
- [ ] "Resolvido ✓" + "executa a fila" arquiva o e-mail com a etiqueta certa.
- [ ] Apagar manda para a lixeira (recuperável), nunca exclui de vez.
- [ ] Nenhuma rotina enviou mensagem, e-mail ou WhatsApp.
- [ ] O texto longo aparece recolhido.
