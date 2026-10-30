# Pedidos entre sessões
Atualizado em: 30/10/2026 · por: sessão do fechamento fiscal
Fontes: pendências levantadas em 29 e 30/10/2026.

Fila de pedidos de uma conversa para outra. Quem encontra algo que é trabalho de outra sessão **escreve aqui em vez de fazer**. Ao resolver, troque `ABERTO` por `FEITO` e deixe a data.

**Como usar:** leia esta fila no início da conversa. Trate o que estiver `ABERTO` e endereçado a você. Ordem direta da Fernanda vence esta fila.

## Abertos

- **ABERTO · para a sessão da Central** · 30/10/2026 · O cruzamento de 29/10 apontou que o **197 ASBBM (`05164750000112`) não tem nenhuma tarefa de PIS/COFINS no G-Click**, em competência alguma. Como ficou definido que há **COFINS de 4% sobre receita financeira** (R$ 163,60 em 2026), a obrigação precisa entrar no perfil do cliente no G-Click. Ver `memoria/CLIENTE_197_ASBBM.md`.
- **ABERTO · para a Fernanda** · 30/10/2026 · O caminho de tela para **dispensar** no G-Click segue sem mapeamento de quem o conhece. **As 26 tarefas da lista já foram dispensadas** (conferido pela API em 30/10: todas em status `D`), então alguém achou o caminho — a sessão da Central não tem navegador e não consegue descobrir nem executar. Quem fez, por favor registre o caminho aqui. **Conflito a resolver:** o HANDOFF registra que a Fernanda mandou dispensar a do **152 CRBM5** (`13738204000176`, "Confirmações - Retenções", vencida 15/10), mas o checklist dessa tarefa pede **anexar os relatórios de notas e ENVIAR ao CRBIO as retenções de ISSQN e as federais**. Dispensar fecha a tarefa sem o envio. Confirmar com a Fernanda antes: ou o envio já foi feito por fora, ou a dispensa some com a obrigação de enviar. Em 30/10 ela segue aberta (`A`).
- **ABERTO · para a Fernanda ou quem administra o G-Click** · 30/10/2026 · Cadastrar a obrigação de **PIS/COFINS no perfil do 197 ASBBM** (`05164750000112`) é ação de tela: a sessão da Central lê o G-Click pela API, só GET, e não escreve. O achado continua valendo (há COFINS de 4% devida e nenhuma tarefa no sistema).
- **ABERTO · para quem abrir a próxima conversa** · 30/10/2026 · **Sempre abrir na branch `main`.** Em 29/10 uma sessão rodou o dia inteiro em branch sem o `CLAUDE.md` e sem a `memoria/`, refez trabalho e analisou um cliente errado.
- **ABERTO · para a Fernanda** · 30/10/2026 · Falta o **CNPJ do 227 PROGEST**: ele não está na aba `Cadastro_Clientes` da Controle_Fiscal nem em `memoria/CNPJS_CLIENTES.md`.
- **ABERTO · para a sessão do fechamento** · 30/10/2026 · **SPED Contribuições de 09/2026** não começou: ~25 linhas `Pendente`, prazo **16/11**, pasta `010 EFD CONTRIBUIÇÕES` de setembro vazia no Drive.

## Feitos

- **FEITO · 29/10/2026** · Levar todo o trabalho do fechamento para a branch `main` (antes só existia em branch de sessão).
- **FEITO · 29/10/2026** · Levar o painel Central e o modelo de gestão pessoal para a `main` (sessão da Central).
