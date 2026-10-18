# Cliente 185 — PALAS ATENA (Rio de Janeiro/RJ)

CNPJ 23.774.370/0001-81. Lucro Presumido, holding com aluguel de imóveis próprios.
Prefeitura (Rio): Fernanda envia em outro local (18/10/2026) e libera depois.

## Fechamento 09/2026 (conferência de 18/10/2026)
- Portal Nacional rodado (18/10 11:57): só `185_PalasAtena_RioDeJaneiro_09.2026_Recebidas.xlsx`; sem Emitidas.
  Recebidas: 1 NFS-e nº 17021298, CERTISIGN (SP), R$ 189,68, competência **10/2026** (ISS 5,50 não retido, CBS 0,64, IBS 0,07, PIS 1,23, COFINS 5,69).
  Não é tomada de 09/2026.
- FAT 185 (modificado 13/10): receita aluguéis set 3.832,51 (3ºTRIM 12.270,20; ago 4.261,77; jul 4.175,92);
  PIS 24,91; COFINS 114,98; IRPJ 3ºTRIM 477,67 (set 183,96); CSLL 3ºTRIM 353,62 (set 110,38); CSLL a compensar 12/2025: 10,41.
  Rendimentos financeiros set 0,00; IRRF s/ resgates 0,00.
- Rendimentos (3ºTRIM 2026): LIBERADO FISCAL = Sim.
- Controle Set2026: só REINF Enviado; demais linhas em branco.
- Domínio: nenhum relatório 185 encontrado em `008 ARQUIVOS DOMÍNIO`/09_SETEMBRO (busca 18/10). Há `185-Recibo DCTF Web 092026.pdf` (14/10) em outra pasta.

## Pendências
- Domínio (Entradas/Saídas/Serviços/Resumo) a salvar para conferir.
- GMA Imobiliária (taxa de administração, ~R$ 305,77/mês, sem NFS-e) — confirmar se lançada.
- Prefeitura/ISSQN (Rio) e DARFs: aguardam Fernanda; DARF só `Enviado` com G-Click.
- IBS/CBS: pós-fechamento.

## Atualização 18/10/2026 (Domínio salvo)
- Rendimentos 3ºTRIM 2026: 185 = **Sim**, observações em branco (não é "Zerado"; há rendimento no trimestre: ago 1,86, IRRF 0,36, já no FAT; set 0,00). Obs.: na aba 3ºTrim 2025 consta "CLIENTE ESTA PROVIDENCIANDO, 14/10" (aba antiga, só informativo).
- Domínio (Empresa 185, Resumo, emissão 18/10 12:11): PIS 24,91 e COFINS 114,98 = FAT. IBS/CBS/ISS zerados.
  **Divergência:** IRPJ/CSLL com base 12.272,06 (= receita 12.270,20 + 1,86 a 100%, sem presunção 32%): CSLL 1.104,49 / IRPJ 1.840,81 (a recolher 1.104,56 e 1.729,24). FAT usa 32%: IRPJ 477,67 e CSLL 353,62. Parametrização de presunção do aluguel no Domínio a corrigir antes das guias (IRPJ/CSLL 30/10).
- Prefeitura Rio: Confirmação de Ausência de Movimento SET/2026, doc 0016911212, emitida 18/10 12:02 (`185_Palas_RioDeJaneiro_09.2026_DeclaraçãoMensal.pdf`).
- Sem Entradas/Saídas/Serviços do 185 no Drive (sem movimento).

## Domínio corrigido (18/10/2026 12:27)
Base IRPJ/CSLL 3.928,32 (= 12.270,20 x 32% = 3.926,46 + rend. 1,86). IRPJ 589,25 - IRRF 0,36 - saldo anterior 111,21 = **477,68 a recolher** (FAT 477,67; 1 centavo). CSLL 353,55 + 0,07 (resíduo do 2ºTRIM, FAT também 353,62) = **353,62**. PIS 24,91 / COFINS 114,98. Total federal 971,19 + ... (PIS/COFINS 139,89). Vence 30/10 (PIS/COFINS 23/10). FAT: "CSLL a compensar 12/2025 10,41" não aplicado no Domínio — decidir. TSV: DARF IRPJ 477,68 e CSLL 353,62 `Pendente` até G-Click.
