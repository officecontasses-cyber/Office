# Cliente 177 — ILS CONSULTORIA EMPRESARIAL E TECNOLOGIA DA INFORMAÇÃO EIRELI (preparação 09/2026, 18/10/2026)

## Cadastro
CNPJ 24.577.763/0001-68, Porto Alegre/RS, IM 282680-2-4, **Lucro Presumido**, não contribuinte de ICMS; CNAE 7020400 e 6204000; sócio-administrador Mario Guilherme Sebben (grupo RFL/CC&D). **Sem certificado no PC** (cliente envia as notas; Inês). Único cliente: **DATASYS SISTEMAS EM INFORMÁTICA LTDA (01.821.978/0001-87)**, que **retém IRRF 1,5% e CSRF 4,65%** em todos os meses.

## Controle_Fiscal Set2026 (export 18/10)
`REINF` Enviado (R-2099 12540600-03-2099-2609-12540600, 04/10; provisório, aguarda movimento da Inês); `DECLARAÇÃO PREFEITURA` Enviado (recibo 03/10 11:20:39, receita 26.520,00, ISS 530,40); `GUIA ISSQN` Enviado 530,40 (G-Click 04/10). **Em branco:** TOMADOS, PRESTADOS, DARF PIS, COFINS, IRPJ, CSLL, SPED (16/11). Rendimentos (3ºTRIM 2026): `NT` (sem conta bancária).

## DecWeb (09/2026)
Prestados: 1 NFS-e, nº 13, 29/09/2026, Datasys, **R$ 26.520,00, ISS 2% = 530,40**, tributação no município, sem retenção de ISS (chave ...1326097821699638) = declaração = guia. Sem arquivo de tomados (Agosto teve Officecont 1001, R$ 626,15, Simples, ISS 0). Declaração: receita 26.520,00, devido 530,40, tomados 0,00.

## FAT 177 (editado até 01/09; setembro em branco)
Meses anteriores: receita 26.520,00/mês; retenções IRRF 397,80, PIS 172,38, COFINS 795,60, CSLL 265,20; ISSQN 530,40; IRPJ líquido 875,16 e CSLL líquida 498,58 por mês (= 26.520 x 32% x 15%/9% menos a retenção). **Para setembro (esperado, se a nota 13 teve a mesma retenção):** receita 26.520,00; IRRF 397,80; PIS 172,38; COFINS 795,60; CSLL 265,20 (ISSQN 530,40); IRPJ 875,16; CSLL 498,58. 3º tri: receita 79.560,00, base 25.459,20, IRPJ 3.818,88 − IRRF 1.193,40 = **2.625,48**; CSLL 2.291,33 − 795,60 = **1.495,73** (soma mensal 1.495,74); sem adicional. PIS/COFINS de set: devidos 172,38 / 795,60 = retenção (precedente de agosto: `Compensado`).

## Falta
Domínio 09/2026 (Entradas/Saídas/Resumo) e confirmação de que a **nota 13 (29/09) teve as retenções da Datasys** (pergunta pendente à Inês; precisa XML ou informe); digitar setembro no FAT; depois TSV de Prestados `Importado` 26.520,00, Tomados (sem nota?), DARFs PIS/COFINS `Compensado`, IRPJ (2.625,48) e CSLL (1.495,73) trimestrais (venc. 30/10), SPED 16/11.

## Domínio 09/2026 conferido (18/10/2026 11:41 a 11:43) — IBS/CBS fica para depois do fechamento
- **Serviços:** nota 13 (emissão 29/09, saída 28/09), Datasys, AC 900, **R$ 26.520,00, ISS 530,40** (= DecWeb = declaração = guia) e retenções **IRRF 397,80 (1,5%), PIS-RET 172,38, COFINS-R 795,60, CSOC-RET 265,20**: a Datasys reteve como em todos os meses (resolve a pergunta pendente).
- **Entradas:** só NFS-e 1037 Officecont (emissão 05/10, entrada 30/09, série 900, CFOP 1-933, **R$ 626,15**, Simples, ISS 0). **Não consta no DecWeb original** (tomados 0,00 na declaração de 03/10). CNPJ do 177 só existe no hub NFS-es do SIEG (sem NF-es/Entrada): sem NF-e de produtos.
- **Resumo:** ISS 530,40; PIS 172,38 e COFINS 795,60 integralmente retidos (a recolher 0; resíduos de centavos: PIS 0,04, COFINS 0,02); **IRPJ 3.818,88 − retido 1.193,40 = 2.625,48; CSLL 2.291,33 − retida 795,60 = 1.495,73** (base trimestral 25.459,20): = FAT esperado. IBS/CBS 0,00.
- **Advertências na importação (print):** 183-IBS e 184-CBS não relacionados ao acum. 900 (dados descartados; pós-fechamento) e data de saída 28/09 < emissão 29/09 (as duas em setembro: sem efeito na competência; não ajustar, regra de 13/10).
