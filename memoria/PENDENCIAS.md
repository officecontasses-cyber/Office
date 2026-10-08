# Pendências e resolvidos — OfficeCont (Fechamento Fiscal)

Documento vivo. **A cada rodada:** atualizar este arquivo (o que foi feito e o que falta), o log detalhado
`PROCESSO_FECHAMENTO_09-2026.md` e salvar o snapshot `PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` na pasta
`ARQUIVOS EXTENSÃO - CODE - CLAUDE` do Drive (regra da Fernanda, 02/10 e 04/10/2026).
Última atualização: **06/10/2026, noite (rodada de 05 e 06/10 registrada na seção K, logo abaixo).**

Convenção: `[ ]` pendente · `[x]` resolvido · `(?)` precisa de confirmação da Fernanda.
Nunca registrar aqui senhas, CPFs completos ou certificados.

**Situação em 04/10/2026:** agosto/2026 está **fechado** e o SPED Contribuições de 08/2026 foi transmitido (23 clientes).
O fechamento de **09/2026** avançou: ISSQN de Porto Alegre quase todo enviado, prefeituras de São Leopoldo, Novo Hamburgo e
Brasília feitas, REINF dos sem retenção enviado, planilha do DP e script prontos. **Retomada na segunda 05/10.**

Arquivos de apoio: `RASCUNHOS_2026-10-05.md` (mensagens e e-mails prontos, seções 1 a 5), `TSV_REINF_RESUMIDO_09-2026.md` e
`TSV_DP_REINF_09-2026.md` (TSV do REINF para o DP e a Controle), `PLANO_FECHAMENTO_10-2026.md` (agilidade em outubro),
skills em `.claude/skills/` (`sao-leopoldo-issqn`, `novo-hamburgo-issqn`, `brasilia-issqn`), script `apps-script/atualizarReinfDP.gs`.

---

## K. RODADA 05–06/10/2026: o que foi feito e o que falta (resumo por cliente)

**Regra de status (Fernanda, 06/10):** onde há movimento (notas a lançar), as linhas Serviços Tomados/Prestados, Entradas e Saídas só vão como
`Importado`/`Enviado` depois do Domínio importado e conciliado; antes ficam `Pendente` ("Em andamento" na observação). Onde **não há nota** na fonte
oficial (SEFAZ/SAT, Portal, prefeitura), vai direto `Sem movimento`. `DECLARAÇÃO PREFEITURA` fica `Enviado` com o recibo. Regra no `CLAUDE.md`.
Competência das NFS-e tomadas: campo `dCompet` do XML.

### Clientes da retenção federal (REINF; Domínio conferido com os relatórios)
- [x] **126 Tatsch & Leite:** Recebidas conferidas (retenção só da BIOLAB 1507: CRF R$ 10,46, cód. 5952); Facebook 144113199 é de agosto (já lançada); Ideal Art 444 = R$ 336,74 (desconto incondicional). **REINF enviado 06/10 06:03** (R-4020 recibo 97463238-10-4020-2609-97463238, R-2099 12127193-10-2099-2609-12127193, R-4099 5830434-10-4099-2609-5830434); TSV do DP e da Controle entregues.
  - [ ] Importar no Domínio as **saídas 1760 a 1841** (82 notas, R$ 67.275,50; o Domínio parou na 1759): ISS (R$ 3.073,23 = guia), PIS/COFINS e IRPJ/CSLL do trimestre só fecham depois; rever o Demonstrativo (PIS/COFINS alvo R$ 998,81 e R$ 4.609,87). Conferir se a guia do DARF 5952 (R$ 10,46) saiu.
- [x] **189 Real Engenharia (Lucro Presumido):** Recebidas = 1 nota (Xavantina 5, R$ 142.933,33, IRRF R$ 2.144,00); Entradas e demonstrativo do IRRF conferem. **REINF enviado 06/10 06:29** (R-4020 20706833-02-4020-2609-20706833, R-2099 12056927-02-2099-2609-12056927, R-4099 5813615-02-4099-2609-5813615); TSV entregue.
  - [ ] Decidir se a **CRF 4,65%** (cerca de R$ 6.646,40) se aplica à representação comercial; confirmar data de pagamento e código do IRRF (provável 8045; DP usa 170806 do modelo). Saídas na rodada de serviços (Domínio traz só a NFS-e 44; Portal R$ 2.868.189,79).
