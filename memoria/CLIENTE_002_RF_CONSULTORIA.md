# Cliente 2 — RF CONSULTORIA: dossiê para o fechamento

**Gatilho (pedido da Fernanda, 17/10/2026):** quando ela disser "fechamento da empresa #2" (ou "fechar a 2"), ler este arquivo, conferir a Controle_Fiscal
do mês e apresentar o que está mapeado (Portal Nacional, prefeitura, particularidades) e o que falta. Atualizar este dossiê a cada fechamento.
Fontes deste dossiê: Cadastro_Clientes e abas Jul/Ago/Set2026 da Controle_Fiscal (export de 17/10/2026), `PENDENCIAS.md`, log `PROCESSO_FECHAMENTO_09-2026.md`
(seções 28k e outras) e `RASCUNHOS_2026-10-05.md` (item 4). Não li nenhum PDF/XML do cliente 2 nesta rodada: o que está abaixo vem das anotações já registradas.

## Cadastro
- Nº **002** (na Controle aparece como 2), RF CONSULTORIA, CNPJ 02.210.396/0001-27, Porto Alegre/RS.
- CNAE principal 6810202 (aluguel de imóveis próprios); sem CNAE secundário. **Lucro Presumido**; contribuinte de ICMS: NÃO; IE isento/N/A.
- Sócios no cadastro: Ricardo Fernandes da Silva (sócio-administrador; contato do cliente, "RFS") e Bruna Freire Fernandes (sócia menor, assistida/representada).
- Portal Nacional (NFS-e): "Obrigatório (Padrão Nacional)".

## Particularidades já mapeadas
- **Sem certificado digital no PC do escritório:** linha CERTIFICADO DIGITAL = "CLIENTE ENVIA AS NOTAS | NÃO TEMOS ACESSO AO CERTIFICADO DIGITAL". O robô do Portal Nacional **não roda** para o 2 (fica entre os 11 sem certificado); as notas dependem do cliente. (?) Em ago/2026 a linha SERVIÇOS PRESTADOS diz "Nenhuma nota de serviços prestados no Portal Nacional (08/2026)": confirmar de onde veio essa consulta.
- **Receita de aluguéis:** até 09/2026 foi **valor fixo** (jul/2026: R$ 21.978,00, `Importado`; PIS R$ 142,86 e COFINS R$ 659,34 em jul, ago e no SPED de 08 = 0,65% e 3% sobre R$ 21.978,00). **A partir de 10/2026 passa a ser o faturamento mensal** (Ricardo Fernandes confirmou por e-mail em 09/10/2026, "sim, exatamente"; a Fernanda perguntou). Regra: **não repetir o valor dos meses anteriores; pedir ao cliente o valor do mês** e conferir com notas/recibos antes de apurar (FAT, PIS/COFINS, IRPJ/CSLL). A mensagem original da Júlia e a imagem do e-mail não foram vistas pela agente: confirmar contrato e valor anterior.
- **ISSQN de Porto Alegre (DecWeb):** só serviços tomados, sem ISS retido; receita R$ 0,00 e imposto R$ 0,00 → **GUIA ISSQN = `Sem movimento`** (sem guia) e **DECLARAÇÃO PREFEITURA `Enviado`** com o recibo (set: recibo 03/10/2026 11:16:19; ago: 01/09 18:44).
- **Serviços tomados recorrentes (dados da prefeitura/Controle):** Officecont (nota mensal; jul e ago R$ 879,30, nº 987 em ago) e **Freire Administração e Serviços Prediais Ltda** (CNPJ 10.420.067/0001-39; ago R$ 1.318,68, ainda sem a nota; set: nº 14263 de 14/09 e nº 14320 de 28/09, R$ 1.142,85 cada, total R$ 2.285,70, sem ISS). Pontos em aberto com o cliente: as duas notas de set têm o mesmo valor (conferir se são serviços distintos) e se houve retenção (IRRF, PIS/COFINS/CSLL, INSS). Rascunho do e-mail em `RASCUNHOS_2026-10-05.md` item 4 (**não enviado**).
- **REINF:** envia-se R-2099 "sem retenção" **provisório** até chegarem as notas (set: 04/10/2026 16:24, recibo 12139055-06-2099-2609-12139055; ago: 09/09/2026 14:30, recibo 11973431-06-2099-2608-11973431). Se a Freire (ou outro prestador) tiver retido, retificar com R-4020/R-2010. Em jul/2026 há também uma linha "R 4010 0,01" `Enviado` (origem não analisada).
- **SPED Contribuições:** 08/2026 transmitido em 04/10/2026 13:51:44 (Original, PIS 142,86 e COFINS 659,34); antes disso estava "sem arquivo na pasta". 09/2026 vence 16/11.
- Cadastro de aluguel: a atividade é locação de imóveis próprios; a presunção de IRPJ/CSLL do aluguel e o tratamento do valor variável devem ser **confirmados na legislação vigente antes de apurar** (recomendo verificar; não afirmei percentuais).

