# Processo do fechamento 09/2026 — mapa e memória (atualizado em 04/10/2026)

Documento vivo. Complementa `PENDENCIAS.md` (o que está pendente) com **o fluxo, onde cada etapa está e o que já foi decidido**.
Regras que não mudam: ver `CLAUDE.md`. Guia só é `Enviado` com comprovação do G-Click; nada vai direto na Controle_Fiscal (TSV inline → aba `Atualizações` → `processarAtualizacoes()`).

## 1. Fluxo mensal (POP) e quem faz cada etapa

| # | Etapa | Quem | Ferramenta / fonte |
|---|---|---|---|
| 0 | Prioridades do mês: Tacom (138, 263) no dia 1; Lopes & Nadal (186) só com documentos | Fernanda | CLAUDE.md |
| 1 | Municipal POA: declaração + guia ISSQN | Robô DecWeb (PC dela) + Claude confere PDFs no Drive | `decweb_login.py --fase T --enviar` |
| 2 | Portal Nacional: baixar Emitidas/Recebidas (clientes com certificado A1) | Robô Portal (PC dela) | `portal_nacional_download.py` |
| 3 | Conciliação DecWeb × Portal (chave de acesso, nota a nota) | Robô de conciliação (PC dela) + Claude analisa | `decweb/conciliacao.py` |
| 4 | Guias ISSQN: upload em lote + envio ao cliente | Fernanda (G-Click) | skill `upload-envio-guias-gclick` |
| 5 | Registro das etapas 1–4 | Fernanda cola TSV | aba `Atualizações` |
| 6 | **Importação no Domínio** (escrituração das notas) | **Fernanda** | Domínio Sistemas |
| 7 | **Conferência XML × Prefeitura × Domínio** (Etapa 1 do POP) | **Claude, a partir do comando salvo no Drive** | skill `conferencia-xml-prefeitura-dominio` (cópia: `ARQUIVOS EXTENSÃO - CODE - CLAUDE/…/conferencia-xml-prefeitura-dominio__SKILL.md`) |
| 8 | Federais: PIS/COFINS (mensal), IRPJ/CSLL (trimestral), REINF | Claude calcula; Fernanda gera/posta | skills de apuração + SENDA + G-Click |
| 9 | FAT do cliente | Claude indica célula e valor; Fernanda digita | `NNN_NOME_FAT2026`, aba 2026 |
| 10 | Consolidação e registro definitivo | Claude monta TSV; Fernanda cola | `consolidacao-fechamento-pre-registro` |

Regras da conferência no Domínio (resumo da skill): comparar **por número de nota** (não só total); Portal filtrado por Competência = mês e Situação = Normal; notas canceladas aparecem no Domínio com valor e alíquota zero; checar retenções (ISS, IRRF, CSRF) e **cadastro da contraparte** (UF × CFOP, CPF/CNPJ, acumulador uniforme, duplicidade, IE); sempre declarar quais das 5 fontes (002, 003, 006, 007, 008) foram consultadas. Esta etapa é só análise: não registra nada em planilha.

## 2. Linha do tempo de 09/2026 (o que já foi feito)

- **01/10** — DecWeb: 16, 18, 117, 133. Regra do prazo: ISSQN POA 09/2026 vence **13/10** (o 09/10 usado antes estava errado; vale a data impressa na guia).
- **02/10** — Tacom: 138 e 263 (declaração; guia do 263 R$ 4.089,69 com G-Click 14:03). Portal Nacional rodou com sessão vazada (baixou dados do 238 para todos): robô corrigido para apagar a sessão antes de cada login; `configuracao.py` do Portal renomeado `portal_config.py`.
- **02–03/10** — Cliente novo **265** BELEM BRASIL: Controle_Fiscal (script rodado), DecWeb (fase T com pendência do responsável, depois enviada), Portal Nacional (certificado A1), SIEG/G-Click/Domínio (Fernanda). Prazos definidos (`definirPrazosSet2026`: 13/10 ×46).
- **03/10** — DecWeb em lote: 10 declarações (11:16–11:26) + 205 (12:26) + 173, 152, 238 (14:02–14:04). Portal Nacional rodado para os 19 clientes com certificado. `conciliacao.py` criado e rodado no PC dela.
- **04/10** — Portal: 117, 247, 258 `sem_movimento` (aceito, coerente com recibos). **186** (documentos recebidos): Portal (E5/R2) → DecWeb enviado 11:26 (receita R$ 11.475,05, guia R$ 422,87). G-Click 11:34: 9 guias subidas (16, 18, 152, 173, 177, 186, 189, 238, 241). FAT do 186: receita de setembro a digitar (R$ 11.475,05).

## 3. Quadro de Porto Alegre (DecWeb) — 04/10/2026

Declarações: **22 de 22 enviadas** (inclui 265 sem movimento).
Guias ISSQN:

| Situação | Clientes (valor) |
|---|---|
| Subidas no G-Click 04/10 (aguardam o check de "Envio ao cliente") | 16 (422,87) · 18 (42,00) · 152 (461,69) · 173 (422,87) · 177 (530,40) · 186 (422,87) · 189 (634,31) · 238 (609,54) · 241 (2.403,15) = **5.949,70** |
| Seguradas | 155 (842,02, aguarda Camila) · 257 (6.500,00, analisar segunda) · 205 (1.915,06, nota de R$ 6.000,00 só no DecWeb) = **9.257,08** |
| Já enviada | 263 Tacom (4.089,69) |
| Sem movimento / sem guia | 138, 117, 258 (confirmar lançamento), 2, 26, 209, 237, 265 (confirmar) |

Conciliação Portal × DecWeb (03/10): sem divergência em 16, 155, 189, 238, 241, 257; divergência em 152 (1 nota de R$ 42,00 só no Portal, ISS igual) e 205 (nota de R$ 6.000,00 só no DecWeb). Sem Portal (sem certificado): 2, 18, 26, 133, 138, 173, 177, 209, 263.

## 4. Pontos de atenção abertos para a etapa 6–7 (Domínio)

