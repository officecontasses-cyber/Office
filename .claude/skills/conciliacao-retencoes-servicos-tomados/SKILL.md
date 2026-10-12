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

Esta skill foi escrita sem acesso à Tabela 01 oficial da Receita (o download falhou no ambiente em que foi redigida). Por isso cada regra traz um selo:

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

🔴 **Atenção:** esta skill **não lista a tabela de códigos de memória**. A natureza de rendimento (Tabela 01) é campo obrigatório do R-4010/R-4020, muda por leiaute e um código errado gera retenção/recolhimento em código errado. Procedimento:

1. Baixar a Tabela 01 vigente (Anexo I do Manual da EFD-Reinf, portal SPED) e salvar na pasta de conferências do mês.
2. Para cada serviço, partir do **código de tributação nacional/item da LC 116** da nota e escolher o código da Tabela 01 **mais aproximado do serviço**, lendo a descrição literal.
3. Conferir se o código de receita da tabela (DARF) é o mesmo usado pelo Domínio (coluna "Cód. Rec.").
4. Registrar no relatório: código, descrição literal da tabela e base de escolha.

Observações úteis:
- Os códigos de natureza se dividem em grupos (por tipo de beneficiário e de rendimento). Fóruns técnicos indicam que o R-4020 usa naturezas de grupos específicos, e que o prestador informa a retenção sofrida no R-4080 e o tomador no R-4020. 🟡 Não confirmado no leiaute oficial.
- Mesmo pagamento **sem retenção** (dispensa) pode precisar ser informado no R-4020 com retenção zero, quando a natureza é sujeita à retenção. 🟡 Verificar no Manual vigente.
- Tabela 06 (tipo de serviço) é outra tabela, usada no **R-2010** para o INSS. Também não está reproduzida aqui. 🔴

Tabela de trabalho (preencher a cada conciliação, **não reutilizar sem conferir**):

| Serviço (item LC 116) | Natureza no Domínio | Natureza correta na Tabela 01 vigente | Descrição literal | Selo |
|---|---|---|---|---|
| (preencher) | (preencher) | (preencher) | (preencher) | ⬜ |

Evidência observada (não validada): na REAT HOLDING (238), 09/2026, o Domínio atribuiu **15044** à manutenção de elevadores (item 14.01) e **15045** à vigilância (item 11.02). A coerência com a Tabela 01 ainda precisa ser conferida. 🔴

Como diferenciar naturezas parecidas: usar o item da LC 116 e a descrição da nota (o texto do "serviço" prevalece sobre o título da nota); se o mesmo prestador faz serviços mistos (ex.: vigilância + monitoramento), classificar por nota, não por fornecedor; se o serviço não encontra descrição na tabela, registrar ⚠️ e consultar o contador responsável.

## 3. Códigos de retenção

| Tributo | Alíquota | Base | Recolhimento | Selo |
|---|---|---|---|---|
| **IRRF** serviços profissionais e outros serviços de PJ | 1,5% | valor do serviço | DARF; código de receita conforme a natureza (Tabela 01) | 🟡 código |
| **IRRF** limpeza, conservação, segurança, vigilância, locação de mão de obra | 1% (as skills internas divergem sobre o código DARF; o Domínio mostrou alíquota 1,50 com valor equivalente a 1%) | valor do serviço | DARF | 🟡 alíquota/código, verificar |
| **CSRF** (CSLL 1% + COFINS 3% + PIS 0,65%) | 4,65% total | valor do serviço | DARF **5952** único (soma dos três) | 🟢 alíquota e 5952 |
| **INSS** cessão de mão de obra/empreitada | 11% | valor bruto (a base pode ser reduzida por materiais/equipamentos quando destacados e permitidos) | Reinf R-2010, débito na DCTFWeb | 🟢 11%, 🟡 base e forma de pagamento |
| **ISS** retido | alíquota do município (mínimo geral 2%, LC 157) | valor do serviço (ou base do item) | guia/DAM do município | 🟢 conceito, 🟡 por município |

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
| Órgãos públicos | Regra própria (Lei 9.430/96 art. 64 e IN RFB 1.234/2012) | Ver skill `conferencia-retencoes-pagamentos-orgao-publico` | 🟡 |
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
- Quando a regra mudou recentemente (reforma tributária IBS/CBS, alterações de leiaute da EFD-Reinf, prazos de recolhimento), avisar o usuário para confirmar a versão vigente.
- Não transmite eventos; prepara o roteiro e confere o resultado.