## Situação por competência (Controle_Fiscal, export de 17/10/2026)
| Linha | Jul/2026 | Ago/2026 | Set/2026 |
|---|---|---|---|
| REINF | Enviado | Enviado (R-2099) | Enviado (R-2099 provisório) |
| SERVIÇOS TOMADOS | Não Enviado (R$ 879,30) | Pendente (R$ 2.197,98: falta a Freire R$ 1.318,68) | em branco |
| SERVIÇOS PRESTADOS | Sem movimento | Sem movimento | em branco |
| RECEITA ALUGUEIS | Importado R$ 21.978,00 | Pendente | em branco |
| GUIA ISSQN | Sem movimento | Sem movimento | Sem movimento |
| DECLARAÇÃO PREFEITURA | Enviado | Enviado | Enviado |
| DARF PIS / COFINS | 142,86 / 659,34 Enviado | Enviado (venc. 25/09; G-Click 14/09) | em branco (venc. 23/10) |
| DARF IRPJ / CSLL | (trimestre) | n/a | em branco (venc. 30/10) |
| SPED CONTRIBUIÇÕES | Enviado | Enviado 04/10 | em branco (venc. 16/11) |
Observação: o log registra que há linhas de agosto ainda `Pendente` (2, entre outros): conferir se estão desatualizadas.

## Roteiro quando a Fernanda disser "fechamento da empresa #2" (próxima competência: 10/2026, feita em novembro)
1. Perguntar/pedir ao Ricardo: **valor do faturamento de aluguéis do mês** (regra nova), notas tomadas do mês (Officecont, Freire e outras), se houve retenção, notas emitidas pelo cliente (o Portal não é acessível sem certificado).
2. DecWeb Porto Alegre (robô, fases 1 a 3): declaração de tomados/prestados; receita zero → guia `Sem movimento`; usar a data impressa na guia se houver guia.
3. Conferir o que o Portal/prefeitura trazem de tomados (sem certificado, via relatório municipal da pasta `002 ARQUIVOS MUNICIPAIS`) e lançar/conciliar no Domínio antes de marcar Serviços Tomados `Importado` (regra de 06/10).
4. REINF: R-2099 só se não houver retenção; com retenção, R-4020 (e R-2010 se INSS) conforme a skill `conciliacao-retencoes-servicos-tomados`.
5. PIS/COFINS cumulativos sobre a receita do mês (0,65% e 3%): DARF dia 25 do mês seguinte (ago/2026 foi 25/09; confirmar o dia na guia); IRPJ/CSLL no fechamento do trimestre (próximo: 4º tri, vence em janeiro/2027); SPED Contribuições até o 10º dia útil... **conferir o prazo vigente** (09/2026 consta 16/11).
6. TSV de 7 colunas inline para a Controle; status só com confirmação; guia só `Enviado` com G-Click.

