# Cliente 16 — QUALIDENTE (Centro Clínico de Odontologia S/S Ltda): dossiê para o fechamento

**Gatilho:** "fechamento da empresa #16". Atualizar a cada fechamento. Criado em 17/10/2026 a partir da Controle_Fiscal (export 17/10), Cadastro_Clientes, FAT 016, apuração federal de 08/2026, contexto do manual NFS-e (24/09), recibo/guia DCTFWeb (13/10) e anotações da memória. Nenhum arquivo do Domínio de 09/2026 do 16 foi localizado no Drive em 17/10.

## Cadastro e particularidades
- CNPJ 04.361.573/0001-00, Porto Alegre/RS, CNAE 8630504 (atividade odontológica), **Lucro Presumido**, não contribuinte de ICMS. Sócios: Paulo Fernando Espindola Martins Junior; Rodrigo Tavares Lopes (sócio-administrador). Não confundir com o 173 (Lopes & Martins Dentistas, mesmos sócios): confirmado em 24/09 que é o código 16. Rodrigo Tavares Lopes consta como profissional nos dois: conferir (pendência antiga).
- **ISSQN: Sociedade de Profissionais (art. 129), ISS fixo por profissional:** R$ 422,87/mês (2 profissionais x 35 UFM x R$ 6,0411), guia própria no G-Click; alíquota 0,00% nas notas; nunca retido. Declaração pelo DecWeb (robô).
- **Portal Nacional:** com certificado (rodou; set sem divergência Portal x DecWeb). Código de tributação 04.12.01 (odontologia), cNBS 123012300, regime especial "Sociedade de Profissionais", IBS/CBS CST 200 / cClassTrib 200029 (redução 60%), PIS/COFINS CST 01 (0,65% e 3%). Tomador: pessoa física. Notas teste ambGer=2 de ago/26.
- **Sem retenção federal** nas notas emitidas e nos tomados (REINF só R-2099). Emitidas 09/2026 (Portal, 03/10): 221 notas, R$ 142.642,60.
- **Apuração federal:** PIS 0,65% e COFINS 3% cumulativos (DARF 8109/2172, dia 25 do mês seguinte, antecipado se não útil) sobre a receita do mês; IRPJ (2089) e CSLL (2372) **trimestrais**, presunção 32% (IRPJ 15% + adicional 10% sobre o que passar de R$ 60.000/tri; CSLL 9%), vencimento no último dia útil do mês seguinte ao trimestre. Método conferido no 2º tri do FAT (receita 430.362,56 → IRPJ 28.429,00 com adicional 7.771,60).
- **DCTFWeb/eSocial (DP):** tem empregados e contribuintes individuais. Set/2026: recibo 0000050000538001234, 13/10/2026 17:59:13; guia R$ 3.382,31 venc. 20/10 (CP segurados, patronal, GILRAT, terceiros).
- Planilha `CONTROLE | Rendimentos`: 3º tri 2026 = `Zerado` (Ø). Sem aplicações.
- Manual NFS-e IBS/CBS: prévia entregue em 24/09 sem capturas (aguardando gravação de emissão de teste).

## Situação por competência (Controle_Fiscal, 17/10/2026)
| Linha | Ago/2026 | Set/2026 |
|---|---|---|
| REINF | Enviado (R-2099 07/09, sem retenção) | Enviado (R-2099 04/10 16:23, recibo 12540601-03-2099-2609-12540601) |
| ENTRADAS | Importado R$ 1.473,31 (informativa) | em branco |
| SERVIÇOS TOMADOS | Importado R$ 1.301,41 (5 notas) | em branco |
| SERVIÇOS PRESTADOS | Importado R$ 118.605,40 (241 notas) | em branco |
| DECLARAÇÃO PREFEITURA | Enviado | Enviado (robô, 01/10 17:28) |
| GUIA ISSQN | Enviado R$ 422,87 | Enviado R$ 422,87 (G-Click 04/10 11:34, venc. 13/10) |
| DARF PIS / COFINS | 771,31 / 3.558,16 Enviado (guia real: PIS 770,94: diferença de R$ 0,37 já apontada no log; a Controle ainda mostra 771,31) | em branco (venc. 23/10) |
| DARF IRPJ / CSLL | n/a (trimestral) | em branco (venc. 30/10) |
| SPED CONTRIBUIÇÕES | Enviado 04/10 13:34:03 | em branco (venc. 16/11) |

## Estimativa de 09/2026 (só pelo Portal; fechar com o Domínio)
Receita set R$ 142.642,60: PIS R$ 927,18 e COFINS R$ 4.279,28. 3º tri: 162.730,80 + 118.605,40 + 142.642,60 = R$ 423.978,80; base 32% = R$ 135.673,22; IRPJ 15% = R$ 20.350,98 + adicional R$ 7.567,32 = R$ 27.918,30; CSLL 9% = R$ 12.210,59. Cálculo da agente, não conferido no Domínio.

