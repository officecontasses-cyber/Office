# Cliente 205 — L S BECKER ANESTESIA (L Schmeling Becker Anestesiologista), Porto Alegre/RS

CNPJ 33.992.781/0001-05, IM 622430-2-0. Lucro Presumido, anestesiologia (cód. 040101), ISS 2%. Rendimentos 3ºTRIM 2026: LIBERADO FISCAL = **Zerado** (Ø). Cadastro duplicado "1205" no Domínio a conferir.

## IBS/CBS — ANOTAR PARA PÓS-FECHAMENTO (pedido da Fernanda, 18/10/2026)
Domínio ao importar os prestados de setembro avisa em cada nota: "O imposto 183-IBS / 184-CBS não está relacionado ao acumulador 900. Os dados serão descartados." (notas 192 a 210; nota 207 ainda alerta sobre cadastro de 'Clientes'). Portal Emitidas (17 notas válidas de 09/2026): CBS total 696,27; IBS total 77,38 (CST 200, cClassTrib 200029, saúde humana). Ajustar acumulador 900 (183/184) depois do fechamento.

## Preparação 09/2026 (18/10/2026)
- Portal Emitidas (03/10): 24 notas; 09/2026: 19 (192–210) — **196 Substituída** (por 197), **194 Cancelada** (R$ 3.000,00): válidas 17 = **R$ 95.753,11** = Declaração Prefeitura (recibo 03/10 12:26:41) = FAT. 5 notas (211–215, R$ 32.277,87) são competência 10/2026.
- Retenções federais em set (COOPA 192 e 205; Abastecedora Mania 203): IRRF **245,30**; PIS 106,30 + COFINS 490,59 + CSLL 163,53 = 760,42 (Portal 760,41). FAT set mostra retenções **zero** (a lançar).
- Sem Recebidas de 09/2026 no Drive (Portal só gerou Emitidas); agosto teve Officecont 997 (R$ 740,80).
- Controle Set2026: REINF Enviado (12/10, R-2099); Declaração Enviado; Guia ISSQN 1.915,06 Enviado (G-Click 09/10); Tomados, Prestados, DARFs, SPED em branco.
- Domínio set/2026: sem relatórios do 205 na pasta 008 ainda (só o aviso IBS/CBS da importação, print).
## Apuração esperada (cálculo meu, conferir com o Domínio)
- PIS 622,40 − ret. 106,30 = **516,10**; COFINS 2.872,59 − ret. 490,59 = **2.382,00** (venc. 23/10; FAT mostra 622,40/2.872,59 sem retenções; "compensações": crédito de IRPJ 03/2026 esgotado em 17/08, a confirmar se há outro crédito).
- 3ºTRIM: receita 332.357,16 (jul 199.218,05 + ago 37.386,00 + set 95.753,11) x 32% = 106.354,29. IRPJ 15% 15.953,14 + **adicional 10% sobre (106.354,29 − 60.000) = 4.635,43** − IRRF 435,11 = **~20.153,46**. CSLL 9% 9.571,89 − retida 470,07 = **~9.101,82**.
- **ALERTA FAT:** o FAT mostra IRPJ 3ºTRIM 15.763,33 e CSLL 9.265,35 **sem o adicional de IRPJ** (não há linha de adicional no FAT do 205, como há no 189) e sem as retenções de set. Corrigir antes de gerar a guia (venc. 30/10; pode ser 3 cotas).

## Conferência 18/10/2026 (Domínio salvo, FAT corrigido) — CONFERIDO
- Domínio Serviços: 192–210 = 95.753,11 (notas 194 cancelada e 196 substituída lançadas com 0,00); ISS 1.915,06; IRRF 245,30; PIS-RET 106,30; COFINS-R 490,59; CSOC-RET 163,52 (Portal 163,53, 1 centavo).
- Domínio Resumo: PIS **516,10**; COFINS **2.382,00**; IRPJ base 106.354,29 → 15.953,14 − IRRF 435,11 + adicional 4.635,43 = **20.153,46**; CSLL 9.571,89 − 470,06 = **9.101,83** (FAT 9.101,82, 1 centavo). IBS/CBS 0.
- Entradas do Domínio: só NFS-e 1040 Officecont (emissão 05/10, entrada 30/09, CFOP 1-933, AC 800, R$ 740,80): é serviço tomado (vai em TOMADOS, não ENTRADAS). Portal Recebidas do 205 **não está no Drive**; Tomados fica `Pendente` até conferir.
- FAT corrigido: retenções set (IRRF 245,30; PIS 106,30; COFINS 490,59; CSLL 163,53), PIS 516,10, COFINS 2.382,00, IRPJ 3ºTRIM 20.153,46, CSLL 9.101,82, adicional 4.635,43.
- Controle (export 18/10 ~20:50): Prestados, Tomados e DARFs ainda em branco no 205.

## Guias 09/2026 (18/10/2026, G-Click 17:59 — print da Fernanda)
- PIS/COFINS: 07.16.26291.8654338-4, total 2.898,10 (COFINS 2172 2.382,00 + PIS 8109 516,10), venc. 23/10, recibo declaração 50000540042351.
- IRPJ/CSLL 3ºTRIM **cota única**: 07.16.26291.8655276-6, total 29.255,29 (IRPJ 2089 20.153,46 + CSLL 2372 9.101,83), venc. 30/10.
- G-Click: "Darf Pis / Cofins" e "CSLL E IRPJ" concluídos por fernanda.officecont em 18/10 17:59 (print sem a linha "Envio ao cliente"). TSV: DARFs `Enviado`.
- Portal Recebidas do 205: **rodar de novo** (a Officecont 1040 foi emitida em 05/10, depois da rodada de 03/10): `python portal_nacional_download.py --competencia 09/2026 --clientes 205` em `C:\Robos\portalnacional`.
