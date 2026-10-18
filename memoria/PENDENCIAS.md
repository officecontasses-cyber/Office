# Pendências e resolvidos — OfficeCont (Fechamento Fiscal)

Documento vivo. **A cada rodada:** atualizar este arquivo (o que foi feito e o que falta), o log detalhado
`PROCESSO_FECHAMENTO_09-2026.md` e salvar o snapshot `PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` na pasta
`ARQUIVOS EXTENSÃO - CODE - CLAUDE` do Drive (regra da Fernanda, 02/10 e 04/10/2026).
Última atualização: **09/10/2026 (recibos SPED 138/248 e retificadora do 138 anotada na seção J); antes: 06/10/2026, noite (rodada de 05 e 06/10 registrada na seção K, logo abaixo).**

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
- [ ] **SPED Fiscal 09/2026 transmitido em 07/10 (provavelmente sem as 4 NF-e** de compra CFOP 1.556; retificadora pós-fechamento, ver seção J) (R$ 657,96, acumulador 106). Regerar e conferir antes de a Leidislaine transmitir (até 08/10); `SPED ICMS - Envio arquivo` fica `Pendente` até lá. Depois, `SPED ICMS (Recibo)`.
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
- [ ] **Apuração de 10/2026 (novembro) — RF Consultoria (cliente 2, a confirmar):** Ricardo Fernandes (RFS) confirmou por e-mail em 09/10/2026 que a partir de 10/2026 a receita de aluguéis **não é mais valor fixo**, e sim o **faturamento mensal**. Pedir o valor do mês ao cliente antes de apurar; não usar o valor fixo dos meses anteriores; conferir com as notas/recibos e refletir em FAT, PIS/COFINS e demais obrigações do mês. (A mensagem original da Júlia e a imagem colada no e-mail não foram vistas por mim: confirmar o cliente e o contrato/valor anterior.)

### A. SEGUNDA 05/10, PRIMEIRO HORÁRIO (mensagens e ligações; textos prontos em `RASCUNHOS_2026-10-05.md`) — (?) a Fernanda não informou o resultado; confirmar
- [ ] **Antes das 11:00: ligar para a Leidislaine (Tacom)** e combinar o acesso à máquina dela (e-mail sem retorno até 03/10). SPED Fiscal da Tacom: a Fernanda prometeu os arquivos até **qua 07/10** (ela transmite até 08/10). (?) vale para 138, 263 ou ambas?
- [x] (resolvido em 12/10, ver seção B) **257 (WhatsApp + e-mail, seção 1):** perguntar se a Lifecombr (nota 31, R$ 130.000,00, item 10.05) deveria ter retido o ISS de R$ 6.500,00 (guia vence 13/10).
- [ ] **E-mail ao Gian, 152 (seção 2):** ISS de Florianópolis (nota 6940 da Litoral Serviços Automotivos, R$ 42,00, incidência Florianópolis/SC, ISS 0,00 no Portal): recolheram ou ele já tem acesso lá? Gian é interno (responsável contábil nos cadastros de São Leopoldo), não contato do cliente.
- [ ] **Gian, 265:** liberar a **procuração eletrônica** (REINF deu erro 15 no Domínio); conferir no OWA (Itens Enviados) se o e-mail sobre o certificado do 258 (vence 14/10) foi enviado (rascunho de 03/10).
- [ ] **Inês (seção 5):** pedir o movimento de setembro de **18, 177 e 133** (pasta `001_DOCUMENTOS DIGITALIZADOS` > `09_SETEMBRO` vazia nos três; e-mail dela não conferido daqui) e perguntar se a **Datasys** reteve imposto nas notas de 29/09 (18: nº 11, R$ 2.100,00; 177: nº 13, R$ 26.520,00). 133: nota tomada nº 18 de MEI, R$ 300,00.
- [ ] **Cliente 2 RF Consultoria (seção 4):** cobrar as notas da **Freire Administração e Serviços Prediais** (nº 14263 de 14/09 e nº 14320 de 28/09, R$ 1.142,85 cada, total R$ 2.285,70, sem ISS; nenhuma é da Officecont); duas notas idênticas no mês, pedir confirmação e se houve retenção.
- [ ] **11 clientes sem certificado (seção 3):** pedir a relação das notas recebidas de setembro e se houve retenção federal (só federal): 2, 18, 26, 133, 138, 173, 177, 185, 209, 248, 263. Tacom (138, 248, 263) apura pela matriz: só interessa quando houver retenção municipal. Provisoriamente entram como sem retenção/sem movimento no REINF.

### B. ISSQN de 09/2026 — Porto Alegre (DecWeb, 22 de 22 enviadas; guias vencem 13/10)
- [x] **205 (R$ 1.915,06):** G-Click 09/10/2026 17:48 (Guia ISS + Envio ao cliente, fernanda.officecont); TSV `Enviado` entregue. Falta conferir o REINF do 205 (R-2099 não consta na lista de enviados). (nota 197 é a substituta da 196; `conciliacao.py` já corrigido.)
- [x] **155 Mainieri (08/10):** retificadora 1 enviada (recibo 08/10 09:39:11, receita R$ 22.676,34, ISS R$ 907,02); guia nova R$ 907,02 (venc. 13/10) com G-Click 10:11 e envio ao cliente 10:12; TSV Enviado entregue. FAT2026 L4 = 22.676,34 a digitar (L14 já calcula 4%). A guia antiga de R$ 842,02 não vale. FAT de agosto (K4 22.477,87) conferida pela Fernanda em 08/10: está OK, sem retificadora.
- [x] **257 (R$ 6.500,00):** resolvido em 12/10/2026 (Fernanda): guia ISSQN gerada e enviada ao cliente, G-Click Guia ISS e Envio ao cliente 12/10/2026 09:56 (fernanda.officecont), venc. 13/10; guia ficou como estava (sem alteração de valor). TSV `Enviado` R$ 6.500,00 entregue. A etiqueta "Ret" vermelha ao lado da Guia ISS no G-Click não foi explicada.
- [ ] **152:** ISS retido total R$ 568,44 = R$ 461,69 POA + **R$ 106,75 Estrela/RS** (ENGI PROJECT, notas 1146 e 1218): **fazer junto com a Fernanda no portal de Estrela** (baixar as notas e declarar); marcar horário. Em agosto foram R$ 25,63 (venc. 23/09).
- [ ] **2 RF Consultoria:** guia ISSQN em branco (não confirmado) até a resposta do cliente. **247 Montenegro:** DMS fora do DecWeb.
- [ ] Rodrigo Tavares Lopes (mesmo CPF) consta como profissional nos clientes 16 e 173: conferir.
- [ ] 155: 63 notas de 08/2026 geradas entre 31/08 e 03/09; sem indício de furo, mas agosto inteiro não foi conferido.
- [ ] Município sem prazo de ISS cadastrado: Brasília, Rio de Janeiro, Novo Hamburgo, São Sebastião do Caí, Montenegro, Palhoça.

