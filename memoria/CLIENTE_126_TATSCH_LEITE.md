# Cliente 126 — TATSCH & LEITE (Centro Odontológico S/S): dossiê para o fechamento

**Gatilho:** "fechamento da empresa #126". Criado em 17/10/2026 a partir da Controle_Fiscal (export 17/10), Cadastro_Clientes, FAT 2026, Rendimentos, Portal (03/10), Domínio (05/10), DCTFWeb (15/10) e memória. Incluir sempre IBS/CBS e a planilha Rendimentos (CLAUDE.md). Skill: `.claude/skills/sao-leopoldo-issqn`.

## Cadastro e particularidades
- CNPJ 10.914.420/0001-37, São Leopoldo/RS (contribuinte 445777), **Lucro Presumido**, não contribuinte de ICMS. CNAE 8630504 (odontológica). Sócios-administradores: Daniel Fortes Leite e Fernanda Abich Tatsch. Certificado A1 vence 16/12/2026.
- **ISSQN:** 2% por nota (04.12.01). A DMS é gerada sozinha pelo ADN (Portal Nacional); a Fernanda gera o faturamento e imprime a guia. 09/2026: DMS (nº 1053665, 02/09) = Portal = guia **R$ 3.073,23** (209 notas, R$ 153.662,41), venc. 15/10, `Enviado` (G-Click 04/10 14:46).
- **Federais:** PIS 0,65% / COFINS 3% cumulativos (DARF 8109/2172, venc. 23/10), IRPJ/CSLL trimestrais (32%; receita do trimestre bem abaixo de R$ 1,25 mi: **sem o +10% da LC 224/2025**). Sem retenção federal sofrida nas Emitidas.
- **Créditos de PIS/COFINS (aba Compensações do FAT):** PERDCOMP 001 (39442.72987.170826.1.3.04-7003) compensou DARF PIS/COFINS 07/2026; saldo remanescente de COFINS 01/2025 R$ 462,54 (valor original; atualizar pela Selic no uso) e PIS 01/2025 R$ 785,32 (duplicidade, ainda sem PER/DCOMP). Em 08/2026 pagaram o valor cheio.
- **Rendimentos (CONTROLE | Rendimentos, 3ºTRIM 2026, linha 126):** LIBERADO FISCAL = **Sim**, sem observação. FAT sem rendimentos financeiros no 3º tri (0,00).
- **DCTFWeb/eSocial (DP):** recibo 50000538005070 (15/10); guia **R$ 2.989,92**, venc. 20/10 (CP segurados/patronal/terceiros + 5952 retenção R$ 10,46).
- **REINF:** R-4020 (CRF R$ 10,46, cód. 5952, BIOLAB nº 1507) + R-2099 + R-4099 enviados 06/10 06:03 (recibos 97463238-10-4020-2609-97463238, 12127193-10-2099-2609-12127193, 5830434-10-4099-2609-5830434).

## Situação em Set2026 (Controle_Fiscal, 17/10)
| Obrigação | Status | Observação |
|---|---|---|
| REINF | Enviado | com retenção (CRF 10,46) |
| DECLARAÇÃO PREFEITURA | Enviado | Livro Fiscal DMS 04/10 |
| GUIA ISSQN | Enviado | 3.073,23, G-Click 04/10 14:46, venc. 15/10 |
| ENTRADAS / SERVIÇOS TOMADOS / SERVIÇOS PRESTADOS | (vazio) | falta Domínio importado e conciliado |
| DARF PIS / COFINS | (vazio) | venc. 23/10 |
| DARF IRPJ / CSLL | (vazio) | 3º tri, venc. 30/10 |
| SPED CONTRIBUIÇÕES | (vazio) | venc. 16/11 |
Agosto (referência): prestados 182 notas R$ 109.035,74 (ISS 2.180,70); tomados R$ 12.666,04 (14 notas); entradas R$ 19.343,94 (inclui NF-e R$ 6.677,90 de mercadoria/uso e consumo, só informativo); PIS 708,73 e COFINS 3.271,07 `Enviado` (G-Click 17/09).