- [ ] **71 Conte:** Recebidas analisadas (139 notas, R$ 456.689,03; retenção da nota 659: IRRF 83,61 + CRF 259,20; ISS retido RIPA 153 R$ 39,43); relatório por código em `ACUMULADORES_71_09-2026.md`. E-mail à Francine sobre a **NFS-e 60 (Laura de Luca)** em `RASCUNHOS_2026-10-06.md` (a Fernanda envia).
  - [ ] Falta: Fernanda lançar as entradas e mandar os PDFs do Domínio para eu conferir; depois REINF (R-4020). Conferir Chanfro nº 2 (competência 08, IRRF 42,00 + CRF 130,20 em agosto?) e Giovani 676 (outubro); Caixa Cartões 30774046 (valor zero).
- [ ] **238 REAT e 152 Conselho:** ainda não iniciados na conferência do Domínio; REINF (R-4020/R-2010) pendente.
- [ ] **A confirmar com a Fernanda (itens de segunda 05/10):** ligação à Leidislaine, mensagens da seção A (257, Gian, Inês, 2 RF, 11 sem certificado) e o resultado dos TSVs do REINF colados no DP e na Controle.

### Tacom 138 (fiscal e cálculo pela matriz)
- [x] **Tomados NFS-e:** as 9 notas da prefeitura (R$ 28.980,50) conciliadas com o Domínio; **Entradas** (8 NF-e R$ 26.607,36 + 9 NFS-e) e **Saídas** (2 NF-e R$ 40.161,90) conferem com o txt do SEFAZ RS e com os XMLs. ICMS do mês zero; saldo credor R$ 17.385,19 vai para 10/2026.
- [x] **GIA RS 09/2026** transmitida (protocolo TED 13542570, 06/10 15:15:59; recibo definitivo depois).
- [ ] **URGENTE: SPED Fiscal 09/2026 sem 4 NF-e** de compra CFOP 1.556 (R$ 657,96, acumulador 106). Regerar e conferir antes de a Leidislaine transmitir (até 08/10); `SPED ICMS - Envio arquivo` fica `Pendente` até lá. Depois, `SPED ICMS (Recibo)`.
- [ ] TSV da fila (`TSV_TACOM_138_09-2026.md`): a Fernanda cola (Tomados/Entradas/Saídas `Importado`, Guia ICMS `Sem movimento`, GIA `Enviado`, SPED envio `Pendente`, recibo `Pendente`).
- [ ] **Após o fechamento (seção J):** acumulador 800 (183/184), CST 410 (acumulador 1007), INSS retido R$ 175,30 da Ellu's 1353 (R-2010 do 138; conferir a 1317 de agosto), produtos 12805/12806/17055/20932/21353 (cClassTrib) e CEST do 20932, PIS/COFINS no acumulador 106, Pluxee R$ 0,00; avisar a matriz sobre as remessas 4698/4699 com IBS/CBS (rascunho em `RASCUNHOS_2026-10-06.md`, item 2).

### Tacom 248 (Palhoça/SC, CNPJ …/0020-03) e 263 (Porto Alegre)
- [x] **248, prefeitura de Palhoça:** declarações de Serviços Prestados (sem documentos) e Tomados (NFe 1017 OfficeCont, R$ 650,00, ISS 0) enviadas em 06/10 (15:40 e 15:41); SAT/SC: sem NF-e/NFC-e emitidas; 1 NF-e recebida (Leonardo Alves Sebastião ME, NF 123, 14/09, R$ 15,00).
- [ ] **248:** Domínio importado em 06/10 (NFS-e 1017, R$ 650,00 = prefeitura; TSV rodada 1 colado pela Fernanda e rodada 2 em `TSV_TACOM_248_09-2026_rodada2.md`). **Falta lançar a NF-e 123 (R$ 15,00, Leonardo Alves Sebastião ME, 14/09)**, GUIA ICMS e SPED ICMS (em agosto "Envio pela Matriz"). DIME `Não se aplica` (dispensada desde junho). **Após o fechamento:** acumulador 800 do 248 (183-IBS/184-CBS); a NFS-e 1020 (01/10, R$ 650,00) ficou fora da importação de setembro por esse aviso: importar em outubro depois do ajuste.
  - [ ] **248, decisão da Fernanda (06/10):** a NF-e 123 não veio do SIEG; ela vai verificar depois, mas **libera o SPED ICMS do 248 sem essa nota** e avisa quando enviar (**enviado em 06/10 às 16:33 pelo G-Click**; TSV em `TSV_TACOM_248_09-2026_rodada3.md`; falta o recibo da Leidislaine). Depois de lançar a NF-e 123 (R$ 15,00, ICMS 0), avaliar se o SPED precisa de retificação e fechar `ENTRADAS` e `GUIA ICMS`.
