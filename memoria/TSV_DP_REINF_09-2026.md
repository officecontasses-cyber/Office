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