## Levantamento do fechamento 09/2026 (17/10/2026)
Fontes lidas: Controle_Fiscal (export 17/10), FAT `002_RFCONSULTORIA_FAT2026` (Drive), relação municipal de tomados `16680626_202609_NFSE_ServTomados.xlsx`, Declaração Mensal e recibo da prefeitura (03/10 11:16:19), relatório REINF (04/10), recibo e guia DCTFWeb (13/10), planilha `CONTROLE | Rendimentos`. Não achei exportações do Domínio (008) nem Portal Nacional (sem certificado) do cliente 2 para 09/2026.
- **Inscrição municipal 166806-2-6.** Prefeitura: receita bruta R$ 0,00, imposto R$ 0,00; só tomados.
- **Tomados na prefeitura:** Freire Administração e Serviços Prediais (CNPJ 10.420.067/0001-39), notas 14263 (14/09) e 14320 (28/09), R$ 1.142,85 cada, total R$ 2.285,70; Simples ("ME ou EPP do Simples Nacional"); ISS 0 e alíquota 0 (tributação no município). Sem a descrição do serviço (cessão de mão de obra com Simples não dispensa INSS 11%: confirmar). Nota Officecont de setembro não consta da relação.
- **FAT 2026 já tem set preenchido (valor fixo):** receita aluguel R$ 21.978,00/mês; 3º tri R$ 65.934,00; PIS 142,86 e COFINS 659,34 em set; IRPJ 3º tri R$ 3.164,83 e CSLL R$ 1.898,90 (conta: 65.934,00 x 32% = 21.098,88; 15% e 9%; abaixo de R$ 60.000/tri, sem adicional); rendimentos financeiros do 3º tri 0,00 (Fev teve 1.384,41 e IRRF s/ resgates 241,17).
- **Rendimentos:** aba 3ºTRIM 2026, linha RF CONSULTORIA: LIBERADO FISCAL = `Sim` (sem "Zerado"): confirmar que o FAT com 0,00 está certo.
- **DCTFWeb/eSocial 09/2026 (DP):** recibo 0000050000538030702, 13/10/2026 19:34:20; CP segurados R$ 178,31 + CP patronal R$ 324,20 = guia R$ 502,51, venc. 20/10/2026 (cód. 1099 e 1138). Base de pró-labore implícita R$ 1.621,00 (178,31 ÷ 11% e 324,20 ÷ 20%; cálculo da agente, não lido na folha).
- **Perguntas abertas:** (a) Freire: descrição do serviço e retenção (INSS/IRRF/CSRF); (b) nota Officecont de set; (c) houve distribuição de lucros/pagamento a PF em set (em jul há R-4010 0,01 e há distribuição em fev no controle de lucros)?; (d) Serviços Prestados set: `Sem movimento` (prefeitura receita 0; Portal não consultado).

## Atualização 17/10/2026 (tarde): decisões da Fernanda e arquivos do Domínio
Fernanda confirmou: **Serviços Prestados set = Sem movimento**; **rendimentos = zerado**; arquivos do Domínio salvos (`Demonstrativo dos Impostos_2_092026.pdf` e `Empresa 2 - RF CONSULTORIA E NEGOCIOS LTDA.pdf`). Domínio set/2026: saídas do 3º tri R$ 65.934,00 (32%); base R$ 21.098,88; PIS R$ 142,86 e COFINS R$ 659,34 (base R$ 21.978,00); IRPJ R$ 3.164,83 (adicional 0); CSLL R$ 1.898,90; ISS retido sem movimento; IBS/CBS zerados; total R$ 5.865,93. Tudo igual ao FAT. Não vi o Acompanhamento de Entradas: não confirmei se as notas da Freire estão lançadas (Serviços Tomados segue pendente).

## Correção e achado (17/10/2026, mais tarde): Entradas e Saídas do Domínio
Eu havia dito que não achei o Acompanhamento de Entradas: ele existia (`Entradas_2_092026.pdf`, `Saídas_2_092026.pdf`, pasta 008); minha busca anterior filtrou por horário e perdeu os arquivos.
- **Entradas set (Domínio):** só a Officecont nota 1050 (CNPJ 35.743.878/0001-00), emissão 05/10/2026, entrada 30/09/2026, CFOP 1.933, acumulador 800, R$ 879,30. **Freire (14263 e 14320, R$ 2.285,70) NÃO está lançada.**
- **Saídas set (Domínio):** nota 202609, "clientes diversos", 30/09, CFOP 5.949, acumulador 1002, R$ 21.978,00 (receita de aluguel).
- **Prefeitura (DecWeb, 03/10):** só a Freire; a Officecont 1050 não consta, provavelmente porque foi emitida em 05/10, depois da declaração (inferência). Efeito no imposto: nenhum (ISS 0), mas a declaração de tomados não inclui a nota 1050.
- Serviços Tomados set: levantado R$ 3.165,00 (879,30 + 2.285,70), `Pendente` até lançar a Freire e conciliar.