### B2. 257 B2B: conciliação de 09/2026 (12/10/2026): revisar no fechamento e avisar o cliente
- [x] Conferido: ISS prestados (Domínio = Portal = DecWeb; guia R$ 6.500,00 enviada G-Click 12/10 09:56); NF-e da 3C Plus (SEFAZ = XML = Domínio; CST 41, imunidade de livro, ICMS 0); apuração ICMS (saldo credor R$ 2.866,13); **CSRF resolvida** (item 10.05: sem previsão legal; Telefônica correta, IRRF 1,5% DARF 8045); **FAT digitado e conferido pela agente em 12/10** (setembro e 3º tri batem com o Domínio: IRPJ R$ 19.321,38, CSLL R$ 10.355,32, ISS R$ 6.500,00).
- [ ] **AVISAR O CLIENTE (rascunho em `RASCUNHOS_2026-10-12.md`):** a Lifecombr (CNPJ 41.583.240/0001-43; Simples até 31/12/2025, excluída, não optante em 2026) **não reteve o IRRF 1,5% da nota 31 (R$ 130.000,00; R$ 1.950,00)** a pedido dela; a retenção cabia à fonte pagadora (art. 718 Decreto 9.580/2018; dispensa só se o prestador fosse Simples). Efeito no 257: sem crédito, paga R$ 1.950,00 a mais em caixa no DARF do IRPJ (30/10; pode ir em até 3 quotas, confirmar). Pedir que guarde por escrito a instrução da Lifecombr. Cliente informou que a Lifecombr não quer reter; (?) confirmar o regime atual dela (Consulta Optantes).
- [ ] **Revisar no fechamento (e no de outubro):** (a) tomados 1025 (Officecont, R$ 1.518,00, Simples) e 347 (Guinter, R$ 1.300,00, Simples) só no Domínio: rodar o Portal e o DecWeb de novo (comandos entregues em 12/10: `portal_nacional_download.py --competencia 09/2026 --clientes 257`, depois `decweb_login.py ... --fase 1 --clientes 257 --retificadora`; envio só `--fase 2 --retificadora --enviar` e `--fase 3`, depois de conferir o Total a recolher); (b) CFOP 2.102 das 3 NF-e de e-book (R$ 8.755,80): revenda ou uso/consumo (2.556)? nota de R$ 7.500,00 para um e-book, perguntar ao cliente; (c) faltam o demonstrativo de PIS/COFINS (DARF 23/10; estimativa PIS R$ 944,13 e COFINS R$ 4.357,52), Retenções a Recolher e as saídas do SEFAZ; (d) **ICMS: Guia ICMS (vence 13/10), GIA RS e SPED ICMS (15/10) em branco na Controle** (Domínio: saídas sem movimento, ICMS a recolher 0); (e) IBS/CBS das tomadas (R$ 12,07 CBS, R$ 1,34 IBS): acumulador 800, já no pós-fechamento; NFS-e emitidas 31 e 32 sem grupo IBS/CBS: confirmar obrigatoriedade; (f) jul e ago do trimestre conferidos só pelo FAT (sem Emitidas desses meses no Portal).
- [x] **257, IRPJ/CSLL do 3º tri liberados (12/10):** planilha `CONTROLE | Rendimentos` (aba `3ºTRIM 2026`, linha 21): LIBERADO FISCAL = **Zerado** (sem rendimento de aplicação; FAT com rendimentos 0,00 e IRRF s/ resgates 0,00) e FAT atualizado. Valores para o DARF de 30/10: IRPJ (2089) R$ 19.321,40 e CSLL (2372) R$ 10.355,32 (valor do Domínio, que usa a retenção nota a nota; o FAT dá R$ 19.321,38). Quotas (até 3, cada uma ≥ R$ 1.000): confirmar com o cliente e juros Selic nas quotas 2 e 3. Falta: gerar os DARFs, subir no G-Click e só então `Enviado`.
- [ ] **257, ATUALIZAÇÃO 12/10 (tarde), conciliação final:** (1) **Retificadora 1 do DecWeb enviada em 12/10/2026 11:10:57** (receita R$ 145.250,72; total R$ 6.500,00; tomados: 15 notas = Portal re-baixado 12/10 11:01 = Domínio, R$ 6.509,23; 347 e 1025 entraram; data de prestação 11/09 e 30/09 explica a data de entrada do Domínio). **Guia nova R$ 6.500,00 (cód. arrecadação 328521610019293, gerada 12/10 11:11, venc. 13/10) substitui a de 03/10 (cód. …207), que foi a enviada no G-Click às 09:56: subir a guia nova no G-Click e enviar ao cliente HOJE** (linha GUIA ISSQN da Controle deve ficar `Pendente` até lá; DECLARAÇÃO PREFEITURA já é a Retificadora 1). (2) **NFS-e 33 (05/10, Lifecombr, R$ 70.000,00, ISS R$ 3.500,00 não retido, competência 10/2026 mas descrição "COMPETÊNCIA DE VENDAS SETEMBRO/26") apareceu nas Emitidas de 12/10:** definir a competência antes de liberar IRPJ/CSLL do 3º tri. Cenário A (outubro, como emitida e como o Domínio lança): IRPJ R$ 19.321,40 e CSLL R$ 10.355,32. Cenário B (setembro): IRPJ R$ 24.921,40 (+5.600,00) e CSLL R$ 12.371,32 (+2.016,00); PIS/COFINS de setembro +R$ 455,00 e +R$ 2.100,00; ISS da competência mudaria. Sem IRRF também nessa nota (R$ 1.050,00 se a Lifecombr devesse reter). Decisão da Fernanda com o cliente. Aviso: a conclusão "IRPJ/CSLL liberados" de 12/10 mais cedo vale só para o cenário A.
- [x] **257, decisões e conferências de 12/10 (fim do dia):** (a) Fernanda: o cliente apura por competência; NFS-e 33 (R$ 70.000,00, comp. 10/2026) **não entra em 09/2026** (cenário A): IRPJ R$ 19.321,40 e CSLL R$ 10.355,32 liberados; PIS R$ 944,13 e COFINS R$ 4.357,52 (Demonstrativo EFD PIS/COFINS do Domínio = FAT, base R$ 145.250,72, CST 51, sem retenção). (b) Domínio ajustado para CFOP 2.556/acumulador 206 nas 3 NF-e de e-book; SPED Fiscal 09/2026 do 257 gerado (`004 ARQUIVOS ICMS`): perfil A, original, 3 C100 (11678, 11693, 12175; chaves = SEFAZ/XML), CFOP 2556, CST 041, ICMS 0, E110 saldo credor R$ 2.866,13 mantido. A conferir antes de transmitir: `0200` EBOOK-01 com TIPO_ITEM 00 (mercadoria para revenda) enquanto o CFOP é 2556 (uso/consumo): ajustar para 07 no cadastro do produto; E115 `RS000032` R$ 7,00 e `RS000033` R$ 22.506,68 (significado não confirmado). (c) Próximos vencimentos do 257: Guia ICMS 13/10 (`Sem movimento`, ICMS a recolher 0), GIA RS e SPED ICMS 15/10, DARF PIS/COFINS 23/10, IRPJ/CSLL 30/10.
- [x] **257, ICMS fechado (12/10, Fernanda enviou e salvou):** SPED Fiscal 09/2026 recebido pelo SERPRO em 12/10/2026 11:35:10 (perfil A, original; hash 8169315CCD5934D755FF26FE97750CF3; ICMS a recolher R$ 0,00; saldo credor R$ 2.866,13); GIA RS 09/2026 transmitida 12/10/2026 11:38:39, protocolo TED 13573925 (comprovante provisório; recibo definitivo na caixa postal da SEFAZ, salvar depois). SAÍDAS: `Sem movimento` (Fernanda). Hash do .txt do Drive não foi conferido com o do recibo.
- [ ] **PÓS-FECHAMENTO, 257:** ajustar no Domínio o cadastro do produto EBOOK-01 (TIPO_ITEM `07` uso e consumo, hoje `00` revenda, coerente com o CFOP 2.556/acumulador 206); o SPED saiu com `00`: só avaliar retificadora se o PVA/SEFAZ apontar. Conferir também o E115 `RS000032` R$ 7,00 e `RS000033` R$ 22.506,68 (significado não confirmado).
- [x] **257, TSV de impostos apurados e validados (12/10):** PIS R$ 944,13 e COFINS R$ 4.357,52 (venc. 23/10); IRPJ R$ 19.321,40 e CSLL R$ 10.355,32 (venc. 30/10; quotas a confirmar): linhas `DARF` ficam `Pendente` com o valor até haver G-Click.
- [ ] Regra da Fernanda: conferir sempre IRPJ/CSLL no FAT do cliente (e a planilha `CONTROLE | Rendimentos`, coluna LIBERADO FISCAL, antes de liberar IRPJ/CSLL) (skill atualizada na cópia do repositório). No FAT do 257, `L9` e `L10` são fórmulas que supõem retenção total: sobrescrever quando a retenção for parcial.

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