- [ ] **263:** DecWeb: tomados R$ 650,00 (OfficeCont, NFS-e 1018) e prestados 9 NFS-e R$ 81.793,56 (ISS R$ 4.089,69 = guia enviada). Falta o Domínio (Entradas/Saídas) para conciliar e gerar o TSV; contribuinte de ICMS = NÃO.

### Reforma tributária e acumuladores (outubro com agilidade)
- [ ] Padronizar acumuladores de serviços tomados (IBS/CBS integral 000/000001, redução 200052, sem incidência 410, sem dados) e transformar em skill; base de IBS/CBS = valor − ISS − PIS/COFINS destacados. Detalhes na seção J.
- [ ] Skill da conferência do Domínio (ler relatório + XML do Portal + SEFAZ) para repetir em outubro.

---

## PENDENTE

### A. SEGUNDA 05/10, PRIMEIRO HORÁRIO (mensagens e ligações; textos prontos em `RASCUNHOS_2026-10-05.md`) — (?) a Fernanda não informou o resultado; confirmar
- [ ] **Antes das 11:00: ligar para a Leidislaine (Tacom)** e combinar o acesso à máquina dela (e-mail sem retorno até 03/10). SPED Fiscal da Tacom: a Fernanda prometeu os arquivos até **qua 07/10** (ela transmite até 08/10). (?) vale para 138, 263 ou ambas?
- [ ] **257 (WhatsApp + e-mail, seção 1):** perguntar se a Lifecombr (nota 31, R$ 130.000,00, item 10.05) deveria ter retido o ISS de R$ 6.500,00 (guia vence 13/10).
- [ ] **E-mail ao Gian, 152 (seção 2):** ISS de Florianópolis (nota 6940 da Litoral Serviços Automotivos, R$ 42,00, incidência Florianópolis/SC, ISS 0,00 no Portal): recolheram ou ele já tem acesso lá? Gian é interno (responsável contábil nos cadastros de São Leopoldo), não contato do cliente.
- [ ] **Gian, 265:** liberar a **procuração eletrônica** (REINF deu erro 15 no Domínio); conferir no OWA (Itens Enviados) se o e-mail sobre o certificado do 258 (vence 14/10) foi enviado (rascunho de 03/10).
- [ ] **Inês (seção 5):** pedir o movimento de setembro de **18, 177 e 133** (pasta `001_DOCUMENTOS DIGITALIZADOS` > `09_SETEMBRO` vazia nos três; e-mail dela não conferido daqui) e perguntar se a **Datasys** reteve imposto nas notas de 29/09 (18: nº 11, R$ 2.100,00; 177: nº 13, R$ 26.520,00). 133: nota tomada nº 18 de MEI, R$ 300,00.
- [ ] **Cliente 2 RF Consultoria (seção 4):** cobrar as notas da **Freire Administração e Serviços Prediais** (nº 14263 de 14/09 e nº 14320 de 28/09, R$ 1.142,85 cada, total R$ 2.285,70, sem ISS; nenhuma é da Officecont); duas notas idênticas no mês, pedir confirmação e se houve retenção.
- [ ] **11 clientes sem certificado (seção 3):** pedir a relação das notas recebidas de setembro e se houve retenção federal (só federal): 2, 18, 26, 133, 138, 173, 177, 185, 209, 248, 263. Tacom (138, 248, 263) apura pela matriz: só interessa quando houver retenção municipal. Provisoriamente entram como sem retenção/sem movimento no REINF.

### B. ISSQN de 09/2026 — Porto Alegre (DecWeb, 22 de 22 enviadas; guias vencem 13/10)
- [ ] **205 (R$ 1.915,06):** Fernanda confirmou a guia; **postar no G-Click**. (nota 197 é a substituta da 196; `conciliacao.py` já corrigido.)
- [x] **155 Mainieri (08/10):** retificadora 1 enviada (recibo 08/10 09:39:11, receita R$ 22.676,34, ISS R$ 907,02); guia nova R$ 907,02 (venc. 13/10) com G-Click 10:11 e envio ao cliente 10:12; TSV Enviado entregue. FAT2026 L4 = 22.676,34 a digitar (L14 já calcula 4%). A guia antiga de R$ 842,02 não vale. Conferir FAT de agosto (K4 22.477,87 x Portal 08/2026 Normal 22.233,73).
- [ ] **257 (R$ 6.500,00):** aguarda a resposta do cliente (item A).
- [ ] **152:** ISS retido total R$ 568,44 = R$ 461,69 POA + **R$ 106,75 Estrela/RS** (ENGI PROJECT, notas 1146 e 1218): **fazer junto com a Fernanda no portal de Estrela** (baixar as notas e declarar); marcar horário. Em agosto foram R$ 25,63 (venc. 23/09).
- [ ] **2 RF Consultoria:** guia ISSQN em branco (não confirmado) até a resposta do cliente. **247 Montenegro:** DMS fora do DecWeb.
- [ ] Rodrigo Tavares Lopes (mesmo CPF) consta como profissional nos clientes 16 e 173: conferir.
- [ ] 155: 63 notas de 08/2026 geradas entre 31/08 e 03/09; sem indício de furo, mas agosto inteiro não foi conferido.
- [ ] Município sem prazo de ISS cadastrado: Brasília, Rio de Janeiro, Novo Hamburgo, São Sebastião do Caí, Montenegro, Palhoça.