## Roteiro quando a Fernanda disser "fechamento da empresa #16"
Ler o Demonstrativo dos Impostos e o Acompanhamento de Serviços/Entradas do Domínio (008/005), conciliar Prestados com Portal (Emitidas, competência = mês) e com a Declaração do DecWeb; Tomados/Entradas; TSV com status só após conferir; DARF PIS/COFINS no G-Click; IRPJ/CSLL no fechamento do trimestre.

## Fechamento 09/2026: conferência com o Domínio (17/10/2026)
Arquivos (008): `Serviços_16_092026.pdf`, `Entradas_16_092026.pdf`, `Empresa 16 - CENTRO CLINICO DE ODONTOLOGIA SS LTDA.pdf` (resumo dos impostos). Portal (003) e município (002) já na pasta.
- **Prestados:** Domínio 221 notas (2823 a 3043, sem lacunas) R$ 142.642,60 = Portal Emitidas (221 normais comp. 09/2026) = DecWeb (receita R$ 142.642,60). Portal tem mais 6 notas de 10/2026 (R$ 2.340,00), corretamente fora.
- **Tomados:** Domínio 4 NFS-e R$ 753,49 (Clinicorp 7589 R$ 7,90 e 17980 R$ 475,69; Icarus 13234 R$ 84,90; Ambientuus 381951 R$ 185,00) = Portal Recebidas; sem retenção.
- **Impostos (Domínio):** ISS fixo R$ 422,87 (= declaração e guia); PIS R$ 927,18 e COFINS R$ 4.279,28 (base 142.642,60; Portal nota a nota dá PIS 927,58, diferença de arredondamento); IRPJ R$ 27.918,30 (20.350,98 + adicional 7.567,32) e CSLL R$ 12.210,59 sobre base R$ 135.673,22 (3º tri R$ 423.978,80 x 32%). Tudo igual ao cálculo da agente.
- **Atenção:** (1) Entradas tem 4 NF-e de mercadoria (R$ 13.843,05; CFOP 1.556 acum. 106 e 2.556 acum. 206) sem conferência com XML; (2) o acum. 206 da Biodental 76043 gerou crédito de ICMS R$ 42,57 e o Domínio mostra saldo credor de ICMS R$ 164,94 num cliente não contribuinte (em ago eram "apenas informativas"); (3) IBS/CBS: Portal tem CBS R$ 494,84 e IBS R$ 54,87 nas emitidas e o Domínio mostra débitos zero (créditos 33,87 e 3,77): ajuste de acumulador no pós-fechamento; (4) FAT 016 ainda sem set; (5) guias de PIS/COFINS e IRPJ/CSLL ainda não geradas; (6) saldo credor de IRRF R$ 0,01.
TSV consolidado entregue em 17/10 (inclui a correção do PIS de ago, R$ 770,94).
```tsv
16	Set2026	SERVIÇOS PRESTADOS	Importado	142642,60	Domínio (Serviços 17/10) = Portal Emitidas = DecWeb: 221 NFS-e normais (nº 2823 a 3043, sem lacunas), R$ 142.642,60; 6 notas de 10/2026 (R$ 2.340,00) fora da competência.	
16	Set2026	SERVIÇOS TOMADOS	Importado	753,49	Domínio (Entradas 17/10) = Portal Recebidas: 4 NFS-e R$ 753,49 (Clinicorp 7589 e 17980, Icarus 13234, Ambientuus 381951); ISS, IRRF e contribuições sem retenção; declaração DecWeb sem imposto retido.	
16	Set2026	ENTRADAS	Pendente	14596,54	Em andamento: Domínio Entradas R$ 14.596,54 (tomados R$ 753,49 + 4 NF-e de mercadoria R$ 13.843,05); falta conferir as 4 NF-e com os XMLs e o ICMS (R$ 42,57) do acum. 206 da Biodental 76043 em cliente não contribuinte.	
16	Set2026	DARF PIS	Pendente	927,18	Domínio: base R$ 142.642,60 x 0,65% (método agregado; soma nota a nota daria R$ 927,58). Venc. 23/10. Guia ainda não gerada/subida no G-Click.	
16	Set2026	DARF COFINS	Pendente	4279,28	Domínio: base R$ 142.642,60 x 3%. Venc. 23/10. Guia ainda não gerada/subida no G-Click.	
16	Set2026	DARF IRPJ	Pendente	27918,30	3º tri: receita R$ 423.978,80 x 32% = base R$ 135.673,22; IRPJ 15% R$ 20.350,98 + adicional 10% R$ 7.567,32 = R$ 27.918,30 (= Domínio). Rendimentos zerado. Venc. 30/10; cota única ou até 3 cotas de R$ 9.306,10 (confirmar).	
16	Set2026	DARF CSLL	Pendente	12210,59	3º tri: base R$ 135.673,22 x 9% = R$ 12.210,59 (= Domínio). Venc. 30/10.	
16	Ago2026	DARF PIS	Enviado	770,94	Correção: guia SENDA de 14/09 (doc. 07.16.26257.8748597-1) traz PIS R$ 770,94 (método agregado), igual ao EFD-Contribuições 08/2026; os R$ 771,31 eram a soma nota a nota (diferença R$ 0,37).	
```