1. **Notas 151 e 152 do 186** (R$ 4.475,05 + R$ 3.792,00 = R$ 8.267,05): emitidas em 03/09, competência 08/2026 no Portal. **Resolvido por Fernanda em 04/10: o Domínio considera a DATA DE SAÍDA**, então elas ficam em agosto e o Domínio de 09/2026 do 186 deve trazer só as 3 notas de setembro (R$ 11.475,05), igual à declaração e à FAT. (A regra 02-D das lições, que falava em data de emissão, não vale para a data de saída.) Conferir na hora que o export de setembro não traz 151/152.
1b. **Importação do 186 no Domínio (04/10):** 3 notas de serviço (153 R$ 2.500,00 · 154 R$ 4.475,05 · 155 R$ 4.500,00 = R$ 11.475,05, batem com o Portal). Advertências: imposto 183-IBS e 184-CBS não relacionados ao acumulador 900 ("os dados serão descartados"); nota 153 com data de saída 29/09 menor que a emissão 30/09; nome da contraparte da 154 aparece como "ANDERLISE4 ADRIANE…" (possível erro de cadastro). 2026 é ano-teste: IBS/CBS informativos, sem efeito na apuração. Configuração do acumulador (900 prestados, 800 tomados) em andamento.
   - **Acumulador 900 do 186** ("P. SERVIÇO A VISTA (ISS NO MUNICÍPIO)", vigência 09/2026 LUCRO PRESUMIDO), aba IVA > IBS, como estava em 04/10: cClassTrib 000001 (tributação integral), CST 000, alíquota 0,10. Aba CBS ainda não vista.
   - **O que o XML das 3 notas de 09/2026 traz (prestados, arquitetura):** CST 200 (alíquota reduzida), cClassTrib 200052 (serviços de profissões intelectuais), redução de 30%; CBS 0,90% nominal → 0,63% efetiva; IBS estadual 0,10% → 0,07%; IBS municipal 0,00%; base IBS/CBS = valor da nota menos PIS e COFINS. Valores por nota (BC · CBS · IBS): 153 = 2.408,75 · 15,18 · 1,69; 154 = 4.311,71 · 27,16 · 3,02; 155 = 4.335,75 · 27,32 · 3,04; totais CBS 69,66 e IBS 7,75.
   - **Tomados (Google, SP):** CST 000, cClassTrib 000001, CBS 0,90% e IBS 0,10% sem redução (nota 22,50: BC 19,77 · CBS 0,18 · IBS 0,02).
   - Não confirmado: se o Domínio lê esses dados do XML ou do acumulador. Teste: importar e comparar com os valores acima.
2. Recebidas do 186: Google (SP) R$ 288,28 (competência 08, gerada 02/09) e R$ 22,50 (competência 09, gerada 02/10), ISS não retido.
3. 257: ISS 7.262,54 com retido só 762,54 — conferir se os tomadores deveriam ter retido (segunda 05/10).
4. 152: ISS retido de Estrela/RS (R$ 106,75) fora da guia de POA: declarar no portal de Estrela (inferência a confirmar).
5. Rodrigo Tavares Lopes (mesmo CPF) aparece como profissional nos clientes 16 e 173: verificar.
6. Cadastro de contraparte no Domínio: 189 (Guntner/Frost Frio) já aparece como pendência antiga.

## 5. O que falta para fechar 09/2026

- Fernanda: conferir "Envio ao cliente" das 9 guias → TSV `Enviado`; importação das notas no Domínio (por cliente); digitar a receita no FAT do 186; PIS/COFINS do 186 (R$ 74,59 + R$ 344,25, vence 23/10) e IRPJ/CSLL do 3º trimestre (vence 30/10).
- Claude: conferir o Domínio × DecWeb × Portal assim que ela disponibilizar o export em `008 ARQUIVOS DOMÍNIO` (pasta `09_SETEMBRO`); começar pelo 186 e depois pelos clientes com divergência (152, 205), seguindo a ordem de prioridade.
- Datas: segunda 05/10 (ligar para a Leidislaine antes das 11:00), quarta 07/10 (SPED Fiscal Tacom), 13/10 (ISSQN), 14/10 (certificado do 258), 15/10 (REINF e EFD de 08/2026), 23/10 (DARF PIS/COFINS), 30/10 (IRPJ/CSLL), 16–31/10 (REAT 238).
- Clientes de outros municípios (71 Brasília, 126 São Leopoldo, 197 e 261 Novo Hamburgo, 247 Montenegro, 264 Brasília): fluxo municipal fora do DecWeb, não tratado nesta sessão; ver planilha.

## 6. Conferência Domínio × DecWeb × Portal — cliente 186 (04/10/2026, 12:13–12:16)

Fontes consultadas: 002 (declaração e guia ISSQN do DecWeb), 003 (Portal Emitidas/Recebidas), 008 (Acompanhamento de Serviços, de Entradas e Demonstrativo dos Impostos de 09/2026). **Não** consultados: XMLs da 006 e da 007 (o Portal já traz os campos de IBS/CBS por nota).

| Item | Domínio | DecWeb / Portal / FAT | Resultado |
|---|---|---|---|
| Serviços prestados 09/2026 | 153 (2.500,00) · 154 (4.475,05) · 155 (4.500,00) = 11.475,05, acumulador 900, ISS 0 | Portal e declaração: 11.475,05 | Bate |
| Entradas | Google 39097102, 22,50, CFOP 2-933, AC 800, UF SP (entrada 30/09, emissão 02/10) | Portal Recebidas 22,50 | Bate; nota 38618431 (288,28) fica em agosto |
| Retenções | todas zero | notas "não retidas" | Bate |
| Receita do 3º trimestre | 27.411,35 (base 32% = 8.771,63) | FAT: 7.669,25 + 8.267,05 + 11.475,05 | Bate (confirma que 151/152 estão em agosto) |
| IRPJ do trimestre | 1.315,74, adicional 0,00 | previsão 1.315,74 | Bate |
| CSLL do trimestre | 789,45 | previsão 789,45 | Bate |
| IBS | débitos 7,75 · créditos 0,02 · saldo 7,73 | previsão 7,75 / 0,02 | Bate (acumulador ajustado funcionou) |
| CBS | débitos 69,66 · créditos 0,18 · saldo 69,48 | previsão 69,66 / 0,18 | Bate |
| **ISS por profissional** | **403,97** | guia da prefeitura e FAT: **422,87** | **Diverge R$ 18,90** (403,97 ÷ 70 = 5,7710 por UFM; 422,87 ÷ 70 = 6,0411). Parâmetro do valor do ISS por profissional no Domínio provavelmente desatualizado (a confirmar) |

Pontos de atenção: nota 153 segue com data de saída 29/09 (emissão 30/09), sem efeito na competência; cadastro do cliente 32 segue como "ANDERLISE4 ADRIANE KLEIN ZIMMER" (nome diferente do Portal; CPF 756.694.470-34 confere); demonstrativos de PIS e COFINS não vieram no PDF (previsão: PIS 74,59 e COFINS 344,25); IBS/CBS em 2026 são informativos (sem recolhimento, segundo as notas do escritório). Pendência: DARF IRPJ (2089) e CSLL (2372, conferir no SENDA) do 3º trimestre, vencimento 30/10.