## Resultado do DecWeb e do e-mail (17/10/2026, noite)
- **Retificadora 1** da declaração de 09/2026 recebida em **17/10/2026 12:48:07** (receita 0, imposto 0, total a recolher 0, sem guia). Tomados da retificadora: Officecont 1050 (emissão 05/10, prestação 30/09, R$ 879,30, Simples), Freire 14263 (R$ 1.142,85) e Freire 14320 (**Cancelada**); total válido **R$ 2.022,15** (o R$ 3.165,00 que eu tinha calculado estava errado: a 14320 foi cancelada).
- **Guias geradas em 17/10:** PIS+COFINS R$ 802,20 (venc. 23/10) e IRPJ+CSLL do 3º tri R$ 5.063,73 (venc. 30/10). Sem comprovação do G-Click: ficam `Pendente`.
- **E-mail (extensão, OWA):** cobrança das notas de set em 04/10 16:18; Ricardo respondeu em 05/10 14:11 repassando a Freire: vale a nota de 14/09 (14263); a de 28/09 (14320) foi emitida em duplicidade e cancelada. Nada sobre descrição do serviço nem retenção. Agosto: cobrança em 14/09 (nota 13882, R$ 1.318,68); Ricardo mandou documentos em 16/09, mas nenhum e-mail cita a 13882. Anexos não abertos pela extensão.
- **Código 19831 = código de proprietário da RF na Freire Imóveis** (demonstrativos de 2019/2020 no Drive): os PDFs "NF - 19831 RF Consultoria" são da Freire para a RF; serviço provavelmente administração de aluguéis (inferência; anexos de 2026 não lidos). Observação não confirmada: 1.318,68 = 6,0% de 21.978,00 e 1.142,85 = 5,2%.
- **Pendências:** abrir/salvar no Drive os PDFs da Freire (69 KB e 30 KB) para confirmar nº, descrição e retenção; nota de agosto 13882 (Controle Ago Serviços Tomados `Pendente`).

TSV consolidado enviado em 17/10 (substitui os anteriores):
```tsv
2	Set2026	SERVIÇOS PRESTADOS	Sem movimento	0,00	Prefeitura (Declaração Mensal): receita bruta R$ 0,00; confirmado pela Fernanda em 17/10/2026. Portal não consultado (sem certificado).	
2	Set2026	RECEITA ALUGUEIS	Importado	21978,00	Domínio (Saídas 17/10): nota 202609 de 30/09, CFOP 5.949, acum. 1002, R$ 21.978,00 (valor fixo até 09/2026) = FAT; PIS/COFINS sobre R$ 21.978,00.	
2	Set2026	DECLARAÇÃO PREFEITURA	Enviado		Retificadora 1 recebida em 17/10/2026 12:48:07 (inclui a Officecont 1050, de 05/10, que não constava da original de 03/10 11:16:19). Receita bruta R$ 0,00 e imposto devido R$ 0,00 (só tomados, sem ISS retido).	
2	Set2026	SERVIÇOS TOMADOS	Pendente	2022,15	Em andamento: DecWeb (Retificadora 1) = Freire 14263 R$ 1.142,85 + Officecont 1050 R$ 879,30 = R$ 2.022,15 (Freire 14320 cancelada). Domínio tem só a Officecont 1050 (R$ 879,30); Freire 14263 sem nota no escritório, não lançada.	
2	Set2026	DARF PIS	Pendente	142,86	Domínio = FAT. Guia PIS+COFINS R$ 802,20 gerada em 17/10 (doc. 07.16.26290.6703422-2), venc. 23/10; sem comprovação do G-Click.	
2	Set2026	DARF COFINS	Pendente	659,34	Domínio = FAT. Mesma guia de R$ 802,20 (doc. 07.16.26290.6703422-2), venc. 23/10; sem comprovação do G-Click.	
2	Set2026	DARF IRPJ	Pendente	3164,83	3º tri: base R$ 21.098,88 x 15%, sem adicional; rendimentos zerado. Guia IRPJ+CSLL R$ 5.063,73 gerada em 17/10 (doc. 07.16.26290.6704807-0), venc. 30/10; sem comprovação do G-Click.	
2	Set2026	DARF CSLL	Pendente	1898,90	3º tri: base R$ 21.098,88 x 9%. Mesma guia de R$ 5.063,73 (doc. 07.16.26290.6704807-0), venc. 30/10; sem comprovação do G-Click.	
```

## Conferência das guias de 09/2026 antes do envio ao cliente (17/10/2026)
Guias lidas (pasta 002 ARQUIVOS MUNICIPAIS/guias): PIS/COFINS doc. 07.16.26290.6703422-2 (venc. 23/10; COFINS 2172 R$ 659,34 + PIS 8109 R$ 142,86 = R$ 802,20) e IRPJ/CSLL doc. 07.16.26290.6704807-0 (venc. 30/10; IRPJ 2089 R$ 3.164,83 + CSLL 2372 R$ 1.898,90 = R$ 5.063,73; PA 3º trim/2026). CNPJ e razão social conferem; valores = Demonstrativo do Domínio = FAT; 25/10 é domingo (PIS/COFINS antecipa para 23/10) e 31/10 é sábado (IRPJ/CSLL em 30/10). CP DCTFWeb (DP): R$ 502,51, venc. 20/10. Total do mês R$ 6.368,44. Pendente: comprovação do G-Click. Cota única nas duas guias; parcelamento do IRPJ em até 3 cotas só se o cliente pedir (cada cota ≥ R$ 1.000; confirmar).