### C. Outras prefeituras (fora do DecWeb)
- [ ] **Faltam:** **247 Montenegro**, **185 Rio de Janeiro**, **227 PROGEST** (estava inativa; entregas começam em 09/2026) e o lote de **São Paulo** (a Fernanda gravou o vídeo e salvou em `09_SETEMBRO` no Drive do PC; ainda não chegou ao Drive acessível pela agente). Transformar cada gravação em skill.
- [x] Feitas em 04/10 (TSV entregue e colado): 126 São Leopoldo, 261 e 197 Novo Hamburgo, 71 e 264 Brasília (ver RESOLVIDO).
- [ ] **71 Brasília:** renomear o arquivo `71_Conte_Brasília_09.2026_LivroFiscalPrestados` para `.csv`; a Fernanda deve **colar a linha corrigida da GUIA ISSQN FORA MUNICÍPIO** (`Enviado` R$ 39,43, guia de Jundiaí/SP nº 00026073855, venc. 26/10, G-Click 04/10 15:39) no lugar da `Pendente`. Conferir o local de execução da nota RIPA nº 153 (item 7.11): o Portal diz São Paulo/SP e a chave aponta Jundiaí.
- [ ] (?) 261: confirmar se as linhas SERVIÇOS PRESTADOS (34.000,00) e SERVIÇOS TOMADOS (483,40) já foram coladas como `Pendente`; nota Google nº 19985753 do protocolo não está no Portal (lá consta a 19171581, comp. 08/2026).

### D. REINF 09/2026 (vence 15/10) e planilha do DP
**Já enviado (R-2099 Sucesso, 04/10):** 2, 16, 18, 26, 133, 155, 173, 177, 185, 186 (12:50), 197, 209, 237, 247, 258, 264 (16:21 a 16:25) e **241, 257, 261** (16:50 a 16:52; no 257 o R-1000 de inclusão retornou `Invalidado`, o R-2099 valeu). Só R-2099, sem R-2010/R-4020.
- [ ] **A enviar, com retenção como tomador (R-4020; R-2010 para INSS em 152 e 238; depois R-2099):** **71, 126, 152, 189, 238** (126 e 189 já enviados em 06/10, ver seção K; faltam 71, 152 e 238). Valores (Recebidas do Portal): 71 IRRF 83,61 + CRF 259,20; 126 CRF 10,46 (Biolab nº 1507, nota de 01/10); 152 IRRF 1.984,70 + contribuições 1.035,82 + INSS 1.269,26; 189 IRRF 2.144,00 (Xavantina nº 5); 238 IRRF 17,75 + contribuições 141,86 + INSS 1.295,45.
- [ ] **205:** sem relatório na pasta REINF (conferir se foi enviado e salvar o PDF; retenção só sofrida, R-2099 sem movimento).
- [ ] **265:** Domínio, erro 15 (para PJ: certificado da matriz, do representante legal ou procurador na Procuração Eletrônica da RFB). `Pendente` até o Gian liberar a procuração (ou usar o A1 do próprio 265).
- [ ] **A decidir:** Tacom 138, 248, 263 (matriz) e 227 PROGEST.
- [ ] **Provisórios (retificar se aparecer retenção):** 2, 18, 133, 177 (aguardam notas/movimento).
- [ ] **152, códigos para a caixa da planilha do DP:** valores provisórios 6190 = R$ 1.534,82 (15 notas, IRRF 4,8% + 4,65%); 6147 = R$ 44,14 (Casa da Moeda, 1,2% + 4,65%); 6228 CSLL = R$ 245,50 (nota 15095); INSS 1162 = R$ 1.269,26. **Classificar o código** do IRRF de R$ 1.178,40 (nota 15095, Implanta) e do IRRF de R$ 17,66 (nota 741590, Rede OK, emitida em 01/10: retenção pode ser de outubro). Conferir pela IN RFB 1.234 (skill de órgão público disponível). Notas 3279/3280 (Realize Next): texto diz `PIS/COFINS Retidos`, mas há CSLL e INSS.
- [ ] **Planilha do DP (`CONTROLE | DP REINF'S`, aba `MOD GERAL 09.2026`):** script `atualizarReinfDP.gs` instalado em 04/10 16:37 e aba `Atualizações REINF` criada. **Falta:** colar o TSV (testar com 16 e 117; depois o resto, mais 241, 257, 261 e o 265) e rodar `processarAtualizacoesReinf()`; depois o TSV das retenções (71, 126, 189, 238 e a caixa do 152) só após conferir os códigos. Em `TSV_REINF_RESUMIDO_09-2026.md`. Linha do 117 no DP só `Sem movimento`.
- [ ] **Controle_Fiscal (REINF Set2026):** colar o TSV resumido (16 clientes + 241, 257, 261; 265 `Pendente`; 117 `Não se aplica`).
- [ ] Depois de cada envio: G-Click `EFD Reinf` (atividade Recibo). **186:** pergunta antiga ainda aberta: houve distribuição de lucros ou pagamento a pessoa física em setembro (R-4010)?
- [x] **Regra permanente 117 TABAJARA:** REINF e obrigações que dependem de certificado/procuração = `Não se aplica` até a baixa da empresa (sócio faleceu, sem procuração); `Invalidado` no R-2099 é esperado, não reenviar.