- [ ] **PÓS-FECHAMENTO, Tacom 138: provável RETIFICADORA do SPED Fiscal 09/2026 (registrado em 09/10/2026).** A Leidislaine transmitiu em **07/10/2026 10:13:48** (recibo `138_Tacom_PortoAlegre_09.2026_ReciboSPEDICMS.pdf`, hash 20AF8EEFF931734B8EE356D16599A157, saldo credor R$ 17.385,19). O `.txt` do Drive (06/10 18:06) tem só 6 NF-e e **não tem as 4 compras CFOP 1.556** (R$ 657,96, acum. 106). Hash do `.txt` não foi calculado: se foi esse arquivo, o SPED saiu sem as compras e precisa de retificação (confirmar com a Leidislaine qual arquivo ela transmitiu). Fazer depois do fechamento: acertar o acumulador 106, regerar, pedir a retificadora e registrar o novo recibo. TSV do recibo entregue com essa ressalva.
- [ ] **PÓS-FECHAMENTO, Tacom 248: lançar a NF-e 123 e avaliar retificadora do SPED ICMS 09/2026 (registrado em 09/10/2026).** SPED transmitido em 07/10/2026 10:23:16 (hash 2F1C93028E7F35F11C60662CE06B7440), sem nenhuma NF-e e com tudo R$ 0,00. A NF-e 123 (Leonardo Alves Sebastião ME, 14/09/2026, R$ 15,00, ICMS 0) ficou de fora. Depois do fechamento: lançar a nota no Domínio, avaliar com a Leidislaine se precisa de retificadora e só então fechar `ENTRADAS` e `GUIA ICMS` do 248.
- [x] (histórico) Tacom 138, SPED Fiscal 09/2026 (era urgente até 08/10; transmitido em 07/10, ver item acima): o arquivo gerado em 06/10 traz só 6 NF-e (C100: 4 retornos CFOP 2.916 e 2 remessas CFOP 6.915). As 4 compras CFOP 1.556 que estão no Domínio e no SEFAZ (ZRZ 4917, Fortpel 1558521, Beller 23640 e 10504, R$ 657,96, acumulador 106) não estão no SPED (em agosto a compra de uso e consumo CFOP 2.556, acumulador 206, entrou). Verificar a configuração do acumulador 106 e gerar de novo; avisar a Leidislaine.

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

- REINF 205 (09/2026): R-2099 enviado com sucesso, recibo 12260744-01-2099-2609-12260744, 12/10 11:49. Pendente: G-Click e conferir cadastro duplicado '1205' no Domínio. Próximos: 238, 152, 71, 227, 265.

- 238 REAT (REINF 09/2026): conciliado Portal x Prefeitura x Domínio; Domínio só tem a nota 19764. Lançar as outras 7 notas no Domínio (STV 20038, Prime System 493/494 etc.), reexportar Retenções a Recolher e depois R-4020 (CRF/IRRF), R-2010 (INSS Prime System) e R-2099. Ver log 28q.

- REGRA (12/10/2026): antes de montar REINF/retenções de qualquer cliente, conciliar Domínio x Portal Nacional x Prefeitura.
- PÓS-FECHAMENTO 238: acumuladores 1005/1006 sem IBS/CBS (notas 20038, 21748, 21806) e data de entrada da nota 555002 (Telefônica). Ver log 28r.
- 238 REINF: conferir pontos (1) a (6) do log 28r, depois R-2010, R-4020 e R-2099.

- Skill nova (12/10/2026): conciliacao-retencoes-servicos-tomados (repo: .claude/skills/conciliacao-retencoes-servicos-tomados/SKILL.md). Tabela 01 de naturezas NÃO foi incluída (fonte oficial inacessível no ambiente); completar com a tabela vigente da Receita.
- 238 REINF: conferir IRRF na nota Atlas (natureza 15044 inclui IR 1708) e tipos de serviço do R-2010 (493 -> 100000025; 494 -> 100000001) na tabela vigente. Ver log 28s.

