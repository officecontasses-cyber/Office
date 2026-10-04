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