## 7. Federais do 186 — 04/10/2026

- DARF de PIS e COFINS (SENDA, 04/10 12:45:04), PA 09/2026, vencimento 23/10/2026, **total R$ 418,84**: COFINS cód. 2172 = 344,25; PIS cód. 8109 = 74,59. Confere com o Domínio (Consulta Apuração) e com a previsão pelas NFS-e.
- G-Click (upload 04/10 12:45): tarefa COFINS / PIS do 186 casou e marcou "Darf Pis / Cofins" (fernanda.officecont). **Falta o check de "Envio ao cliente"**; só então vale `Enviado` na Controle_Fiscal (DARF PIS 74,59 e DARF COFINS 344,25).
- ISSQN do 186 (R$ 422,87) já foi enviado antes, sozinho (04/10 11:34), porque vence 13/10; a regra "ISSQN junto com os demais impostos" não pôde ser cumprida, pois IRPJ/CSLL (vencem 30/10) aguardam o contábil.
- IRPJ (1.315,74) e CSLL (789,45) do 3º trimestre: provisórios, dependem de rendimentos financeiros e IRRF informados pelo contábil.
- **REINF 186 (04/10):** R-2099 Fechamento dos Eventos Periódicos, competência 09/2026, **Sucesso**, recibo 12122144-09-2099-2609-12122144, enviado 04/10/2026 12:50, ambiente Oficial. G-Click: tarefa "EFD Reinf - (Ativo)" com a atividade "Recibo" concluída por fernanda.officecont em 04/10 12:51 (vencimento 15/10, meta 13/10). Relatório lista só o R-2099 (sem R-2010/R-2020/R-4010/R-4020). Retenções do mês: nenhuma (prestados "não retido", IRRF e contribuições retidas 0,00; única entrada é a Google/SP sem retenção; Domínio com retenções zeradas) → "Sem movimento" na planilha do DP. Pergunta em aberto: houve distribuição de lucros ou pagamento a pessoa física em setembro (R-4010)? A ausência no relatório só mostra que não foi enviado.
- **Planilha do DP** (`CONTROLE | DP REINF'S`): abas `MOD GERAL MM.2026`; no layout de 08.2026 cada linha é Nº · Empresa · Obrigação · Status · Observações (Sem movimento / COM RETENÇÃO) · detalhes · "ok". A aba de 09.2026 não apareceu na leitura (última lida: 08.2026); Fernanda atualiza a linha do 186 (nunca escrevemos no DP).

## 8. Auditoria da Controle_Fiscal para o 186 (04/10/2026, 12:54 — planilha lida no Drive)

Já lançado e processado: DECLARAÇÃO PREFEITURA (Enviado), GUIA ISSQN 422,87 (Enviado, G-Click 11:34 + envio ao cliente), DARF PIS 74,59 e DARF COFINS 344,25 (Enviado). Fila `Atualizações` vazia de pendências do 186.
**Faltava na Set2026:** REINF (sem status), SERVIÇOS PRESTADOS (11.475,05), SERVIÇOS TOMADOS (22,50), DARF IRPJ e DARF CSLL (pendentes do contábil). TSV entregue para os cinco itens. SPED CONTRIBUIÇÕES de 09/2026 vence 16/11 (sem ação agora). **Ago2026 do 186: SPED CONTRIBUIÇÕES ainda Pendente, vence 15/10.**
Conferência do DecWeb (relações ISSQNdec 09/2026): prestados 153/154/155 = 11.475,05, ISS 0 (sociedade de profissionais) e chaves iguais às do Portal; tomados: Google 22,50 com ISS 0,65 devido em SP (não retido, sem recolhimento pelo tomador).
Regra anotada: o status `Enviado` já tinha sido colado pela Fernanda; conferir sempre a planilha antes de repetir pendência.

## 9. SPED Contribuições 08/2026 do 186 (vence 15/10/2026) — preparação em 04/10

- Regime: Lucro Presumido, PIS/COFINS cumulativos (0,65% / 3%), prestação de serviços (arquitetura). Sem créditos no Bloco M (vedado no cumulativo); retenções F600: nenhuma.
- Fontes de agosto conferidas no Drive (`008 ARQUIVOS DOMÍNIO`, 08_AGOSTO): Serviços 186 (gerado 18/09): notas 151 (4.475,05) e 152 (3.792,00), emitidas em 03/09 com **data de saída 31/08**, AC 900, total R$ 8.267,05. Entradas 186: Officecont nota 996 (R$ 612,40, CFOP 1-933, AC 800) e Google nota 38618431 (R$ 288,28, CFOP 2-933, UF SP, AC 800, emissão 02/09, entrada 31/08), total R$ 900,68.
- **Valores esperados no PVA:** M200 (PIS cód. 8109-02, cumulativo) = **R$ 53,74** sobre base 8.267,05; M600 (COFINS cód. 2172-01) = **R$ 248,01**. Batem com os DARF de agosto (PIS 53,74 e COFINS 248,01, G-Click 07/09 16:04).
- DCTFWeb 08/2026 (guia 07.16.26253.1195912-6, R$ 1.005,02, vencimento 18/09, recibo 50000526102454): só INSS de contribuintes individuais (pró-labore): cód. 1099 = 356,62 e cód. 1138 = 648,40. PIS/COFINS não constam na DCTFWeb (o débito vai pela MIT; não verificado).
- Arquivo a gerar no Domínio: `EFD_contribuições0000186.txt`, pasta `08_AGOSTO\010 EFD CONTRIBUIÇÕES` (padrão das competências anteriores: os arquivos de 07/2026 estão em `07_JULHO\010 EFD CONTRIBUIÇÕES`). Fluxo no PVA: Nova > Importar (Ctrl+I) > validar > conferir M200/M600 > assinar > transmitir (checkpoint humano na assinatura).
- Em 07/2026 o 186 passou sem erro estrutural (os erros do reg. 0120 foram 026, 173, 185, 189, 197, 209, 258).
- **Correção de rota (04/10 16:08):** a pasta que a Fernanda criou em `08_AGOSTO` chamava-se `0010 EFD CONTRIBUIÇÕES`; renomeada para **`010 EFD CONTRIBUIÇÕES`** (padrão de julho). O código do PIS cumulativo é 8109-02 (M205 = 810902), não 8109-01 como anotado antes.
- **Conferência do arquivo `EFD_contribuições0000186.txt` (gerado 04/10 16:04, 1.679 bytes):** período 01/08–31/08/2026, CNPJ 28.516.249/0001-73 (dígitos verificadores conferem), IBGE 4314902, inscrição municipal 28993128, 0110 = cumulativo, escrituração consolidada (F550), conta 411. F550: receita 8.267,05, PIS 0,65% = 53,74, COFINS 3% = 248,01; 1900: 2 documentos. M200 = 53,74 (M205 810902); M600 = 248,01 (M605 217201); M210/M610 CST 51. Contadores de registros consistentes (0990=7, F990=4, M990=8, 1990=3, 9990=37, 9999=67, 9900|9900=34). Estrutura idêntica à de 07/2026 (arquivo assinado, 0100 e 0140 iguais; julho = 7.669,25, PIS 49,85, COFINS 230,08). Falta: importar no PVA, validar (0 erros), assinar e transmitir até 15/10; depois registrar o recibo na Ago2026 (SPED CONTRIBUIÇÕES do 186).
- **SPED Contribuições 08/2026 do 186 TRANSMITIDO em 04/10/2026 às 13:11:36** (Original, ReceitaNet/SERPRO, PVA 6.2.0). Identificação do arquivo 1EB24004D73D4310AC56D9473607A8AA0D4A79E9. Recibo 84.89.7F.F5.AC.CB.88.C9.9F.10.42.39.31.F8.4E.F3.1E.B2.40.04.D7.3D.43.10.AC.56.D9.47.36.07.A8.AA.0D.4A.79.E9-6. Apuração cumulativa: PIS 53,74 e COFINS 248,01 (igual ao arquivo, ao Domínio e aos DARF pagos); não-cumulativo e CP sobre receitas zerados. Falta apenas registrar na Ago2026 (TSV entregue).
- Arquivos EFD de 08/2026 de outros clientes já gerados em `08_AGOSTO\010 EFD CONTRIBUIÇÕES` em 04/10 (vistos: 016, 026, 173, 189, e outros): conferir antes de importar no PVA; prazo comum 15/10.