## Conferência de 17/10/2026
- **Portal Nacional (03/10):** Emitidas 09/2026: 209 notas, R$ 153.662,41, ISS R$ 3.073,23, **sem retenção e sem dados de IBS/CBS** (CST vazio nas 209 notas: conferir no XML). Recebidas 09/2026: 15 notas, R$ 10.981,61; retenção só a Biolab nº 1507 (CRF 10,46); IBS/CBS em 4 notas: CBS 5,97 e IBS 0,66 (3 notas CST 000/000001, 1 nota CST 200/200029; base 866,19). Nota: o Controle diz tomados de agosto R$ 12.666,04 (14 notas).
- **Domínio de 05/10 desatualizado:** Demonstrativo (05/10 18:56): ISS a recolher R$ 1.727,73 (a guia é 3.073,23) e IRPJ R$ 17.907,37 (14.344,42 + adicional 3.562,95), isto é, só parte das saídas; falta importar as **saídas 1760 a 1841** (PENDENCIAS) e regerar Entradas, Saídas/Serviços e Resumo/Demonstrativo. Não há relatório mais novo no Drive.
- **FAT 126:** jul preenchido (receita 103.419,41); **ago e set em branco** (ago deveria ser 109.035,74; set 153.662,41); sem rendimentos; aba Compensações como acima.
- **PIS/COFINS de setembro (estimativa; Domínio manda):** base 153.662,41: PIS 0,65% = **998,81**; COFINS 3% = **4.609,87** (total 5.608,68, venc. 23/10). Possível usar o crédito de PIS 785,32 (+ Selic) e COFINS 462,54 via PER/DCOMP (decisão da Fernanda; em 08/2026 pagaram cheio).
- **IRPJ/CSLL do 3º tri (estimativa, método do FAT; confere com o 1º tri do FAT):** receita 366.117,56 (jul 103.419,41 + ago 109.035,74 + set 153.662,41) x 32% = base 117.157,62; IRPJ 15% 17.573,64 + adicional 10% sobre (base - 60.000) 5.715,76 = **23.289,40**; CSLL 9% = **10.544,19**; sem retenções e sem rendimentos. Venc. 30/10 (possível 3 quotas, a confirmar).

## O que falta
1. Importar as saídas 1760 a 1841 e regerar Domínio (Entradas, Serviços, Resumo/Demonstrativo); conciliar Entradas (tomados + NF-e) com Portal e XML.
2. FAT 126 de ago e set (e, se for o caso, ajustar os créditos de PIS/COFINS na aba Compensações).
3. IBS/CBS: prestados (XML das emitidas, sem dados no Portal) e tomados (CBS 5,97 / IBS 0,66; acumulador 800 com 200/200029 e 000/000001).
4. DARF PIS/COFINS (23/10) e IRPJ/CSLL (30/10): gerar e comprovar no G-Click.
5. SPED Contribuições set (16/11).

## Domínio do 126 regerado (17/10/2026 19:40) — conferência
- **Serviços (saídas importadas):** 209 notas (saídas 1633 a 1841), Total Série = Total Geral = **R$ 153.662,41**, ISS 3.073,23 = Portal = DMS = guia. Serviços Prestados pronto para `Importado`.
- **Resumo (19:40):** PIS 998,81 e COFINS 4.609,87 (a recolher integral, sem retenção nem compensação), CSLL 10.544,19 e IRPJ **23.289,40** (15% 17.573,64 + adicional): **= estimativa**. ISS 3.073,23; contribuições retidas (5952) 10,46. IBS: saldo anterior 32,47, débito 0,31, crédito 9,86, saldo credor 42,02; CBS: anterior 291,99, débito 2,80, crédito 89,03, saldo credor 378,22.
- **Entradas (Domínio):** total R$ 34.469,16 = NF-e/CT-e **R$ 20.929,80** (11 linhas) + NFS-e tomadas R$ 13.539,36 (17 linhas). NFS-e: Portal Recebidas 15 notas R$ 10.981,61; diferença R$ 2.557,75 explicada: Facebook 146442407 (1.703,92, emitida 02/10) e Officecont 1056 (864,25, emitida 05/10) não estão no export do Portal (03/10) e Ideal Art 444 (Domínio 336,74 x Portal 347,16: desconto incondicional 10,42) = 1.703,92 + 864,25 - 10,42. 
- **NF-e no SIEG (`007 ARQUIVOS SIEG` > CNPJ 10914420000137 > Entrada > 2026 > Setembro):** 11 XMLs; 10 coincidem por número com as NF-e do Domínio (563218, 132190, 1008460, 4128, 1011991, 1011099, 1647221, 461527, 563221, 462789); valores dos XMLs não abertos (exceto o 461485). O 11º XML é a **NF 461485 (JJGC, 01/09, finNFe 4, CFOP 1202, devolução de R$ 778,75, ICMS desonerado, IBS 0,31 / CBS 2,80, CST 200/200030)**: está lançada em **Saídas** (CFOP 5-202, R$ 778,75) e gera os **débitos de IBS 0,31 e CBS 2,80** do Resumo. CT-e 4175904 (São Miguel, R$ 76,00) não tem XML no hub NF-e.
- **IBS/CBS créditos:** Domínio IBS 9,86 / CBS 89,03; Portal NFS-e IBS 0,66 / CBS 5,97 (Clinicorp, Ambientuus, Ideal Art); resto (IBS 9,20 / CBS 83,06) viria das NF-e (e talvez Facebook/Officecont), não conferido XML a XML.

