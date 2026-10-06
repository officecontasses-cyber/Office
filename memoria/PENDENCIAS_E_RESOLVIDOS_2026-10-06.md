# Snapshot PENDENCIAS_E_RESOLVIDOS 2026-10-06

Cópia da rodada de 05 e 06/10/2026. O documento completo está em `memoria/PENDENCIAS.md` (repositório Office, branch claude/sharp-meitner-bilpus).

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
- [ ] **248:** falta o Domínio (tomados e a NF-e de R$ 15,00), GUIA ICMS, SPED ICMS e DIME; TSV provisório em `TSV_TACOM_248_09-2026.md` (Declaração `Enviado`; Prestados, Guia ISSQN e Saídas `Sem movimento`; Tomados PREF `Pendente` até o Domínio).
- [ ] **263:** DecWeb: tomados R$ 650,00 (OfficeCont, NFS-e 1018) e prestados 9 NFS-e R$ 81.793,56 (ISS R$ 4.089,69 = guia enviada). Falta o Domínio (Entradas/Saídas) para conciliar e gerar o TSV; contribuinte de ICMS = NÃO.

### Reforma tributária e acumuladores (outubro com agilidade)
- [ ] Padronizar acumuladores de serviços tomados (IBS/CBS integral 000/000001, redução 200052, sem incidência 410, sem dados) e transformar em skill; base de IBS/CBS = valor − ISS − PIS/COFINS destacados. Detalhes na seção J.
- [ ] Skill da conferência do Domínio (ler relatório + XML do Portal + SEFAZ) para repetir em outubro.