## 10. Conferência dos TXT de EFD-Contribuições 08/2026 (04/10/2026) — pasta `08_AGOSTO\010 EFD CONTRIBUIÇÕES`

Arquivos lidos (21 além do 186): 016, 018, 026, 071, 117, 126, 133, 155, 173, 177, 185, 189, 205, 209, 237, 238, 241, 247, 257, 258, 261. Método: M200/M600 recalculados a partir da base (0,65% e 3%; 238 e 133 no não-cumulativo) e comparados com a linha DARF PIS/COFINS da `Ago2026`. Todos os cálculos internos dos arquivos conferem.
- **Batem com a Controle e com os DARF:** 126 (708,73 / 3.271,07), 155 (146,11 / 674,34), 185 (27,70 / 127,85), 205 (200,53 / 925,50 após retenções), 189 (retido integralmente), 018 e 177 (compensados por retenção), 026, 117, 173, 209, 247 (zerados), 186 (transmitido).
- **Divergência:** 016 — PIS no arquivo R$ 770,94 (118.605,40 × 0,65%) × R$ 771,31 na Controle (R$ 0,37 a mais; COFINS 3.558,16 igual).
- **Controle ainda `Pendente` com valor definido pelo arquivo (venc. 25/09 já passou; confirmar pagamento no G-Click):** 241 (PIS 231,78 / COFINS 1.069,82, após retenções 180,11 e 831,23); 257 (820,45 / 3.786,69, sem retenção); 238 Real (PIS 576,15 / COFINS 2.655,03, após créditos 684,86 e 3.154,53 sobre depreciação; receita de aluguel 76.375,40 e financeira 125,81); 133 Real (PIS 11,55 / COFINS 53,22, DARF 6912 e 5856); 071 (retenções cobrem tudo: PIS 6.840,32 e COFINS 31.570,71, a recolher zero; Controle ainda Pendente).
- **Arquivo zerado e Controle `Pendente`:** 237, 258, 261 (status `Sem movimento` só com confirmação da Fernanda).
- **Sem arquivo na pasta:** 002 (aluguel; Controle PIS 142,86 / COFINS 659,34), 227 PROGEST, 264 ZENITH. 197 (dispensada) e 152 (autarquia) não entregam.
- **Atenção PVA:** registros 0120 (meses sem movimento) em 026, 173, 185, 189, 209 e 258 (173, 209 e 258 incluem o próprio 08/2026) — os mesmos clientes com erro de 0120 em 07/2026; diferenças de centavos entre M200/M600 e os controles 1300/1700 em 071, 177 e 189; em 018 o saldo de retenção de 06, 07 e 08/2026 aparece sem uso nos registros 1300/1700, embora M200/M600 usem a retenção do mês (conferir no Domínio para não carregar saldo indevido). 257 é contribuinte de ICMS e o arquivo traz só F550 (sem bloco C): confirmar se a receita de R$ 126.223,13 inclui mercadoria.
- **Desdobramentos (04/10 à tarde):** Fernanda confirmou `Sem movimento` de 237, 258 e 261 (DARF PIS/COFINS de 08/2026; TSV entregue). **016:** o DARF do SENDA (14/09, doc. 07.16.26257.8748597-1) traz PIS R$ 770,94 e COFINS R$ 3.558,16 (total R$ 4.329,10), iguais ao EFD; os R$ 771,31 da Controle eram erro de digitação na planilha (TSV de correção entregue).
- **DARF de agosto no Drive (`009 IMPOSTOS FEDERAIS`), gerados em 20/09:** 241 = R$ 1.301,60 (PIS 231,78 + COFINS 1.069,82, doc. 07.16.26263.3887550-9); 257 = R$ 4.607,14 (PIS 820,45 + COFINS 3.786,69, doc. 07.16.26263.3911296-7); 133 PIS = R$ 11,55 (cód. 6912, doc. 07.16.26263.4008537-4). Valores iguais aos do EFD; todos com recibo de declaração. A Controle seguia `Pendente` (sem evidência de postagem no G-Click). **Não achei no Drive:** DARF de 133 COFINS (R$ 53,22, cód. 5856), 238 PIS (576,15) e COFINS (2.655,03) e 071 (zero por retenção). Existe no Drive `MEMORIA_2026-10-02_Cliente_Novo_265_Belem_e_Pendencia_238.md` (não lido). Próximo passo: Fernanda confere no G-Click a tarefa COFINS / PIS AGO/2026 de 241, 257, 133, 238 e 071; só com a evidência vira `Enviado`.
- **Esclarecimentos da Fernanda (04/10):** 133 COFINS de 08/2026 (R$ 53,22, cód. 5856) foi **compensada via PER/DCOMP** (sem DARF) → status `Compensado`. 071: se tudo foi retido, nada a pagar → `Retido` (EFD: PIS 6.840,32 e COFINS 31.570,71 integralmente cobertos; no registro 1300 a retenção de PIS é 6.840,31, R$ 0,01 abaixo, valor sem DARF por ser menor que R$ 10). 238: PDF dos DARF no Drive do cliente ou na apuração em lote (`Apuracao-completa-08-2026`); a FAT `238_REAT HOLDING_FAT 2026` (aba "2026 retificada 072026") confirma agosto: DARF PIS 6912 R$ 576,15 e COFINS 5856 R$ 2.655,03 (iguais ao EFD; débitos 1.261,01 e 5.809,56; créditos 684,86 e 3.154,53). **Em aberto no 238:** retificação de junho/2026 com guia complementar "A gerar" e pagamento "Pendente" (PIS 38,96 e COFINS 239,77, total R$ 278,73). Falta evidência de postagem no G-Click de 241, 257, 133 (PIS 11,55) e 238.

