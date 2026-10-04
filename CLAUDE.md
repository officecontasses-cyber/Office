# OfficeCont — Fechamento Fiscal

Contexto do escritório (Fernanda, officecont.asses@gmail.com). Respostas em português,
passo a passo, um passo por vez.

## Memória de pendências (ler primeiro, atualizar sempre)

`memoria/PENDENCIAS.md` guarda **o que está pendente e o que já foi resolvido**. Leia no início de cada sessão e atualize a cada
etapa; salve também um snapshot datado (`PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md`) na pasta `ARQUIVOS EXTENSÃO - CODE - CLAUDE` do Drive.
A Fernanda pediu em 02/10/2026: "não podemos perder os contextos".
**A cada rodada (04/10/2026):** registrar tudo na memória: `PENDENCIAS.md` (o que foi feito e o que ainda está pendente),
o log `PROCESSO_FECHAMENTO_09-2026.md` e o snapshot datado no Drive. Agosto/2026 está fechado; o SPED Contribuições de 08/2026
(prazo 15/10) está em envio e depois o fechamento de 09/2026 continua.

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
- **LOPES & NADAL (cliente 186) também é prioridade**, mas com outra regra: **só se roda depois que a cliente envia os documentos**
  do mês. Quando chegarem, vai na frente de todos os outros (logo depois da Tacom) e o **ISSQN é enviado junto com o
  restante dos impostos**, tudo de uma vez, não a guia do ISSQN sozinha. (Regra dada em 02/10/2026.)
  Não confundir com o 258 (Nadal Participações), que é outro cliente. Enquanto os documentos não chegarem, o 186 fica
  fora das rodadas em lote (DecWeb e Portal Nacional).

- **TACOM — SPED Fiscal de 10/2026 (prazo combinado com a cliente):** a Leidislaine Ribeiro (Tacom) entra de férias em outubro e
  pediu os **arquivos do SPED Fiscal para transmissão até quinta 08/10/2026**. A Fernanda respondeu em 02/10/2026 que envia
  **até quarta 07/10/2026**. Também pediu para **acessar a máquina dela na segunda 05/10/2026** (para buscar as notas fiscais),
  em horário **antes das 11:00**, pois ela não consegue nesse horário. Esses prazos vêm antes do prazo legal (SPED ICMS RS 15/10).
  Não está claro no e-mail se vale para só uma ou para todas as empresas Tacom (138, 263); confirmar com a Fernanda.
  Este item **furou a fila**: conferir a data antes de qualquer outra rodada na semana de 05/10.

## Pendências com data

- **REAT HOLDING (238), 2ª quinzena de outubro/2026 (16 a 31/10):** a Fernanda deve enviar à cliente o **relatório de débitos
  ref. 06/2026** (Relatório Fiscal de 21/08/2026, enviado pela Júlia Rocha) **+ o IRPJ e a CSLL vencidos de meses anteriores**.
  (Pedido de 02/10/2026; a Controle_Fiscal tem a observação nas linhas DARF IRPJ e DARF CSLL do 238.)

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
Entram **todos os clientes da base** (aba Cadastro_Clientes, 29 em 02/10/2026; 30 com o 265), não só Porto Alegre.
O período baixado sai da competência (dia 1 ao último dia do mês seguinte). A extensão do Chrome usada é de terceiros:
só no perfil dedicado do robô. Ver `portalnacional/LEIA-ME.md`.

## Cliente novo: 265 BELEM BRASIL HOLDING (02/10/2026)

BELEM BRASIL ARQUITETURA E PARTICIPACOES LTDA (nome registrado; no grupo aparece como "Arquitetura e Holding"), Porto Alegre/RS
(Belém Novo), CNPJ 69.405.790/0001-91 (lido do nome do arquivo do certificado; dígitos conferem), NIRE 43212412791, registrada na
JUCISRS em 30/09/2026, atividades desde 08/09/2026. **Lucro Presumido**, sem empregados. Objeto: arquitetura, holding, aluguel e
compra e venda de imóveis próprios (13 imóveis integralizados no capital). Sócios-administradores: Marcelo Michelon Cornetet
(sócio também da Zenith Paracuru, 264) e Mariangela Conte Cornetet (sócia também da Conte Arquitetura, 071).
Cartão CNPJ (02/10/2026): ATIVA desde 30/09/2026, ME. CNAE principal 71.11-1-00 (arquitetura); secundários 64.62-0-00 (holding),
68.10-2-02 (aluguel de imóveis próprios) e 68.10-2-01 (compra e venda de imóveis próprios). Av. Juca Batista, 8000, casa 802,
Belém Novo, Porto Alegre/RS, CEP 91.781-200. **Prefeitura: Porto Alegre; inscrição municipal 049298-2-9; acesso ao DecWeb feito.**
Em aberto: entrar no `clientes.csv` do DecWeb e do Portal Nacional (local, com senha só no PC), certificado A1 instalado no PC e
divergência de capital (R$ 5,95 mi na proposta x R$ 5,98 mi no contrato). Script que inclui o cliente: `apps-script/incluirClienteBelemSet2026.gs`
(atualizado, ainda não rodado).
