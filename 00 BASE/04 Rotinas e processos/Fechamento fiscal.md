# Fechamento fiscal mensal
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: protótipo "Fechamento Fiscal OfficeCont" (ago/2026, decisão de 01/09/2026); planilha Controle_Fiscal, aba Set2026 (lida em 27/10/2026); Central Officecont Fernanda

## Quem
Fernanda (única pessoa no fiscal). Tarefas no G-Click; registro na `Controle_Fiscal` (Presumido e Real)
e na `SIMPLES 2026` (Simples).

## Ordem dos blocos
1. **Municipal** (pasta 002)
2. **REINF** (pasta 001)
3. Portal Nacional (003)
4. ICMS (004)
5. Conferências (005)
6. XML Portal Nacional (006)
7. SIEG (007)
8. Domínio (008)
9. Impostos Federais (009)

**Municipal vem antes do REINF** (decisão de 01/09/2026): a carteira é majoritariamente Presumido/Real e
precisa importar os serviços tomados da prefeitura antes de apurar e enviar o REINF. O número de pasta é
o código da pasta no Drive (ex.: `001 ARQUIVOS REINF`, `002 ARQUIVOS MUNICIPAIS`); a ordem de trabalho é a da lista.

## Obrigações que aparecem na Controle_Fiscal (por cliente e mês)
REINF · Serviços tomados · Serviços prestados · Receita (ex.: aluguéis) · Declaração da prefeitura ·
Guia ISSQN · DARF PIS · DARF COFINS · DARF IRPJ · DARF CSLL (trimestrais no Presumido) · SPED Contribuições.
Cada linha tem data, valor, status (Enviado, Importado, Sem movimento, Pendente…), prazo e observação.

## Liberação para a contabilidade
Ao fim, a aba GATILHO marca a competência do cliente (`SIM`/`SEM PENDÊNCIA` = liberado). No **Lucro Real**,
os DARFs de IRPJ/CSLL ficam "aguardando a contabilidade liberar a apuração"; no **Presumido**, a Fernanda
apura e envia direto.