## 11. Rodada de 04/10/2026 (fim da tarde): agosto fechado e memória por rodada
- Fernanda informou: **agosto/2026 está fechado**; estamos enviando o SPED Contribuições de 08/2026 (prazo 15/10) e depois voltamos ao fechamento de 09/2026. Linhas DARF de agosto ainda `Pendente` na Ago2026 viram apenas atualização de planilha, não bloqueio.
- Pedido permanente: registrar a cada rodada, na memória e na pasta do Drive, o que foi feito e o que ainda está pendente. Feito: `memoria/PENDENCIAS.md` reorganizado (pendente por assunto e data; resolvido por data), regra incluída no `CLAUDE.md` e snapshot `PENDENCIAS_E_RESOLVIDOS_2026-10-04.md` criado em `ARQUIVOS EXTENSÃO - CODE - CLAUDE` no Drive (id 1YQth02zyIvOnwaiyFl1rSPXHrDlnQ93K).
- Estado da Set2026 (leitura da Controle às 12:54): GUIA ISSQN `Enviado` em 16, 18, 152, 173, 177, 186, 189, 238, 241 e 263; `Sem movimento` em 117, 133, 138 e 265; `Pendente` em 155, 205 e 257; em branco em 2, 26, 209, 237, 258 (e nos municípios fora do DecWeb: 71, 126, 185, 197, 227, 247, 248, 261, 264).

## 12. SPED Contribuições de 08/2026 transmitidos (04/10/2026, 13:11 a 13:44)
Recibos (PDF e .REC) lidos na pasta `010 EFD CONTRIBUIÇÕES`: 22 transmitidos (Original, ReceitaNet, PVA 6.2.0): 186 às 13:11:36; 261 13:32:19; 257 13:32:26; 258 13:32:31; 241 13:32:37; 247 13:32:43; 237 13:32:48; 238 13:32:53; 205 13:32:58; 209 13:33:03; 189 13:33:07; 173 13:33:13; 177 13:33:17; 185 13:33:22; 155 13:33:28; 133 13:33:33; 126 13:33:38; 071 13:33:44; 026 13:33:53; 018 13:33:58; 016 13:34:03; 264 13:44:39 (arquivo gerado depois, com receita zero). Todos os valores dos recibos batem com a conferência dos TXT (seção 10). Sem recibo: 117, 002, 227. Formato do recibo: número = assinatura (16 bytes) + identificação do arquivo (20 bytes) + dígito, em pares hexadecimais com pontos; o TSV `Enviado` da Ago2026 leva o número completo na observação. O PVA não barrou os arquivos com registro 0120.
Próximo: voltar ao fechamento de 09/2026 (confirmar sem movimento 2, 26, 209, 237, 258 na guia ISSQN; FAT do 186; Domínio dos demais clientes; segunda 05/10: Tacom e 257).
- **Atualização (04/10, noite):** recibo do **002 RF Consultoria** lido: transmitido às 13:51:44 (Original), PIS 142,86 e COFINS 659,34 a recolher, iguais ao DARF de agosto; TSV `Enviado` entregue (total 23 transmitidos; faltam 117 e 227). O PDF do 264 reenviado é o mesmo recibo das 13:44:39. Fernanda colou o TSV dos 21 e confirmou `Sem movimento` na guia ISSQN de 09/2026 de 26, 209, 237 e 258 (TSV entregue); o 2 segue em branco.


## 13. São Leopoldo (126), ISSQN 09/2026 (04/10/2026)
- A Fernanda gravou o processo no portal (vídeo de 2m34s, guardado por ela). Resumo e passo a passo em `.claude/skills/sao-leopoldo-issqn/SKILL.md`.
- Conciliação: Portal Emitidas (209 notas, R$ 153.662,41, ISS R$ 3.073,23) = DMS prestador = guia R$ 3.073,23 (venc. 15/10/2026, `ISSV 2026: 9/0`). Recebidas sem retenção; tomador do DMS tem 16 notas (ISS 65,41, não retido).
- A sessão da nuvem não alcançou o Chrome (ferramentas da extensão indisponíveis); a extensão rodou em sessão própria do app desktop, sem acesso ao repositório.
- Também nesta rodada: `conciliacao.py` corrigido (nota de substituição gerada conta como normal); 205 liberada; 257 e 152 analisados (ver PENDENCIAS.md).

## 14. Novo Hamburgo (261 e 197), ISSQN 09/2026 (04/10/2026)
- Gravação da Fernanda do processo no Atende.Net/IPM (261 Giatech); skill em `.claude/skills/novo-hamburgo-issqn/SKILL.md`. Diferente de POA e São Leopoldo: a declaração precisa ser protocolada (Prestados e Tomados) e o carnê emitido na hora.
- 261: Prestados R$ 34.000,00 (ISS R$ 680,00, guia venc. 20/10/2026) conciliado com o Portal; Tomados R$ 483,40 (ISS retido em NH zero; outros municípios R$ 5,57); divergência de nota Google (19985753 no protocolo x 19171581 comp. 08/2026 no Portal).
- 197 ASBBM (feito em 04/10, 15:10 e 15:11): Prestados sem notas; Tomados 2 notas, R$ 5.500,00 (ISS outros municípios R$ 175,00, não retido); sem guia; conciliado com o Portal.

## 15. Brasília (71 e 264), ISSQN 09/2026 (04/10/2026)
- 4 gravações da Fernanda (ISSNet On-Line / Nota Control). Skill `.claude/skills/brasilia-issqn/SKILL.md`. 71: protocolo 42 notas, R$ 1.091.077,54 = Portal, retenção integral (Caixa), sem guia; Não Movimento em Contratados. 264: pendente de gravação e protocolo.

