# Prompt para o Claude in Chrome — exportar dados do HüB SIEG para o script

Cole tudo abaixo da linha na extensão, com você logado em https://hub.sieg.com/.

---

Você está no meu Chrome, logado no HüB SIEG. Preciso coletar as exportações que alimentam o meu script de controle de certidões, débitos e parcelamentos da carteira da Fernanda. A tarefa é de LEITURA e EXPORTAÇÃO: nada pode ser alterado no portal.

## Regras
- Pode clicar em **Exportar Todos** e **Baixar Todos** (são só downloads). NÃO clique em "Atualizar", "Solicitar atualização", "Consultar", "Gerar DAS", "Gerar nova chave API" nem em nada que dispare consulta nova, envio por e-mail/WhatsApp ou altere cadastro.
- NÃO use "Administrar carteira" nem "Gerenciar usuários" além de visualizar.
- Se aparecer senha, 2FA, confirmação ou aviso de custo, pare e me pergunte.
- Abra cada tela em nova aba e feche ao terminar.

## Passos
1. **Carteira da Fernanda.** Abra Pendências → Carteira (https://iris.sieg.com/Carteira). Veja se existe carteira da Fernanda (pode aparecer como "Fernanda" ou com sobrenome).
   - Se existir: liste CNPJ e nome de cada cliente dela (tabela com colunas `cnpj` e `nome`).
   - Se não existir: diga isso e liste os nomes das carteiras que existem. Não crie nada.
2. **Certidões.** Pendências → Situação Fiscal → Certidões. Clique em **Exportar Todos** e anote o nome do arquivo baixado.
3. **Diagnóstico Fiscal.** Situação Fiscal → Diagnóstico Fiscal → **Exportar Todos**; anote o nome do arquivo.
4. **Parcelamentos.** Pendências → Parcelamentos → **Exportar Todos** na Visão Geral; anote o nome do arquivo. Se as abas (Simples Nacional, PGFN, PERT etc.) tiverem exportação própria, exporte também e anote cada nome.
5. Se algum download não puder ser confirmado (o Chrome não mostra o arquivo), diga exatamente o que apareceu na tela.

## Entrega (Markdown)
1. **Carteira da Fernanda:** tabela `cnpj | nome`, ou "NÃO EXISTE" com as carteiras encontradas.
2. **Exportações:** para cada tela, o nome do arquivo baixado, o formato (xlsx/csv) e, se você conseguir ler o conteúdo, a **lista exata de colunas** e **2 linhas de exemplo com CNPJ e razão social substituídos por 00.000.000/0000-00 e "EMPRESA EXEMPLO"**.
3. **Observações:** botões que não encontrou, erros, ou qualquer coisa diferente do esperado.

Não invente colunas nem valores: se não conseguir ler algo, escreva "NÃO LIDO".

Depois me diga para levar o resultado ao Claude Code. Lá eu salvo os arquivos em `sieg_controle/exports/` como `certidoes.xlsx`, `diagnostico.xlsx` e `parcelamentos.xlsx` e rodo `python controle.py --inspect`.
