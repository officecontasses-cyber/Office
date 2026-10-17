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

## 24. Tacom 138: SPED, GIA e fila do Controle_Fiscal (06/10/2026)
- GIA RS 09/2026: protocolo TED 13542570, 06/10/2026 15:15:59 (comprovante de transmissão; recibo definitivo depois). SPED Fiscal 09/2026 enviado à Leidislaine pelo G-Click em 06/10 15:18; E110 sem débito/crédito, saldo credor R$ 17.385,19 a transportar.
- Alerta: o SPED não traz as 4 NF-e de compra CFOP 1.556 (R$ 657,96; acumulador 106) que constam no Domínio e no SEFAZ (C100 = 6 notas).
- TSV da fila (8 linhas: Serviços Tomados, Serviços Prestados, Entradas, Saídas, Guia ICMS, GIA RS, SPED envio e SPED recibo) em `TSV_TACOM_138_09-2026.md`.

## 25. Tacom 263 (Tacom Projetos POA): levantamento prévio da prefeitura (06/10/2026)
- DecWeb 09/2026 (IM 954945-2-9, CNPJ 01.005.845/0021-86): Serviços Tomados 1 nota (OfficeCont, NFS-e 1018, 01/09, R$ 650,00, ISS 0, ME/EPP); Serviços Prestados 9 NFS-e (54 a 62), R$ 81.793,56, ISS 5% = R$ 4.089,69 (igual à guia enviada). Tomadores: Consórcio Gestor de Bilhetagem Metropolitano (7 notas), Catsul Guaíba, Expresso Charqueadas.
- A fazer quando a Fernanda trouxer os relatórios: conciliar com o Domínio (Entradas/Saídas) e o ICMS (Controle indica contribuinte ICMS = NÃO para o 263); gerar TSV para Serviços Tomados e Serviços Prestados.

## 26. Tacom 248 Palhoça/SC (CNPJ 01.005.845/0020-03): prefeitura e ICMS (06/10/2026)
- Os arquivos baixados em 06/10 são do 248 (não do 263): Declaração de Serviços Prestados (sem documentos, R$ 0,00, protocolo 10e087db7f1edc0c56a385b360e040, 15:40:50) e de Serviços Tomados (NFe 1017 da OfficeCont, 01/09/2026, R$ 650,00, serviço 17.19.01, incidência Porto Alegre, ISS R$ 0,00, protocolo e63627324fa60197accea2cdf1e85c, 15:41:57).
- SAT/SC: sem NF-e e sem NFC-e emitidas em 09/2026 (consulta por emitente); como destinatário, 1 NF-e: Leonardo Alves Sebastião ME (06.331.140/0001-29), NF 123 série 1, 14/09/2026, R$ 15,00, ICMS 0, evento Ciência da Operação (planilha `248_DFE - Excel Notas NF-es_092026.xlsx`).
- TSV provisório em `TSV_TACOM_248_09-2026.md`. Pendentes: Domínio (tomados e entrada de R$ 15,00), GUIA ICMS, SPED ICMS, DIME. 263 (POA): aguardando os relatórios do Domínio.

### 26b. Regra de status reforçada pela Fernanda (06/10/2026)
- Declaração à prefeitura e serviços tomados da prefeitura = Enviado (recibo). Linhas que dependem da importação no Domínio (Serviços Tomados/Prestados, Entradas, Saídas) ficam Pendente ("em andamento") até haver o Domínio conferido. "Em andamento" não existe no vocabulário da planilha (Set/Ago/Jul): usar Pendente com "Em andamento" na observação. TSV do 248 revisado: Serviços Prestados e Saídas passam a Pendente.

## 27. Revisão geral e regra de status do Domínio (06/10/2026)
- Regra gravada no CLAUDE.md e na seção K do PENDENCIAS: o que depende do Domínio fica Pendente até importar e conciliar. Aplicada: 248 (tomados PREF, prestados, guia ISSQN e saídas Pendente; declaração Enviado) e 138 (SPED ICMS - Envio arquivo Pendente até regerar o SPED com as 4 NF-e).
- Seção K do PENDENCIAS reescrita com tudo de 05 e 06/10 (126, 189, 71, 238, 152, 138, 248, 263); snapshot `PENDENCIAS_E_RESOLVIDOS_2026-10-06.md`.

### 27b. Correção da regra de status (06/10/2026)
- A Fernanda corrigiu: onde não há nota na fonte oficial (ex.: SAT/SC sem NF-e/NFC-e emitidas), não há o que importar no Domínio; a linha vai como `Sem movimento`. `Pendente` vale só onde há movimento ainda não importado/conciliado. TSV do 248 refeito (Prestados, Guia ISSQN e Saídas `Sem movimento`; Tomados PREF `Pendente`). CLAUDE.md, PENDENCIAS e snapshot ajustados.

## 28. Tacom 248: Domínio e entradas (06/10/2026)
- Fernanda colou o TSV da rodada 1 do 248. Domínio, Entradas 09/2026 (16:23): só NFS-e 1017 OfficeCont (cód. 22, 01/09, R$ 650,00, CFOP 2.933, acumulador 800) = prefeitura. Importação: NFS-e 1020 (01/10/2026, R$ 650,00) desmarcada (outubro); aviso "183-IBS e 184-CBS não estão no acumulador 800".
- SEFAZ/SC (planilha DFe): NF-e 123 de Leonardo Alves Sebastião ME, 14/09/2026, R$ 15,00, chave 42260906331140000129550010000001231001583000, não está no Domínio: lançar.
- Em agosto (precedente): DIME `NÃO SE APLICA` (dispensada desde junho), SPED envio "Envio pela Matriz". TSV da rodada 2 em `TSV_TACOM_248_09-2026_rodada2.md`. Ajuste do acumulador 800 do 248 anotado para depois do fechamento.

### 28b. 248: SPED ICMS liberado sem a NF-e 123 (06/10/2026)
- A NF-e 123 (R$ 15,00) não veio do SIEG; a Fernanda verifica depois e libera o SPED ICMS do 248 mesmo assim; avisará quando enviar. Entradas e Guia ICMS ficam Pendente até lançar a nota; avaliar retificação do SPED depois.

### 28c. 248: SPED ICMS enviado (06/10/2026)
- G-Click "EFD ICMS/IPI (Dia 12) SET/2026": Arquivo Sped 16:32 e Envio arquivo 16:33 (Fernanda); Recibo entrega pendente (Leidislaine). Enviado sem a NF-e 123. TSV em `TSV_TACOM_248_09-2026_rodada3.md`.

### 28d. Ordem de retomada (06/10/2026, noite)
- Os SPED ICMS das Tacom eram o que tinha prazo (Leidislaine, 07-08/10). Próximo: voltar ao **71 Conte**, de onde paramos (aguardando o Domínio da Fernanda: Entradas, Retenções a Recolher e Demonstrativo). Segue pendente o 138 (regerar o SPED com as 4 NF-e) e o Domínio do 263.

## 28e. Auditoria declarações municipais x GUIA ISSQN sem valor (06/10/2026)
- Base: export Controle_Fiscal de 06/10 18:20 (Set2026). Declaração Enviado + ISS zerado + GUIA ISSQN em branco: **só o 2 (RF Consultoria)** (recibo 03/10 11:16:19, receita e imposto R$ 0,00, só tomados sem ISS retido). TSV entregue no chat (GUIA ISSQN → Sem movimento, 0).
- Já corretos: 117, 133, 138, 197, 209, 237, 258, 26, 264, 265 (Sem movimento) e 71 (Sem Recolhimento — Retenção Integral). 117, 133 e 265 estão com Valor vazio (cosmético: 0).
- Sem declaração entregue (fora da auditoria): 185 (RJ), 227, 247 (Montenegro). 248: TSV rodada 1 já tem Guia ISSQN Sem movimento (conferir se colado).

