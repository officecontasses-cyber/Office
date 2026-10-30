# Repositório único da OfficeCont
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: roteiro "Monte o repositório único do escritório" (29/10/2026)

## O que é
Um só lugar para o que precisa ser lembrado entre conversas, sessões e pessoas. Toda sessão lê este
arquivo primeiro. Em conflito com a memória de um chat, vale a base.

Repositório: `officecontasses-cyber/office` · pasta `00 BASE` · uso atual: só a responsável pelo
escritório (o time entra depois).

## Índice
| Pasta | O que guarda |
|---|---|
| `01 Como eu trabalho` | O jeito da pessoa e do escritório: estilo de texto, o que nunca fazer, como nomear arquivo, como revisar |
| `02 Equipe e contatos` | Quem é quem, quem recebe o quê, contatos externos e parceiros |
| `03 Clientes` | Um arquivo por cliente, no padrão `NNN Nome.md` |
| `04 Rotinas e processos` | Como se faz cada coisa que se repete |
| `05 Projetos` | O que tem começo, meio e fim |
| `06 Sistemas e integrações` | Que sistema serve para quê, onde fica, como se conecta |
| `07 Diário` | Um arquivo por mês, `AAAA-MM.md`, com uma linha por etapa concluída |
| `08 Skills` | A cópia mestra das skills, mais um catálogo dizendo onde cada uma está instalada |
| `99 Arquivo` | O que saiu de uso e não é lixo |

`HANDOFF.md`, ao lado deste arquivo: fila de pedidos de uma sessão para outra (`ABERTO` / `FEITO`).

Não crie pastas novas. Se algo não se encaixa, pergunte onde guardar.

## Formato de todo arquivo da base
```
# Título
Atualizado em: DD/MM/AAAA · por: <qual sessão ou pessoa>
Fontes: <de onde veio a informação>

## Seções curtas, com o fato primeiro
```

## Regras de gravação
1. **Um assunto, um arquivo.** Procure antes de criar.
2. **Atualizar no lugar.** Nada de `v2`, `final`, `_novo` ou cópia com data.
3. **O fato, não a conversa.** Decisão, data, responsável, o que vale daqui para frente.
4. **Data absoluta sempre** (DD/MM/AAAA).
5. **Fonte no cabeçalho.**
6. **Nunca senha, token ou login.** Aponte onde a credencial fica, não qual é. Vale também para nome
   de arquivo que contenha senha.
7. **O que saiu de uso vai para `99 Arquivo`**, ou some, se for lixo.
8. **Uma linha no Diário a cada etapa concluída.**
9. **A base vence a memória local.** Em conflito, siga a base e avise a pessoa.
