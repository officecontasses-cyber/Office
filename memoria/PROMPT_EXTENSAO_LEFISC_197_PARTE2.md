# Prompt para a extensão Claude no Chrome — ASBBM (197), Parte 2: o que ficou "não confirmado"

Cole o bloco abaixo na extensão (Chrome já logado no Lefisc). Somente leitura.

---
**Contexto.** Sou contadora e estou analisando o enquadramento tributário da ASBBM (associação privada sem fins lucrativos, CNAE 9412-0/99, natureza jurídica 3999, Novo Hamburgo/RS): isenta (Lei 9.532/1997 art. 15), imune (art. 12) ou Lucro Presumido, e como corrigir as ECFs 2019-2024. Você já levantou, no Lefisc, o texto de Lei 9.532 arts. 12-16, MP 2.158-35 arts. 13-14, CTN arts. 9º/14, CF art. 150/195, LC 187/2021, IN RFB 1.700/2017, RIR/2018, IN RFB 2.004/2021, IN RFB 2.121/2022 e a SC 84/2025. Agora preciso fechar o que ficou "não encontrado / a confirmar".

**Regras (valem para tudo):**
1. Somente leitura. Não envie e-mails, não preencha formulários, não faça login em nada além do Lefisc que já está aberto, não altere nada em nenhum site.
2. **Autorizo abrir e ler (na tela) PDFs e páginas** de `normas.receita.fazenda.gov.br`, `gov.br/receitafederal`, `planalto.gov.br` e `stf.jus.br`. Não precisa salvar/baixar arquivo no computador; copie o texto.
3. Fontes aceitas, nesta ordem: Lefisc; site oficial da Receita (normas.receita.fazenda.gov.br, Perguntas e Respostas, Manual da ECF no gov.br); Planalto; STF. Blogs, consultorias e IA não valem como fonte da norma.
4. Copie o **texto literal** entre aspas e diga o **caminho/URL exato** e a **data de vigência/atualização exibida**. Separe sempre: TEXTO DA NORMA / COMENTÁRIO DA FONTE / SEU COMENTÁRIO. Não resuma no lugar do texto. Não invente número de norma, artigo, ementa ou data: se não achar, escreva "NÃO ENCONTRADO" e liste o que tentou.
5. No final, entregue um único arquivo Markdown `Base_legal_ASBBM_parte2.md` com uma lista "NÃO ENCONTRADO / A CONFIRMAR" atualizada.

**Itens a pesquisar:**

**A. Soluções de Consulta (texto/ementa literal, órgão emissor e data):**
 1. SC Cosit nº 243/2019 (COFINS sobre receitas de entidade isenta; atividades próprias vs. financeiras).
 2. SC Cosit nº 19/2022 (associação civil; venda de medicamentos aos associados; isenção COFINS).
 3. SC Cosit nº 218/2021 (aluguel recebido por entidade isenta; IRPJ e retenção).
 4. SC Cosit nº 50/2019 — se existir; tente também no site da Receita (busca por número/ano em normas.receita.fazenda.gov.br, "Solução de Consulta Cosit 50 2019"). Se não existir, diga.
 Na matéria Lefisc "Entidades sem fins lucrativos – Aspectos tributários" (junho/2023) esses PDFs estão linkados para `normas.receita.fazenda.gov.br` (idArquivoBinario 65167, 53708 e 64062; a ordem do número com a SC é incerta: confira o cabeçalho de cada PDF).
 5. Qualquer SC/Parecer Normativo que trate de **associação profissional/científica/cultural: imune (art. 12) ou isenta (art. 15)**.
 6. Qualquer SC sobre **IRRF em aplicação financeira** de entidade isenta e de entidade imune.
 7. SC 84/2025: confirme se o órgão emissor é a Cosit (cabeçalho do PDF no site da Receita).

**B. Itens do facilitador "Terceiro Setor" do Lefisc que abriram em branco:** "Pis sobre Folha de Salários. Cofins sobre Atividade Não Própria." e "Cofins regime cumulativo. Receitas Financeiras." Tente de novo (recarregar, outra aba) e copie o texto. Se continuar em branco, diga.

**C. COFINS sobre receita financeira de entidade isenta (4%):** localize o dispositivo que fixa a alíquota (hipótese minha, **não confirmada**: Decreto 8.426/2015, que fixaria 4% de COFINS e 0,65% de PIS sobre receitas financeiras no regime não cumulativo). Copie o artigo. Diga se vale para entidade isenta do art. 15 e em que condições (regime cumulativo × não cumulativo para receitas não próprias).