### E. Federais 09/2026 (apuração; DARF PIS/COFINS vence 23/10, IRPJ/CSLL 30/10)
- [ ] **Retenção federal sofrida nas Emitidas (INSS = 0 em todos, sem R-2020):** 71 IRRF 52.371,72 + contribuições 10.910,78 (Caixa; notas dizem 4,65%, coluna traz 1,0%: **conferir com o informe da Caixa**); 189 43.022,85 + 133.370,83 (Guntner); 205 245,30 + 760,41 (COOPA e Abastecedora Mania); 241 só contribuições 1.348,61; 257 IRRF 228,76 (Telefônica); 261 510,00 + 1.241,00 (Betha). Sem retenção sofrida: 16, 126, 155, 186. Usar como crédito na apuração. 189: nas duas notas o ISS aparece não retido e zerado (motivo não analisado).
- [ ] **186:** IRPJ (1.315,74) e CSLL (789,45) do 3º trimestre provisórios, dependem do contábil (rendimentos financeiros e IRRF). Linhas DARF IRPJ e CSLL `Pendente`. **SPED Contribuições de 09/2026 vence 16/11.**
- [ ] **Sex 16/10 (sugerido): retorno do contábil** (rendimentos/IRRF do 3º tri). Planilha `CONTROLE | Rendimentos.xlsx` (aba `3ºTRIM 2026`): incluir **227 PROGEST, 264 ZENITH PARACURU e 265 BELEM BRASIL HOLDING** (linhas 24 a 26; classificar A2:D26 pela coluna A); (?) 133 RFL e 238 REAT (Lucro Real) saíram dos blocos: confirmar. E-mail ao contábil em rascunho.
- [ ] **Conferência no Domínio dos demais clientes** (quando a Fernanda importar e exportar para `008 ARQUIVOS DOMÍNIO`, `09_SETEMBRO`): começar por 152 e 205, seguir a ordem de prioridade. Acumuladores IBS/CBS: o do 186 foi ajustado (cClassTrib 200052/CST 200 nos prestados); não replicar para outras atividades sem conferir.
- [ ] **16 a 31/10: REAT HOLDING (238):** enviar à cliente o relatório de débitos ref. 06/2026 (Relatório Fiscal de 21/08, Júlia Rocha) + IRPJ e CSLL vencidos de meses anteriores (?) quais meses. **238, retificação de junho/2026:** guia complementar "A gerar" (PIS R$ 38,96 + COFINS R$ 239,77 = R$ 278,73); confirmar se foi gerada e paga.