- REGRA (12/10/2026, Fernanda): sempre que criar/atualizar uma skill, copiar o arquivo para a pasta ARQUIVOS EXTENSÃO - CODE - CLAUDE do Drive, com o NOME DA SKILL (ex.: conciliacao-retencoes-servicos-tomados.md). Já no Drive: conciliacao-retencoes-servicos-tomados.md (id 1MgXNeMeJFgFM1z7Vnl0pFnnXM5Dst-lB); conciliador-tributario-fiscal está como SKILL.md (id 1DTjkH9VeUwSG2mGL1dxVZ1HoDnBWXvBd), renomear se ela quiser.
- 238 REINF: relatório de conferência OK; falta recibo (R-2010, R-4020, R-2099) para TSV; DARF 5952 R$ 141,86 e IRRF 1708 R$ 17,75 (venc. CSRF 20/10); INSS R$ 1.295,45 via DCTFWeb. Ver log 28u.
- 238 REINF ENVIADO 12/10 13:49 (recibos no log 28v). Faltam: DARF 5952 (20/10), IRRF 1708, INSS via DCTFWeb, recibo no G-Click, declaração Simples Prime System, cadastro '1238' x '238' (e '1205' x '205') no Domínio.
- Skill conciliacao-retencoes-servicos-tomados atualizada (12/10/2026): seção 10 Pós-transmissão (Controle_Fiscal + planilha do DP), regras LeFisc (CSRF limite R$10 por pagamento, venc. 2º decêndio, Simples declaração, manutenção isolada). Drive: id 1mJyZhTVu1ZEVyYpf3NurUn7acVuCFXsM (versão antiga 1MgXNeMe... enviada à lixeira).
- 71 REINF 09/2026: retenções conferidas (só nota 659 Giovani Gazen: IRRF 83,61 + CRF 259,20; sem INSS). Falta: confirmar data de pagamento, Chanfro nº 2 (comp. 08) em agosto, transmitir R-4020 + R-2099 + R-4099; ~39 notas do Portal ainda não lançadas no Domínio. Ver log 28x.
- 71 REINF ENVIADO 12/10 14:24 (log 28y). Faltam: DARF 1708 R$ 83,61 e 5952 R$ 259,20 (5952 até 20/10), recibo no G-Click, Chanfro nº 2 (comp. 08) conferir agosto, decidir status SERVIÇOS TOMADOS do 71.
- 71: 3 notas no Domínio sem Portal (nº 1/17/1030, R$ 3.155,00, emissão em outubro com entrada em setembro): rodar Portal Nacional 71 (09/2026) e decidir competência; Serviços Tomados 71 só após isso. Ver log 28z.

- CNPJs na Controle_Fiscal (12/10/2026): em Set2026 e Ago2026 a coluna B está numérica em 27 clientes; 5 perderam o zero à esquerda (13 dígitos): 26 Raldi 05.057.885/0001-89, 71 Conte 08.307.701/0001-80, 138 Tacom Sistemas FL RS 08.196.752/0002-62, 197 ASBBM 05.164.750/0001-12, 263 Tacom Projetos FL RS 01.005.845/0021-86 (todos com DV válido ao completar o zero e iguais ao Cadastro_Clientes). Corrigir: formatar coluna B como texto ou formato personalizado 00"."000"."000"/"0000"-"00. Cliente 227 Progest está nas abas mas NÃO está no Cadastro_Clientes. Jul2026 e Cadastro_Clientes estão em texto (ok).
- 71 (Portal rodado 12/10): lançar no Domínio nº 2 Monique (R$ 1.272,82) e a nota da Laura de Luca que falta (nº 60 ou 61, R$ 2.500,00); ajustar entrada das notas 1, 17 e 1030 (entrada < emissão). Depois Serviços Tomados 71. Log 28aa.
- REGRA (13/10/2026, Fernanda): o que vale é a COMPETÊNCIA da nota. Advertência do Domínio 'data de entrada inferior à emissão' é esperada quando a nota tem competência do mês fechado e foi emitida depois (ex.: 71 notas 1, 17 e 1030, competência 09/2026 emitidas em outubro): NÃO ajustar a data de entrada. Só nota com emissão e entrada no mesmo mês (ex.: Telefônica 555002 do 238) pode ter a data ajustada, no pós-fechamento.

- PÓS-FECHAMENTO 71 (13/10/2026, pedido da Fernanda): notas **2 Monique de Azevedo Chaves (R$ 1.272,82, 07/10, chave 33045572267662436000117000000000000226100125049818)** e **61 Laura de Luca Baccarin (R$ 2.500,00, 06/10, chave 43149022245454954000102000000000006126100693472954)**, competência 09/2026 no Portal, ainda NÃO lançadas no Domínio (XML não encontrado; SIEG sem pasta Outubro). Serviços Tomados do 71 fica Pendente; a Fernanda revisa depois do fechamento. Sem retenção federal nessas notas. Não importar o XML 2_P_4625 (P. Marques, competência 10/2026).
- ESTILO (13/10/2026, Fernanda): em mensagens e textos, REINF no feminino: 'a REINF' (não 'o REINF').

- [ ] **152 (14/10/2026):** Domínio (Retenções a Recolher) x planilha do Gian conciliados: códigos 6190 5.680,81 / 6147 141,25 / 6188 40,00 / 6228 55,91 / 6230 36,34 / 6243 167,73 / INSS 1162 1.269,26 batem. Em aberto: Life Card 159 (704,59 x 131,40), Realize 3279 (natureza 17032 x 17031), J. Ronier (17003 x 17099), Volpmann 42703 (competência) e 48337, nota 741590. Depois: REINF e TSV da caixa do DP. Ver log 28ac.
- [ ] **152 (14/10, decisões):** corrigir no Domínio Life Card 159 (BC 131,40); Realize 3279 é PORTARIA (natureza a definir, não 17031/17032); Volpmann 48337 com retenção federal 35,59 (IRRF 18,07 + contribuições 17,52) fora do Domínio/planilha: confirmar pagamento em setembro e lançar; ISS PoA 461,69 confere com a Declaração Mensal. Ver log 28ac.
- [ ] **152 (14/10, decisões finais):** Volpmann 48337 ignorada (não paga; outubro). Ajustar no Domínio: Life Card 159 (BC 131,40) e Realize 3279 (natureza 17031); reexportar Retenções a Recolher; depois transmitir R-2010/R-4020/R-2099/R-4099 (venc. 15/10) e TSV da caixa do DP (total 7.391,30).
- [x] **152 REINF enviada 14/10/2026 19:36** (recibos no log 28ad). [ ] Fernanda colar os 2 TSV (Controle_Fiscal e DP) e rodar os scripts; [ ] salvar o relatório de conferência da 152 para checar valores por evento; [ ] status de Serviços Tomados da 152 (confirmar); [ ] DP gerar as guias (DARF das retenções e INSS na DCTFWeb); [ ] REINF de outubro: Volpmann 48337 (retenção federal 35,59 se paga).
- [x] **152 REINF conferida pelos totalizadores da Receita (R-2099 e R-4099) = Domínio = planilha do Gian.** [ ] 741590 (Rede OK) e 255/4517: verificar pagamento em outubro para a REINF de outubro.
- [ ] **152 (17/10):** Fernanda colar o TSV de Serviços Tomados `Importado` na Atualizações e rodar `processarAtualizacoes()`; confirmar se o TSV da caixa do DP (7 linhas) já foi colado/rodado (`processarAtualizacoesReinf()`).
- [x] **Snapshot 17/10/2026 salvo no Drive** (`PENDENCIAS_E_RESOLVIDOS_2026-10-17.md`, id 1hx_EYkZfz3W9B7mUUwX61EovJ3tzMiIW, pasta ARQUIVOS EXTENSÃO - CODE - CLAUDE). Dossiê do cliente 2 criado: `CLIENTE_002_RF_CONSULTORIA.md` (gatilho "fechamento da empresa #2", linha no CLAUDE.md).
- [ ] **#2 RF Consultoria 09/2026 (17/10):** Freire sem nota (não lançável); rodar retificadora DecWeb para incluir Officecont 1050 (comando entregue) e enviar o novo recibo; localizar no e-mail se já cobrou o Ricardo (prompt entregue); TSV tomados `Pendente` 3.165,00 e TSV prestados/aluguel/DARFs entregues (Fernanda cola).
- [ ] **#2 RF Consultoria (17/10 noite):** retificadora DecWeb enviada (recibo 17/10 12:48:07); tomados válidos R$ 2.022,15 (Freire 14320 cancelada); guias PIS/COFINS 802,20 e IRPJ/CSLL 5.063,73 geradas, falta G-Click; abrir PDFs da Freire (confirmar nota 14263 e a 13882 de agosto, descrição e retenção); Fernanda cola o TSV consolidado (log 28ak).