**D. IRRF de aplicações de entidade imune:**
 1. Texto **vigente** da IN RFB 1.585/2015 art. 72 (dispensa por declaração, Anexo III). Verifique se a IN 1.585/2015 ainda está vigente ou foi revogada/substituída (e por qual norma).
 2. ADI 1802 (STF): ementa, data do julgamento, resultado e efeito sobre o art. 12 §1º da Lei 9.532 (rendimentos de aplicação financeira de imunes). Fonte: stf.jus.br.

**E. ECF — forma de tributação:** no **Manual de Orientação do Leiaute da ECF** vigente (gov.br/receitafederal / SPED), registro 0010, campo `FORMA_TRIB`: copie a tabela de códigos e diga qual código é **imune** e qual é **isenta** (minha lembrança de "8 = imune, 9 = isenta" **não está confirmada**). Idem: regra de preenchimento do bloco U180 para imunes/isentas e do X390.

**F. Lucro Presumido para entidade isenta/imune e retificação:**
 1. Procure dispositivo, Pergunta e Resposta da ECF ou Solução de Consulta que diga se uma entidade isenta (art. 15) **pode ou deve** apurar IRPJ/CSLL pelo Lucro Presumido (ou se só tributa receitas não relacionadas às finalidades e rendimentos de aplicação).
 2. Perguntas e Respostas da Receita sobre **retificação de ECF**: caso de entidade que entregou como Lucro Presumido e quer retificar para imune/isenta (IN RFB 2.004/2021 art. 7º §2º veda mudar o regime de tributação). Há orientação oficial sobre a exceção ou sobre a forma de corrigir? Copie.
 3. Prazo decadencial e consequência de ECF entregue com forma de tributação errada (multa do art. 12 da Lei 8.218/1991, se aplicável): só normas/Perguntas e Respostas, sem opinião.

**G. Obrigações acessórias para imunes/isentas** (apenas o que a norma diz sobre obrigatoriedade ou dispensa, com artigo): **DCTF** (IN RFB 2.005/2021 — confira o número e o artigo), **EFD-Contribuições** (matéria Lefisc "EFD CONTRIBUIÇÕES – ENTIDADES IMUNES E ISENTAS"), **EFD-Reinf** (IN RFB 2.043/2021 — confira), **DIRF** (confirme se ainda existe para 2026 ou foi substituída; norma e data). Não assuma número de IN: confirme cada um.

**H. Pendências de redação:**
 1. Lei 9.532/1997 arts. 12-16: texto no **Planalto** (planalto.gov.br) com todas as notas de alteração; diga se a Lei 13.204/2015 alterou algum desses artigos e qual. Existe art. 15 §5º? (o RIR/2018 art. 184 §5º o cita).
 2. Origem da referência "extensão da isenção à CSLL": o art. 10 da Lei 10.637/2002 trata do prazo do PIS (já visto). Procure o dispositivo que fundamenta a isenção de CSLL das associações (candidatos a verificar, sem confirmação: Lei 9.532 art. 15 §1º; outras leis de 2002-2003 sobre CSLL). Diga qual é o correto.
 3. MP 2.158-35/2001 art. 13: redação final e o **art. 13-A** (IN RFB 2.121/2022 art. 302 o cita como incluído pela Lei 13.353/2016) — copie o texto.
 4. Código de DARF do **PIS sobre a folha** das entidades do art. 13 da MP 2.158-35 (a matéria Lefisc cita 8109; minha lembrança é que 8109 é PIS faturamento e que o da folha é outro — **não confirmado**). Fonte: tabela de códigos da Receita / IN 2.121 / Lefisc.
 5. Vigência da LC 214/2025 no art. 9º IV do CTN (1º/01/2026), conforme anotação.

**Formato da resposta:** para cada item (A1, A2, ..., H5): "Fonte e caminho", "TEXTO DA NORMA" (literal), "COMENTÁRIO DA FONTE", "SEU COMENTÁRIO", "Situação: CONFIRMADO / PARCIAL / NÃO ENCONTRADO". Termine com a lista "NÃO ENCONTRADO / A CONFIRMAR" e o aviso de que não é parecer jurídico.
---