## Rendimentos e IBS/CBS (17/10/2026)
- Planilha `CONTROLE | Rendimentos`, aba 3ºTRIM 2026, linha 16 QUALIDENTE: LIBERADO FISCAL = `Zerado` (observação Ø). FAT sem rendimentos financeiros.
- IBS/CBS, prestados (acumulador 900; Domínio com débitos zero porque o acumulador não relaciona 183-IBS/184-CBS): as 221 notas de 09/2026 do Portal têm todas CST 200, cClassTrib 200029 (serviços de saúde humana), cIndOp 030101, CBS 0,90% nominal com redução 60% (0,36%), IBS estadual 0,10% com redução 60% (0,04%), IBS municipal 0,00%; base IBS/CBS = valor - PIS - COFINS (total R$ 137.435,74); esperado após o ajuste: CBS R$ 494,84 e IBS R$ 54,87.
- Tomados (acumulador 800): Portal CST 000 / cClassTrib 000001, base R$ 737,50, CBS R$ 6,64 e IBS R$ 0,74; o Domínio mostra créditos de CBS R$ 33,87 e IBS R$ 3,77 (maiores: diferença de R$ 27,23 e R$ 3,03, origem não identificada, talvez NF-e).

## Entradas 09/2026 — conferência dos XMLs (17/10/2026)
XMLs na SIEG (Setembro). Todos os valores e datas batem com o Domínio (total R$ 14.596,54).
| NF | Fornecedor | Valor | Observação |
|---|---|---|---|
| 9167 | Distribuidora Dentária Bassanello | 4.949,07 | Simples (CSOSN 400), mesma UF, ICMS 0, 28 itens CFOP 5102 |
| 37276 | Dental Ortholay | 5.748,70 | Simples (CSOSN 102/500), ICMS 0, boleto |
| 25042 | Medlog | 2.197,50 | Simples, 4 itens, 3 duplicatas |
| 76043 | Biodental (SC) | 947,78 | CRT 3, venda interestadual a não contribuinte; ICMS 42,57 (4%/12%); DIFAL R$ 118,58 devido pelo vendedor; IBS 0,95 / CBS 8,53 |
PONTO DE ATENÇÃO: crédito de ICMS R$ 42,57 no acum. 206 (Biodental 76043) parece indevido (Qualidente é prestadora de serviços, não contribuinte de ICMS). Revisar acumulador; créditos IBS/CBS das entradas só pós-fechamento (ano-teste informativo). Sem crédito de ICMS nas demais (Simples).

## Conferência IBS/CBS pós-ajustes (17/10/2026, relatórios Domínio salvos de novo)
- Entradas: ICMS removido (base 0, ICMS 0; Biodental 76043 em duas linhas do acum. 206: 889,68 + 58,10 = 947,78). Total Entradas 14.596,54 e Serviços Tomados 753,49 inalterados. Prestados 142.642,60.
- Resumo dos Impostos (13:45): IBS débito 54,87 / crédito 3,77 / a recolher 51,10; CBS débito 494,84 / crédito 33,87 / a recolher 460,97. Débitos = esperado (CBS 494,84, IBS 54,87) -> ajuste dos prestados OK.
- Origem dos créditos do Domínio (conferido): XML 9167 Bassanello (IBSCBSTot: IBS 2,82, CBS 25,34) + XML 76043 Biodental (IBS 0,95, CBS 8,53) = CBS 33,87 e IBS 3,77 (batem exatamente). XMLs 37276 Ortholay e 25042 Medlog: sem grupo IBS/CBS.
- NFS-e tomadas (Portal, 4 notas, CST 000 / cClassTrib 000001): CBS 0,75+1,62+4,20+0,07 = 6,64; IBS 0,08+0,18+0,47+0,01 = 0,74. NÃO estão nos créditos do Domínio (acum. 800 sem relacionar 183/184).
- Após ajustar o acumulador 800: créditos esperados CBS 40,51 e IBS 4,51 (saldo CBS 454,33 e IBS 50,36). Informativo em 2026.