### F. SPED Contribuições 08/2026 e agosto (agosto está fechado)
- [ ] **Sem SPED de 08/2026:** **117** (sem procuração/certificado, baixa em andamento: propor `Não se aplica`, a confirmar) e **227** PROGEST (sem arquivo; começa em 09/2026). 152 (autarquia) e 197 já `Não se aplica`.
- [ ] Observações: 257 é contribuinte de ICMS e o arquivo só tem serviços (confirmar se a receita de R$ 126.223,13 inclui mercadoria); 018 com saldo de retenção sem uso nos registros 1300/1700 (conferir no Domínio).
- [ ] Linhas DARF PIS/COFINS de agosto ainda `Pendente` na Ago2026 (071, 133 COFINS, 237, 238, 241, 257, 258, 261): atualizar quando convier (071 `Retido`, 133 COFINS `Compensado` por PER/DCOMP, 237/258/261 `Sem movimento`).

### G. Datas
- [ ] **Qua 07/10:** SPED Fiscal da Tacom. **13/10:** ISSQN de Porto Alegre 09/2026 (prazo impresso na guia). **14/10:** certificado A1 do 258 vence (155 em 27/10, 71 em 13/11, 117 em 11/12, 126 em 16/12). **15/10:** REINF e ISS de São Leopoldo (126). **20/10:** guia ISS de Novo Hamburgo (261). **23/10:** DARF PIS/COFINS 09/2026. **26/10:** guia Jundiaí (71). **30/10:** IRPJ/CSLL do 3º tri. **16/11:** SPED Contribuições 09/2026.

### H. Cliente 265 BELEM BRASIL HOLDING
- [ ] **Segurança:** trocar a senha do DecWeb (foi digitada no chat em 02/10); renomear o arquivo do certificado A1 no Drive (o nome contém a senha); apagar a mensagem do WhatsApp com a senha do certificado.
- [ ] ISSQN nos meses seguintes: só a arquitetura (71.11-1-00) gera ISS (?); outubro: nota SAFEWEB 182232 (R$ 275,00, ISS 2% não retido). Pró-labore dos sócios; (?) SIEG e G-Click cadastrados; incluir na planilha de rendimentos (item E).

### I. Robôs, configuração e estruturais
- [ ] Clientes sem certificado neste PC: ver item A (Tacom por outro caminho). Portal Nacional: (?) 173 "PENDENTE DE CADASTRO"; 71, 197 e 261 "Em Transição (Prefeitura)": o Padrão Nacional já vale?
- [ ] `conciliacao.py` (corrigido para nota de substituição): copiar para `C:\Robos\decweb` e `pip install pypdf` (opcional) se ainda não foi feito; rodar de novo para 152, 205 e 186.
- [ ] Salvar logs do robô no Drive (sem senhas) para a agente conferir sem pedir `resultados.csv`.
- [ ] R-4010 do 189; PER/DCOMP do 133; conferência do 238; as 7 linhas "Não se aplica" fixas; possível gerador de TSV a partir dos PDFs do robô.
- [ ] Se a BrasilAPI falhar em sessão nova, liberar `publica.cnpj.ws` e `receitaws.com.br` na rede do ambiente.
- [ ] **Outubro com agilidade:** seguir `PLANO_FECHAMENTO_10-2026.md` (Tacom no dia 1, pedidos aos clientes nos dias 1 e 2, skills por município, gravar São Paulo/Montenegro/Rio/PROGEST, renovar certificados antes do dia 1).

---

## RESOLVIDO (resumo por data)

