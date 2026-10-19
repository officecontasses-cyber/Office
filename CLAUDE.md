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
- **Status das linhas que dependem do Domínio (regra da Fernanda, 06/10/2026):** onde **há movimento** (notas a lançar), Serviços Tomados,
  Serviços Prestados, Entradas e Saídas só viram `Importado`/`Enviado` depois que o Domínio foi importado e **conciliado** com a
  prefeitura/Portal/SEFAZ; enquanto isso ficam **`Pendente`** ("Em andamento" na observação; esse status não existe na planilha).
  Onde **não há nota** na fonte oficial (SEFAZ/SAT, Portal, relatório da prefeitura), não há o que importar: a linha vai direto como
  **`Sem movimento`**. `DECLARAÇÃO PREFEITURA` fica `Enviado` com o recibo/protocolo.
  **ENTRADAS (regra da Fernanda, 17/10/2026):** a linha ENTRADAS é só de **compra de produtos** (NF-e de mercadoria/uso e consumo, CT-e de frete). **NFS-e de serviços tomados NÃO entram em ENTRADAS** (vão em SERVIÇOS TOMADOS). Se não há NF-e no hub SIEG (pasta `Entrada` do CNPJ) e não consta no Domínio, ENTRADAS = `Sem movimento`.
- **DCTFWeb não é do fiscal (Fernanda, 18/10/2026):** não listar guia/recibo da DCTFWeb (CP, IRRF folha etc.) como pendência do fechamento fiscal nem cobrar comprovação no G-Click; é de outro setor.
- **Rendimentos financeiros (Fernanda, 19/10/2026): incidem só sobre RESGATES.** Rendimento "provisionado/acumulado" que não foi resgatado não entra na base do trimestre; entra o **rendimento pago nos resgates** (extrato de depósito a prazo detalhado do Sicredi: colunas Resgates, Rendimentos e IRRF). No FAT: `RENDIM. FINANCEIROS` = rendimento pago no resgate; `IRRF S/RESGATES` = IRRF do resgate (crédito no IRPJ). Extratos da aplicação ficam em `001_DOCUMENTOS DIGITALIZADOS` > mês (ex.: `PORTOOUT_...pdf`, `EXTRATOS_...pdf`, do 247).
- **Montenegro/RS (cliente 247): NÃO há entrega de declaração, só geração de guias (Fernanda, 19/10/2026, conferido no ISS Digital):** o portal da prefeitura (ISS Digital > "Guias para pagamentos/Consulta situação fiscal") só tem as telas de guias do prestador e do tomador (Carnê Retenção ISS); vencimento das guias no dia 10 do mês seguinte. O "Livro Fiscal Eletrônico (DMS)" é **gerado pela integração com o ADN** (PDF anônimo, sem recibo): serve só para conferir os tomados. Leis antigas da prefeitura (art. 50-A, Decreto 4.314/2007 art. 33-G) falam em declaração/"sem movimento", mas o sistema atual (Portal/ADN) não exige a entrega; vale a prática confirmada pela Fernanda. `DECLARAÇÃO PREFEITURA` do 247: o DMS gerado vale como registro (Ago2026 `Enviado` com a data da geração do DMS; manter o padrão) e, onde não houver nada, `Não se aplica`; o que importa é a **guia**: só há guia se houver ISS a recolher (tomador: só quando o ISS é retido; honorário "não retido" = nada). Fonte consultada só por busca: site bloqueado para a agente.
- **Receita do 247 (Porto Mais Alegre):** o cliente informa vendas pelo Forms, mas a Fernanda **sempre valida nos extratos bancários** do mês os créditos com cara de receita (venda de imóvel, sinal, parcelas) que não tenham sido informados. Sem o extrato do mês no Drive, receita = `Pendente`, não `Sem movimento`.
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

- **RF CONSULTORIA (cliente 2, a confirmar) — apuração de 10/2026 (feita em novembro):** o Ricardo Fernandes (RFS) confirmou em 09/10/2026
  que **a partir de 10/2026 a receita de aluguéis deixa de ter valor fixo**: passa a valer o **faturamento mensal**. Não repetir o valor
  de meses anteriores; pedir ao cliente o valor do mês antes de apurar (e conferir com as notas/recibos). Ver `memoria/PENDENCIAS.md`.

- **Gatilho "fechamento da empresa #N" (pedido da Fernanda, 17/10/2026):** ao ouvir isso, ler `memoria/CLIENTE_00N_*.md` (dossiê do cliente: Portal Nacional, prefeitura e particularidades já mapeadas), conferir a Controle_Fiscal do mês e levantar o que falta.
  **Conferência IBS/CBS (pedido da Fernanda, 17/10/2026) — entra em todo "fechamento da empresa #N":** comparar os dados de IBS/CBS (ano-teste 2026, informativo) em três pontos:
  (1) **Prestados:** Portal Nacional (relatório `Emitidas`: CST, cClassTrib, base, CBS/IBS) x Domínio (Resumo dos Impostos: débitos IBS/CBS; acumulador 900 precisa relacionar 183-IBS/184-CBS);
  (2) **Serviços tomados (NFS-e):** Portal (`Recebidas`/`ServTomados`: CST, cClassTrib, CBS e IBS destacados) x créditos no Domínio (acumulador 800);
  (3) **Entradas (NF-e):** XML (grupo `IBSCBSTot`: `vIBS`, `vCBS`, e por item CST/cClassTrib) x créditos no Domínio (acumulador 206 etc.).
  Fechar a soma: créditos do Domínio = NFS-e tomadas + NF-e (Simples costuma vir sem IBS/CBS). Apontar divergência e o que ajustar no acumulador.
  **Rendimentos financeiros (pedido da Fernanda, 17/10/2026) — sempre conferir ao preparar a empresa (#N):** abrir a planilha `CONTROLE | Rendimentos` (Drive, pasta `1IgWAiAS7sxB7qAq8ZCjePeyNDlImJ4Kd`; arquivo `CONTROLE | Rendimentos.xlsx`, id `1ucTfGyMAsMT7AWpNJdI4Nbn0iTZ0UmBA`), aba do trimestre (`3ºTRIM 2026` etc.), linha da empresa: `LIBERADO FISCAL` (Sim / Zerado / NT = não tem conta / em branco = não liberado) e `Observações` (ex.: "Falta só Informe de Rend. ... BRADESCO"). Em branco = IRPJ/CSLL do trimestre não fecha. Trazer o resultado no resumo da preparação. Dossiê existente: `memoria/CLIENTE_002_RF_CONSULTORIA.md` (empresa #2).

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

Vocabulário de Status já usado: `Enviado`, `Pendente`, `Em andamento` (pedido da Fernanda em 19/10/2026: linhas cuja pendência foi deixada para o **pós-fechamento**; antes ficava só na observação), `Sem movimento`, `Importado`,
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