- **#16 Qualidente 09/2026 — Entradas (17/10):** 4 XMLs conferidos, valores batem (14.596,54). Pendente: decidir o crédito de ICMS R$ 42,57 da NF 76043 (Biodental, acum. 206) e créditos IBS/CBS (pós-fechamento).

- **#16 IBS/CBS (17/10):** prestados e entradas OK no Domínio. Pendente: relacionar o acumulador 800 (serviços tomados) a IBS/CBS para entrarem créditos CBS 6,64 / IBS 0,74. **Regra nova:** "fechamento da empresa #N" sempre confere IBS/CBS (Portal/XML x Domínio) — ver CLAUDE.md.

- **#16 IBS/CBS (17/10, após ajuste do acum. 800):** resolvido, com diferença imaterial de R$ 0,02 (IBS) / R$ 0,14 (CBS) por base (valor contábil x BC do Portal). Seguem pendentes do #16: guias PIS/COFINS e IRPJ/CSLL no G-Click, FAT set, correção da DARF PIS de agosto.

- **#16 guias (17/10):** PIS/COFINS 5.206,46 (23/10) e IRPJ/CSLL 40.128,89 (30/10) conferidas, sem divergência. Pendente: subir/enviar no G-Click e comprovar (status das DARFs fica `Pendente` até lá).

- **#16 guias ENVIADAS (17/10, G-Click 18:11):** PIS/COFINS e IRPJ/CSLL concluídas. Resta no #16: FAT set e correção da DARF PIS de agosto (770,94).

- **#16 concluído (17/10):** FAT set e correção da DARF PIS de agosto feitos (Fernanda). Nada pendente do #16 além do que já estava pós-fechamento.
- **#18 CC&D (17/10):** dossiê criado (`CLIENTE_018_CCD_INFORMATICA.md`). Em aberto: retenção da Datasys na nota 11 (R$ 2.100,00; pergunta à Inês desde 05/10), Domínio set, PIS/COFINS, IRPJ/CSLL 3º tri, REFIS 31,50 (30/10), IBS/CBS, SPED Contribuições.

- **#18 (17/10, Domínio conferido):** IRPJ 56,70 e CSLL 118,44 (3º tri, venc. 30/10) e REFIS 31,50 (30/10) a gerar; PIS/COFINS dependem da confirmação da retenção da Datasys na nota 11. Pendente: Entradas/Saídas do Domínio, XML da nota 11 (CST IBS/CBS e retenções), confirmar 16% de presunção do IRPJ (receita anual <= R$ 120.000), saldo credor de retenção PIS 48,95 / COFINS 225,00.

- **#18 (17/10, conferido):** retenção da Datasys confirmada (nota 11). Pendente: gerar guia IRPJ 56,70 + CSLL 118,44 (30/10); G-Click do REFIS 31,50 (guia gerada 17/10) e das guias de IRPJ/CSLL; conferir NF 1029 Officecont (474,80, emitida 05/10) nos tomados da prefeitura e no IBS/CBS; saldo credor de retenção PIS 48,95 / COFINS 225,00; SPED Contribuições set (16/11).

- **#18 REFIS enviado (G-Click 17/10 18:30).** TSV final do #18 aguarda o restante (IRPJ/CSLL, NF 1029 Officecont) por pedido da Fernanda.

- **#26 Raldi (17/10, preparado):** dossiê criado. Aguarda Domínio set e fontes para `Sem movimento` em tomados/prestados, DARF PIS/COFINS e IRPJ/CSLL (3º tri; conferir planilha Rendimentos); SPED set 16/11. Cadastro mostra IE "Baixada" (não contribuinte de ICMS).

- **#18 fechado, salvo Serviços Tomados (17/10):** TSV final entregue; IRPJ 56,70, CSLL 118,44 e REFIS 31,50 `Enviado` (G-Click 18:30/18:35). Pendente: NF 1029 Officecont (474,80) na prefeitura/IBS-CBS, saldo credor de retenção PIS 48,95 / COFINS 225,00, SPED Contribuições set (16/11).

- **#26 (17/10):** Domínio e DecWeb zerados; Portal Nacional não lido (sem certificado). Pendente: confirmar rendimentos 3º tri (planilha Rendimentos), decidir `Sem movimento` com ressalva do Portal, SPED set (16/11).

- **#18 retificadora (17/10 18:42:44) conferida:** tomados NF 1029 confirmada na prefeitura (474,80) -> `Importado`. Pendente: confirmar se a guia original de 42,00 (venc. 13/10) foi paga antes de decidir sobre a guia nova de 42,82; IBS/CBS da NF 1029; SPED set 16/11.

- **#71 (17/10, preparado):** dossiê `CLIENTE_071_CONTE.md`. Prestados `Importado` (conciliado); tomados dependem de lançar 2 notas (Monique 2, Laura 61); rendimentos 3º tri em branco (falta informe Bradesco); FAT set em branco; estimativa IRPJ ~104.929,63 / CSLL ~69.457,26 (venc. 30/10); IBS/CBS dos prestados sem dado no Portal (conferir XML).
- **#26:** Rendimentos 3º tri `Zerado` confirmado. **Regra:** sempre conferir a planilha `CONTROLE | Rendimentos` ao preparar a empresa.

- **#71 (17/10, Domínio regerado) ALERTA:** receita de set em dobro no Domínio (série 900 + série U); Resumo mostra PIS 7.091,99 / COFINS 32.732,25 / IRPJ 152.373,51 / CSLL 98.569,15 inflados. Corrigir e regerar antes de gerar DARF/TSV. Entradas ainda sem as notas 2 (Monique) e 61 (Laura); informe Bradesco 3º tri pendente.

