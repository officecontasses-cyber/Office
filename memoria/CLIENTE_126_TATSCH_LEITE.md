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