## 16. Retenção federal nas Recebidas do Portal, 09/2026 (04/10/2026)
Lidas as 15 planilhas Recebidas da pasta 003 (16 clientes têm arquivos; 205 só Emitidas). Notas normais, competência 09/2026 (130 notas de outras competências e 10 canceladas ficaram fora). Retenção federal: 71, 126, 152, 189, 238 (valores em PENDENCIAS.md). Notas do 152 com retenção (nº, prestador, valor, IRRF, contrib., INSS): 12804/12800/12799 House Parts 435,10/435,09/435,10 (20,88; 20,23; 0 cada); 356287 Solides 165,90 (7,96; 7,72); 48337 Volpmann 376,53 (18,07; 17,52); 739715 Rede OK 368,00 (17,66; 17,11); 15095 Implanta 24.550,00 (1.178,40; 245,50); 10442 Omega 469,00 (22,51; 21,81); 8234 Maxx 874,27 (41,96; 40,65); 3280/3279 Realize Next 4.890,23/6.648,48 (234,73/319,13; 227,40/309,15; INSS 537,93/731,33); 11959/11958/11957/11956 House Parts (13,17; 11,14; 13,17; 11,14, contrib. 12,75; 10,79; 12,75; 10,79); 159 Life Card 704,59 (6,31; 6,10); 3934 Casa da Moeda 754,53 (9,05; 35,09); 741590 Rede OK 368,00 (17,66; 0). 238: INSS 278,06 e 1.017,39 (Prime System, 11%), IRRF 17,75 e contribuições 82,54 (STV), contribuições 59,32 (Atlas Schindler). Resultado completo da leitura em scratchpad (não versionado).

## 17. Retenção sofrida nas Emitidas e preparo do REINF/DP (04/10/2026)
Emitidas 09/2026 (10 clientes): INSS retido zero. 16 Centro Clínico 221 notas R$ 142.642,60 sem retenção; 71 42 notas R$ 1.091.077,54, IRRF 52.371,72, contribuições 10.910,78; 126 209 notas R$ 153.662,41 sem retenção; 155 107 notas R$ 21.051,25 sem retenção; 186 3 notas R$ 11.475,05 sem retenção; 189 2 notas R$ 2.868.189,79, IRRF 43.022,85, contribuições 133.370,83; 205 17 notas R$ 95.753,11, IRRF 245,30, contribuições 760,41; 241 32 notas R$ 48.063,00, contribuições 1.348,61; 257 2 notas R$ 145.250,72, IRRF 228,76; 261 1 nota R$ 34.000,00, IRRF 510,00, contribuições 1.241,00. Pontos: 71 nota diz 4,65% e a coluna só traz 1,0%; 189 ISS não retido e zerado nas duas notas (motivo não analisado).

## 18. REINF 09/2026 e planilha do DP (04/10/2026)
Pasta `001 ARQUIVOS REINF` (18 PDFs: 17 individuais e 1 consolidado): R-2099 Sucesso para 16 clientes (recibos no TSV) e **117 Invalidado**. Planilha do DP: aba `MOD GERAL 09.2026` (A Nº, B Empresa, C Obrigação, D Status, E e F Observações, G ok do DP, H e I caixa de valores do 152); modelo do 186: D `Enviado`, E `Sem movimento`, F `Enviado dd/mm/aaaa hh:mm (Oficial). Sem retenção`. Criado o script `apps-script/atualizarReinfDP.gs` (fila `Atualizações REINF` colada em TSV, igual à da Controle_Fiscal) e o TSV em `memoria/TSV_DP_REINF_09-2026.md`. Valores de retenção sofridos por mês se repetem (71: 83,61 e 259,20; 152: INSS 1.269,26; 189: IRRF 2.144,00), o que confere com os meses anteriores da planilha do DP.

## 19. Domínio 126 — conferência 05/10/2026
- Saídas do Domínio param na NFS-e 1759 (17/09): 127 notas, R$ 86.386,91 (ISS R$ 1.727,73). Faltam importar as notas 1760 a 1841 (82 notas, R$ 67.275,50). Com elas: 209 notas = R$ 153.662,41 (= Portal Emitidas de setembro; ISS R$ 3.073,23 = guia). Notas 1842 a 1848 (R$ 7.570,00) são de 01 e 02/10: ficam em outubro.
- Retenção a recolher: só BIOLAB 1507, R$ 225,00, CRF 4,65% = R$ 10,46, cód. 5952 — confere com o Portal.
- Entradas: Facebook no Domínio é 146442407 (R$ 1.703,92, emissão 02/10, entrada 30/09); o Portal de setembro traz 144113199 (02/09, R$ 1.922,60) que não está no Domínio. Ideal Art 444 lançada por R$ 336,74 (Portal R$ 347,16). A confirmar.
- IRPJ/CSLL do trimestre (receita R$ 298.842,06 até 17/09) estão subestimados até importar as saídas restantes.

### 19b. 126 — XMLs conferidos (05/10/2026)
- Facebook 144113199: emitida 02/09, **competência 31/08** (anúncios de agosto), R$ 1.922,60. Pertence a agosto (confirmar que entrou na Entradas de 08/2026). A 146442407 (emissão 02/10, entrada 30/09, R$ 1.703,92) é a de setembro: Domínio correto.
- Ideal Art 444: serviço R$ 347,16 − desconto incondicional R$ 10,42 = **líquido R$ 336,74**. Domínio correto (valor contábil líquido). CST 200 / cClassTrib 200029, redução de 60%: CBS 0,36% (R$ 1,21), IBS 0,04% (R$ 0,13).
- BC de IBS/CBS = valor do serviço − ISS − PIS/COFINS destacados (Facebook: 1.922,60 − 55,75 − 31,72 − 146,12 = 1.689,00; Clinicorp: 383,85 − 7,68 ISS = 376,17).
- Facebook: "vTotalRet" 177,84 do XML são tributos aproximados (Lei 12.741) e PIS/COFINS próprios do prestador; não há retenção federal.
- BIOLAB 1507 (emissão 01/10, entrada 30/09): Fernanda confirmou, mantém em setembro.
- 126: fica pendente apenas importar as saídas 1760–1841 e rever o demonstrativo (PIS/COFINS, IRPJ/CSLL) na rodada dos serviços prestados.