## G-Click (print de 17/10/2026)
Tarefa CSLL e IRPJ - LP (Trimestral): concluída por fernanda.officecont em 17/10/2026 13:00 (venc. 30/10). Tarefa COFINS / PIS (venc. 23/10): check verde, usuário e horário cortados no print. TSV de `Enviado` entregue (IRPJ/CSLL com prova completa; PIS/COFINS sujeito à confirmação da Fernanda).
```tsv
2	Set2026	DARF IRPJ	Enviado	3164,83	G-Click: tarefa "CSLL e IRPJ - LP (Trimestral)" concluída por fernanda.officecont em 17/10/2026 13:00 (meta 27/10, venc. 30/10). 3º tri: base R$ 21.098,88 x 15%, sem adicional; guia IRPJ+CSLL R$ 5.063,73 (doc. 07.16.26290.6704807-0).	
2	Set2026	DARF CSLL	Enviado	1898,90	G-Click: tarefa "CSLL e IRPJ - LP (Trimestral)" concluída por fernanda.officecont em 17/10/2026 13:00 (venc. 30/10). 3º tri: base R$ 21.098,88 x 9%; mesma guia de R$ 5.063,73.	
2	Set2026	DARF PIS	Enviado	142,86	G-Click: tarefa "COFINS / PIS" com check verde de concluída (meta 21/10, venc. 23/10; usuário e horário não aparecem no recorte do print). Guia PIS+COFINS R$ 802,20 (doc. 07.16.26290.6703422-2).	
2	Set2026	DARF COFINS	Enviado	659,34	G-Click: tarefa "COFINS / PIS" com check verde de concluída (venc. 23/10; usuário e horário não aparecem no recorte do print). Mesma guia de R$ 802,20 (doc. 07.16.26290.6703422-2).	
```

## ALERTA (17/10/2026, tarde): nota Freire 14263 e demonstrativo mostram distrato do locatário em 26/08/2026
Arquivos lidos (zip salvo na pasta 013: `2_RF CONSULTORIA_Fwd__Demonstrativo_e_Nota_fiscal.zip`): `NF - 19831 RF Consultoria (Com.).pdf` = **NFS-e 14263** (14/09/2026, Freire Administração e Serviços Prediais, Simples, 17.12.01 "Administração de imóveis e de condomínios", "TAXA DE ADMINISTRAÇÃO DE ALUGUEL", R$ 1.142,85; ISS não retido; sem retenção federal; IBS/CBS CST 200 / cClassTrib 200046, redução 50%, CBS R$ 5,14 e IBS R$ 0,57) e `dem19831.pdf` = demonstrativo de proprietário competência 08/2026.
Demonstrativo: único locatário pagante = Consulado Geral da Itália (imóvel 979, contrato desde 01/01/2023), **Distrato: 26/08/2026**; aluguel de agosto só de 26 dias = R$ 19.047,60 (= 21.978,00 x 26/30), taxa de administração R$ 1.142,85 (6%), devolução de taxa R$ 190,48, líquido R$ 18.095,23 pago em 01/09/2026. Os demais imóveis aparecem como "Cortesia".
Consequência a confirmar: o Domínio e o FAT lançam R$ 21.978,00 de aluguel em ago e em set (valor fixo). Se não há outro locatário, set teria receita zero e ago R$ 19.047,60. Exemplo (cenário A, competência): PIS/COFINS de set zerados (guia R$ 802,20 não seria devida); ago PIS 123,81 e COFINS 571,43 (pagos 142,86 e 659,34); 3º tri receita R$ 41.025,60, base 32% R$ 13.128,19, IRPJ R$ 1.969,23 e CSLL R$ 1.181,54 (R$ 3.150,77 em vez de R$ 5.063,73). Regime (caixa ou competência) e outras receitas não confirmados. Guias de PIS/COFINS e IRPJ/CSLL já estão no G-Click: segurar o envio ao cliente/pagamento até confirmar.
Nota 14263: sem retenção; a Freire 13882 (12/08, R$ 1.318,68, taxa de julho) segue sem documento. Entradas do Domínio com as duas notas (Officecont 1050 + Freire 14263 = R$ 2.022,15) ainda não vistas no Drive (arquivo Entradas_2_092026.pdf continuava com só a Officecont às 16:2x).
