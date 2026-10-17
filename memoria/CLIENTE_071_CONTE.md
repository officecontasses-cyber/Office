# Cliente 71 — CONTE (Conte Cornetet Arquitetura e Consultoria Ltda): dossiê para o fechamento

**Gatilho:** "fechamento da empresa #71". Criado em 17/10/2026 a partir da memória (seções 21, 28i–28ab, 28x–28ab), Controle_Fiscal (export 17/10), Cadastro_Clientes, FAT 2026, Rendimentos, DCTFWeb 09/2026 e os relatórios do Domínio/Portal de 12/10. Incluir sempre IBS/CBS e a planilha Rendimentos (CLAUDE.md).

## Cadastro e particularidades
- CNPJ 08.307.701/0001-80 (na Controle perdeu o zero à esquerda), Brasília/DF, IE 0817205500132, **Lucro Presumido**, não contribuinte de ICMS. CNAE 7111100 (arquitetura); secundários 7112000, 7119703, 7119799. Sócias: Betina Conte Cornetet Fittipaldi (administradora), Mariangela Conte Cornetet, Thais Gerhardt, Thais Rodrigues Barboza. Mariangela também sócia da Belém Brasil (265).
- **Prefeitura:** Brasília/DF (ISSNet On-Line / Nota Control; skill `brasilia-issqn`): Protocolo de Serviços Prestados, **Declaração de Não Movimento de Contratados**, guia, Livro Fiscal. Portal Nacional "Em Transição (Prefeitura até 01/10/2026)" (conferir se o Padrão Nacional já vale). **Tem certificado A1** (vence 13/11/2026: renovar).
- **Receita:** serviços de arquitetura para a **Caixa Econômica Federal** (órgão público: retenção integral na fonte): IRRF 4,8%, PIS 0,65% + COFINS 3% + CSLL 1% retidos na nota (PIS/COFINS coberto integralmente, `Retido`, sem DARF), ISS 100% retido pelos tomadores (`Sem Recolhimento (Retenção Integral)`). 42 notas em set; maioria incide em Brasília (ISS DF), algumas fora (CE, RJ, GO, SP).
- **ISS retido que o 71 deve recolher fora do DF:** NFS-e 153 RIPA (item 7.11, R$ 39,43): guia de Jundiaí/SP nº 00026073855, venc. 26/10, `Enviado` (G-Click 04/10 15:39). Pendente: confirmar o local de execução (Portal diz São Paulo/SP; a chave aponta Jundiaí).
- **FAT:** base de IRPJ/CSLL com presunção 32% até R$ 1.250.000 por trimestre e **35,2% sobre o excedente** (método do FAT; conferi só que reproduz os adicionais de 1º e 2º tri; base legal não verificada). Adicional de IRPJ 10% sobre a base acima de R$ 60.000 por trimestre. Rendimentos financeiros (Caixa e Bradesco) entram na base; IRRF sobre eles é crédito.
- **Rendimentos (planilha CONTROLE | Rendimentos, aba 3ºTRIM 2026, linha 71):** LIBERADO FISCAL **em branco**; observação "**Falta só Informe de Rend. 3º trim/2026 BRADESCO**" → IRPJ/CSLL do 3º tri ainda não liberados. (FAT já tem os mensais do Bradesco e da Caixa.)
- **Mútuo à CBR Engenharia:** DARF IOF R$ 16.900,00 (cód. 1150, venc. 15/10) e tratamento em `MUTUO_CONTE_CBR_LEFISC_2026-10-08.md` (juros entram na base de IRPJ/CSLL; estimativa 3º tri R$ 2.494,56). Confirmar pagamento e se o juros de set entram no 3º tri.

## Situação em Set2026 (Controle_Fiscal, 17/10)
| Obrigação | Status | Observação |
|---|---|---|
| REINF | Enviado | R-4020 34371371-01-4020-2609-34371371; R-2099 12261147-01-2099-2609-12261147; R-4099 5894554-01-4099-2609-5894554 (12/10 14:24); sem R-2010 |
| DECLARAÇÃO PREFEITURA | Enviado | Protocolo Prestados + Não Movimento, 04/10 |
| SERVIÇOS PRESTADOS | Pendente | 42 notas 1.091.077,54; "falta conferência XML x Domínio" (feita abaixo: bate) |
| SERVIÇOS TOMADOS | Sem movimento | refere-se à Não Movimentação de Contratados DF; **Domínio tem 145 notas de outros municípios** (ver abaixo) |
| ENTRADAS | (vazio) | falta lançar 2 notas no Domínio |
| GUIA ISSQN | Sem Recolhimento (Retenção Integral) | ISS apurado 52.553,62 (DF 46.949,88 + fora 5.603,74) |
| GUIA ISSQN FORA MUNICÍPIO | Enviado | R$ 39,43 Jundiaí venc. 26/10 |
| DARF PIS / COFINS | (vazio) | venc. 23/10 |
| DARF IRPJ / CSLL | (vazio) | 3º tri, venc. 30/10 |
| SPED CONTRIBUIÇÕES | (vazio) | venc. 16/11 |