## 20. 189 Real Engenharia: Recebidas do Portal (05/10/2026)
- Uma NFS-e tomada: nº 5, 08/09/2026, XAVANTINA EMPREENDIMENTOS IMOBILIARIOS LTDA (CNPJ 38.543.058/0001-54, não optante), R$ 142.933,33, item 10.09 (representação comercial), NBS 102010000. DPS 5, série 70000. ISS 2% = R$ 2.858,67, **não retido**, incidência Chapecó/SC.
- **IRRF R$ 2.144,00** (1,5% de 142.933,33). PIS/COFINS/CSLL "não retidos" no XML. **Sem nenhum campo de IBS/CBS** (CST, cClassTrib, base, valores vazios).
- A confirmar: (1) código do IRRF (provável 8045, comissões e corretagens PJ, 1,5%) e natureza de rendimento do R-4020; (2) data do pagamento (fato gerador do IRRF); (3) se a CRF 4,65% (IN RFB 459/2004, intermediação de negócios) é devida mesmo com "não retido" no XML (seria R$ 6.646,40; não confirmado).

### 20b. 189: Domínio conferido e REINF enviado (06/10/2026)
- Entradas: NFS-e nº 5 (08/09, Xavantina, R$ 142.933,33), espécie 39, acumulador 1005, CFOP 2-933, UF SC, IRRF 1,50% = R$ 2.144,00. Demonstrativo do IRRF: saldo devedor R$ 2.144,00. ISS retido 0, IBS/CBS 0. Confere.
- Regime: Lucro Presumido trimestral (presunção 32%). ISS "débito por profissional habilitado" R$ 634,31 = guia já enviada.
- REINF: R-4020, R-2099 e R-4099 com Sucesso em 06/10/2026 06:29 (recibos no TSV). Ainda sem resposta: CRF 4,65%, data do pagamento e código do IRRF (provisório 170806 do modelo do DP).
- Saídas do 189 ficam para a rodada de serviços prestados: Domínio traz em setembro só a NFS-e 44 (09/09, R$ 1.348.516,53); o Portal Emitidas de setembro soma R$ 2.868.189,79.

## 21. 71 Conte Arquitetura: Recebidas do Portal (06/10/2026; arquivo baixado em 03-04/10)
- Competência 09/2026: 139 notas normais, R$ 456.689,03 (fora: 5 canceladas + 1 substituída; 22 notas de competência 08 e 83 de competência 10).
- Retenção em setembro: nota 659 Giovani Gazen (R$ 5.574,32): IRRF 83,61 (1,5%) + CRF 259,20 (4,65%), INSS 0. ISS retido pelo tomador: nota 153 RIPA, R$ 39,43, Portal indica incidência São Paulo/SP (local de execução ainda a confirmar; guia de Jundiaí já emitida).
- A conferir: Chanfro nº 2 (competência 08/2026, emitida 14/09): IRRF 42,00 + CRF 130,20; verificar se entrou em agosto. Giovani nº 676 (competência 10/2026): IRRF 83,61 + CRF 259,20 pertence a outubro.
- IBS/CBS (set): 13 notas com dados (CBS R$ 145,38; IBS R$ 16,14; base R$ 17.558,31; CST 000/000001 em 9 e 200/200052 em 4). 126 sem dados (121 ME/EPP/MEI + 5 não optantes: Kontik 1142004/1142005, Paulo Sampaio 250, CIEE 81654, Giovani 659).
- Atenção: Caixa Cartões Pré-Pagos 30774046 com valor zero; 18 notas de competência 09 emitidas em 02/10.

## 22. Tacom 138: importação das notas tomadas no Domínio (06/10/2026)
- Prefeitura (DecWeb, Serviços Tomados 09/2026, IM 233879-2-0, CNPJ 08.196.752/0002-62): 9 notas, R$ 28.980,50, deduções R$ 1.914,66, ISS R$ 108,28, ISS retido 0. Notas: VOJ 40 (R$ 24.490,73, Simples), Ellu's 1353 (1.593,68), Contrei 6423 (141,89, BH), Unifique 443812 (9,90), Valesul 499455 (9,07), Unimed BH 1915711 (143,91) e 1977955 (2.591,32), Pluxee 8803672 e 8803674 (valor 0,00, SP).
- Portal Nacional: não há Recebidas do 138 na pasta 003. XMLs no Drive (SIEG): pasta 09 = Valesul 499455, Pluxee 8803672 e 8803674; pasta 10 = Unifique 460991 (02/10), VOJ 41 e Ellus 1387.
- Domínio (importação): advertências nos 4 XMLs com IBS/CBS (Unifique 460991 de 02/10, Valesul, Pluxee x2): "imposto 183-IBS e 184-CBS não está relacionado no acumulador 800, dados descartados"; Pluxee com valor contábil zerado.
- A fazer: ajustar acumulador 800 (IBS 183 / CBS 184); decidir Pluxee valor 0; conferir Unifique 460991 (outubro) e as 6 notas da prefeitura sem XML na pasta 09. Prazo: SPED ICMS para Leidislaine até 07/10.

### 22b. Tacom 138: conteúdo dos XMLs do Drive (06/10/2026)
- Valesul 499455 (22/09, Cachoeirinha, não optante): cTribNac 100201, ISS 2,5% R$ 0,23 não retido; IBS/CBS CST 000 / 000001, cIndOp 100301, base R$ 8,84, IBS 0,10% R$ 0,01, CBS 0,90% R$ 0,08.
- Pluxee 8803672 e 8803674 (15/09, São Paulo, não optante): cTribNac 171201, valor R$ 0,00; CST 000 / 000001, cIndOp 100301, tudo zero.
- Unifique 460991 (emitida 02/10, competência 10/2026, Porto Alegre, não optante): cTribNac 010701 "SUPORTE 24H - PJ", R$ 9,90, ISS 2% R$ 0,20; IBS/CBS CST 410 / cClassTrib 410999, cIndOp 100401, base R$ 9,70, alíquotas e valores zerados.
- VOJ 41 (emitida 05/10, ME/EPP, cTribNac 170301, R$ 24.490,73) e Ellu's 1387 (emitida 05/10, ME/EPP, cTribNac 170501 "LIMPEZA SET 26", R$ 1.593,68, ISS 5% R$ 79,68, INSS retido R$ 175,30): sem IBS/CBS; são de outubro.
- Pendente: XMLs de VOJ 40, Ellu's 1353, Unifique 443812, Contrei 6423 e Unimed BH (1915711 e 1977955), ainda não vistos; conferir se a Ellu's 1353 teve INSS retido (R-2010).

