# OfficeCont — Fechamento Fiscal

Contexto do escritório (Fernanda, officecont.asses@gmail.com). Respostas em português,
passo a passo, um passo por vez.

## Regras que não se discutem

- **GUIA só vai para a fila como "Enviado" com envio comprovado pelo G-Click.** Gerar a guia,
  baixar o PDF e salvar no Drive **não** é envio. Sem a comprovação do G-Click, o status da
  guia fica `Pendente`. (Regra dada pela Fernanda em 01/10/2026.)
  A **DECLARAÇÃO PREFEITURA** é diferente: o recibo da própria prefeitura comprova o envio.
- **Nada é escrito direto na Controle_Fiscal.** Toda atualização entra pela aba `Atualizações`
  (fila), em TSV **inline no chat**, e a Fernanda roda o script `processarAtualizacoes()`.
- **Status só com confirmação explícita** dela. Nunca deduzir que algo foi entregue.
- **Nunca abrir** `G:\_BACKUPS - Senhas e controles`.
- **Senhas** (o `clientes.csv` do robô) não vão para repositório, nem para pasta sincronizada
  com o Drive, nem para o chat. O robô fica fora do "Meu Drive" (`C:\Robos\decweb`).

## Prioridade no fechamento

- **TACOM de Porto Alegre vem sempre primeiro**, em todo fechamento mensal: clientes **138 (Tacom Sistemas)**
  e **263 (Tacom Projetos)**. O cliente quer as guias do ISSQN **no dia 1** do mês. Antes de qualquer outro
  cliente, rodar o robô para os dois e entregar à Fernanda os PDFs (`DeclaraçãoMensal.pdf` e `ISSQN.pdf`)
  para ela encaminhar. (Regra dada em 02/10/2026.)
- Lembrar: a Tacom é apurada pela matriz, e só o ISSQN de Porto Alegre entra nessa prioridade.
  O robô roda no PC do escritório, não na nuvem: a agente prepara o comando e confere o resultado.

## Prazos que já erramos

- **ISSQN de Porto Alegre, competência 09/2026, vence 13/10/2026** — está impresso na própria guia do
  DecWeb ("Não receber esta guia após 13/10/2026"). Eu tinha usado 09/10 (supondo que o dia 10 caía no
  sábado e antecipava); estava errado. **Na dúvida, o prazo é o da guia, nunca uma regra deduzida.**
  Nos meses seguintes, conferir a data na primeira guia gerada antes de gravar o prazo na planilha.

## Armadilhas já vividas

- **Portal Nacional, 02/10/2026:** o perfil do Chrome do robô é compartilhado e guardava a sessão do portal; a rodada inteira
  baixou os dados do 238. O robô agora apaga a sessão antes de cada login. Resultado "sem movimento" repetido em vários
  clientes seguidos é sinal de alerta, não de verdade: conferir o log antes de aceitar.
- Dois robôs na mesma máquina não podem ter módulos com o mesmo nome (`configuracao.py` do DecWeb e do Portal Nacional
  colidiram). O do Portal Nacional agora é `portal_config.py`.

## Planilha Controle_Fiscal

Abas por mês (`Set2026`, `Ago2026`...), mais `Atualizações` e `Cadastro_Clientes`.

Colunas das abas de mês: Município/UF | CNPJ | Nº | Empresa | Obrigação | Data | Valor (R$) |
Status | Prazo | Dias p/ Vencer | Observações | Contribuinte ICMS

Colunas da fila `Atualizações` (7): Nº | aba | Obrigação (prefixo) | Status | Valor |
Observações | Processado (deixar em branco; o script marca).

Vocabulário de Status já usado: `Enviado`, `Pendente`, `Sem movimento`, `Importado`,
`Compensado`, `Retido`, `Sem Recolhimento (Retenção Integral)`, `Não se aplica`, `Confirmado`.

Prazo é **texto com contagem regressiva** ("dd/mm/aaaa · N dias"); `Dias p/ Vencer` lê a data
desse texto. Não trocar por data pura — há processo próprio que reescreve a coluna.

## Robô DecWeb (ISSQN Porto Alegre)

`decweb/` neste repositório; instalado em `C:\Robos\decweb` no PC do escritório.
21 clientes de Porto Alegre. Raiz do Drive no PC: `I:\Meu Drive\1015_ROTINA AUTOMATICA\001 FECHAMENTO FISCAL\001_FECHAMENTO FISCAL`.

Ver `decweb/README.md` para fases, flags e o tratamento dos avisos de escrituração.

## Robô Portal Nacional (NFS-e Emitidas/Recebidas)

`portalnacional/` neste repositório; instalar em `C:\Robos\portalnacional` (local, sem acento, fora do Meu Drive).
Entra com o **certificado A1 de cada empresa** (precisa estar instalado no PC) e baixa Emitidas e Recebidas para
`<raiz>\<MM_MES>\003 ARQUIVOS PORTAL NACIONAL`. Cliente sem certificado ou vencido é pulado e fica de fora.
Entram **todos os clientes da base** (aba Cadastro_Clientes, 29 em 02/10/2026), não só Porto Alegre.
O período baixado sai da competência (dia 1 ao último dia do mês seguinte). A extensão do Chrome usada é de terceiros:
só no perfil dedicado do robô. Ver `portalnacional/LEIA-ME.md`.