## Conferência de 17/10/2026
- **Prestados (Portal Emitidas x Domínio Serviços, 12/10) = OK:** 42 notas 1806 a 1847, R$ 1.091.077,54 (Total Série); nota a nota iguais, sem nota só de um lado. Retenções Domínio = Portal: IRRF 52.371,72; CSLL 10.910,78; PIS 7.092,02 e COFINS 32.732,35 (Portal igual; 0,65% e 3% exatos dão 7.092,00 e 32.732,33: centavos de arredondamento por nota); ISS 52.553,63 (prefeitura 52.553,62). ISS DF 46.949,88 = prefeitura. O "Total Geral" do Domínio mostra valor contábil, IRRF e ISS em dobro (2.182.155,08): é artefato do relatório (Total Série fecha 1.091.077,54).
- **Tomados (Portal Recebidas de 12/10, 17:39) x Domínio Entradas (12/10 17:23):** Portal 147 notas de 09/2026 = R$ 469.779,47; Domínio 145 notas = R$ 466.006,65 (inclui NFS-e Caixa Cartões 39.459.331/0006-34 com valor 0,00). Faltam no Domínio: **nota 2 Monique de Azevedo Chaves (CNPJ 67.662.436/0001-17, R$ 1.272,82, emissão 07/10)** e **nota 61 Laura de Luca Baccarin (CNPJ 45.454.954/0001-02, R$ 2.500,00, emissão 06/10)**; soma 3.772,82 = a diferença exata. As demais 145 batem por CNPJ e valor (inclui a nota de substituição de 12.629,50). Não há relatório do Domínio mais novo no Drive: se as 2 notas já foram lançadas, regerar Entradas.
- **Retenções (tomados):** só a nota 659 Giovani Gazen (IRRF 83,61 + CRF 259,20), R-4020 enviado; DCTFWeb (guia 3.574,45, venc. 20/10, DP) inclui 1708 83,61 e 5952 259,20. ISS retido: RIPA 153 (39,43).
- **IBS/CBS:** Prestados: o Portal Emitidas **não traz** CST/CBS/IBS nas 42 notas (colunas vazias) -> conferir no XML (SIEG, pasta de emitidas, ou XML do Portal) antes de concluir. Tomados (Portal, 147 notas): 13 com dados, CBS 161,13 e IBS 17,89 (CST 000/000001 em 8; CST 200/200052 em 5); o Domínio ainda não foi visto (sem Resumo dos Impostos do 71 no Drive).
- **DARF PIS/COFINS set:** receita 1.091.077,54: PIS 7.092,00 e COFINS 32.732,33 integralmente cobertos pela retenção (7.092,02 e 32.732,35 no Domínio): precedente de agosto = `Retido`, sem DARF.
- **IRPJ/CSLL do 3º tri (estimativa pelo método do FAT; NÃO é o valor final, o Domínio e a liberação dos rendimentos mandam):** receita 3.118.259,98 (jul 974.825,34 + ago 1.052.357,10 + set 1.091.077,54); rendimentos financeiros 60.593,14 (set: Caixa 21.391,97 + Bradesco 30,71); base 1.118.220,65 (1.250.000 x 32% + excedente x 35,2% + rendimentos); IRPJ 15% 167.733,10 + adicional 105.822,07 = 273.555,16; retido IRRF serviços 149.676,48 + IRRF rendimentos 18.949,05 = 168.625,53; **IRPJ a pagar ~ 104.929,63**; CSLL 9% = 100.639,86 - retido 31.182,60 = **~ 69.457,26**. Não inclui juros do mútuo. O FAT do 71 está com setembro em branco (receita 0,00 e retenções 0,00): preencher.

## O que falta
1. Lançar no Domínio as notas 2 (Monique) e 61 (Laura) e regerar Entradas; depois Serviços Tomados `Importado` (decisão da Fernanda: hoje `Sem movimento` pela Não Movimentação de Contratados DF).
2. Preencher o FAT 071 de setembro; conferir com o Domínio (Resumo dos Impostos / Retenções a Recolher de set, regerar).
3. Informe de rendimentos 3º tri do Bradesco (liberar IRPJ/CSLL); definir juros do mútuo.
4. IBS/CBS: XML das emitidas (prestados) e créditos dos tomados no Domínio.
5. Local de execução da NFS-e 153 (RIPA); nota 60 Laura (Francine); Chanfro nº 2 (comp. 08; IRRF 42,00 + CRF 130,20; conferir se saiu no REINF de agosto); Caixa Cartões valor zero.
6. SPED Contribuições set (16/11); certificado A1 (13/11).
