# TSV da planilha do DP (CONTROLE | DP REINF'S), aba MOD GERAL 09.2026 (04/10/2026)

Script: `apps-script/atualizarReinfDP.gs` (colar no Apps Script da planilha do DP; rodar `prepararAbaAtualizacoesReinf()` uma vez e depois `processarAtualizacoesReinf()`).
Colunas: Nº | aba | Status | Observação | Detalhe | Rótulo caixa | Valor caixa | Processado (em branco).

## Lote 1: R-2099 enviados em 04/10/2026 (sem movimento) e o 117 invalidado
```tsv
2	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:24 (Oficial). Recibo 12139055-06-2099-2609-12139055. Sem retenção. Provisório até receber as notas do cliente (Freire).			
16	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:23 (Oficial). Recibo 12540601-03-2099-2609-12540601. Sem retenção.			
18	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:21 (Oficial). Recibo 12177287-01-2099-2609-12177287. Sem retenção. Provisório até receber o movimento (Inês).			
26	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:24 (Oficial). Recibo 12060343-05-2099-2609-12060343. Sem retenção.			
133	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:24 (Oficial). Recibo 12113783-10-2099-2609-12113783. Sem retenção. Provisório até receber o movimento (Inês).			
155	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:22 (Oficial). Recibo 12060341-05-2099-2609-12060341. Sem retenção.			
173	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:22 (Oficial). Recibo 12177288-01-2099-2609-12177288. Sem retenção.			
177	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:22 (Oficial). Recibo 12540600-03-2099-2609-12540600. Sem retenção. Provisório até receber o movimento (Inês).			
185	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:23 (Oficial). Recibo 12113779-10-2099-2609-12113779. Sem retenção.			
197	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:21 (Oficial). Recibo 12113778-10-2099-2609-12113778. Sem retenção.			
209	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:22 (Oficial). Recibo 12198572-08-2099-2609-12198572. Sem retenção.			
237	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:24 (Oficial). Recibo 12139054-06-2099-2609-12139054. Sem retenção.			
247	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:23 (Oficial). Recibo 12177294-01-2099-2609-12177294. Sem retenção.			
258	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:22 (Oficial). Recibo 12043662-02-2099-2609-12043662. Sem retenção.			
264	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 04/10/2026 16:25 (Oficial). Recibo 12177295-01-2099-2609-12177295. Sem retenção.			
117	MOD GERAL 09.2026		Sem movimento				
```

## Retenções (colar só depois de conferir; Status em branco até o REINF ser enviado)
152: valores provisórios (6190 = 15 notas com IRRF 4,8% + contribuições 4,65%; 6147 = Casa da Moeda 1,2% + 4,65%; CSLL = nota 15095; INSS = Realize Next). Ficam de fora: IRRF 1.178,40 da nota 15095 (Implanta) e IRRF 17,66 da nota 741590 (Rede OK, emitida em 01/10): classificar o código.
```tsv
71	MOD GERAL 09.2026		COM RETENÇÃO	IRRF (Cód. Rec. 170806): R$ 83,61\nCRF (Cód. Rec. 5952): R$ 259,20			
126	MOD GERAL 09.2026		COM RETENÇÃO	CRF (Cód. Rec. 5952): R$ 10,46			
189	MOD GERAL 09.2026		COM RETENÇÃO	IRRF (Cód. Rec. 170806): R$ 2.144,00			
238	MOD GERAL 09.2026		COM RETENÇÃO	IRRF (Cód. Rec. 170806): R$ 17,75\nCRF (Cód. Rec. 5952): R$ 141,86\nINSS: R$ 1.295,45			
152	MOD GERAL 09.2026		COM RETENÇÃO	VALORES AO LADO	COD 6190 COSIRF S/SERVIÇOS	1534,82	
152	MOD GERAL 09.2026				COD 6147 COSIRF S/MERCADORIAS	44,14	
152	MOD GERAL 09.2026				COD 6228 CSLL	245,50	
152	MOD GERAL 09.2026				INSS 1162	1269,26	
```