## 28f. 155 Mainieri: retificadora DecWeb x Emitidas do Portal (08/10/2026)
- Camila (06/10 09:47): faturamento 09/2026 R$ 22.676,34; notas de R$ 0,00 canceladas; retificadora aberta no DecWeb. Original (03/10): receita R$ 21.051,25, ISS R$ 842,02.
- Fase 1 do robô (08/10 09:26): reaproveitou a retificadora Aberta, baixou ServPrestados/ServTomados; nada enviado.
- Emitidas baixada de novo (Drive 08/10 12:44): competência 09/2026, 112 notas Normal, todas 4%, ISS não retido = **R$ 22.676,34, ISS R$ 907,02** (confere com a Camila). 4 canceladas de 09/2026 com R$ 0,00 (nº 913, 963, 966, 972). Competência 08/2026: 3 canceladas em 03/09 (R$ 430,47, ISS R$ 18,40; nº 813, 814, 821) — conferir se o Ago estava ok.
- Falta: conferir a tela do DecWeb (receita 22.676,34), rodar fase 2 `--retificadora --enviar` e fase 3; guia nova substitui a de R$ 842,02; G-Click comprova o envio.

## 28g. 155 Mainieri: retificadora enviada (08/10/2026)
- Recibo (Retificadora 1): recebida 08/10/2026 09:39:11; receita bruta R$ 22.676,34; imposto próprio R$ 907,02; retido de terceiros R$ 0,00; compensação 0,00; total a recolher R$ 907,02 (bate com a Emitidas do Portal).
- Guia nova (Retificadora 1, gerada 08/10 09:39): R$ 907,02, venc. 13/10/2026 (impresso na guia). Substitui a de R$ 842,02 (03/10), que não vale mais. PDFs na pasta 002 ARQUIVOS MUNICIPAIS (mesmos nomes de arquivo, sobrescritos).
- Planilha: DECLARAÇÃO PREFEITURA Enviado (recibo); GUIA ISSQN Pendente R$ 907,02 até o G-Click comprovar o envio (regra de 01/10). Subir a guia nova no G-Click e conferir que a antiga não foi enviada à cliente.

## 28h. 155 Mainieri: G-Click e FAT (08/10/2026)
- G-Click (print): Guia ISS 08/10 10:11 e Envio ao cliente 08/10 10:12 (fernanda.officecont), vencimento 13/10 → GUIA ISSQN `Enviado` R$ 907,02.
- FAT `155_MAINIERI E OLIVEIRA_FAT2026`, aba 2026: **L4 (SETEMBRO, receita serviços) = 22676,34**; L14 (ISSQN) já tem fórmula `=L4*4%` = 907,05 (guia: 907,02, diferença de R$ 0,03 por arredondamento nota a nota); IRPJ/CSLL/PIS/COFINS calculam sozinhos.
- Alerta: K4 (agosto) = 22.477,87, enquanto a Emitidas 08/2026 Normal soma 22.233,73 (3 notas canceladas em 03/09, R$ 430,47). Conferir se agosto foi declarado e lançado com valor correto.
- **Fernanda (08/10): agosto do 155 está OK** (K4 22.477,87 da FAT x Emitidas 08/2026 22.233,73 + canceladas): conferido por ela, sem retificadora. Alerta encerrado.

## 28i. 71 Conte: DARF de IOF sobre mútuo à CBR Engenharia (e-mail do Gian, 07/10/2026; revisão 08/10)
- DARF (Drive: `DARF IOF MUTOI CBR 06102026 VCTO 15102026.pdf`, emitido no Sicalc Web em 07/10 08:12): CNPJ 08.307.701/0001-80 (Conte Cornetet Arquitetura), código **1150** (IOF operações de crédito PJ), principal R$ 16.900,00, sem multa/juros, vencimento **15/10/2026**, PA exibido 10/10/2026 (no detalhe "PA 01/10/2026"), obs. "IOF MUTUO CBR". 16.900 = 3,38% de R$ 500.000.
- Precedente: DARF idêntico (R$ 16.900,00, código 1150, venc. 15/06/2026, obs. "IOF MUTUO CBR 05.06.2026") na pasta de junho. Perguntar se outubro é um segundo mútuo de R$ 500 mil ou renovação do de junho.
- Instrução do Gian: contabilizar no ATIVO conta específica "CBR Engenharia" = R$ 516.900,00 (R$ 500.000,00 de empréstimo + R$ 16.900,00 de IOF pago por conta do mutuário); conferir o extrato de 10/2026 e o pagamento do IOF.
- A conferir (não confirmado): contrato de mútuo escrito (prazo, juros, cláusula de ressarcimento do IOF); tratamento dos juros na Conte (Lucro Presumido) e IRRF retido pela CBR; quem paga o DARF; linha na Controle_Fiscal (aba Out2026, a criar). Códigos, alíquotas e prazo de recolhimento do IOF devem ser conferidos na legislação vigente/Sicalc.

## 28j. 71 Conte: pesquisa LeFisc do mútuo (08/10/2026)
- Resultado detalhado em `MUTUO_CONTE_CBR_LEFISC_2026-10-08.md`: IRRF (tabela regressiva, retém a CBR), IRPJ/CSLL (juros integrais na base presumida), PIS/COFINS (tendência de não incidência), IOF (código 1150 e vencimento 15/10 conferem; valor do DARF R$ 16.900,00 x R$ 16.865,00 a 0,0082% ou R$ 9.382,50 a 0,0041%: alíquota vigente a confirmar). Correção: art. 13 da Lei 9.779 é IOF, não IRRF.
- 08/10: documentos do mútuo achados no Drive da 71 (contrato de 05/06/2026, extrato Caixa 06/2026, DARFs de junho e outubro); sem contrato/PIX de outubro. Detalhes e achados em `MUTUO_CONTE_CBR_LEFISC_2026-10-08.md`.
- 08/10 (2ª pesquisa LeFisc): IN RFB 1.700/2017 art. 215 § 3º, I, "e" inclui juros de mútuo na base de IRPJ e CSLL; competência ou caixa conforme § 9º (art. 216 só para aplicações financeiras). Estimativa 3º tri: R$ 2.494,56 (DARF 2089 e 2372, vcto 30/10). Detalhes em `MUTUO_CONTE_CBR_LEFISC_2026-10-08.md`.

## 28k. RF Consultoria: receita de aluguéis variável a partir de 10/2026 (09/10/2026)
- E-mail "RF Consultoria | Informativo receita aluguéis": Fernanda perguntou se o informativo se refere ao faturamento mensal e se "a partir de 10/2026 não terá mais o valor fixo de receita"; Ricardo Fernandes (RFS) respondeu "sim, exatamente". Registrado em CLAUDE.md (pendências com data) e PENDENCIAS.md para a apuração de 10/2026.

## 28l. Revisão ISSQN e fechamento municipal pendentes (09/10/2026, export da Controle_Fiscal de 09/10)
- **Guias ISSQN Set/2026 `Pendente` (vcto 13/10, sem comprovação G-Click):** 205 L S Becker R$ 1.915,06; 257 B2B R$ 6.500,00. Demais: `Enviado` (com G-Click) ou `Sem movimento`. 152: GUIA ISSQN e GUIA ISSQN - FORA MUNICÍPIO com mesmo valor (R$ 461,69) e mesma observação: conferir duplicidade.
- **Sem declaração/guia lançada:** 185 (RJ), 227 (inativa até 09/2026), 247 (Montenegro, DMS fora do DecWeb).
- **Serviços Tomados/Prestados em branco em Set/2026 (conferência XML x Portal x Domínio):** 2, 16, 18, 26, 117, 126, 133, 152, 155, 173, 177, 189, 205, 209, 237, 238, 241, 257, 258, 263 (e 185, 227, 247). Candidatos a Prestados `Sem movimento` (receita zero na declaração): 2, 26, 117, 133, 209, 237, 258 (117 e 258 já confirmados sem Emitidas no Portal). Com `Pendente` correto por regra (aguardando Domínio): 71 Prestados; 197 Tomados; 261 Tomados e Prestados.
- **Ago/2026 ainda com `Pendente` no export** (CLAUDE.md diz agosto fechado): 2, 18, 71 (2), 138, 152 (2), 155, 185, 227 (4), 237, 241 (3), 247, 248 (2), 257 (2), 258 (2), 261, 263 (2); Jul/2026: 177, 238 (2), 248, 263. Conferir se são linhas desatualizadas.
- 09/10 17:48: **205 L S Becker**, guia ISSQN R$ 1.915,06 (venc. 13/10) subida e enviada ao cliente no G-Click (print). TSV `Enviado` entregue. Segue pendente a guia do 257 (aguarda a resposta do cliente sobre a retenção da nota 31) e o REINF do 205.