- **#71 (17/10 22:xx):** Domínio corrigido (série U). Pendentes: lançar notas 2 (Monique) e 61 (Laura) (baixar XMLs do Portal e colar em `007 ARQUIVOS SIEG\_71`); rendimentos Caixa/Bradesco no Domínio (informe Bradesco); FAT set; conferir ADI 7936 (liminares sobre o +10%); IBS/CBS dos 41 XMLs restantes.
- **#117 (17/10):** tudo `Sem movimento` conforme prefeitura (baixa em andamento, sócio faleceu); TSV entregue; SPED set (16/11) a decidir (`Não se aplica`).

- **#71 (17/10 22:2x):** Resumo com rendimentos: IRPJ 104.929,65 / CSLL 69.457,20 (venc. 30/10; guias a gerar após liberar rendimentos/ADI 7936). Pasta `_71` sem os XMLs das notas 2 (Monique) e 61 (Laura): baixar do Portal pelas chaves (em `CLIENTE_071_CONTE.md`).

- **#71 (17/10):** XMLs das notas 2 e 61 conferidos (= Portal). Pendente: lançar no Domínio e regerar Entradas (esperado 469.779,47) e Resumo (créditos IBS 17,89 / CBS 161,13); informe Bradesco; guias IRPJ/CSLL.

- **#71 (17/10 22:25) conferido:** Entradas 469.779,47 = Portal; IBS/CBS = Portal; Prestados/Tomados prontos para `Importado`. Pendente: guias IRPJ 104.929,65 e CSLL 69.457,20 (30/10) após informe Bradesco/ADI 7936; G-Click; FAT set (receita 1.091.077,54, retenções); SPED set (16/11); pendências menores (RIPA 153, nota 60 Laura/Francine, Chanfro nº 2, Caixa Cartões zero, IOF mútuo).

- **#126 (17/10, preparado):** dossiê `CLIENTE_126_TATSCH_LEITE.md`. Pendentes: importar saídas 1760–1841 e regerar Domínio; FAT ago/set; IBS/CBS (XML dos prestados); DARF PIS/COFINS (23/10, ~998,81/4.609,87) e IRPJ/CSLL (30/10, ~23.289,40/10.544,19); créditos PIS 785,32 e COFINS 462,54 (PER/DCOMP); SPED set.

- **Regra nova (17/10):** ENTRADAS só de compra de produtos (NF-e/CT-e); sem NF-e no SIEG e no Domínio = `Sem movimento`. **#71 ENTRADAS = `Sem movimento`** (corrige TSV anterior).
- **#126 (17/10 22:4x):** Domínio regerado e conferido (ver dossiê). Pendente: abrir os valores dos 10 XMLs de NF-e e fechar créditos IBS/CBS; Portal novo p/ Facebook e Officecont 1056; DARF PIS/COFINS (23/10) e IRPJ/CSLL (30/10); créditos PIS 785,32 / COFINS 462,54; FAT ago/set; SPED.