## 152 CRBM5, versão de 13/10/2026 (substitui os valores provisórios acima; Status fica em branco até o REINF ser enviado)
Critério (Anexo I da IN RFB 1.234, tabela de órgãos públicos): serviços (IRRF 4,8% + 4,65%) = 6190; mercadorias/serviços com materiais (1,2% + 4,65%) = 6147; só CSLL 1% (nota 15095) = 6228; INSS 11% (Realize Next 3279/3280) = 1162. IRRF 1.178,40 da Implanta (4,8%) entra em 6190. Ficam fora: nota 741590 Rede OK IRRF 17,66 e 255/4517 (emitidas em 01/10), 734991 (competência 08) e Life Card 159 (R$ 6,31 + 6,10, base não fecha com a tabela).
```tsv
152	MOD GERAL 09.2026		COM RETENÇÃO	VALORES AO LADO	COD 6190 COSIRF S/SERVIÇOS	2756,92	
152	MOD GERAL 09.2026				COD 6147 COSIRF S/MERCADORIAS	44,14	
152	MOD GERAL 09.2026				COD 6228 CSLL	245,50	
152	MOD GERAL 09.2026				INSS 1162	1269,26	
```

## 152 CRBM5, VERSÃO FINAL de 14/10/2026 (REINF enviada; substitui as versões de 13/10 e as provisórias)
Fonte: Retenções a Recolher do Domínio (emissão 14/10/2026) = planilha do Gian (setembro/2026) = recibos. Total R$ 7.391,30 (federais 6.122,04 + INSS 1.269,26). Fora: Volpmann 48337 (não paga; outubro) e nota 741590. Atenção: a CSLL 6228 agora é só a dos Correios (55,91); a CSLL da Implanta (nota 15095) ficou dentro do 6190. O script só grava rótulo que já exista na caixa do DP (H) e avisa se não achar: se faltar "COD 6188", "COD 6230 PIS" ou "COD 6243 COFINS", incluir a linha na caixa antes.
Controle_Fiscal (aba Atualizações):
```tsv
152	Set2026	REINF	Enviado		R-2010 Sucesso recibo 5745056-04-2010-2609-5745056; R-4020 Sucesso, 14 recibos (um por beneficiário) 23511133-04-4020-2609-23511133 a 23511146-04-4020-2609-23511146; R-2099 Sucesso 12203533-04-2099-2609-12203533; R-4099 Sucesso 5930225-04-4099-2609-5930225; enviados 14/10/2026 19:36 (Oficial).	
```
Planilha do DP (aba Atualizações REINF):
```tsv
152	MOD GERAL 09.2026	Enviado	COM RETENÇÃO	VALORES AO LADO\nEnviado 14/10/2026 19:36 (Oficial): R-2010 + R-4020 + R-2099 + R-4099.	COD 6190 COSIRF S/SERVIÇOS	5680,81	
152	MOD GERAL 09.2026				COD 6147 COSIRF S/MERCADORIAS	141,25	
152	MOD GERAL 09.2026				COD 6188	40,00	
152	MOD GERAL 09.2026				COD 6228 CSLL	55,91	
152	MOD GERAL 09.2026				COD 6230 PIS	36,34	
152	MOD GERAL 09.2026				COD 6243 COFINS	167,73	
152	MOD GERAL 09.2026				INSS 1162	1269,26	
```

### 152, atualização de 14/10/2026 (após relatórios de conferência da Receita)
Controle_Fiscal, linha REINF da 152 com os totalizadores (substitui a anterior):
```tsv
152	Set2026	REINF	Enviado		R-2010 Sucesso recibo 5745056-04-2010-2609-5745056; R-4020 Sucesso, 14 recibos (um por beneficiário) 23511133-04-4020-2609-23511133 a 23511146-04-4020-2609-23511146; R-2099 Sucesso 12203533-04-2099-2609-12203533; R-4099 Sucesso 5930225-04-4099-2609-5930225; enviados 14/10/2026 19:36 (Oficial). Totalizadores da Receita conferidos com o Domínio: INSS 1162-01 R$ 1.269,26 (base R$ 11.538,71) e retenções federais R$ 6.122,04 (614705 141,25; 618805 40,00; 619005 5.680,81; 622805 55,91; 623005 36,34; 624305 167,73). Fora: nota 741590 (Rede OK) e Volpmann 48337, a verificar em outubro.	
```