## 28m. SPED ICMS Tacom 138 e 248: recibos (09/10/2026)
- Fernanda: a Leidislaine já transmitiu; falta registrar na planilha e subir os recibos no G-Click. Recibos no Drive (pasta do 138/248, salvos 08/10).
- **138** (CNPJ …/0002-62, IE RS, perfil A): recebido pelo SERPRO em 07/10/2026 10:13:48, hash 20AF8EEFF931734B8EE356D16599A157, remessa original, débitos/créditos/ICMS a recolher R$ 0,00, saldo credor R$ 17.385,19. O `.txt` do Drive (06/10 18:06) tem 6 C100 (4 retornos CFOP 2.916 e 2 remessas 6.915) e nenhuma compra CFOP 1.556; hash não conferido. **Provável retificadora (pós-fechamento, registrado na seção J da PENDENCIAS).**
- **248** (CNPJ …/0020-03, IE SC, perfil B): recebido em 07/10/2026 10:23:16, hash 2F1C93028E7F35F11C60662CE06B7440, remessa original, tudo R$ 0,00; arquivo sem NF-e, coerente. NF-e 123 (R$ 15,00) segue fora.
- TSV entregue (138 recibo; 248 envio e recibo, `Enviado`). Número do recibo não transcrito (leitura do PDF embaralhada).
- Pós-fechamento (pedido da Fernanda, 09/10): 248, lançar a NF-e 123 e avaliar retificadora do SPED ICMS; anotado na seção J da PENDENCIAS.

## 28n. 257 B2B: guia ISSQN enviada (12/10/2026)
- Print do G-Click: tarefa ISSQN SET/2026, cliente 257 B2B Soluções, Guia ISS e Envio ao cliente em 12/10/2026 09:56 (fernanda.officecont), vencimento 13/10, etiqueta "Ret" na Guia ISS (significado não confirmado). Fernanda: pendência resolvida e guia enviada ao cliente; a guia ficou como estava. TSV `GUIA ISSQN` `Enviado` R$ 6.500,00 entregue (valor da memória; o print não mostra o valor).
- Restam no 257 (ICMS, contribuinte): ENTRADAS, SAÍDAS, GUIA ICMS (13/10), GIA RS e SPED ICMS (15/10) em branco na Controle de 09/10.

## 28o. 257 B2B: conciliação (skill Conciliador Tributário e Fiscal) e pastas padrão (12/10/2026)
- Conciliação do 257 (09/2026): Prestados (2 NFS-e, R$ 145.250,72) Domínio = Portal = DecWeb; guia R$ 6.500,00. Tomados: 13 notas do Portal = DecWeb; Domínio tem a mais Officecont 1025 (R$ 1.518,00, 05/10) e Guinter 347 (R$ 1.300,00, 07/10), emitidas depois da exportação de 03/10 (rodar o Portal de novo).
- XMLs das 3 NF-e da 3C Plus (11678, 11693, 12175; R$ 8.755,80): produto EBOOK-01, NCM 4901.99.00, CST 41, PIS/COFINS CST 06: ICMS zero coerente com imunidade de livro (confirmar citação). CFOP 2.102 do Domínio: confirmar se é revenda ou uso/consumo (2.556); nota de R$ 7.500,00 para um e-book merece pergunta ao cliente.
- Demonstrativo (Domínio): ICMS a recolher 0, saldo credor R$ 2.866,13; ISS R$ 6.500,00; IRPJ 3º tri saldo devedor R$ 19.321,40 (retido R$ 3.443,38, bate com 1,5% das 4 notas com retenção); CSLL R$ 10.355,32 sem retenção; IBS/CBS sem créditos no mês (reforma, pós-fechamento). Faltam: PIS/COFINS, Retenções a Recolher, saídas SEFAZ.
- Pastas padrão (Fernanda, 12/10): XMLs para conferência em `...\09_SETEMBRO\007 ARQUIVOS SIEG` (por cliente); demonstrativos de apuração em `...\09_SETEMBRO\005 ARQUIVOS CONFERÊNCIAS`. Incluído na skill de conta (cópia local, não salva na conta) e na cópia do repositório `.claude/skills/conciliador-tributario-fiscal/SKILL.md`.
- **FAT do 257 (`257_TEC2BR TECNOLOGIA_FAT2026`), conferência 12/10:** Jul R$ 88.085,97 e Ago R$ 126.223,13 batem com o Domínio; **SETEMBRO em branco no FAT** (Domínio: receita R$ 145.250,72, ISS retido R$ 762,54, IRRF R$ 228,76, ISS a recolher R$ 6.500,00). Com setembro o 3º tri fica: IRPJ R$ 19.321,38 (FAT) x R$ 19.321,40 (Domínio) e CSLL R$ 10.355,33 x R$ 10.355,32 (centavos de arredondamento). Regra da Fernanda: conferir sempre IRPJ/CSLL no FAT do cliente; incluída na skill (cópia do repo). IBS/CBS das tomadas: já está no pós-fechamento (acumulador 800), revisar depois (Fernanda, 12/10).
- **257, CSRF resolvida (LeFisc, item 10.05 / código 100501, 12/10):** CSRF (contribuições sociais): "Não há previsão legal para retenção" (a Telefônica não reteve e está correto). IRRF: 1,50%, DARF 8045, art. 718 do Decreto 9.580/2018, retido pelo tomador (comissão/corretagem; dispensa se o prestador for Simples/imune ou valor ≤ R$ 10,00 por pagamento; auto-retenção só nas hipóteses da IN SRF 153/87 etc.). Nota 32 (R$ 15.250,72): IRRF R$ 228,76 correto. Nota 31 (Lifecombr, R$ 130.000,00): sem IRRF; seria R$ 1.950,00 se a Lifecombr devesse reter (obrigação dela; confirmar se é Simples). Não vale para o 189 sem checar o item de serviço dele (representação comercial pode ser outro item, ex.: 10.09).
- **FAT do 257, como digitar setembro (12/10):** a agente não tem ferramenta para editar célula de planilha; Fernanda digita. Só `L4` é entrada; `L9` (ISSQN retido = 5% da receita) e `L10` (IRRF = 1,5% da receita) são FÓRMULAS que supõem retenção total. Em setembro a retenção foi parcial (só a nota 32), então sobrescrever `L4 = 145.250,72`, `L9 = 762,54` e `L10 = 228,76`. Resultado esperado: ISSQN L15 R$ 6.500,00; IRPJ L17 R$ 6.743,27; CSLL L19 R$ 4.183,22; COFINS L21 R$ 4.357,52; PIS L23 R$ 944,13; 3º tri: IRPJ M17 R$ 13.815,47 + adicional M25 R$ 5.505,91 = R$ 19.321,38; CSLL M19 R$ 10.355,33. Cuidado em meses futuros: se a retenção não for total, as fórmulas de L9/L10 superestimam o crédito de IRRF e escondem o ISS a recolher.