## 23. Tacom 138: conciliação ICMS 09/2026 e advertências do Domínio (06/10/2026)
- ICMS: Domínio (Entradas e Saídas) x txt SEFAZ RS x 10 XMLs: tudo confere. 8 entradas = R$ 26.607,36 (CFOP 1.556: ZRZ 4917 R$ 135,00, Fortpel 1558521 R$ 477,16, Beller 23640 R$ 7,96 e 10504 R$ 37,84; CFOP 2.916 retorno de conserto da Tacom Projetos MG: 33132 R$ 2.619,96, 33166 R$ 6.010,72, 33188 R$ 8.302,64, 33204 R$ 9.016,08). 2 saídas CFOP 6.915 remessa para conserto = R$ 40.161,90 (4698 R$ 14.916,59 e 4699 R$ 25.245,31). Sem ICMS próprio no mês; ICMS destacado nas compras CFOP 1.556 (R$ 55,57: Fortpel 47,79, Beller 1,35 e 6,43) não creditado.
- Remessas 4698 e 4699 saíram com IBS/CBS CST 000/000001 (IBS R$ 40,17; CBS R$ 361,46); os retornos 33132/33166/33188/33204 vieram sem grupo IBS/CBS (CST 41, ICMS suspenso). A confirmar com o Fiscal.
- Advertências do Domínio: (a) PIS/COFINS da guia Estoque sem os impostos no acumulador (Beller 10504 e 23640); (b) cClassTrib IBS/CBS inválido (XML sem IBS/CBS) nos produtos 12805, 12806, 17055, 20932, 21353 (notas 33166, 33188, 33204); (c) CEST 2103400 do produto 20932 (nota 33188) diferente do cadastro (em branco). Configurar os produtos e o acumulador após o fechamento.
- Tomados NFS-e: o relatório de Entradas enviado traz só as NF-e (espécie 36); falta o relatório com as NFS-e (espécie 39) para conciliar com a prefeitura (9 notas, R$ 28.980,50).

### 23b. Tacom 138: conciliação dos tomados NFS-e (06/10/2026)
- Domínio (Entradas set/2026, total geral R$ 26.616,43 = NF-e R$ 26.607,36 + NFS-e R$ 9,07): NFS-e lançadas 4089 Valesul 499455 (R$ 9,07, 1-933, ac. 800), 4090 e 4091 Pluxee 8803672 e 8803674 (R$ 0,00, 2-933, ac. 800). Unifique 460991 (outubro) não aparece: correto.
- Prefeitura (DecWeb) 9 notas R$ 28.980,50: faltam no Domínio 6 notas, R$ 28.971,43: VOJ 40 (24.490,73), Ellu's 1353 (1.593,68), Contrei 6423 (141,89), Unifique 443812 (9,90), Unimed BH 1915711 (143,91) e 1977955 (2.591,32). Sem XML na pasta do Drive; lançar manualmente ou subir os XMLs.
- Conferir INSS retido (11%, R$ 175,30) na Ellu's 1353 para o R-2010.

### 23c. Tacom 138: as 6 NFS-e faltantes são de setembro (06/10/2026)
- Zip "08.2026_138" (pasta do Portal por competência 08, que cobre emissões até 30/09). XMLs: dCompet de setembro em todos (01/09 a 11/09). A prefeitura de agosto traz outros números (VOJ 39, Ellu's 1317, Contrei 5577, Unifique 353551, Unimed 1630783 e 1672302), portanto as 6 notas são de setembro e precisam ser lançadas em 09/2026.
- Dados: VOJ 40 (170301, R$ 24.490,73, ME/EPP, sem ISS); Ellu's 1353 (170501, R$ 1.593,68, ISS 5% R$ 79,68, INSS retido R$ 175,30, líquido R$ 1.418,38); Contrei 6423 (070101, R$ 141,89, ISS 2,5% R$ 3,55, BH, PIS 0,92 e COFINS 4,26 destacados do prestador); Unifique 443812 (010701, R$ 9,90, ISS 0,20, CST 410/410999); Unimed BH 1915711 (042301, R$ 143,91, dedução R$ 100,74, base R$ 43,17, ISS 1,30) e 1977955 (042301, R$ 2.591,32, dedução R$ 1.813,92, base R$ 777,40, ISS 23,32).
- Com as 6, o Domínio fecha as 9 NFS-e da prefeitura: R$ 28.980,50.

### 23d. Tacom 138: critério de competência das NFS-e (06/10/2026)
- Fernanda pediu para avaliar a competência, não a emissão. Pelo campo de competência do XML (dCompet) as 6 notas são de 09/2026. Pelo período do serviço descrito: Ellu's 1353 "LIMPEZA AGOSTO 26" e Unimed 1915711 "Referência 08/2026" = agosto; Contrei 6423 "SETEMBRO/2026" = setembro; Unimed 1977955 "Mensalidade 10/2026" = outubro; VOJ 40 e Unifique 443812 sem referência.
- Critério pendente de decisão (campo dCompet x período do serviço). No 126 (Facebook) foi usado o campo de competência do XML. Se valer o período do serviço, Ellu's 1387 "LIMPEZA SET 26" (INSS R$ 175,30), Unifique 460991 e VOJ 41 (emitidas em outubro) entram em setembro, e Ellu's 1353 e Unimed 1915711 iriam para agosto (fechado).

### 23e. Tacom 138: conciliação final dos tomados NFS-e (06/10/2026)
- Critério confirmado pela Fernanda: competência pelo campo dCompet do XML (as 6 notas ficam em 09/2026).
- Domínio Entradas set/2026: NF-e CFOP 1.556 R$ 657,96 + NFS-e CFOP 1.933 R$ 26.103,38 (Valesul 4089, Ellu's 4093, VOJ 4097, Unifique 4098 no acumulador 1007) + NF-e CFOP 2.916 R$ 25.949,40 + NFS-e CFOP 2.933 R$ 2.877,12 (Pluxee 4090 e 4091 zeradas, Unimed 4094 e 4095, Contrei 4101) = R$ 55.587,86 = NF-e do SEFAZ (R$ 26.607,36) + NFS-e da prefeitura (R$ 28.980,50).
- Pendências: INSS retido da Ellu's 1353 (R$ 175,30), R-2010 do 138, impostos 183/184 no acumulador 800, base de ISS das Unimed (dedução).

### 23f. Tacom 138: INSS retido da Ellu's fica para depois do fechamento (06/10/2026)
- A Fernanda confirmou que o cálculo é feito pela matriz. Registrado para ajuste após o fechamento: acumulador da Ellu's 1353 (INSS retido R$ 175,30), conferência da Ellu's 1317 (agosto) e aviso à matriz sobre o R-2010, junto com os cadastros de produtos e as demais advertências (seção J do PENDENCIAS).
