# Painel do fechamento (mod do Claude Code)

Painel que fica ao lado do chat com as pendências do fechamento fiscal, no lugar da lista em texto.

- **Caixa de comando livre** no topo: digita e manda para o chat (Enter ou o botão `Enviar`; `Limpar` apaga).
- **Cartões por prazo:** vencido, depende de decisão sua, amanhã, novembro e sem prazo legal. Cada cartão traz cliente, obrigação e uma linha de contexto.
- **Botões por cartão:** a ação principal manda o pedido pronto ao chat; `Escrever` joga o pedido na caixa já identificado, para você completar; `Pular` esconde o item (o botão no fim do painel traz de volta).
- **Comando `/fechamento`** reabre o painel.

As pendências ficam na constante `GRUPOS` em `hooks/register.tsx`: para atualizar, é só editar essa lista. O que foi pulado e o rascunho da caixa ficam no estado da sessão (`types/index.d.ts`).

## Instalação neste container

Copiar a pasta para `/root/.claude/dev-mods/<id da sessão>/painel-fechamento` e autorizar quando o Claude Code perguntar se liga os mods da sessão. Conferir com `claude plugin validate <pasta>`.
