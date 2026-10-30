# Base do escritório OfficeCont — por onde começar
Atualizado em: 30/10/2026 · por: sessão do fechamento fiscal (branch `claude/sharp-meitner-bilpus`)
Fontes: estrutura real do repositório em 30/10/2026; roteiro "Monte o repositório único do escritório" (29/10/2026), adotado em parte.

**Toda conversa nova lê este arquivo primeiro.** Depois lê o `CLAUDE.md` (as regras) e o `HANDOFF.md` (pedidos de outra sessão).

## O que é este repositório
É o lugar único do que precisa ser lembrado entre conversas: regras do escritório, dossiê de cada cliente, pendências, robôs e painéis. O que não está escrito aqui, a próxima sessão não sabe.

## Onde fica cada coisa
| Caminho | O que guarda |
|---|---|
| `CLAUDE.md` | **As regras que não se discutem.** Lido automaticamente no início de toda sessão |
| `HANDOFF.md` | Fila de pedidos de uma sessão para outra (`ABERTO` / `FEITO`) |
| `memoria/PENDENCIAS.md` | O que está pendente e o que já foi resolvido, em ordem de data |
| `memoria/PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` | Snapshot do dia (o mesmo arquivo vai para a pasta do Drive) |
| `memoria/CLIENTE_NNN_*.md` | **Um dossiê por cliente**: cadastro, prefeitura, particularidades, histórico das apurações |
| `memoria/CNPJS_CLIENTES.md` | CNPJ de todos os clientes, só números |
| `memoria/PROCESSO_FECHAMENTO_MM-AAAA.md` | Log da rodada de fechamento do mês |
| `memoria/PROMPT_EXTENSAO_*.md` | Prompts prontos para o Claude in Chrome (e-mail, Lefisc, portais) |
| `memoria/TSV_*`, `RASCUNHOS_*` | Material de trabalho de uma rodada; não é fonte de verdade |
| `diario/AAAA-MM.md` | **Uma linha por etapa concluída**, com data e sessão |
| `decweb/`, `portalnacional/` | Robôs (ISSQN de Porto Alegre e NFS-e do Portal Nacional) |
| `apps-script/` | Scripts da planilha Controle_Fiscal |
| `paineis/` | Painéis-artefato (Central Officecont) |
| `mods/` | Painel do fechamento ao lado do chat (Claude Code) |
| `templates/` | Modelos reaproveitáveis |

## Regras de gravação
1. **Um assunto, um arquivo.** Procure antes de criar.
2. **Atualizar no lugar.** Nada de `v2`, `final` ou cópia com data — a exceção é o snapshot diário, que é datado de propósito.
3. **O fato, não a conversa.** O que foi decidido, por quem, quando, e o que vale daqui para frente.
4. **Data absoluta sempre** (DD/MM/AAAA).
5. **Fonte no cabeçalho** ou na própria linha.
6. **Nunca senha, token ou login.** Aponte onde a credencial fica, não qual é.
7. **Uma linha no diário a cada etapa concluída.**
8. **Esta base vence a memória do chat.** Em conflito, siga o que está escrito aqui e avise a Fernanda.

## Como abrir uma conversa nova
Aponte para o repositório `officecontasses-cyber/Office`, branch **`main`** — ela tem tudo. Se precisar de uma frase: *"leia a base antes de responder"*.

## O que ainda não existe aqui
Pastas de **equipe e contatos**, **rotinas**, **projetos** e **sistemas** não foram criadas: o que há sobre isso está dentro do `CLAUDE.md` e dos dossiês. Criar só quando houver conteúdo real para elas.