## 28p. REINF 205 (L Schmeling Becker) — 12/10/2026
R-2099 Fechamento, Sucesso, recibo 12260744-01-2099-2609-12260744, 12/10/2026 11:49 (Oficial). Sem movimento (sem retenção como tomador, sem INSS retido sofrido).
Relatório: `205 - L SCHMELING BECKER ANESTESIOLOGISTA.pdf` (Drive). O mesmo relatório mostra R-1000 (inclusão e alteração, 11:49) em nome da empresa "1205": conferir se o cadastro "1205" no Domínio é duplicado.
TSV entregue; falta ela confirmar/subir recibo no G-Click. Próximos REINF: 238, 152, 71, 227, 265.

## 28q. 238 REAT — conciliação Portal Nacional x Prefeitura x Domínio (12/10/2026)
Portal (Recebidas, 8 notas, R$ 16.180,90): ISS retido 609,54 = Declaração Mensal PA (recibo 03/10 14:03:48) OK.
Domínio (Entradas + Retenções a Recolher 09/2026): só nota 19764 Atlas (CRF 59,32). Faltam no Domínio 7 notas.
Retenções no Portal não refletidas no Domínio: STV 20038 (CRF 82,54 + IRRF 17,75); Prime System 493/494 (INSS 1.017,39 + 278,06 = 1.295,45, mão de obra 17.05.01 -> R-2010).
Conclusão: REINF do 238 não deve ser enviado antes de lançar as notas no Domínio e reexportar Retenções a Recolher. Pendente: Serviços Tomados 238 segue Pendente. Verificar data de pagamento (fato gerador R-4020): Atlas venc. 10/10, STV 05/10.

## 28r. 238 REAT — reconciliação após reimportação (12/10/2026 ~12:07)
Domínio agora: 7 notas (R$ 15.730,90 = Portal 16.180,90 menos nota 121 Castro, competência 08/2026). Retenções a Recolher: IRRF 17,75 (STV 20038), ISS ret 609,54 (493, 494, 994), CRF 141,86 (STV 82,54 + Atlas 59,32), INSS 1.295,45 (493, 494); total 2.064,60 = Portal. Bate com Declaração Mensal PA (ISS 609,54).
Pontos de atenção: (1) IRRF STV aparece com alíq. 1,50% mas valor 17,75 = 1%; verificar alíquota/código (1% x 1,5% = diferença R$ 8,87). (2) Primegrid 994 (07.02.01, 'abastecimento de gerador'): sem CRF; verificar enquadramento. (3) Atlas: sem IRRF; verificar. (4) Prime System é ME/EPP (Simples): sem IRRF/CRF, INSS 11% retido; verificar declaração do Simples arquivada. (5) fato gerador do R-4020 = pagamento (Atlas venc. 10/10, STV 05/10): confirmar data de pagamento. (6) Notas 21748 Atlas (06/10) e 21806 STV (07/10) são de outubro: fora de setembro.
REINF 238: R-2010 (Prime System, INSS 1.295,45), R-4020 (Atlas CRF; STV IRRF+CRF), depois R-2099. Naturezas no Domínio: 15044 (Atlas), 15045 (STV); códigos de receita mostrados: 170806 (IRRF), 595207 (CRF), 1162 (INSS): conferir na tabela da Receita.
## Pós-fechamento (advertências da importação XML, 12/10)
- Notas 20038, 21748, 21806: imposto 183-IBS e 184-CBS não relacionados ao acumulador 1005/1006 ("dados serão descartados"): ajustar acumuladores no pós-fechamento.
- Nota 555002 Telefônica: data de entrada 07/09 anterior à emissão 10/09: corrigir data de entrada (pós-fechamento).
## Regra para as próximas rodadas
Antes de qualquer REINF/retenção, conciliar Domínio x Portal Nacional x Prefeitura (Recebidas e Declaração Mensal) e só então enviar.

## 28s. Skill de retenções atualizada com as tabelas enviadas (12/10/2026)
Tabela de Correlação R-4020 (consultoria, não oficial) incluída na skill conciliacao-retencoes-servicos-tomados: confirma 15044 = Conservação/Manutenção (Atlas 14.01) e 15045 = Segurança/Vigilância (STV 11.02), ambas com IR 1708 + agregado 5952. Tabela 06 (tipo de serviço R-2010) vem de MINUTA v3.0 de 08/2019: conferir vigente. PDF 'tabela_retencao' é a tabela de ÓRGÃOS PÚBLICOS (IN RFB 1.234), não vale para tomador privado.
Efeitos no 238: R-2010 Prime System: nota 493 (recepcionista) -> tipo 100000025 (Portaria, recepção ou ascensorista); nota 494 (limpeza/conservação) -> 100000001. Atlas (15044) tem IR 1708 na natureza: verificar se IRRF é devido (só houve CRF). Códigos do Domínio em 6 dígitos (170806, 595207): sufixo não identificado.

## 28t. 238 — relação municipal de Serviços Tomados conferida (12/10/2026)
Eu havia marcado "n/a" para o município sem abrir `002 ARQUIVOS MUNICIPAIS\...\238_..._NFSE_ServTomados\71456724_202609_NFSE_ServTomados.xlsx` (corrigido a pedido da Fernanda). Conteúdo: 7 notas, valor R$ 15.730,90 (= Domínio), ISS devido 717,96, ISS retido 609,54 (= Declaração Mensal e Portal). Nota 121 (Castro, comp. 08/2026) fora, coerente. Nota 555002 Telefônica: emissão 10/09, prestação 07/09, 'tributação fora do município' (explica a data de entrada 07/09 do Domínio; ajustar no pós-fechamento). O relatório municipal só traz ISS: IRRF/CRF/INSS não têm fonte municipal (coluna 'não se aplica'). Regra: abrir TODAS as fontes da pasta 002/003 antes de marcar qualquer coluna como n/a.

## 28u. 238 REINF 09/2026: decisões e relatório de conferência (12/10/2026)
Fernanda: (1) alíquota 1,50 exibida no Domínio é só demonstração; cálculo e valor a recolher estão corretos (IRRF STV R$ 17,75 = 1%); (2) LeFisc 14.01 (Atlas): IRRF do art. 716 só para limpeza e conservação de BENS IMÓVEIS (1%, cód. 1708), logo sem IRRF para manutenção de elevadores; CSRF 4,65% (5952) aplica (manutenção recorrente, não conserto isolado); vencimento CSRF = último dia útil do 2º decêndio do mês seguinte (art. 35 Lei 10.833) = 20/10/2026 (terça) para fatos de setembro; DCTFWeb/MIT código 5952/07 desde 01/2025 (explica o sufixo 07 do Domínio); (5) data do R-4020 = data da nota (Atlas 04/09, STV 11/09).
Relatório '238_REAT_EFD-Reinf - Envio de Arquivos.pdf' (pasta 005 conferências) confere com o Domínio: R-2010 Prime System 493 (tipo 100000025) e 494 (tipo 100000001) = R$ 1.295,45; R-4020 15044 Atlas 04/09 CSRF 59,32; 15045 STV 11/09 IRRF 17,75 + CSRF 82,54; totais IR 17,75 / agregado 141,86. Recibo do REINF AINDA NÃO localizado no Drive (R-2010/R-4020/R-2099): aguardando sincronizar; REINF fica Pendente até o recibo. Em aberto: declaração do Simples da Prime System (se ausente: IRRF 1% R$ 117,77 + CSRF 4,65% R$ 547,63); Primegrid 994 (abastecimento de gerador: leitura = fora da lista do art. 30, sem CSRF; decisão dela).

## 28v. 238 REINF 09/2026 ENVIADO (12/10/2026 13:49, Oficial)
Relatório '238 - REAT HOLDING LTDA.pdf' (pasta REINF): R-2010 Sucesso recibo 5402225-02-2010-2609-5402225; R-4020 Sucesso recibos 20902902-02-4020-2609-20902902 e 20902903-02-4020-2609-20902903 (um por beneficiário: Atlas e STV); R-2099 Sucesso 12127476-02-2099-2609-12127476; R-4099 Sucesso 5867440-02-4099-2609-5867440. Conferência do envio = Domínio (R-2010 1.295,45; R-4020 IRRF 17,75, agregado 141,86). Observação: alguns eventos aparecem com empresa '1238' e outros '238' (mesmo padrão do 205/'1205'): verificar duplicidade de cadastro no Domínio.
TSV entregue (REINF Enviado + SERVIÇOS TOMADOS Importado). Pendentes: DARF 5952 R$ 141,86 (venc. 20/10), DARF IRRF 1708 R$ 17,75, INSS R$ 1.295,45 via DCTFWeb (gerar agora que o R-2099 foi enviado), subir recibo no G-Click, declaração do Simples da Prime System.

