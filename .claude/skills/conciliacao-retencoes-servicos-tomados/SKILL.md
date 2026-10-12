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
- 15044 traz **IR 1708 e agregado 5952**: logo, o IRRF da manutenção/conservação é uma questão real a verificar (no 238 só houve CRF na nota Atlas).
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

Aplicação ao 238 (Prime System): nota 493 (recepcionista, item 17.05.01) → 100000025; nota 494 (limpeza e conservação) → 100000001. Selecionar pelo **serviço efetivamente prestado**, não pelo item da LC 116.

Tabela de trabalho (preencher a cada conciliação):

| Serviço (item LC 116) | Natureza no Domínio | Natureza correta | Descrição literal | Selo |
|---|---|---|---|---|
| (preencher) | (preencher) | (preencher) | (preencher) | ⬜ |

Como diferenciar naturezas parecidas: o texto do serviço prevalece sobre o título da nota; se o mesmo prestador faz serviços mistos (ex.: vigilância + monitoramento), classificar **por nota**, não por fornecedor; se não houver descrição na tabela, ⚠️ e consultar o contador responsável.

## 3. Códigos de retenção

| Tributo | Alíquota | Base | Recolhimento | Selo |
|---|---|---|---|---|
| **IRRF** serviços profissionais e outros serviços de PJ | 1,5% | valor do serviço | DARF; código de receita conforme a natureza (Tabela 01) | 🟡 código |
| **IRRF** limpeza, conservação, segurança, vigilância, locação de mão de obra | 1% (as skills internas divergem sobre o código DARF; o Domínio mostrou alíquota 1,50 com valor equivalente a 1%) | valor do serviço | DARF | 🟡 alíquota/código, verificar |
| **CSRF** (CSLL 1% + COFINS 3% + PIS 0,65%) | 4,65% total | valor do serviço | DARF **5952** único (soma dos três) | 🟢 alíquota e 5952 |
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

Atenção: no Domínio os códigos aparecem com 6 dígitos (ex.: 170806, 595207). Interpretar como código de receita (1708, 5952) seguido de sufixo de 2 dígitos que **não identifiquei**; confirmar com o suporte do Domínio ou com o leiaute. 🔴

Prazos (🟡, divergem entre fontes internas, **conferir na legislação vigente**):
- IRRF: o prazo depende do código de receita; não afirmar de memória. Consultar a regra vigente do código usado.
- CSRF 5952: as skills internas citam "último dia útil da quinzena seguinte"; a regra atual pode ser "último dia útil do segundo decêndio do mês seguinte". Verificar.
- INSS retido: prazo da DCTFWeb/guia do mês seguinte. Verificar o dia.
- ISS retido: lei municipal (Porto Alegre: ver guia gerada no DecWeb; usar a data impressa na guia, nunca regra deduzida).

**Regra do somatório da CSRF** (🟡): a dispensa vale quando o valor a reter (soma dos três tributos) é ≤ R$ 10,00, o que equivale a pagamento ≤ R$ 215,05 (10 ÷ 0,0465). O teste se faz **somando os pagamentos do mês ao mesmo prestador**: quando a soma ultrapassa R$ 215,05, retém-se sobre o total do mês, descontando o que já foi retido. Confirmar a base mensal no texto vigente.

**Valor abaixo do limite de dispensa:** retenção zero é o resultado **correto**, não divergência. Registrar a conta (valor x 4,65% = X ≤ R$ 10) no relatório.

## 4. Dispensas e isenções

Sempre exigir comprovação por escrito arquivada com a nota:

| Hipótese | Efeito | Condição a comprovar | Selo |
|---|---|---|---|
| Prestador optante do Simples Nacional | Dispensa IRRF e CSRF | Declaração do prestador anexa à nota (modelo da IN RFB 1.234/2012, art. a confirmar); o Portal mostra a opção, mas não substitui a declaração | 🟡 |
| Simples com cessão de mão de obra/empreitada (serviços do art. 18, §5º-C da LC 123, Anexo IV) | **Não dispensa o INSS 11%** | Enquadramento do serviço | 🟡 |
| MEI | Sem IRRF/CSRF; INSS 11% só nas atividades de cessão/empreitada permitidas ao MEI (hidráulica, elétrica, pintura, alvenaria, carpintaria, manutenção/reparo de veículos) | CCMEI e atividade | 🟡 |
| Valor mínimo | CSRF ≤ R$ 10 retido (pagamento mensal ≤ R$ 215,05); IRRF de valor ≤ R$ 10 | Cálculo | 🟡 |
| Entidades imunes/isentas | Dispensa de IRRF/CSRF conforme a norma | Declaração/comprovação de imunidade ou isenção | 🟡 |
| Órgãos públicos | Regra própria (Lei 9.430/96 art. 64 e IN RFB 1.234/2012). A Tabela de Retenção do Anexo I tem IR + CSLL + COFINS + PIS por natureza: p.ex. 4,80% de IR (total 9,45%, código 6190) para vigilância, limpeza, locação de mão de obra e demais serviços; **não vale para tomador privado** | Ver skill `conferencia-retencoes-pagamentos-orgao-publico` | 🟡 |
| Serviço fora da lista das retenções de CSRF | Sem CSRF | Item da lista da Lei 10.833, art. 30 (a nota deve ser enquadrada, não presumida) | 🟡 |
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
4. **ISS: Domínio x município:** a soma do ISS retido no Domínio deve ser igual ao "imposto retido de contribuinte substituído" da Declaração Mensal (ou do relatório municipal) e da guia.
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
| Dispensa indevida | Dispensa aplicada sem comprovação (declaração do Simples ausente, acumulado que passou do limite) | Obter a declaração ou reter; recolher e retificar |
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
- [ ] Acumulado do mês do prestador (teste dos R$ 215,05) e valor líquido a pagar
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

**Exemplo 1: tudo bate (REAT 238, Atlas, nota 19764).** Serviço 14.01 de R$ 1.275,60, prestador não optante. CSRF: 1.275,60 x 4,65% = 59,32. Portal 59,32, Domínio 59,32, retenção em 5952. ✅ Falta confirmar natureza e data de pagamento.

**Exemplo 2: alíquota divergente (STV, nota 20038).** Vigilância de R$ 1.774,97. Portal: IRRF 17,75 (= 1%). Domínio: alíquota exibida 1,50, valor 17,75. ⚠️ Corrigir a alíquota do cadastro (ou o valor, se a regra vigente for 1,5% = 26,62, diferença de R$ 8,87).

**Exemplo 3: Simples com INSS (Prime System, notas 493 e 494).** Optante do Simples, mão de obra (17.05.01): sem IRRF/CSRF (dispensa com declaração), INSS 11% retido (1.017,39 e 278,06) e ISS 5% (462,45 e 126,39). Portal = Domínio = Declaração Mensal (ISS total 609,54). ✅ Reinf: R-2010.

**Exemplo 4: abaixo do limite (Telefônica, R$ 13,43, software).** 13,43 x 4,65% = 0,62 ≤ R$ 10. Retenção zero correta. ✅ Registrar a conta.

**Exemplo 5: fora da competência (Castro, nota 121).** Emitida em 11/09, competência 08/2026: não entra em setembro; conferir se foi lançada em agosto. ⚠️

**Exemplo 6: nota duvidosa (Primegrid, nota 994).** "Abastecimento de gerador" lançado como 07.02.01; ISS 3% retido corretamente; Portal diz PIS/COFINS não retidos. ⚠️ Verificar o enquadramento (se fosse manutenção/conservação, CRF de R$ 32,09).

## 10. Limites desta skill

- Não calcula tributo sobre a receita do prestador, nem substitui a leitura da legislação vigente.
- A tabela de naturezas (2.2) é correlação de consultoria; a Tabela 06 vem de minuta de 2019. Atualizar quando a Fernanda trouxer o Manual/Anexo I vigente da EFD-Reinf.
- Quando a regra mudou recentemente (reforma tributária IBS/CBS, alterações de leiaute da EFD-Reinf, prazos de recolhimento), avisar o usuário para confirmar a versão vigente.
- Não transmite eventos; prepara o roteiro e confere o resultado.