- [ ] **126 IBS/CBS (17/10):** NF-e conferidas XML a XML (valores = Domínio); créditos do Domínio excedem os XMLs em IBS 1,56 / CBS 14,02 (acumulador/lançamento a identificar). ENTRADAS produtos 20.929,80 pronta para `Importado`.
- [ ] **126 (17/10, decisão da Fernanda):** IBS/CBS (divergência 1,56/14,02) fica para **depois do fechamento**. Fernanda vai **compensar PIS/COFINS** e atualizar o FAT 126; aguardar o aviso dela antes de gerar DARF PIS/COFINS (23/10), IRPJ (23.289,40) e CSLL (10.544,19) (30/10).
- [ ] **126 (17/10 noite):** compensação conferida (COFINS 09/2026 → DARF 3.093,09; PIS 998,81 integral, venc. 23/10; gerar/comprovar no G-Click). Fernanda cola ajustes no FAT (ISSQN set 3.073,23; aba Compensações zerada). Conferir nº do doc. de arrecadação do PER/DCOMP 003. IRPJ 23.289,40 / CSLL 10.544,19 (30/10). IBS/CBS depois.
- [x] **126 (17/10 20:34):** DARFs PIS/COFINS e IRPJ/CSLL cota 1 enviados no G-Click; TSV final entregue (PIS, COFINS, IRPJ, CSLL Enviado; Prestados e Entradas Importado). [ ] Pendentes 126: SERVIÇOS TOMADOS (OK da Fernanda ou novo export do Portal com Facebook 146442407 e Officecont 1056), cotas 2 e 3 IRPJ/CSLL (nov/dez, Selic), IBS/CBS pós-fechamento, nº do doc. de arrecadação no PER/DCOMP 003, SPED Contribuições set (16/11), certificado A1 vence 16/12.
- [ ] **126 SERVIÇOS TOMADOS (17/10):** Fernanda verifica depois do restante do fechamento; sem TSV até lá.
- [ ] **133 RFL (17/10, preparado, dossiê CLIENTE_133_RFL.md):** faltam Domínio 09/2026 e apuração Lucro Real (IRPJ/CSLL 3º tri); crédito de compensação só R$ 5,78 (set PIS 11,56 + COFINS 53,26 = 64,82: outro crédito ou DARF 23/10); **PIS 08/2026 (11,55) a confirmar**; 133 fora da aba 3ºTRIM de Rendimentos; Movimento RFL 09-2026.zip não aberto; SPED 16/11.
- [ ] **133 (18/10):** retificadora 1 do DecWeb (tomados 1.552,35) rodada; **PDF retificado ausente no Drive**; Domínio sem a NFS-e nº 18 MEI (300,00); falta Serviços_133 e balancete/LALUR p/ IRPJ/CSLL; PIS ago e crédito de set (ver acima).
- [ ] **133 (18/10):** retificadora 1 do DecWeb enviada à mão pela Fernanda (robô parou no modal 'Preparar Declaração para envio'); rodar fase 3 e conferir PDF (Retificadora 1, tomados 1.552,35).
- [ ] **133:** lançar no Domínio a NFS-e nº 18 (Shaiane MEI, R$ 300,00, paga 14/09, docs em 001 `Movimento RFL 09-2026`); depois regerar Entradas/Resumo.
- [x] **133 (18/10):** nota 18 lançada, Entradas 1.552,35 = DecWeb; retificadora 1 baixada (0,00). [ ] Regerar Resumo; PIS ago; crédito/DARF PIS-COFINS set (23/10); IRPJ/CSLL Lucro Real; SPED 16/11.
- [ ] **152 (18/10):** TSV Prestados `Sem movimento` e Entradas `Pendente` entregues; salvar `Entradas_152_092026.pdf` (e Saídas) do Domínio para conferir NF-e (50+ XMLs no SIEG, pasta Setembro) e fechar ENTRADAS. [ ] 133: TSV entregue (Tomados, Entradas, Prestados, Declaração); regerar Resumo; DARF PIS/COFINS, IRPJ/CSLL.
- [x] **133 PIS/COFINS 09/2026 (18/10 10:58):** guia 57,57 (COFINS 46,01 + PIS 11,56) enviada no G-Click; PER/DCOMP 29817.01875.181026.1.3.04-9972 (7,25). [ ] Corrigir nº da PerdComp na linha 028 do FAT; [ ] PIS ago a conferir; [ ] IRPJ/CSLL Lucro Real; [ ] SPED 16/11; crédito de 10/2024 esgotado (out em diante: DARF cheio).
- [ ] **152 (18/10):** Domínio Entradas/Saídas salvos: NF-e 38.874,53 (33 docs) + energia 331,18; Saídas = 4 devoluções 1.112,26. ENTRADAS aguarda decisão/conferência dos XMLs (SIEG Setembro) para `Importado`; PRESTADOS `Sem movimento` (anotar devoluções). IBS/CBS do 152 não conferido.
- [ ] **155 Mainieri (18/10, preparado, dossiê CLIENTE_155_MAINIERI.md):** falta Domínio 09/2026; corrigir ISSQN set no FAT (907,05 -> 907,02); reverificar agosto (63 x 62 notas); DARF PIS 147,40/COFINS 680,29 (23/10), IRPJ 3.307,90/CSLL 1.984,74 (30/10); certificado A1 vence 27/10.
- [ ] **133 IRPJ/CSLL (18/10):** dependem da liberação da contabilidade (Lucro Real); TSV `Pendente` entregue; venc. 30/10.
- [ ] **173 Lopes & Martins (18/10, preparado, dossiê CLIENTE_173_LOPES_MARTINS.md):** falta Domínio 09/2026; propostas: PRESTADOS/TOMADOS/DARF PIS-COFINS-IRPJ-CSLL `Sem movimento` (base zerada, rendimentos Zerado) após confirmar no Domínio; SPED 16/11.
- [ ] **155 (18/10):** Domínio conferido; pendentes: Imobzi 229513 (530,13) fora do Portal, IBS/CBS acumuladores 900/800, ISSQN set no FAT (907,05 -> 907,02), agosto 63 x 62 notas, DARFs.
- [ ] **173 (18/10):** DecWeb/Domínio analisados (receita 0, ISS 422,87); conferir valor 8,71 no Resumo; TSV Sem movimento depois da confirmação.
- [ ] **177 ILS (18/10, preparado, dossiê CLIENTE_177_ILS.md):** falta Domínio 09/2026 e confirmar retenções da Datasys na nota 13; FAT setembro em branco; IRPJ 2.625,48 / CSLL 1.495,73 esperados (30/10).
- [x] **155 (18/10):** Portal rodado de novo; Recebidas 4.334,21 = Domínio (Imobzi 229513 apareceu). TSV Prestados/Tomados Importado, Entradas Sem movimento entregue. [ ] DARFs, IBS/CBS pós-fechamento, FAT ISS 907,02, agosto 63 x 62, certificado 27/10.
- [x] **155 (18/10):** guias PIS/COFINS 827,69 e IRPJ/CSLL 5.292,64 conferidas e enviadas no G-Click; TSV entregue. [ ] IBS/CBS pós-fechamento, FAT ISS 907,02, agosto 63 x 62, certificado A1 27/10.
- [ ] **177 (18/10):** Domínio conferido (retenções Datasys confirmadas); [ ] DARF IRPJ 2.625,48 / CSLL 1.495,73 (30/10) a gerar e comprovar; [ ] Officecont 1037 (626,15) fora do DecWeb: retificadora?; [ ] FAT set a digitar; [ ] IBS/CBS pós-fechamento; SPED 16/11.
- [x] **173 (18/10):** TSV (seis `Sem movimento`) entregue.
- [ ] **185 (18/10):** Portal rodado (só Recebidas, Certisign fora de 09); FAT e Rendimentos (Sim) lidos; [ ] salvar Domínio 185 para conferir; [ ] Prefeitura (Fernanda libera); [ ] GMA taxa de administração; [ ] DARFs PIS 24,91/COFINS 114,98 e IRPJ/CSLL do 3ºTRIM (conferir com Domínio); [ ] IBS/CBS pós-fechamento.
- [ ] **185 (18/10):** Domínio conferido; PIS 24,91/COFINS 114,98 ok; [ ] corrigir presunção IRPJ/CSLL no Domínio (100% x 32%) antes das guias (30/10); [ ] GMA; Rendimentos = Sim; Prefeitura: ausência de movimento emitida.
- [x] **177 (18/10):** guia IRPJ/CSLL 4.121,21 gerada e enviada (G-Click 12:14); TSV `Enviado` entregue. [ ] Officecont 1037/Tomados, FAT set, IBS/CBS pós-fechamento.
- [ ] **177/185 (18/10):** TSV dos faltantes do 177 (Prestados, Tomados Pendente, DARF PIS/COFINS retenção integral) e 185 RECEITA ALUGUEIS entregue; aguardam colagem. 185 ainda: presunção IRPJ/CSLL no Domínio, GMA, DARFs PIS/COFINS com G-Click.
- [x] **185 (18/10):** Domínio corrigido (IRPJ 477,68; CSLL 353,62). [ ] guias PIS 24,91/COFINS 114,98 (23/10) e IRPJ/CSLL (30/10) com G-Click; [ ] CSLL a compensar 10,41; [ ] GMA. 177 e 185 TSV colados.
- [ ] **186 (18/10):** Controle Rendimentos 3ºTRIM 2026: LIBERADO FISCAL em branco (não liberado); obs.: "Solicitei outro formato de extrato de aplicações". IRPJ/CSLL do trimestre não fecha até liberar. 185: TSV IRPJ/CSLL Pendente colado, guias em andamento.
- [ ] **189 (18/10) preparado:** [ ] lançar NFS-e 45 (1.519.673,26) no Domínio; [ ] corrigir CSOC-RET (44/42) e cadastro do tomador; [ ] rendimentos financeiros no Domínio; [ ] FAT set; [ ] novo relatório Domínio; [ ] CRF 4,65% Xavantina; [ ] IRPJ ~391.472,54/CSLL ~128.933,04 (cotas 30/10); [ ] DCTFWeb 4.971,86 (20/10) comprovação G-Click.
- [x] **185 (18/10):** guias PIS/COFINS 139,89 e IRPJ/CSLL 831,30 enviadas no G-Click; TSV final entregue. [ ] GMA, CSLL a compensar 10,41, IBS/CBS pós-fechamento, SPED.
- [x] **189 (18/10):** Domínio refeito conferido (notas 44/45, CSOC-RET 1%, IRPJ 391.472,54, CSLL 128.933,06); TSV Prestados/Tomados/PIS/COFINS/IRPJ/CSLL entregue. [ ] guias IRPJ/CSLL (cotas?), FAT set, CRF 4,65% Xavantina, cadastro do tomador, IBS/CBS, DCTFWeb 4.971,86 (20/10).
- [x] **189 (18/10):** TSV colado; IRPJ/CSLL em cota única; DCTFWeb **não é do fiscal** (retirada das pendências).
- [ ] **197 (18/10) em preparação:** [ ] salvar Domínio 197; [ ] Tomados XML x Domínio; [ ] PIS/COFINS sem folha/anuidade (confirmar); [ ] CSLL 95,64 (30/10) e IRPJ −79,60 (PER/DCOMP?); [ ] IBS/CBS.
- [x] **189 (18/10):** guia IRPJ/CSLL 520.405,60 (cota única, 30/10) conferida e enviada no G-Click; TSV entregue. [ ] FAT set, CRF 4,65% Xavantina, cadastro tomador, IBS/CBS, SPED.
- [ ] **197 (18/10):** avaliar enquadramento (associação sem fins lucrativos? isenta/imune de IRPJ/CSLL?) — pedir cartão CNPJ/estatuto/natureza jurídica; DARF IRPJ/CSLL não lançados; demais pendências do 197 mantidas. 189 TSV colado.
- [ ] **205 L S Becker (18/10) preparado:** [ ] FAT: lançar retenções de set (IRRF 245,30; PIS 106,30/COFINS 490,59/CSLL 163,53) e o adicional de IRPJ (4.635,43) — IRPJ 3ºTRIM ~20.153,46, CSLL ~9.101,82; PIS 516,10/COFINS 2.382,00 (23/10); [ ] salvar Domínio 205; [ ] Prestados 95.753,11 / Tomados; [ ] cadastro "1205" duplicado; [ ] **IBS/CBS pós-fechamento** (acum. 900: 183/184; Portal CBS 696,27/IBS 77,38).
- [ ] **197 (18/10):** estatuto indica associação sem fins lucrativos; confirmar isenção/imunidade (cartão CNPJ, histórico de IRPJ/CSLL) antes de lançar DARF.
- [x] **205 (18/10):** Domínio e FAT corrigido conferidos (PIS 516,10; COFINS 2.382,00; IRPJ 20.153,46; CSLL 9.101,83). [ ] Portal Recebidas 205 (Officecont 1040, 740,80); [ ] guias PIS/COFINS (23/10) e IRPJ/CSLL (30/10, cota?); [ ] IBS/CBS pós-fechamento.
- [ ] **197 (18/10):** rascunho ao Gian (`RASCUNHOS_2026-10-18.md`): ECF 2019-21 isento, 2022-23 imune, 2024 LP; falta natureza/enquadramento atual, ECF 2025, requisitos; DARF 197 só depois da resposta.
- [ ] **Rede do ambiente:** sites do governo (planalto.gov.br, gov.br/receitafederal) bloqueados; se quiser que eu leia a lei direto, liberar esses domínios em Network access.
- [x] **205 (18/10):** guias PIS/COFINS 2.898,10 e IRPJ/CSLL 29.255,29 (cota única) conferidas, G-Click 17:59; TSV `Enviado`. [ ] rodar Portal 205 (Recebidas) para fechar Tomados (Officecont 1040, 740,80); [ ] IBS/CBS pós-fechamento.
- [ ] **209 (18/10) preparado:** Sem movimento (prestados/PIS/COFINS/IRPJ/CSLL), Tomados `Não se aplica`; confirmar com Fernanda; aporte do sócio R$ 500 (contabilizar como aporte); rend. R$ 0,01; sem certificado/Domínio.
- [x] **205 (18/10):** Portal rodado, Recebidas = Officecont 1040 R$ 740,80 = Domínio; TSV Tomados `Importado` entregue. Resta: IBS/CBS pós-fechamento (acum. 900/183/184), cadastro "1205" duplicado. 209: TSV colado.
- [ ] **197 (18/10):** Fernanda roda `PROMPT_EXTENSAO_LEFISC_197.md` na extensão; trazer o resultado para atualizar o rascunho ao Gian.
- [ ] **227 PROGEST (18/10) em preparação:** rodar Portal (certificado A1 no PC?), REINF R-2099, declaração/guia ISS São Sebastião do Caí, Domínio, FAT 2026, linhas de agosto `Pendente`, cadastro; indício de nota R$ 40.000,00 em set. (manual 25/09); ⚠ .pfx com senha no nome do arquivo no Drive.
- [ ] **227 (18/10):** incluir no `clientes.csv` do Portal (comando entregue) e no `Cadastro_Clientes` (TSV entregue); rodar Portal 227; declaração SSC 09/2026 não salva.
- [ ] **227 (18/10):** Portal ok: NFS-e 1 R$ 40.000,00 (ISS 1.200; IRRF 600; CS 1.860) e Safeweb R$ 275,00. [ ] Domínio 227; [ ] declaração/guia ISS São Sebastião do Caí 09/2026 (passo a passo não registrado; gravar); [ ] REINF R-2099; [ ] FAT 2026; [ ] cadastro/clientes.csv; [ ] IRPJ 1.320/CSLL 752 (30/10).
- [x] **227 (18/10):** FAT 2026 criado no Drive (002_FISCAL), set/2026 preenchido (IRPJ 1.320 / CSLL 752; rendimentos NT = 0). [ ] Jan–Jun a confirmar; [ ] Domínio, declaração/guia SSC, REINF, cadastro/clientes.csv.
- [ ] **197 (18/10):** Lefisc devolveu base legal (ver `BASE_LEGAL_ASBBM_LEFISC_2026-10-18.md`): provável isenta (art. 15 Lei 9.532); obstáculo à retificação da ECF: IN 2.004 art. 7º §2º. Salvar relatório completo no Drive; enviar ao Gian; sem DARF até decisão.
- [ ] **237 (18/10) preparado:** IRPJ 3.824,15 / CSLL 3.383,84 (3ºTRIM, venc. 30/10); Rendimentos = Sim; FAT confere. Falta: Portal de novo (honorário OfficeCont set.), Domínio set., decisão cota única/3 cotas, guia + G-Click, Tomados/Prestados/PIS/COFINS (propostos sem movimento onde cabe). Ver `CLIENTE_237_REAL_REPRESENTACAO.md`.
- [ ] **237 (18/10):** Portal rodado de novo: set. sem receita; NFS-e 14 (R$ 60.233,22) é de 10/2026 (guardar para outubro: ISS 1.204,66 sem retenção, IRRF 903,50, PIS 391,52, COFINS 1.807,00); honorário OfficeCont de set. não apareceu; falta Domínio set.
- [ ] **227 IBS/CBS (pós-fechamento):** acumulador 910 sem 183-IBS/184-CBS (Domínio descarta); conferir CBS 336,06 / IBS 37,34 da NFS-e 1 depois do fechamento.
- [x] **237 (18/10 noite):** Domínio salvo/conferido; TSV entregue (`TSV_237_09-2026.md`); cota única. [ ] gerar guias IRPJ 3.824,15 / CSLL 3.383,84 (venc. 30/10) e comprovar no G-Click; [ ] IBS/CBS pós-fechamento.
- [ ] **Honorários não emitidos (aviso ao Gian):** 237 (set.). Analisar os demais clientes (Portal Recebidas 09/2026: nota OfficeCont comp. 09) e avisar o Gian — `HONORARIOS_NAO_EMITIDOS_AVISO_GIAN.md`.