## 28w. Planilha do DP: CONTROLE | DP REINF'S (12/10/2026)
Id 14idmBAj9YO4V_R8_pRbVc4iyDQIhGo9OZwDVOPsPmmM, aba 'MOD GERAL 09.2026' (Nº | Empresa | Obrigação | Status | Observações | Observações-detalhe) e fila 'Atualizações REINF' (Nº | aba | Status | Observação | Detalhe | Rótulo caixa | Valor caixa | Processado). Em branco na 09.2026 e JÁ enviados: 205 (R-2099 sem movimento, 12/10 11:49) e 238 (COM RETENÇÃO: IRRF 170806 R$ 17,75; CRF 595207 R$ 141,86; INSS 1162 R$ 1.295,45; R-2010+R-4020+R-2099+R-4099, 12/10 13:49). Ainda sem envio: 71, 152, 265 (aguardando procuração Gian), 117 (sem procuração). TSV de fila entregue com '\n' literal no Detalhe (padrão da linha 189).

## 28x. 71 CONTE — conciliação de retenções 09/2026 (12/10/2026 ~14:00)
Fontes: Portal Recebidas (142 notas competência 09/2026, R$ 462.851,65), Domínio Entradas (R$ 365.955,02) e Retenções a Recolher (14:02), guia Jundiaí ISS. Retenções federais no Portal em 09/2026: só a nota 659 Giovani Gazen Advogados (01.368.305/0001-13): IRRF 83,61 (1,5%) + CRF 259,20 (4,65%) sobre R$ 5.574,32 = Domínio (170806 / 595207, nat. 15004 Advocacia, item 17.14) ✅. Sem INSS (sem cessão de mão de obra): R-2010 não se aplica. Plano: R-4020 (1 beneficiário) + R-2099 + R-4099.
Divergência: ~39 notas do Portal 09/2026 (R$ ≈ 96.077,71, em geral MEI/Simples e sem retenção federal) não aparecem no Domínio por CNPJ+valor (conferência automática; confirmar por tela): inclui nota 60 Laura de Luca (aguardando Francine) e RIPA 153 (ISS retido 39,43, guia Jundiaí nº 00026073855, venc. 26/10, G-Click 04/10). Serviços Tomados 71 segue Pendente.
Atenção: Chanfro nº 2 (competência 08, IRRF 42,00 + CRF 130,20) e Giovani nº 676 (competência 10, IRRF 83,61 + CRF 259,20) estão na Recebidas mas fora de setembro; confirmar se Chanfro saiu no REINF de agosto. Declaração Mensal de Tomados de Brasília é PDF imagem (não lido).
Pendente: data de pagamento da nota 659 (usar data da nota 01/09/2026 se a Fernanda confirmar), DARF 1708 R$ 83,61 e 5952 R$ 259,20 (5952 vence até 20/10).

## 28y. 71 CONTE REINF 09/2026 ENVIADO (12/10/2026 14:24, Oficial)
Relatório '71 - CONTE CORNETET ARQUITETURA E CONSULTORIA.pdf': R-4020 Sucesso recibo 34371371-01-4020-2609-34371371 (14:24); R-2099 Sucesso 12261147-01-2099-2609-12261147 (14:24); R-4099 Sucesso 5894554-01-4099-2609-5894554 (14:25). Sem R-2010 (sem INSS). Conferência: R-4020 Giovani Gazen 01.368.305/0001-13, nat. 15004, 01/09/2026, bruto 5.574,32, IR 83,61, agregado 259,20 = Domínio. Empresa aparece '171' em R-2099/R-4020 e '71' no R-4099 (mesmo padrão 1205/1238).
Conciliação final: Retenções a Recolher (14:13) = IRRF 83,61 + ISS ret 39,43 (RIPA 153, 29/09) + CRF 259,20 = 382,24; todas as 142 notas do Portal 09/2026 localizadas no Domínio (CNPJ+valor); guia Jundiaí R$ 39,43 'Enviado' na Controle. Fora de setembro: Chanfro nº 2 (comp. 08, IRRF 42,00 + CRF 130,20; conferir se saiu em agosto) e Giovani nº 676 (comp. 10). Controle: SERVIÇOS TOMADOS está 'Sem movimento' (Não Movimento Contratados DF); proposta de 'Importado' fica a critério da Fernanda.
TSV entregue: DP (Atualizações REINF) e Controle_Fiscal (REINF Enviado).

## 28z. 71 — conciliação Portal x Domínio após importar as 39 notas (12/10/2026)
Portal 09/2026: 142 notas (R$ 462.851,65). Domínio Entradas: 142 notas, total série R$ 466.006,65. Nenhuma nota do Portal falta no Domínio (CNPJ+valor+nº). Sobram 3 notas no Domínio sem correspondente no export do Portal (gerado em 03/10): nº 1 CNPJ 69.106.330/0001-62 R$ 1.000,00 (emissão 03/10, entrada 30/09, RJ); nº 17 CNPJ 61.333.593/0001-00 R$ 1.080,00 (emissão 05/10, entrada 01/09, PB; mesmo prestador MEI da nota 16 de 08/2026); nº 1030 CNPJ 35.743.878/0001-00 R$ 1.075,00 (emissão 05/10, entrada 30/09, RS). Soma R$ 3.155,00 = diferença exata entre Domínio e Portal. Emissão em outubro e entrada em setembro (entrada < emissão). Ação: rodar de novo o Portal Nacional do 71 (competência 09/2026) para ver a competência dessas 3 e decidir (setembro x outubro) antes de marcar Serviços Tomados.

## 28aa. 71 — Portal Nacional rodado de novo (12/10/2026 ~14:40)
Novo export Recebidas: 278 notas (antes 250; +28), 09/2026 = 147 notas, R$ 469.779,47. As 3 notas que sobravam no Domínio (nº 1 Luiza Teixeira R$ 1.000,00; nº 17 Vinicius Ferreira R$ 1.080,00; nº 1030 OFFICECONT R$ 1.075,00) agora aparecem no Portal com competência 09/2026 (emitidas em 03 e 05/10): ficam em setembro; ajustar a data de entrada (hoje entrada < emissão). Novas de 09/2026 ainda fora do Domínio: nº 2 Monique de Azevedo (CNPJ 67.662.436/0001-17, MEI, Rio de Janeiro, R$ 1.272,82, emissão 07/10) e uma das duas notas da Laura de Luca Baccarin (45.454.954/0001-02, R$ 2.500,00 cada; Portal tem nº 60 e nº 61, Domínio tem uma). Diferença Portal x Domínio = R$ 3.772,82 (1.272,82 + 2.500,00) = 469.779,47 - 466.006,65. Sem retenção federal nas novas: retenções do Portal em 09/2026 continuam só 659 (IRRF 83,61 + CRF 259,20) e 153 (ISS 39,43). Notas de competência 10/2026 (106) ficam fora. Controle: Serviços Tomados 71 só depois de lançar as 2 notas.

