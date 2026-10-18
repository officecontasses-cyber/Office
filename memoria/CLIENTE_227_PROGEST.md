# Cliente 227 — PROGEST GESTÃO DE PROJETOS LTDA (São Sebastião do Caí/RS)

CNPJ 45.087.762/0001-05. Lucro Presumido, consultoria (CNT 17.01.01, NBS 114011100), ISSQN 3% recolhido pela própria Progest (São Sebastião do Caí). Não consta no `Cadastro_Clientes` (só nas abas Jul/Ago/Set). Controle: Jul2026 `CLIENTE INATIVO`; Ago2026 linhas `Pendente` ("ANALISAR ACESSO" em Declaração/Guia); **entregas começam em 09/2026**. Rendimentos 3ºTRIM 2026: LIBERADO FISCAL = **NT** (sem conta bancária), obs. "SEM MOVIMENTO" (4ºTRIM em branco). Cadastro de Rendimentos foi incluído em 16/10 (PENDENCIAS).

## Preparação 09/2026 (18/10/2026)
- Controle Set2026: todas as linhas em branco (REINF, Tomados, Prestados, Declaração, Guia, DARFs, SPED).
- Agosto: `227_Progest_SãoSebastiãoDoCaí_08.2026_DeclaraçãoMensal.pdf` = "Comprovante de lançamento de sem movimento" (20/09) — as linhas de agosto na Controle continuam `Pendente`.
- **Manual NFS-e IBS/CBS (Officecont, 25/09/2026):** cita "uma nota real da Progest, de R$ 40.000,00, emitida em setembro de 2026" (IRRF 1,5% = 600; PIS 0,65% 260; COFINS 3% 1.200; CSLL 1% 400 se o cliente for PJ fora do Simples; ISS 3% = 1.200 pela Progest). **Isso indica receita em setembro** — confirmar no Portal Nacional (Emitidas) antes de qualquer `Sem movimento`.
- Drive: sem Emitidas/Recebidas de 09/2026 do 227 na pasta 003; sem Domínio do 227; FAT só 2023 (`227_PROGEST_FAT2023.xls`); certificado .pfx do 227 existe na pasta de certificados do Drive (⚠ a senha aparece no nome do arquivo — renomear/tirar do Drive; não reproduzir aqui).
- Se a nota de R$ 40.000,00 for a única do trimestre (hipótese, a confirmar): PIS 260 e COFINS 1.200 cobertos pela retenção (a recolher 0); 3ºTRIM base 32% = 12.800: IRPJ 1.920 − IRRF 600 = ~1.320; CSLL 1.152 − 400 = ~752; ISS 1.200 (vence conforme o município; conferir na guia).
## Pendências
Rodar Portal Nacional (certificado A1 instalado?) para o 227; REINF R-2099 (próximo da fila); declaração/guia ISS de São Sebastião do Caí (sistema a mapear; sem skill/gravação); Domínio; FAT 2026; ajustar linhas de agosto; incluir 227 no Cadastro_Clientes; IBS/CBS pós-fechamento (CST 000/000001 por manual).

## 18/10/2026 (tarde) — cmd do Portal e cadastro
- Print do cmd (18:06–18:15): **205** OK (login por certificado, CNPJ confirmado, Emitidas e Recebidas 09/2026 salvas na `003`); **227**: "Cliente(s) não encontrado(s) em clientes.csv: 227" (30 clientes carregados) → falta a linha em `C:\Robos\portalnacional\config\clientes.csv` (formato `numero,apelido,razao_social,cnpj,cidade`; sem acentos; sem senha).
- Dados do CNPJ (BrasilAPI 18/10): PROGEST GESTAO DE PROJETOS LTDA, nome fantasia PROGEST, Sociedade Empresária Limitada, ativa, início 31/01/2022, micro empresa, capital R$ 1.000, RS 122 nº 9798, Vila Conceição, CEP 95760-000, São Sebastião do Caí/RS; CNAE 7020-4/00 (consultoria em gestão empresarial); sec. 7119-7/99; sócio-administrador Leandro Mini; ECF 2023 = Lucro Presumido.
- Linha do `Cadastro_Clientes` (TSV, entra entre 209 e 237): `227	PROGEST	45087762000105	SAO SEBASTIAO DO CAI / RS	7020400 - Atividades de consultoria em gestão empresarial, exceto consultoria técnica específica	7119799 - Atividades técnicas relacionadas à engenharia e arquitetura não especificadas anteriormente	LEANDRO MINI (Sócio-Administrador)	Lucro Presumido	Obrigatório (Padrão Nacional)	NÃO	Isento / N/A` (IE e adesão: assumidos, a confirmar).
- Declaração de São Sebastião do Caí de 09/2026: **não há arquivo salvo no Drive** (só `08.2026_DeclaraçãoMensal.pdf`, "Comprovante de lançamento de sem movimento", 20/09).