### 04/10/2026
- [x] **SPED Contribuições de 08/2026:** 23 clientes transmitidos (016, 018, 026, 071, 126, 133, 155, 173, 177, 185, 186, 189, 205, 209, 237, 238, 241, 247, 257, 258, 261, 264 e o 002 às 13:51:44); recibos conferidos; TSV entregue.
- [x] **186 Lopes & Nadal** fechado até onde depende da casa: DecWeb 11:26, guia enviada, PIS/COFINS (R$ 418,84) `Enviado`, REINF R-2099 (recibo 12122144-09-2099-2609-12122144), Domínio conferido, FAT digitado, auditoria da Controle e TSV colados.
- [x] **ISS de São Leopoldo, 126:** DMS (ADN, nº 1053665) = Portal = guia **R$ 3.073,23** (209 notas, R$ 153.662,41), venc. 15/10, Nosso Número 14400000001431673-7; Declaração `Enviado`; guia `Enviado` (G-Click 04/10 14:46). Skill `sao-leopoldo-issqn`.
- [x] **ISS de Novo Hamburgo:** 261 Giatech guia **R$ 680,00** venc. 20/10 (G-Click 15:02/15:03, `Enviado`), Tomados R$ 483,40 (ISS outros municípios R$ 5,57); 197 ASBBM sem guia (Prestados sem notas; Tomados 2 notas R$ 5.500,00, ISS outros municípios R$ 175,00); skill `novo-hamburgo-issqn`.
- [x] **ISS de Brasília:** 71 Conte (42 notas, R$ 1.091.077,54, retenção integral pela Caixa, sem guia; guia de Jundiaí R$ 39,43 `Enviado` G-Click 15:39; Não Movimento em Contratados); 264 Zenith (Não Movimento dos dois, 15:42/15:43; `Enviado`/`Sem movimento`); skill `brasilia-issqn`.
- [x] **Conciliações de POA:** 257 explicado (guia R$ 6.500,00 = ISS da nota 31, não retida); 205 provável OK (nota substituta 197); 152 (nota R$ 42,00 só no Portal é de Florianópolis, ISS 0,00; Estrela R$ 106,75). `conciliacao.py` corrigido (nota de substituição gerada conta como normal; teste incluído). `aceitar_avisos` resetado (173, 238, 152, 265).
- [x] **Portal Nacional:** Recebidas e Emitidas de 09/2026 lidas por agentes de apoio (retenções tomadas e sofridas); 117, 247 e 258 sem movimento confirmados no log (login por certificado OK); 14 clientes sem retenção federal própria; 11 sem certificado listados.
- [x] **REINF:** lote 1 (16 clientes, 04/10 16:21 a 16:25) e lote 2 (241, 257, 261) com Sucesso; script e TSV do DP prontos; regra do 117.
- [x] **227 PROGEST:** inativa até 09/2026 (entregas começam agora); **FAT do 186: feito**; Fernanda confirmou `Sem movimento` na guia ISSQN de 26, 209, 237 e 258.
- [x] Planejamento do fechamento de outubro registrado (`PLANO_FECHAMENTO_10-2026.md`).

### 03/10/2026
- [x] DecWeb 09/2026: 22 de 22 enviadas (186 em 04/10). 173 NÃO é sem guia: Sociedade de Profissionais, guia 422,87.
- [x] Portal Nacional rodado para os 19 clientes com certificado; `conciliacao.py` criado e rodado.
- [x] 265: declaração enviada e fila processada; capital resolvido (R$ 5.980.000,00); cadastro via extensão do Chrome.
- [x] Prazos de ISSQN de Porto Alegre corrigidos para 13/10 (46 linhas).

### 01–02/10/2026
- [x] DecWeb: 16, 18, 117, 133 (01/10) e Tacom 138 e 263 (02/10); guia do 263 (R$ 4.089,69) enviada pelo G-Click. Guias ISSQN enviadas e na Controle: 16 (422,87), 18 (42,00), 152 (461,69), 173 (422,87), 177 (530,40), 186 (422,87), 189 (634,31), 238 (609,54), 241 (2.403,15), 263.
- [x] Bug de sessão do Portal Nacional corrigido; `portal_config.py` renomeado; certificados verificados (19 com, 11 sem). Aba Set2026 criada (320 linhas).

### Regras e memória registradas
- [x] Guia só vira `Enviado` com envio comprovado pelo G-Click; declaração da prefeitura é comprovada pelo recibo/protocolo/DMS.
- [x] Tacom de Porto Alegre sempre primeiro; Lopes & Nadal (186) após os documentos, ISSQN junto com os demais impostos quando possível.
- [x] Domínio considera a **data de saída** das notas (não a de emissão).
- [x] Registrar a memória a cada rodada: este arquivo + `PROCESSO_FECHAMENTO_09-2026.md` + snapshot datado no Drive.

---

## J. REVISAR APÓS OS FECHAMENTOS: Reforma Tributária (IBS/CBS) e cadastros no Domínio (registrado em 06/10/2026)

- [ ] **URGENTE Tacom 138, SPED Fiscal 09/2026 (conferir antes da Leidislaine transmitir, até 08/10):** o arquivo gerado em 06/10 traz só 6 NF-e (C100: 4 retornos CFOP 2.916 e 2 remessas CFOP 6.915). As 4 compras CFOP 1.556 que estão no Domínio e no SEFAZ (ZRZ 4917, Fortpel 1558521, Beller 23640 e 10504, R$ 657,96, acumulador 106) não estão no SPED (em agosto a compra de uso e consumo CFOP 2.556, acumulador 206, entrou). Verificar a configuração do acumulador 106 e gerar de novo; avisar a Leidislaine.

Pedido da Fernanda: registrar tudo o que faltou configurar sobre a reforma para ser revisado depois do fechamento, sem pressa agora.