## 28ab. 71 — XMLs das notas que faltam no Domínio (13/10/2026)
SIEG (Drive): `007 ARQUIVOS SIEG\NFS-es\08307701000180\Servico Tomado\2026\{Julho, Agosto, Setembro}`; sem pasta Outubro até 12/10 13:38. As 5 notas com competência 09/2026 do Portal emitidas em outubro têm AAMM 2610 na chave (SIEG separa por mês de emissão), por isso não estão no Drive. Chaves (Portal): nota 2 Monique de Azevedo R$ 1.272,82 (07/10) 33045572267662436000117000000000000226100125049818; nota 61 Laura de Luca R$ 2.500,00 (06/10) 43149022245454954000102000000000006126100693472954. Já no Domínio, só ajustar data de entrada: nota 1 Luiza 33045572269106330000162000000000000126109826798428; nota 17 Vinicius 25075072261333593000100000000000001726102186470951; nota 1030 OFFICECONT 43149022235743878000100000000000103026109523049152. Nota 60 Laura (02/10) já importada. XMLs de Monique nota 1 (04/09, comp. 08, R$ 798,53) e Laura nota 57 (01/09, comp. 08, R$ 2.583,33) existem no SIEG/Setembro, mas são competência 08.

## 28ac. 152 CRBM5 — Retenções a Recolher (Domínio, emissão 14/10/2026) x planilha de retenções do Gian (14/10/2026)
Fontes: PDF `152_CRBM5_Retenções_a_Recolher` (Domínio, 01 a 30/09/2026) e planilha `SETEMBRO 2026` (Drive, compartilhada pela Fernanda). Total Geral Domínio R$ 7.968,86 = ISS 577,56 + PIS 36,34 + COFINS 167,73 + CSLL 55,91 + INSS 1.269,26 + COSIRF 5.862,06.
**Bateu (por código):** 6190 = 5.680,81; 6147 = 141,25; 6188 = 40,00; 6228 = 55,91; 6230 = 36,34; 6243 = 167,73; INSS 1162 = 1.269,26; federais sem INSS = 6.122,04 (planilha = Domínio). Implanta nota 15095: IRRF 1.178,40 (4,8%) classificado no 6190 / natureza 17099 na planilha e no Domínio.
**Divergências abertas (a decidir):** (1) Life Card nota 159: valor R$ 704,59 no Domínio x R$ 131,40 na planilha (retenção 12,41 igual; 12,41 só confere com 9,45% de 131,40); (2) Realize Next nota 3279: natureza 17032 (limpeza) no Domínio x 17031 (vigilância) na planilha; (3) J. Ronier: planilha classifica natureza 17099 / "Compra uso e consumo"; Domínio 17003 (6147, mercadoria); (4) Volpmann nota 42703: emissão 17/08 (planilha), Domínio com data 08/09; ISS 9,12 entra no Domínio (577,56) mas a soma sem ela dá 568,44 = ISS total do planejado (461,69 PoA + 106,75 Estrela); confirmar competência; (5) Volpmann nota 48337 (16/09, ISS 9,41) está no Domínio e não na planilha (a planilha não lista ISS de outros municípios); (6) datas do Domínio (emissão) x pagamento da planilha, todas dentro de setembro; (7) nota 741590 (Rede OK, IRRF 17,66) não está no Domínio nem na planilha.
ISS retido de Estrela = Engi Project R$ 106,75 (notas 1146 e 1218), confere com o Domínio. Outros ISS fora de PoA no Domínio: Projetac 26,20, House Parts 115,91, RFA 21,70 (municípios não conferidos).
Próximo: decisão sobre (1) a (5), enviar a REINF da 152 (R-2010 INSS + R-4020 + R-2099/R-4099) e então o TSV da caixa do DP (valores acima).

### 28ac (continuação, 14/10/2026) — decisões da Fernanda e conferência de XML/prefeitura
Decisões: (1) Life Card nota 159: vale a BC R$ 131,40 (planilha); corrigir o valor da nota no Domínio (704,59 -> 131,40), retenção 12,41 não muda. (3) J. Ronier = mercadoria (Domínio 6147/17003 certo; natureza 17099 da planilha está errada). (4) Volpmann 42703 é de agosto, mas pago em setembro: federais entram em setembro; ISS é de agosto.
XML Realize Next (SIEG/Setembro, ambas emitidas e com competência 02/09/2026): 3279 = "Referente a servico de PORTARIA do mes de AGOSTO de 2026" (nem vigilância 17031 nem limpeza 17032; valores 6190 iguais, muda só a natureza/tipo de serviço); 3280 = "servico de limpeza do mes de AGOSTO de 2026". Natureza de portaria no código 170xx não confirmada (tabela de órgão público não disponível); R-2010 tipo de serviço 100000025 (portaria/recepção) p/ 3279 e 100000001 (limpeza) p/ 3280 (Tabela 06, minuta 2019).
ISS PoA: Declaração Mensal 09/2026 = R$ 461,69 (imposto retido de contribuinte substituído; recibo 03/10 14:02:14). Domínio ISS 577,56 - Estrela 106,75 (Engi) - Volpmann 42703 (9,12, agosto) = 461,69, bate. Correção de afirmação anterior: HAVIA combinação exata.
Achado novo: Volpmann 48337 (16/09, R$ 376,53): XML do Portal tem IRRF 18,07 + CSLL/PIS/COFINS 17,52 (= 3,77 + 2,45 + 11,30) = 35,59 de retenção federal que NÃO aparece no Domínio (Retenções a Recolher) nem na planilha do Gian (só a 42703 está). Conferir se foi paga em setembro e lançar a retenção (6190 passaria de 5.680,81 para 5.716,40 se confirmada).

### 28ac (decisões finais 152, 14/10/2026)
Fernanda: Volpmann 48337 NÃO foi paga: ignorar (fora do R-4020 de setembro; sai para outubro quando paga). Realize 3279 (portaria): natureza 17031 (a planilha estava certa; Domínio tem 17032: ajustar). Ajustes no Domínio antes do REINF: (a) nota 159 Life Card valor 704,59 -> 131,40; (b) nota 3279 Realize natureza 17032 -> 17031; depois reexportar Retenções a Recolher. Totais finais para o REINF: federais 6.122,04 (6190 5.680,81; 6147 141,25; 6188 40,00; 6228 55,91; 6230 36,34; 6243 167,73) + INSS 1162 1.269,26 = 7.391,30. R-2010: 3279 (6.648,48; 731,33) e 3280 (4.890,23; 537,93).

## 28ad. 152 CRBM5 — REINF enviada e TSV (14/10/2026 19:36, Oficial)
Relatório de consulta do envio (Drive, `152 - CONSELHO DE BIOMEDICINA 5 REGIAO.pdf`): todos Sucesso. R-2010 recibo 5745056-04-2010-2609-5745056; R-4020 14 recibos 23511133 a 23511146 (14 beneficiários = 14 do Domínio/planilha); R-2099 12203533-04-2099-2609-12203533; R-4099 5930225-04-4099-2609-5930225. Relatório de conferência (valores por evento) NÃO encontrado no Drive: valores transmitidos não conferidos evento a evento (só pelo número de eventos). TSV da Controle_Fiscal e da caixa do DP em `TSV_DP_REINF_09-2026.md` (versão final 14/10). Serviços Tomados da 152 segue sem linha de status (aguarda confirmação da Fernanda).

### 28ad (continuação) — conferência pelos totalizadores da Receita (prints da Fernanda, 14/10/2026)
R-2099 (totalizador INSS): prestador 01.352.504/0001-33, base R$ 11.538,71 (= 6.648,48 + 4.890,23), código 1162-01, contribuição R$ 1.269,26 (11%), exigibilidade suspensa 0, processado 14/10/2026 19:36:56. R-4099 (totalizador IRRF/CSRF): por natureza 17002 15,21; 17003 126,04 (Casa da Moeda 44,14 + Ronier 81,90); 17027 40,00; 17031 662,77 (Realize 3279 628,28 + Volpmann 34,49); 17032 462,13; 17037 2.046,11; 17099 2.509,80; 17030 55,91 / 36,34 / 167,73. Por código: 614705 141,25; 618805 40,00; 619005 5.680,81; 622805 55,91; 623005 36,34; 624305 167,73 = 6.122,04. Tudo igual ao Domínio e à planilha do Gian. Fernanda ajustou o tipo de serviço da 3279 no R-2010 para 100000025 (portaria); o print não mostra o tipo, registrado pela informação dela. Nota 741590 (Rede OK, emitida em 01/10) não consta da planilha de setembro: fica para outubro, confirmar a data de pagamento.

