# Base de conhecimento do escritório — índice e regras
Atualizado em: 30/10/2026 · por: Claude Code (sessão na nuvem)
Fontes: roteiro "Monte o repositório único do escritório" (29/10/2026); escolha do local feita pela pessoa responsável em 30/10/2026

## O que é isto
Um só lugar para tudo o que precisa ser lembrado entre conversas, sessões e pessoas. Fica neste repositório git (`officecontasses-cyber/office`), na pasta `00 BASE`. Toda sessão começa lendo este arquivo e o `HANDOFF.md`.

## Estrutura
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

Na raiz: `LEIA-ME.md` (este arquivo) e `HANDOFF.md` (fila de pedidos de uma sessão para outra, com itens `ABERTO` e `FEITO`).

Não crie pastas novas. Se algo não se encaixa, pergunte à pessoa onde quer.

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
4. **Data absoluta sempre** (DD/MM/AAAA). Nunca "semana passada".
5. **Fonte no cabeçalho.**
6. **Nunca senha, token ou login.** Aponte onde a credencial fica, não qual é.
7. **O que saiu de uso vai para `99 Arquivo`** — ou some, se for lixo.
8. **Uma linha no Diário a cada etapa concluída.**
9. **A base vence a memória local.** Em conflito, siga a base e avise a pessoa.

## Estado da montagem
- Passo 1 (local): feito em 30/10/2026 — a base mora neste repositório git.
- Passo 2 (estrutura): feito em 30/10/2026.
- Passos 3 a 7 (levantar o que existe, migrar por tema, apontar o Claude, fechar): pendentes.