**Tacom 138 (e 248/263): fiscal é tratado pela matriz; alertar a equipe da matriz**
- [ ] Avisar a matriz: remessas para conserto 4698 e 4699 (Tacom Sistemas, 01/09 e 22/09, R$ 40.161,90) saíram com IBS/CBS (CST 000 / cClassTrib 000001; IBS R$ 40,17 e CBS R$ 361,46), enquanto os retornos 33132, 33166, 33188 e 33204 (Tacom Projetos MG, R$ 25.949,40) vieram sem grupo IBS/CBS. Verificar se o destaque nas remessas está correto.
- [ ] Domínio, cadastro de produtos: preencher CST/cClassTrib de IBS/CBS dos produtos 12805, 12806, 17055, 20932 e 21353 (advertência "cClass Trib inválido"); classificação correta de retorno de conserto a confirmar com o Fiscal.
- [ ] Domínio, produto 20932 (POS TACOM GPOS700, NCM 8471.90.19): preencher o CEST (XML traz 2103400; confirmar o código).
- [ ] Domínio, acumulador das compras CFOP 1.556 (Beller 10504 e 23640): relacionar PIS/COFINS ou limpar PIS/COFINS da guia Estoque dos produtos, conforme o regime/uso (a definir).
- [ ] Domínio, acumulador 800 (serviços tomados): relacionar os impostos 183-IBS e 184-CBS; criar acumulador separado para CST 410 / cClassTrib 410999 (ex.: Unifique, suporte 010701).
- [ ] Decidir o que fazer com NFS-e de valor R$ 0,00 (Pluxee 8803672 e 8803674): o Domínio avisa "valor contábil zerado".
- [x] Tomados NFS-e de 09/2026 (Tacom 138) conciliados em 06/10: 9 NFS-e da prefeitura = Domínio, R$ 28.980,50; critério de competência = campo dCompet do XML (decisão da Fernanda). Pendente: conferir INSS retido R$ 175,30 da Ellu's 1353 no Domínio e decidir o R-2010 do 138 (conferir também a Ellu's 1317 de agosto); relacionar 183-IBS/184-CBS no acumulador 800; Unifique 443812 está no acumulador 1007 (CST 410).
- [ ] Unifique 460991, VOJ 41 e Ellu's 1387 (INSS retido R$ 175,30) são de outubro: lançar no fechamento de 10/2026.
- [ ] **Tacom 138, ajustar após o fechamento (INSS retido, registrado em 06/10/2026):** a Tacom é apurada pela matriz, mas é preciso ajustar no Domínio o acumulador de serviços tomados da Ellu's 1353 (cód. 170501, mão de obra, 01/09/2026, R$ 1.593,68) para registrar o **INSS retido de R$ 175,30 (11%)**; conferir se a Ellu's 1317 de agosto teve a mesma retenção; alertar a matriz sobre o R-2010. Fazer junto com os cadastros de produtos e as demais advertências desta seção.

**Demais clientes**
- [ ] 126: acumuladores de tomados com IBS/CBS (Facebook, Clinicorp, Ambientuus, Ideal Art 200/200029); base IBS/CBS = valor − ISS − PIS/COFINS destacados; importar saídas 1760 a 1841.
- [ ] 71: acumuladores de tomados por código de serviço (arquivo `ACUMULADORES_71_09-2026.md`: 13 notas com IBS/CBS, CST 000/000001 e 200/200052); nota 60 Laura de Luca aguardando retorno da Francine; Caixa Cartões 30774046 valor zero; Chanfro nº 2 (competência 08, IRRF 42,00 + CRF 130,20) conferir; local de execução da nota 153 (RIPA).
- [ ] 189: acumulador de tomados sem IBS/CBS (nota 5 Xavantina); decidir CRF 4,65% e confirmar data de pagamento e código do IRRF (R-4020 já enviado).
- [ ] Geral: padronizar acumuladores de serviços tomados por tipo (com IBS/CBS integral, com redução 200052, sem incidência 410, sem dados), transformar em skill para outubro.

---

## Como manter este documento
1. Ao fim de cada rodada: mover o item de PENDENTE para RESOLVIDO (com a data) ou ajustar o texto; acrescentar o que surgiu.
2. Atualizar o log detalhado em `PROCESSO_FECHAMENTO_09-2026.md`.
3. Salvar o snapshot `PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` na pasta do Drive e dar `git push`.
4. Conferir a planilha Controle_Fiscal antes de repetir uma pendência (a Fernanda pode já ter colado o TSV).