### 28ae. 152 (17/10/2026)
Fernanda confirmou: Serviços Tomados da 152 pode ser `Importado` (TSV em TSV_DP_REINF_09-2026.md). Verificado na Controle_Fiscal exportada em 17/10: REINF 152 já `Enviado` (processada a versão sem totalizadores); Serviços Tomados 152 ainda em branco; fila Atualizações sem linhas pendentes. A agente não grava na planilha (regra): Fernanda cola e roda `processarAtualizacoes()`.

## 28af. 17/10/2026 — snapshot no Drive e dossiê do cliente 2
Snapshot `PENDENCIAS_E_RESOLVIDOS_2026-10-17.md` criado no Drive (id 1hx_EYkZfz3W9B7mUUwX61EovJ3tzMiIW, 44.303 bytes = cópia de PENDENCIAS.md de 17/10 com 1 linha de cabeçalho; as linhas acrescentadas depois da cópia não estão nele). Dossiê `CLIENTE_002_RF_CONSULTORIA.md` montado a partir da Controle_Fiscal (Jul/Ago/Set2026, Cadastro_Clientes) e das anotações; CLAUDE.md ganhou o gatilho "fechamento da empresa #N".

## 28ag. 17/10/2026 — fechamento empresa #2 (09/2026), levantamento
Dossiê `CLIENTE_002_RF_CONSULTORIA.md` atualizado (seção "Levantamento do fechamento 09/2026"). Achados: FAT já tem set (IRPJ 3.164,83, CSLL 1.898,90, PIS 142,86, COFINS 659,34); DCTFWeb 13/10 com CP 502,51 (venc. 20/10, DP); tomados Freire 2.285,70 (Simples); Controle com Serviços Tomados/Prestados/Receita Aluguéis e DARFs em branco; nada de Domínio/Portal do 2 para set.

## 28ah. 17/10/2026 — empresa #2: Domínio conferido; empresa #16 dossiê
#2: Demonstrativo do Domínio = FAT (PIS 142,86; COFINS 659,34; IRPJ 3.164,83; CSLL 1.898,90). Fernanda: prestados sem movimento, rendimentos zerado. #16: dossiê `CLIENTE_016_QUALIDENTE.md` criado (sem Domínio de set localizado; estimativa pelo Portal PIS 927,18, COFINS 4.279,28, IRPJ 27.918,30, CSLL 12.210,59).

## 28ai. 17/10/2026 — empresa #2, Entradas/Saídas do Domínio
Entradas set: só Officecont 1050 (R$ 879,30; emissão 05/10, entrada 30/09; CFOP 1.933; acum. 800). Saídas set: nota 202609 R$ 21.978,00 (CFOP 5.949; acum. 1002). Freire (2.285,70) fora do Domínio; Officecont fora da prefeitura (emitida depois de 03/10). TSV Serviços Tomados `Pendente` R$ 3.165,00 entregue. Correção: eu tinha dito que o arquivo de Entradas não existia.

## 28aj. 17/10/2026 — empresa #2: decisões e comandos
Fernanda: (1) a Freire não pode ser lançada no Domínio porque não temos as notas (fica Pendente); (2) pediu o comando de retificadora do DecWeb para incluir a Officecont 1050 nos tomados (fase 1 `--retificadora` sem enviar; conferir; fase 2 `--retificadora --enviar`; fase 3); (3) acha que já cobrou o Ricardo: prompt para a extensão Claude no navegador procurar no e-mail (somente leitura), entregue no chat.

## 28ak. 17/10/2026 (noite) — empresa #2: DecWeb retificadora, e-mail, guias
Retificadora 1 (12:48:07): tomados Officecont 1050 + Freire 14263 válidas = R$ 2.022,15; Freire 14320 cancelada. Correção: o valor de 3.165,00 que informei antes estava errado. Guias: PIS/COFINS 802,20 (23/10) e IRPJ/CSLL 5.063,73 (30/10) geradas 17/10, sem G-Click. E-mail: cobrança 04/10, resposta 05/10 (14320 duplicada/cancelada). Código 19831 = proprietário RF na Freire Imóveis.

## 28al. 17/10/2026 — #2 guias conferidas
PIS/COFINS 802,20 (23/10), IRPJ/CSLL 5.063,73 (30/10) = Domínio = FAT; CP DCTFWeb 502,51 (20/10, DP). Sem divergência. Falta G-Click.

## 28am. 17/10/2026 — #2 G-Click: IRPJ/CSLL concluídas 13:00; PIS/COFINS check sem data no print. TSV Enviado entregue.

## 28an. 17/10/2026 — empresa #16 (Qualidente) conferida
Domínio = Portal = DecWeb nos prestados (221 notas, R$ 142.642,60) e tomados (R$ 753,49). Impostos Domínio: PIS 927,18; COFINS 4.279,28; IRPJ 27.918,30; CSLL 12.210,59; ISS 422,87. Pontos de atenção: NF-e das entradas sem XML, crédito de ICMS (acum. 206) em não contribuinte, IBS/CBS, FAT set, guias a gerar. Detalhes no dossiê.

## 28ao. 17/10/2026 — #2 ALERTA distrato do locatário; #16 rendimentos e IBS/CBS
#2: nota Freire 14263 lida (taxa de administração R$ 1.142,85, sem retenção); demonstrativo ago/2026 mostra distrato do Consulado Geral da Itália em 26/08/2026 (aluguel de agosto R$ 19.047,60 em 26 dias): receita fixa de R$ 21.978,00 em ago e set precisa ser confirmada com o cliente antes de enviar/pagar as guias. #16: rendimentos 3º tri `Zerado`; dados de IBS/CBS do acumulador 900 (CST 200 / 200029 / red. 60%) levantados.

## 28ap. 17/10/2026 — #16 Entradas: XMLs conferidos
4 NF-e (9167, 37276, 25042, 76043) = Domínio, R$ 14.596,54. Único ponto: crédito de ICMS R$ 42,57 da Biodental 76043 (acum. 206) sem suporte para não contribuinte; ajustar/ confirmar. Detalhes no dossiê #16.

## 28aq. 17/10/2026 — #16 IBS/CBS reconferido; IBS/CBS vira item fixo do "fechamento da empresa #N"
Fernanda ajustou IBS/CBS dos prestados e removeu o ICMS das entradas. Domínio: débitos IBS 54,87 / CBS 494,84 (ok). Créditos 3,77/33,87 = NF-e 9167 + 76043. Faltam créditos das 4 NFS-e tomadas (CBS 6,64 / IBS 0,74, acum. 800). CLAUDE.md: gatilho agora inclui conferência IBS/CBS (prestados, tomados, entradas XML).

## 28ar. 17/10/2026 — #16 IBS/CBS após ajuste do acum. 800
Créditos IBS 4,53 / CBS 40,65 (esperado 4,51 / 40,51; Domínio usou o valor contábil e não a BC sem ISS do Portal). Débitos conferem. Diferença R$ 0,02/0,14, informativa; aceita salvo decisão contrária da Fernanda.

## 28as. 17/10/2026 — #16 guias PIS/COFINS e IRPJ/CSLL conferidas
PIS/COFINS 5.206,46 (23/10) e IRPJ/CSLL 40.128,89 (30/10) = Domínio, códigos e PA corretos. Falta envio e comprovação no G-Click.

## 28at. 17/10/2026 — #16 guias enviadas (G-Click 18:11)
Tarefas CSLL e IRPJ - LP (Trimestral) e COFINS / PIS concluídas no G-Click em 17/10 18:11, com confirmação da Fernanda. TSV `Enviado` para DARF PIS 927,18, COFINS 4.279,28, IRPJ 27.918,30 e CSLL 12.210,59.