## Conferência XML a XML das NF-e de entrada (17/10/2026, SIEG > Entrada > 2026 > Setembro)
Todos os 10 XMLs abertos; nº, emitente e vNF batem com o Domínio. IBS/CBS = grupo `IBSCBSTot` (valores lidos do XML decodificado):

| NF | Emitente | vNF | vIBS | vCBS |
|---|---|---|---|---|
| 4128 | Fatto 3D | 413,01 | 0,30 | 2,74 |
| 132190 | JB Embalagens | 398,24 | 0,37 | 3,26 |
| 461527 | JJGC (devolvida em 461485) | 778,75 | 0,31 | 2,80 |
| 462789 | JJGC | 5.004,98 | 2,01 | 18,18 |
| 563218 | JJGC PR | 3.575,00 | 0,00 | 0,00 (redução 100%) |
| 563221 | JJGC PR | 2.941,90 | 0,00 | 0,00 (CST 410) |
| 1008460 | Dentalshop | 1.296,04 | 1,12 | 10,03 |
| 1011099 | Dentalshop | 769,80 | 0,64 | 5,70 |
| 1011991 | Dentalshop | 549,00 | 0,45 | 4,06 |
| 1647221 | Quantity SC | 5.127,08 | 2,44 | 22,27 |
| **Soma 10 NF-e** | | **20.853,80** | **7,64** | **69,04** |

- Valores = Domínio nas 10 NF-e (+ CT-e 4175904 São Miguel 76,00, sem XML no hub = 20.929,80). ENTRADAS (produtos) conferida.
- **IBS/CBS créditos NÃO fecham:** Domínio IBS 9,86 / CBS 89,03; menos NFS-e Portal 0,66 / 5,97 = 9,20 / 83,06 esperado das NF-e; XMLs somam 7,64 / 69,04. **Sobra no Domínio: IBS 1,56 / CBS 14,02** (proporção 0,1%/0,9% ⇒ base ≈ R$ 1.558). Causa não identificada (hipóteses: Facebook/Officecont fora do Portal; CT-e; base sem desconto na 1008460; acumulador). Conferir lançamento a lançamento no Domínio.

## Compensação PIS/COFINS 09/2026 (17/10/2026) — conferida
- PER/DCOMP 002 `00350.22053.171026.1.3.04-0009`: crédito COFINS 01/2025 (DARF 20/03/2025, 2172-01), saldo do PERDCOMP 001: original 462,54, Selic 21,55% = **562,22**; saldo do crédito original após = 0,00. Débito: COFINS 09/2026 (venc. 23/10), DCTFWeb recibo 050000540023248.
- PER/DCOMP 003 `00672.82985.171026.1.3.04-1725`: crédito PIS 01/2025 (**8109-02**, original 785,32), Selic 21,55% = **954,56**; saldo 0,00. Débito: COFINS 09/2026. **Atenção:** o PDF traz o mesmo nº de documento de arrecadação do COFINS (07.16.25079.4208194-3); conferir se o DARF de PIS tem número próprio.
- COFINS 09/2026: 4.609,87 − 562,22 − 954,56 = **3.093,09** (= FAT). PIS 09/2026 **998,81** a recolher integral (não compensado).
- Rendimentos (CONTROLE | Rendimentos, 3ºTRIM 2026): 126 = `Sim` (liberado), sem observação; FAT com rendimentos 0,00 no tri.
- FAT: ISSQN set estava 3.073,25; guia/Domínio/Portal = 3.073,23. Aba Compensações ainda com banner e saldos "pendentes" (462,54 / 785,32) já consumidos.
