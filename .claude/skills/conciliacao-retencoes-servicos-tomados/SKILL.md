---
name: conciliacao-retencoes-servicos-tomados
description: "Conciliação de retenções na fonte de serviços tomados (IRRF, PIS/COFINS/CSLL, INSS e ISS) entre Portal Nacional (NFS-e e EFD-Reinf), Domínio (Retenções a Recolher, Acompanhamento de Entradas, razão) e relatórios municipais. Cobre naturezas de rendimento, códigos de retenção, dispensas, regras de conciliação, tipos de divergência e checklist por fornecedor. Use antes de transmitir R-2010, R-4010, R-4020 e R-2099."
---

# Conciliação de retenções de serviços tomados

Papel: especialista sênior em retenções na fonte e EFD-Reinf, atuando como conciliador. O **Domínio deve ser o espelho do Portal Nacional e da prefeitura**: ao final, os valores de retenção batem entre as três fontes, por fornecedor, competência, base, alíquota e código.

Escopo: **somente retenções sobre serviços tomados**. Fora do escopo: escrituração geral, apuração de tributos sobre a receita do prestador e outras obrigações.

## Como ler esta skill (índice por tema)

| Preciso de... | Vá para |
|---|---|
| Entender o que está marcado como "verificar" | [0. Legenda de confiança](#0-legenda-de-confiança) |
| Fluxo completo da conciliação | [1. Fluxo e fontes](#1-fluxo-e-fontes) |
| Natureza de rendimento e tipo de serviço (Reinf) | [2. Naturezas de rendimento](#2-naturezas-de-rendimento-efd-reinf) |
| Alíquota, base, código e prazo de cada retenção | [3. Códigos de retenção](#3-códigos-de-retenção) |
| Quando não reter | [4. Dispensas e isenções](#4-dispensas-e-isenções) |
| Como cruzar nota x lançamento x Reinf x município | [5. Regras de conciliação](#5-regras-de-conciliação) |
| Classificar e corrigir um erro | [6. Divergências](#6-tratamento-de-divergências) |
| Validar um fornecedor | [7. Checklist por fornecedor](#7-checklist-por-fornecedor) |
| Formato da resposta e integração com o fechamento | [8. Entrega](#8-formato-de-entrega-e-integração-com-o-fechamento) |
| Exemplos práticos | [9. Exemplos](#9-exemplos-práticos) |
| Registrar o REINF enviado nas planilhas (Controle_Fiscal e DP) | [10. Pós-transmissão](#10-pós-transmissão-registro-nas-planilhas) |

## 0. Legenda de confiança

Esta skill foi escrita a partir de: (a) a **Tabela de Correlação da EFD-Reinf (evento R-4020)** fornecida pela Fernanda em 12/10/2026, material de consultoria **sem caráter oficial** (a própria fonte avisa que não existe correlação oficial entre itens da LC 116 e naturezas); (b) o **Anexo I dos Leiautes da EFD-Reinf v3.0, que é uma minuta de agosto/2019** (usada só para a Tabela 06; a numeração de natureza dessa minuta não é a que o Domínio usa); (c) a lista de códigos de receita (COD_REC) da Receita; (d) a Tabela de Retenção do Anexo I da IN RFB 1.234 (pagamentos de **órgãos públicos**, não de empresas privadas). Nada disso substitui o Manual vigente. Cada regra traz um selo:

- 🟢 **Consolidado**: regra estável, conferida entre as skills internas e a prática do escritório.
- 🟡 **Verificar**: depende de legislação que muda, de número de artigo, de código que não pude confirmar ou de divergência entre fontes. **Confirme na versão vigente antes de aplicar** e diga isso ao usuário.
- 🔴 **Não confirmado**: não afirmar; buscar na fonte oficial.

Fontes oficiais a consultar: Manual de Orientação do Contribuinte da EFD-Reinf e seu Anexo I (Tabela 01 naturezas de rendimento x código de receita, Tabela 06 tipos de serviço) no portal SPED da Receita; LeFisc/Decreto 9.580/2018 (RIR/2018); IN RFB 1.234/2012 (retenções de CRF e IRRF, com alterações); Lei 10.833/2003 arts. 30 a 36; Lei 8.212/1991 art. 31; LC 116/2003 e leis do município.

Regra de ouro: **na dúvida, o documento oficial vence a regra deduzida** (guia, Portal, Tabela 01), e a dúvida vai para o relatório como ⚠️, nunca como certeza.

## 1. Fluxo e fontes

Competência e fato gerador (🟢 conceito, 🟡 detalhes):
- **ISS e INSS (R-2010):** pela competência da nota/serviço.
- **IRRF e CSRF (R-4020):** o fato gerador é o **pagamento/crédito**. Nota emitida em setembro e paga em outubro entra no R-4020 de outubro. Sempre pedir a data de pagamento.

Fontes por esfera:

| Esfera | Documento | O que extrair |
|---|---|---|
| Portal Nacional (NFS-e) | "Recebidas - Completa" (xlsx/csv) | Nº, competência, prestador, valor, Simples/MEI, Cód. Tributação Nacional (item LC 116), ISS e retenção, IRRF, contrib. sociais retidas (PIS/COFINS/CSLL), contrib. previdenciária retida, descrição |
| Portal Nacional (Reinf) | Relatório de consulta do envio (EFD-Reinf) | Evento, tipo de envio, situação, nº do recibo, data/hora |
| Domínio | Acompanhamento de Entradas | Nota, datas de emissão e entrada, CFOP, acumulador, valor contábil, base/alíquota/valor por imposto |
| Domínio | Retenções a Recolher | Fornecedor, nota, data, valor, retenção, **Cód. Rec.** e **Nat. Rend.** por imposto |
| Município | Declaração Mensal / relatório de serviços tomados | ISS retido por contribuinte substituído, recibo e data |
| Pagamento | Comprovantes/extrato/G-Click | Data e valor pagos, DARF/GPS/guia recolhidos |

Passos:
1. Conferir o **CNPJ dentro do arquivo** (nunca só o nome; já houve arquivo de um cliente com dados de outro).
2. Filtrar a competência (relatórios trazem notas de meses vizinhos) e excluir canceladas.
3. Montar uma linha por **nota x tributo** com as quatro fontes lado a lado (seção 5).
4. Classificar cada diferença (seção 6) e só depois liberar o Reinf.

## 2. Naturezas de rendimento (EFD-Reinf)

### 2.1 Como escolher a natureza (R-4020, pagamentos a PJ)
1. Partir do **código de tributação nacional/item da LC 116** da nota (Portal) e da **descrição do serviço**.
2. Achar a natureza na tabela 2.2 (a coluna de itens é só referência interpretativa).
3. Conferir se o **código de receita** da natureza (IR e/ou agregado 5952) é o que o Domínio mostra em "Cód. Rec." na Retenções a Recolher.
4. Na dúvida entre duas naturezas, ficar com a de **descrição mais específica**; se nenhuma serve, usar **15099** (demais serviços técnicos, de assistência técnica/administrativa e semelhantes), registrando ⚠️.
5. Registrar no relatório: código, descrição literal e item da LC 116 usado.

Ressalvas (🟡): (i) a tabela abaixo é correlação de consultoria, não oficial; confirmar a natureza no Manual vigente (os códigos de 5 dígitos 15xxx são os usados hoje pelo Domínio); (ii) a natureza indica **quais tributos podem incidir** (IR e/ou agregado), mas **não prova que a retenção é devida** no caso concreto: dispensas (seção 4), limites e regime do prestador continuam valendo; (iii) o pagamento sem retenção pode ter de ser informado com retenção zero.

### 2.2 Tabela de correlação (natureza x código de receita x itens LC 116)

"Agreg. 5952" = retenção agregada de CSLL + COFINS + PIS (DARF 5952). Em "IR" aparece o código de receita do IRRF.

| Cód. | Natureza | IR | Agreg. | Itens LC 116 |
|---|---|---|---|---|
| 15001 | Cooperativas de trabalho: serviços pessoais prestados por associados | 3280 | – | diversos |
| 15002 | Associações de profissionais: serviços pessoais prestados por associados | 1708 | 5952 | diversos |
| 15003 | Administração de bens ou negócios em geral (exceto consórcios/fundos mútuos) | 1708 | 5952 | 17.12 |
| 15004 | Advocacia | 1708 | 5952 | 17.14 |
| 15005 | Análise clínica laboratorial | 1708 | 5952 | 4.02, 5.03 |
| 15006 | Análises técnicas | 1708 | 5952 | 17.01 a 17.09 |
| 15007 | Arquitetura | 1708 | 5952 | 7.01 a 7.19 |
| 15008 | Assessoria e consultoria técnica (exceto assistência técnica a terceiros ligada a ramo de indústria/comércio do prestador) | 1708 | 5952 | 17.01 a 17.03 |
| 15009 | Assistência social | 1708 | 5952 | 27.01 |
| 15010 | Auditoria | 1708 | 5952 | 17.16 |
| 15011 | Avaliação e perícia | 1708 | 5952 | 17.09, 28.01 |
| 15012 | Biologia e biomedicina | 1708 | 5952 | 30.01, 4.01 |
| 15013 | Cálculo em geral | 1708 | 5952 | 17.18 |
| 15014 | Consultoria | 1708 | 5952 | 1.06, 17.01, 17.20 |
| 15015 | Contabilidade | 1708 | 5952 | 17.19 |
| 15016 | Desenho técnico | 1708 | 5952 | 23.01, 31.01, 32.01 |
| 15017 | Economia | 1708 | 5952 | 17.20 |
| 15018 | Elaboração de projetos | 1708 | 5952 | 7.03 |
| 15019 | Engenharia (exceto construção de estradas, pontes, prédios e obras assemelhadas) | 1708 | 5952 | 7.01 a 7.19 |
| 15020 | Ensino e treinamento | 1708 | 5952 | 8.02, 17.24 |
| 15021 | Estatística | 1708 | 5952 | 17.21 |
| 15022 | Fisioterapia | 1708 | 5952 | 4.08 |
| 15023 | Fonoaudiologia | 1708 | 5952 | 4.08 |
| 15024 | Geologia | 1708 | 5952 | 7.01 |
| 15025 | Leilão | 1708 | 5952 | 17.13 |
| 15026 | Medicina (exceto ambulatório, banco de sangue, casa de saúde/repouso sob orientação médica, hospital e pronto-socorro) | 1708 | 5952 | 4.01 |
| 15027 | Nutricionismo e dietética | 1708 | 5952 | 4.10 |
| 15028 | Odontologia | 1708 | 5952 | 4.12 |
| 15029 | Organização de feiras, congressos, seminários, simpósios e congêneres | 1708 | 5952 | 17.10 |
| 15030 | Pesquisa em geral | 1708 | 5952 | 2.01, 17.01 |
| 15031 | Planejamento | 1708 | 5952 | 1.08, 17.03 |
| 15032 | Programação | 1708 | 5952 | 1.01, 1.02, 1.04, 1.07, 1.08 |
| 15033 | Prótese | 1708 | 5952 | 4.14 |
| 15034 | Psicologia e psicanálise | 1708 | 5952 | 4.15, 4.16 |
| 15035 | Química | 1708 | 5952 | 7.12, 30.01 |
| 15036 | Radiologia e radioterapia | 1708 | 5952 | 4.02 |
| 15037 | Relações públicas | 1708 | 5952 | 35.01 |
| 15038 | Serviço de despachante | 1708 | 5952 | 33.01 |
| 15039 | Terapêutica ocupacional | 1708 | 5952 | 4.08 |
| 15040 | Tradução ou interpretação comercial | 1708 | 5952 | 17.02 |
| 15041 | Urbanismo | 1708 | 5952 | 7.01, 7.19 |
| 15042 | Veterinária | 1708 | 5952 | 5.01 |
| 15043 | **Limpeza** | 1708 | 5952 | 7.10, 7.11, 14.01 |
| 15044 | **Conservação/Manutenção**, exceto reformas e obras assemelhadas | 1708 | 5952 | 7.10, 7.11, 14.01 |
| 15045 | **Segurança/Vigilância/Transporte de valores** | 1708 | 5952 | 11.02, 11.05 |
| 15046 | **Locação de mão de obra** | 1708 | 5952 | 17.05 |
| 15047 | Assessoria creditícia, mercadológica, gestão de crédito, seleção e riscos, administração de contas a pagar e a receber | 5944 | 5952 | 10.04 |
| 15050 | Transporte internacional de valores por empresas nacionais; estaleiros navais (REB) em conservação, modernização, conversão e reparo | 1708 | – | n/a |
| 15051 | Pagamento a empresas estrangeiras de transporte de valores | 1708 | – | n/a |
| 15052 | Demais comissões, corretagens ou outra importância por representação comercial ou mediação de negócios civis e comerciais (fora dos códigos do grupo 20) | 8045 | – | 10.09 |
| 15099 | Demais serviços técnicos, de assistência técnica, de assistência administrativa e semelhantes | 1708 | 5952 | 14.02, 31.01, outros |

Pontos de atenção da tabela:
- **Confirma o que o Domínio usou no 238:** 15044 = Conservação/Manutenção (Atlas, item 14.01) e 15045 = Segurança/Vigilância (STV, item 11.02). 🟡 (conferência com a tabela de consultoria, não com o Manual vigente.)
- 15044 traz **IR 1708 e agregado 5952**: logo, o IRRF da manutenção/conservação é uma questão real a verificar (no 238 só houve CRF na nota Atlas). Resolvido no 238 pelo LeFisc: o IRRF do art. 716 incide só sobre limpeza e conservação de **bens imóveis** (1%, código 1708); manutenção de elevadores fica sem IRRF.
- 15003 a 15042 e 15099 são serviços profissionais e técnicos; 15043 a 15046 são limpeza, conservação, vigilância e mão de obra, que na prática de retenção têm IRRF de 1% e CSRF (ver seção 3).
- Item **10.05** (corretagem de bens móveis/imóveis, caso real da 257) **não aparece** na correlação; a tabela mapeia comissões/corretagens ao item 10.09 (15052, DARF 8045). Para 10.05 usar o código 8045 e registrar ⚠️ (usado na 257).
- Códigos de natureza com a minuta v3.0/2019 (numeração de 9 dígitos, ex.: 500000052) **não** são os do Domínio: não usar.

### 2.3 Tipo de serviço do R-2010 (INSS: cessão de mão de obra/empreitada), Tabela 06 (minuta v3.0, ago/2019 🟡)

| Código | Tipo de serviço |
|---|---|
| 100000001 | Limpeza, conservação ou zeladoria |
| 100000002 | Vigilância ou segurança |
| 100000003 | Construção civil |
| 100000004 | Serviços de natureza rural |
| 100000005 | Digitação |
| 100000006 | Preparação de dados para processamento |
| 100000007 | Acabamento |
| 100000008 | Embalagem |
| 100000009 | Acondicionamento |
| 100000010 | Cobrança |
| 100000011 | Coleta ou reciclagem de lixo ou de resíduos |
| 100000012 | Copa |
| 100000013 | Hotelaria |
| 100000014 | Corte ou ligação de serviços públicos |
| 100000015 | Distribuição |
| 100000016 | Treinamento e ensino |
| 100000017 | Entrega de contas e de documentos |
| 100000018 | Ligação de medidores |
| 100000019 | Leitura de medidores |
| 100000020 | Manutenção de instalações, de máquinas ou de equipamentos |
| 100000021 | Montagem |
| 100000022 | Operação de máquinas, de equipamentos e de veículos |
| 100000023 | Operação de pedágio ou de terminal de transporte |
| 100000024 | Operação de transporte de passageiros |
| 100000025 | Portaria, recepção ou ascensorista |
| 100000026 | Recepção, triagem ou movimentação de materiais |
| 100000027 | Promoção de vendas ou de eventos |
| 100000028 | Secretaria e expediente |
| 100000029 | Saúde |
| 100000030 | Telefonia ou telemarketing |
| 100000031 | Trabalho temporário na forma da Lei nº 6.019/1974 |

Aplicação ao 238 (Prime System): nota 493 (recepcionista, item 17.05.01) → 100000025; nota 494 (limpeza e conservação) → 100000001. Selecionar pelo **serviço efetivamente prestado**, não pelo item da LC 116. Esses tipos foram usados no envio do 238 em 12/10/2026 e constam no relatório de conferência.

Tabela de trabalho (preencher a cada conciliação):

| Serviço (item LC 116) | Natureza no Domínio | Natureza correta | Descrição literal | Selo |
|---|---|---|---|---|
| (preencher) | (preencher) | (preencher) | (preencher) | ⬜ |

Como diferenciar naturezas parecidas: o texto do serviço prevalece sobre o título da nota; se o mesmo prestador faz serviços mistos (ex.: vigilância + monitoramento), classificar **por nota**, não por fornecedor; se não houver descrição na tabela, ⚠️ e consultar o contador responsável.

## 3. Códigos de retenção

| Tributo | Alíquota | Base | Recolhimento | Selo |
|---|---|---|---|---|
| **IRRF** serviços profissionais e outros serviços de PJ | 1,5% | valor do serviço | DARF; código de receita conforme a natureza (Tabela 01) | 🟡 código |
| **IRRF** limpeza e conservação de bens imóveis (LeFisc: art. 716, Decreto 9.580/2018, nota 1) | 1% | valor do serviço | DARF 1708 | 🟢 alíquota e 1708 |
| **IRRF** segurança, vigilância e locação de mão de obra | 1% (o Domínio pode exibir "1,50" como demonstração; o valor a recolher é o que vale); confirmar a regra no LeFisc | valor do serviço | DARF | 🟡 |
| **CSRF** (CSLL 1% + COFINS 3% + PIS 0,65%) | 4,65% total | valor do serviço | DARF **5952** único (soma dos três); confissão na DCTFWeb (MIT) como 5952/07 desde os fatos geradores de 01/2025 | 🟢 alíquota e 5952 |
| **INSS** cessão de mão de obra/empreitada | 11% | valor bruto (a base pode ser reduzida por materiais/equipamentos quando destacados e permitidos) | Reinf R-2010, débito na DCTFWeb | 🟢 11%, 🟡 base e forma de pagamento |
| **ISS** retido | alíquota do município (mínimo geral 2%, LC 157) | valor do serviço (ou base do item) | guia/DAM do município | 🟢 conceito, 🟡 por município |

Códigos de receita relevantes (lista COD_REC da Receita; confirmar a vigência):

| Código | Descrição na lista |
|---|---|
| 1708 | Remuneração de serviços profissionais prestados por Pessoa Jurídica |
| 5952 | Retenções de Contribuições, pagamento PJ a PJ de Direito Privado (CSLL + COFINS + PIS) |
| 5979 | PIS/PASEP, retenção pagamento PJ a PJ de Direito Privado |
| 5960 | COFINS, retenção pagamento PJ a PJ de Direito Privado |
| 5987 | CSLL, retenção pagamento PJ a PJ de Direito Privado |
| 8045 | Comissões e corretagens pagos à PJ e serviços de propaganda prestados por PJ (art. 53 da Lei 7.450/85) |
| 5944 | Pagamento de PJ a PJ por serviços de factoring |
| 3280 | Serviços pessoais prestados por associados de cooperativas de trabalho |
| 8863 | Bens e serviços adquiridos de sociedades cooperativas e associações profissionais (**tabela de órgãos públicos**) |
| 6147, 6175, 6188, 6190, 9060, 8739, 8767, 8850 | Retenções **de órgãos públicos federais** (IN RFB 1.234, Anexo I): não se aplicam a tomador privado |

Atenção: no Domínio e na planilha do DP os códigos aparecem com 6 dígitos (ex.: 170806, 595207). O sufixo `07` de 595207 corresponde à variação 5952/07 da CSRF na DCTFWeb (fonte: LeFisc). O sufixo `06` de 170806 é interpretado como variação equivalente do 1708, **sem confirmação**. 🟡

Prazos:
- **CSRF 5952 (🟢, LeFisc, art. 35 da Lei 10.833):** até o último dia útil do **2º decêndio do mês subsequente** ao mês dos fatos geradores (fatos de setembro: vence até o último dia útil até 20/10).
- IRRF (🟡): o prazo depende do código de receita; não afirmar de memória. Consultar a regra vigente do código usado.
- INSS retido (🟡): prazo da DCTFWeb/guia do mês seguinte. Verificar o dia.
- ISS retido: lei municipal (Porto Alegre: ver guia gerada no DecWeb; usar a data impressa na guia, nunca regra deduzida).

**Regra do limite de dispensa da CSRF (🟢 LeFisc/Solução de Consulta Cosit 258/2024):** fica dispensada a retenção de valor igual ou inferior a R$ 10,00 (exceto DARF eletrônico via Siafi). O limite é verificado **sobre o valor a ser retido em cada pagamento** (soma das três alíquotas, 4,65%), mesmo que haja mais de um pagamento no mesmo dia. R$ 10,00 ÷ 4,65% = R$ 215,05 de pagamento, referência prática. 🟡 A leitura anterior de "somar os pagamentos do mês" foi substituída por esta, que vem da solução de consulta citada pelo LeFisc.

**Manutenção em caráter isolado (🟢 LeFisc, IN SRF 459/2004 art. 1º §2º II):** não há retenção de CSRF se a manutenção for efetuada em caráter isolado, como mero conserto de bem defeituoso. Manutenção contratada de forma recorrente (ex.: elevadores, mensal) retém.

**Valor abaixo do limite de dispensa:** retenção zero é o resultado **correto**, não divergência. Registrar a conta (valor x 4,65% = X ≤ R$ 10) no relatório.

## 4. Dispensas e isenções

Sempre exigir comprovação por escrito arquivada com a nota:

| Hipótese | Efeito | Condição a comprovar | Selo |
|---|---|---|---|
| Prestador optante do Simples Nacional | Dispensa IRRF e CSRF | Declaração do prestador, **em 2 vias assinadas pelo representante legal**, modelo do Anexo I da IN SRF 459/2004 (arts. 3º e 11) e IN RFB 765/2007; o Portal mostra a opção, mas não substitui a declaração. Sem a declaração, o tomador deve reter. | 🟢 (LeFisc) |
| Simples com cessão de mão de obra/empreitada (serviços do art. 18, §5º-C da LC 123, Anexo IV) | **Não dispensa o INSS 11%** | Enquadramento do serviço | 🟡 |
| MEI | Sem IRRF/CSRF; INSS 11% só nas atividades de cessão/empreitada permitidas ao MEI (hidráulica, elétrica, pintura, alvenaria, carpintaria, manutenção/reparo de veículos) | CCMEI e atividade | 🟡 |
| Valor mínimo | CSRF: valor a reter ≤ R$ 10,00 por pagamento; IRRF de valor ≤ R$ 10 | Cálculo | 🟢 CSRF / 🟡 IRRF |
| Cooperativas (CSLL) | Sem retenção de CSLL; PIS e COFINS retidos (cooperativa em geral) | Natureza 15001/15002 e art. 21 da Lei 10.865/2004 | 🟡 |
| Entidades imunes/isentas | Dispensa de IRRF/CSRF conforme a norma; se isenta só de alguns tributos, retém-se pelos demais (recolhimento individualizado 5987 CSLL, 5979 PIS, 5960 COFINS) | Declaração/comprovação, com o enquadramento legal na nota | 🟡 |
| Órgãos públicos | Regra própria (Lei 9.430/96 art. 64 e IN RFB 1.234/2012). A Tabela de Retenção do Anexo I tem IR + CSLL + COFINS + PIS por natureza: p.ex. 4,80% de IR (total 9,45%, código 6190) para vigilância, limpeza, locação de mão de obra e demais serviços; **não vale para tomador privado** | Ver skill `conferencia-retencoes-pagamentos-orgao-publico` | 🟡 |
| Serviço fora da lista das retenções de CSRF | Sem CSRF | Item da lista da Lei 10.833, art. 30: limpeza, conservação, manutenção, segurança, vigilância, transporte de valores, locação de mão de obra, assessoria creditícia/mercadológica, gestão de crédito, seleção e riscos, administração de contas a pagar e a receber, e serviços profissionais (a nota deve ser enquadrada, não presumida). Ex.: "abastecimento de gerador" não consta (decisão do contador). | 🟢 lista / 🟡 enquadramento |
| ISS: prestador estabelecido em outro município e serviço não listado como retido pelo tomador | Sem retenção pelo tomador; ISS recolhido na origem | Local de incidência (LC 116 art. 3º e 6º e LC 175/2020) e lei municipal | 🟡 |

Cuidados:
- "Simples" no Portal = optante; não prova dispensa se faltar a declaração.
- Item 10.05 (comissão/corretagem): IRRF 1,5%; sem CSRF por falta de previsão legal confirmada no LeFisc (caso real da 257). Não generalizar para outros itens.
- Notas com texto "isento de retenção de INSS conforme IN RFB 2110/2022 art. 111" (monitoramento de alarmes etc.): confirmar se o serviço realmente não é cessão de mão de obra.

## 5. Regras de conciliação

Montar para **cada nota e tributo** a linha:

`Nota | Prestador/CNPJ | Competência | Data pagamento | Valor | Tributo | Base | Alíq. | Portal NFS-e | Reinf (evento/recibo) | Domínio (Entradas) | Domínio (Retenções a Recolher + Cód. Rec. + Nat. Rend.) | Município | Selo`

Cruzamentos obrigatórios:
1. **Nota x Domínio Entradas:** valor contábil, datas (entrada ≥ emissão), CFOP/acumulador, base, alíquota e valor por imposto. A soma por imposto do relatório deve bater com o total da seção "Total Geral".
2. **Domínio Entradas x Retenções a Recolher:** mesmo fornecedor, nota e valor; total geral das retenções = soma dos totais por imposto.
3. **Portal x Domínio:** retenção destacada na nota = retenção lançada. Conferir por tributo (IRRF, PIS/COFINS/CSLL, INSS, ISS). Lembrar que o Portal pode trazer retenção de PIS/COFINS/CSLL "não retidos" em campos separados.
4. **ISS: Domínio x município:** a soma do ISS retido no Domínio deve ser igual ao "imposto retido de contribuinte substituído" da Declaração Mensal (ou do relatório municipal) e da guia. Abrir também a relação de serviços tomados do município (`002 ARQUIVOS MUNICIPAIS`).
5. **Reinf x Domínio:** R-2010 por nota (INSS: valor bruto, base, retenção, tipo de serviço); R-4020 por pagamento (natureza, base, IRRF, CSRF) com data de pagamento; totais do evento = Retenções a Recolher da competência; conferir recibo e se R-2099/R-4099 fecharam.
6. **Pago/recolhido:** DARF/GPS/guia pagos x valor retido, por código de receita e período de apuração.
7. **Competência:** nota com competência diferente da pedida fica fora (ex.: competência 08 emitida em setembro; competência de outubro emitida antes). Registrar como "fora da competência" e verificar se foi lançada no mês certo.
8. **Fornecedor:** CNPJ do fornecedor igual nas quatro fontes (filial x matriz muda a inscrição e o código do município).

Tolerância: diferença de R$ 0,01 por arredondamento nota a nota é ✅ com observação.

## 6. Tratamento de divergências

| Tipo | Como identificar | Ajuste recomendado |
|---|---|---|
| Retenção não feita | Base sujeita, sem retenção em Portal/Domínio | Verificar dispensa; se devida, retificar nota/lançamento e recolher; avaliar cobrança ao prestador (se já pago), multa e juros |
| Retenção a maior | Valor retido > base x alíquota | Estornar o excesso, devolver/compensar com o prestador, retificar DARF/Reinf |
| Retenção a menor | Valor retido < esperado | Complementar com recolhimento em atraso e retificação |
| Natureza incorreta | Natureza do Domínio/Reinf não condiz com o item da nota | Corrigir cadastro/lançamento no Domínio e retificar o evento |
| Dispensa indevida | Dispensa aplicada sem comprovação (declaração do Simples ausente, valor a reter acima de R$ 10) | Obter a declaração ou reter; recolher e retificar |
| Código de recolhimento errado | DARF com código de receita diferente do da natureza | Retificar DARF/PER-DCOMP e ajustar o Reinf |
| Domínio x Portal | Falta nota, valor, alíquota ou fornecedor | Lançar/corrigir no Domínio (o Domínio espelha o Portal); se o Portal estiver errado, pedir cancelamento/substituição ao prestador |
| Domínio x município | ISS retido diferente da Declaração Mensal | Corrigir lançamento ou retificar a declaração municipal |
| Competência/data | Competência errada ou entrada anterior à emissão | Ajustar no Domínio; reposicionar no mês certo |
| Advertência de importação XML | Impostos IBS/CBS sem acumulador, datas | Ajustar acumuladores/datas no pós-fechamento (não trava o fechamento) |

Regra: divergência é **achado para o contador decidir**, não correção automática. Enquanto houver divergência aberta, a linha de Serviços Tomados fica `Pendente` e o REINF não é transmitido.

## 7. Checklist por fornecedor

- [ ] CNPJ conferido dentro dos arquivos (Portal, Domínio, município)
- [ ] Regime: Simples, MEI, Presumido/Real, imune/isento? (Portal + consulta de CNPJ quando necessário)
- [ ] Declaração do Simples/imunidade arquivada?
- [ ] Natureza da prestação e **código de tributação nacional/item LC 116**
- [ ] É cessão de mão de obra ou empreitada? (INSS 11%)
- [ ] Local de incidência do ISS e se o tomador é responsável (LC 116 art. 3º/6º, lei municipal)
- [ ] Valor a reter por pagamento (limite de R$ 10,00 da CSRF) e valor líquido a pagar
- [ ] Data de pagamento (fato gerador de IRRF/CSRF)
- [ ] Natureza de rendimento e tipo de serviço conferidos na tabela vigente
- [ ] Domínio = Portal = município = Reinf = guia paga
- [ ] Competência correta e data de entrada ≥ emissão
- [ ] Dispensa documentada ou retenção feita e recolhida no código certo

## 8. Formato de entrega e integração com o fechamento

Entrega visual, com selos ✅ ❌ ⚠️ ⬜:
1. Painel-resumo por tributo: Domínio | Portal | Município | Reinf | Diferença | Selo.
2. Tabela por nota (seção 5) e memória de cálculo (base x alíquota = devido x retido).
3. Pendências por risco (alto/médio/baixo), responsável e prazo.
4. Roteiro dos eventos: R-2010, R-4010, R-4020, R-2099 (e R-4099 se aplicável), com data de pagamento para o R-4020.
5. Ajustes na Domínio (inclusive pós-fechamento).

Integração com a rotina da OfficeCont (CLAUDE.md):
- `Serviços Tomados` só `Importado`/`Enviado` depois que o Domínio foi importado e **conciliado**; até lá `Pendente`.
- Nada é escrito direto na Controle_Fiscal; TSV de 7 colunas na aba `Atualizações`; status só com confirmação explícita.
- O REINF `Enviado` tem recibo do Portal como comprovação (R-2099: nº do recibo e data/hora).
- Registrar a rodada na memória (`memoria/PENDENCIAS.md`, log do processo e snapshot no Drive).

## 9. Exemplos práticos

**Exemplo 1: tudo bate (REAT 238, Atlas, nota 19764).** Serviço 14.01 de R$ 1.275,60, prestador não optante. CSRF: 1.275,60 x 4,65% = 59,32. Portal 59,32, Domínio 59,32, retenção em 5952, natureza 15044, sem IRRF (manutenção de elevadores não é limpeza/conservação de imóvel). ✅

**Exemplo 2: alíquota exibida diferente (STV, nota 20038).** Vigilância de R$ 1.774,97. Portal: IRRF 17,75 (= 1%). Domínio exibe 1,50 como demonstração, valor a recolher 17,75. ✅ (decisão da Fernanda: o cálculo e o valor a recolher estão corretos).

**Exemplo 3: Simples com INSS (Prime System, notas 493 e 494).** Optante do Simples, mão de obra (17.05.01): sem IRRF/CSRF (dispensa com declaração), INSS 11% retido (1.017,39 e 278,06) e ISS 5% (462,45 e 126,39). Portal = Domínio = Declaração Mensal (ISS total 609,54). Sem a declaração do Simples arquivada, IRRF 1% (R$ 117,77) e CSRF 4,65% (R$ 547,63) seriam devidos. ✅ Reinf: R-2010 (tipos 100000025 e 100000001).

**Exemplo 4: abaixo do limite (Telefônica, R$ 13,43, software).** 13,43 x 4,65% = 0,62 ≤ R$ 10. Retenção zero correta. ✅ Registrar a conta.

**Exemplo 5: fora da competência (Castro, nota 121).** Emitida em 11/09, competência 08/2026: não entra em setembro; conferir se foi lançada em agosto. ⚠️

**Exemplo 6: nota duvidosa (Primegrid, nota 994).** "Abastecimento de gerador" lançado como 07.02.01; ISS 3% retido corretamente; Portal diz PIS/COFINS não retidos. Fora da lista do art. 30 da Lei 10.833: sem CSRF; se fosse enquadrado como manutenção, CRF de R$ 32,09. ⚠️ decisão do contador.

## 10. Pós-transmissão: registro nas planilhas

Depois que o Reinf for transmitido, o registro vai para **duas planilhas diferentes**. Nunca escrever direto nelas: entregar TSV inline para a Fernanda colar na aba de fila e rodar o script de processamento.

### 10.1 Ordem de trabalho (aprendida no 238, 09/2026)
1. **Conciliar antes de transmitir** (seções 1 a 7): Domínio x Portal Nacional (Recebidas) x município (Declaração Mensal **e** relação de serviços tomados da pasta `002 ARQUIVOS MUNICIPAIS`). Abrir **todas** as fontes das pastas 002 e 003 antes de marcar qualquer coluna como indisponível. O município só informa ISS: para IRRF, CRF e INSS escrever "não se aplica, a prefeitura só informa ISS" (não "n/a").
2. **Decidir as dúvidas** (alíquota, dispensa, enquadramento, data do fato gerador do R-4020). Registrar a decisão da Fernanda no log. Exemplo de decisão: a alíquota exibida no Domínio pode ser só demonstração; o valor a recolher é o que vale.
3. A Fernanda transmite e salva **dois PDFs**: (a) o **relatório de conferência** ("EFD-Reinf - Envio de Arquivos") na pasta de conferências e (b) o **relatório de consulta do envio** (com nº do recibo, situação e data/hora) na pasta REINF, nome `NNN - NOME DA EMPRESA.pdf`.
4. Conferir (a) contra o Domínio: R-2010 (valor contábil, base, retenção, **tipo de serviço**) e R-4020 (natureza, data, base, IRRF, agregado por beneficiário), com os totais por evento.
5. Ler (b): confirmar **Sucesso** em cada evento (R-2010, R-4020, R-2099, R-4099 quando houver retenção), nº do recibo e data/hora. Sem o relatório (b), não afirmar que foi enviado e manter `Pendente`.
6. Montar os dois TSV abaixo, conferir a lista de pendências e registrar a rodada na memória.

Observações práticas:
- O fato gerador do R-4020 é o pagamento. A Fernanda pode orientar a usar a **data da nota** (competência) quando o pagamento ocorre no mesmo mês; registrar essa orientação no log e avisar que, se a data real de pagamento for diferente, o evento precisa ser retificado.
- Cadastro duplicado: o relatório pode mostrar a empresa como `1238` em alguns eventos e `238` em outros (e `1205`/`205`). É o mesmo CNPJ; registrar e pedir para conferir duplicidade de cadastro no Domínio.
- Um R-4020 por beneficiário pode gerar vários recibos. Listar todos.

### 10.2 Planilha Controle_Fiscal (aba `Atualizações`, 7 colunas)
`Nº | aba | Obrigação (prefixo) | Status | Valor | Observações | Processado (em branco)`

- Linha **REINF**: `Enviado`, com os recibos e a data/hora de cada evento, mais "sem movimento: sem retenção como tomador e sem INSS retido sofrido" quando só houver R-2099.
- Linha **SERVIÇOS TOMADOS**: `Importado` só depois de importado no Domínio e conciliado; senão `Pendente`.
- Exemplos:
```
205	Set2026	REINF	Enviado		R-2099 Fechamento dos Eventos Periódicos, Sucesso, recibo <nº>, enviado <data hora> (Oficial). Sem movimento: sem retenção como tomador e sem INSS retido sofrido.	
238	Set2026	REINF	Enviado		R-2010 Sucesso recibo <nº>; R-4020 Sucesso recibos <nº> e <nº>; R-2099 Sucesso <nº>; R-4099 Sucesso <nº>; enviados <data hora> (Oficial).	
```
- Antes de entregar, conferir no `Set2026` quais linhas de REINF estão em branco ou `Pendente` e quais clientes não têm linha de REINF (ex.: Tacom 138, 248 e 263 não têm; perguntar se a obrigação se aplica).

### 10.3 Planilha do DP: `CONTROLE | DP REINF'S`
Local: Drive, planilha `CONTROLE | DP REINF'S` (id `14idmBAj9YO4V_R8_pRbVc4iyDQIhGo9OZwDVOPsPmmM`).
- Abas por mês: `MOD GERAL MM.AAAA` (ex.: `MOD GERAL 09.2026`). Colunas: `Nº | Empresa | Obrigação | Status | Observações (Sem movimento ou COM RETENÇÃO) | Observações (detalhe)`. A caixa lateral (colunas H e seguintes) é do 152 (CRBM5), com os códigos de retenção de órgãos públicos.
- Fila: aba **`Atualizações REINF`**, colunas `Nº | aba | Status | Observação | Detalhe | Rótulo caixa | Valor caixa | Processado`. O script grava Status, Observação e Detalhe e marca `Processado`.
- **Passo a passo:**
  1. Ler a aba `MOD GERAL` do mês e listar os clientes com **Status em branco**.
  2. Cruzar com os relatórios de envio na pasta REINF. Só entram na fila os já **enviados**.
  3. Os que dependem de procuração, baixa ou não enviados ficam de fora (apenas mencionar).
  4. Montar o TSV: `Observação` = `Sem movimento` ou `COM RETENÇÃO`. No `Detalhe`, quebra de linha como `\n` literal (padrão da linha já processada do 189).
  5. Rótulo caixa e Valor caixa em branco, exceto para o 152.
- **Formato do Detalhe:**
  - Sem retenção: `Enviado dd/mm/aaaa hh:mm (Oficial). Sem retenção no mês.`
  - Com retenção, uma linha por tributo com o **código de receita usado pelo DP**: `IRRF (Cód. Rec. 170806): R$ x,xx\nCRF (Cód. Rec. 595207): R$ x,xx\nINSS Retido (Cód. Rec. 1162): R$ x,xx\nEnviado dd/mm/aaaa hh:mm (Oficial): R-2010 + R-4020 + R-2099 + R-4099.` (quando só houver CRF, `CRF (Cód. Rec. 5952): R$ x,xx` como na linha do 126).
- **Exemplos (09/2026):**
```
205	MOD GERAL 09.2026	Enviado	Sem movimento	Enviado 12/10/2026 11:49 (Oficial). Sem retenção no mês.			
238	MOD GERAL 09.2026	Enviado	COM RETENÇÃO	IRRF (Cód. Rec. 170806): R$ 17,75\nCRF (Cód. Rec. 595207): R$ 141,86\nINSS Retido (Cód. Rec. 1162): R$ 1.295,45\nEnviado 12/10/2026 13:49 (Oficial): R-2010 + R-4020 + R-2099 + R-4099.			
```
- Os códigos de 6 dígitos (170806 e 595207) são os que o Domínio e o DP usam; o `07` de 5952/07 é a variação da CSRF na DCTFWeb (MIT) desde 01/2025 (fonte: LeFisc). O sufixo `06` do 170806 é interpretado como variação equivalente, sem confirmação. 🟡

### 10.4 Fechamento da rodada
- Registrar na memória: `memoria/PENDENCIAS.md`, o log do processo e o snapshot datado no Drive.
- Listar o que falta recolher: DARF 5952 (CSRF, vence no último dia útil do 2º decêndio do mês seguinte), DARF do IRRF, INSS via DCTFWeb depois do R-2099 (🟡 confirmar vencimentos), recibo no G-Click e declaração do Simples dos prestadores dispensados.

## 11. Limites desta skill

- Não calcula tributo sobre a receita do prestador, nem substitui a leitura da legislação vigente.
- A tabela de naturezas (2.2) é correlação de consultoria; a Tabela 06 vem de minuta de 2019. Atualizar quando a Fernanda trouxer o Manual/Anexo I vigente da EFD-Reinf.
- Quando a regra mudou recentemente (reforma tributária IBS/CBS, alterações de leiaute da EFD-Reinf, prazos de recolhimento), avisar o usuário para confirmar a versão vigente.
- Não transmite eventos; prepara o roteiro e confere o resultado.