## 28au. 17/10/2026 — #16 encerrado (FAT e DARF PIS ago colados); #18 CC&D preparado
Fernanda confirmou que o FAT de set e a correção da DARF PIS de ago do #16 já estão feitos. Criado `memoria/CLIENTE_018_CCD_INFORMATICA.md`: cadastro, Datasys (retenção 129,15 em ago), REFIS 31,50, Set2026 (declaração/guia/REINF enviados; tomados, prestados, DARFs, SPED em aberto). Aguarda a Fernanda indicar onde salvou os dados mapeados.

## 28av. 17/10/2026 — #18 CC&D: Domínio conferido (só o resumo dos impostos salvo)
PIS/COFINS 13,65/63,00 compensados por retenção (assumida: nota 11 Datasys); IRPJ 56,70 (16%) e CSLL 118,44 (32%) do 3º tri; REFIS 31,50; IBS 1,98 / CBS 17,83. Faltam Entradas/Saídas, XML da nota 11 e confirmação da retenção.

## 28aw. 17/10/2026 — #18 CC&D conferido (nota 11, Saídas, Entradas, FAT, guia REFIS)
Retenção da Datasys confirmada na DANFSe (129,15); Domínio, FAT e nota batem (PIS/COFINS compensados, IRPJ 56,70 / CSLL 118,44, IBS 1,98 / CBS 17,83). Entradas: Officecont NF 1029 R$ 474,80 (emitida 05/10, após o DecWeb). REFIS 31,50 guia gerada. Falta guia IRPJ/CSLL, G-Click do REFIS e conferir a NF 1029 na prefeitura.

## 28ax. 17/10/2026 — #18 REFIS comprovado no G-Click (18:30)
Tarefa REFIS concluída em 17/10 18:30. TSV final do #18 só depois que a Fernanda enviar o restante (pedido dela).

## 28ay. 17/10/2026 — #26 Raldi preparado
Criado `memoria/CLIENTE_026_RALDI.md`. Empresa sem movimento (FAT 2026 todo zero; Ago2026 `Sem movimento`). Set: declaração (03/10, receita 0,00), guia `Sem movimento` e REINF enviados; faltam tomados/prestados, DARFs, SPED e confirmação nas fontes e no Domínio.

## 28az. 17/10/2026 — #18 TSV final entregue
Guia IRPJ/CSLL 175,14 conferida (56,70 + 118,44) e G-Click concluído 18:35; REFIS 18:30. TSV final: prestados `Importado`, PIS/COFINS `Compensado`, IRPJ/CSLL/REFIS `Enviado`; tomados `Pendente` 474,80 (NF 1029).

## 28ba. 17/10/2026 — #26 Raldi: Domínio zerado, sem certificado
Resumo dos Impostos do Domínio zerado (saldos credores antigos PIS 1,90 / COFINS 8,78 / CSLL 8,43). `--verificar-certificados`: 26 SEM CERTIFICADO (Portal não lido). TSV `Sem movimento` proposto com ressalva; rendimentos 3º tri a confirmar.

## 28bb. 17/10/2026 — #18 retificadora 1 do DecWeb conferida; #26 sem certificado
#18: Retificadora 1 enviada 18:42:44 (receita 2.100,00, ISS 42,00); tomados mostram a NF 1029 Officecont 474,80 (prestação 30/09) = Domínio: Serviços Tomados `Importado`. A guia nova é 42,82 (venc. 30/10), com 0,82 de acréscimo; não enviar antes de confirmar o pagamento da original (42,00). Arquivo da guia foi sobrescrito. #26: ver 28ba.

## 28bc. 17/10/2026 — #71 Conte preparado; regra fixa: conferir CONTROLE | Rendimentos ao preparar a empresa
Criado `memoria/CLIENTE_071_CONTE.md`. Prestados Portal x Domínio: 42 notas, R$ 1.091.077,54, tudo igual. Tomados: Portal 147 (469.779,47) x Domínio 145 (466.006,65): faltam nota 2 Monique (1.272,82) e nota 61 Laura (2.500,00). Rendimentos 3º tri do 71: não liberado ("Falta só Informe de Rend. 3º trim/2026 BRADESCO"); estimativa IRPJ ~104.929,63 e CSLL ~69.457,26 (método do FAT). #26: Rendimentos 3º tri `Zerado`. CLAUDE.md: conferir a planilha Rendimentos em todo "fechamento da empresa #N".

## 28bd. 17/10/2026 — #71 Domínio regerado: receita de setembro duplicada (série 900 e série U)
Serviços_71: 42 notas em duas séries (900 e U), Total Geral 2.182.155,08; Resumo com base de PIS/COFINS 2.182.155,08 (PIS 7.091,99 e COFINS 32.732,25 a recolher indevidos) e IRPJ 152.373,51 / CSLL 98.569,15 inflados. Entradas inalteradas (466.006,65; faltam notas 2 e 61). IBS/CBS créditos 16,14/145,38 = Portal sem a nota 61. XML 1811 sem IBS/CBS. Não gerar DARF antes de corrigir o Domínio.

## 28be. 17/10/2026 — #71 Domínio corrigido; pasta _71 criada; #117 sem movimento
#71: série U corrigida (Total Geral = Total Série 1.091.077,54); Resumo PIS/COFINS 0 a recolher; IRPJ 108.730,41 e CSLL 64.003,82 (sem rendimentos); estimativa com rendimentos IRPJ ~104.929,63 / CSLL ~69.457,26; FAT conferido (reproduz 1º, 2º e parcial do 3º tri); LC 224/2025 +10% já considerado, ADI 7936 com liminares noticiadas. Entradas ainda sem as notas 2 e 61 (XMLs fora do Drive; pasta `_71` criada em 007 ARQUIVOS SIEG). #117: tudo sem movimento conforme prefeitura (processo de baixa, sócio falecido), Rendimentos 3º tri Zerado; dossiê `CLIENTE_117_TABAJARA.md`; TSV entregue.

## 28bf. 17/10/2026 — #71 Resumo com rendimentos e pasta _71 conferida
Resumo 19:15: IRPJ 104.929,65 e CSLL 69.457,20 (= estimativa). Pasta `_71` tem o pacote do Portal de 06/10 (sem as notas 2 Monique e 61 Laura; só a 60 Laura). Entradas inalterado. Falta baixar os XMLs das 2 notas, lançar, regerar; informe Bradesco; guias IRPJ/CSLL.

## 28bg. 17/10/2026 — #71 XMLs das notas 2 e 61 conferidos
Nota 2 Monique (MEI, R$ 1.272,82, comp. 20/09, sem IBS/CBS) e nota 61 Laura (R$ 2.500,00, comp. 30/09, CST 200/200052, IBS 1,75 e CBS 15,75) = Portal. Falta lançar no Domínio e regerar Entradas/Resumo.

## 28bh. 17/10/2026 — #71 Domínio final conferido
Entradas 147 notas, 469.779,47 = Portal; créditos IBS 17,89 / CBS 161,13 = Portal; Serviços 1.091.077,54 sem duplicidade; IRPJ 104.929,65 / CSLL 69.457,20; PIS/COFINS 0. TSV: Prestados e Tomados `Importado`, PIS/COFINS `Retido`; IRPJ/CSLL `Pendente` (guias).

## 28bi. 17/10/2026 — #126 Tatsch & Leite preparado; #71 Domínio final conferido (log 28bh)
Criado `memoria/CLIENTE_126_TATSCH_LEITE.md`: Portal 209 emitidas (153.662,41, sem IBS/CBS) / 15 recebidas (10.981,61, CRF 10,46, CBS 5,97 / IBS 0,66); Domínio de 05/10 desatualizado (faltam saídas 1760–1841); FAT ago/set em branco; estimativas PIS 998,81 / COFINS 4.609,87 e IRPJ 23.289,40 / CSLL 10.544,19; Rendimentos 3º tri `Sim`.
