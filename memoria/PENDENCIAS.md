# Pendências e resolvidos — OfficeCont (Fechamento Fiscal)

Documento vivo. **Atualizar a cada etapa** e salvar um snapshot datado na pasta `ARQUIVOS EXTENSÃO - CODE - CLAUDE` do Drive,
para não perdermos contexto. Última atualização: **03/10/2026** (sessão 2: cliente 265 cadastrado e com 09/2026 fechado; falta o restante do fechamento de 09/2026).

Convenção: `[ ]` pendente · `[x]` resolvido · `(?)` precisa de confirmação da Fernanda.

---

Mapa do processo e linha do tempo de 09/2026: ver `memoria/PROCESSO_FECHAMENTO_09-2026.md`.

## PENDENTE

### Com data marcada
- [ ] **E-mail ao Gian: certificado A1 do 258 Nadal vence em 14/10/2026** (e avisar os próximos: 155 em 27/10, 71 em 13/11, 117 em 11/12, 126 em 16/12). Conferir nos Itens Enviados do OWA se já foi enviado; rascunho entregue à Fernanda em 03/10. Rodar o Portal Nacional do 258 antes de 14/10.
- [ ] **Tacom: ligar para a Leidislaine na segunda 05/10 cedo.** O e-mail enviado não teve retorno até 03/10 (sábado); confirmar o acesso à máquina dela antes das 11:00.
- [ ] **Tacom — SPED Fiscal (10/2026):** enviar os arquivos à Leidislaine Ribeiro **até quarta 07/10** (ela transmite até quinta 08/10; entra de férias).
  Acesso à máquina dela na **segunda 05/10, antes das 11:00** (a Fernanda não consegue nesse horário; conferir se ela confirmou). (?) vale para 138, 263 ou ambas?
- [ ] **ISSQN Porto Alegre 09/2026 vence 13/10.** Rodar o DecWeb nos clientes restantes antes disso (ver abaixo).
- [ ] **REAT HOLDING (238) — 2ª quinzena de outubro (16 a 31/10):** enviar à cliente o **relatório de débitos ref. 06/2026** (Relatório Fiscal de 21/08, Júlia Rocha)
  **+ IRPJ e CSLL vencidos de meses anteriores.** (?) quais meses estão vencidos. Fila sugerida (Pendente) para DARF IRPJ e DARF CSLL do 238 na Set2026: não confirmado que foi colada.
- [ ] **Certificados que vencem:** 258 Nadal (14/10/2026), 155 Mainieri (27/10), 71 Conte (13/11), 117 Tabajara (11/12), 126 Tatsch Leite (16/12). Providenciar renovação.
- [ ] **SPED Contribuições 09/2026:** prazo 16/11 (na planilha). Pendência de agosto: SPED Contribuições 15/10.

### Fila da Controle_Fiscal (aba Atualizações) — a confirmar que foi colada e processada
- [x] Tacom 09/2026: 263 declaração e guia (R$ 4.089,69, G-Click 02/10 14:03) já `Enviado` na planilha (conferido em 03/10). 138 declaração `Enviado`; **138 guia: Fernanda confirmou "sem movimento" em 03/10** → TSV `Sem movimento` entregue; colar e processar.
- [ ] Corrigir observações das guias do 16 e do 18 (dizem "Venc. 09/10"; o correto é **13/10/2026**).
- [ ] Guias do 16 (R$ 422,87) e do 18 (R$ 42,00): continuam `Pendente` até o envio comprovado no G-Click; depois `Enviado`.

### Guias ISSQN POA 09/2026 — decisões de 03/10 (após conciliação Portal x DecWeb)
- [ ] **155 (R$ 842,02): NÃO postar ainda** — aguardar confirmação da Camila (Fernanda, 03/10). Conciliação sem divergência.
- [ ] **257 (R$ 6.500,00): conferir com o cliente e analisar na SEGUNDA 05/10.** ISS 7.262,54, retido só 762,54; a Fernanda estranhou porque o cliente geralmente retém tudo. Verificar se os tomadores deveriam ter retido (notas de prestados do 257) antes de postar a guia.
- [ ] **205 (R$ 1.915,06): segurar.** Conciliação: DecWeb tem 1 nota de R$ 6.000,00 (ISS 120,00) que o Portal não tem; 3 canceladas no Portal x 2 no DecWeb. Identificar a nota (`findstr /I "Becker" notas_09_2026.csv`); se cancelada, retificar declaração e refazer guia.
- [ ] 152 (R$ 461,69): divergência só de 1 nota de R$ 42,00 no Portal (ISS e retido iguais); retido total 568,44 = 461,69 POA + 106,75 Estrela. Fernanda decide postar; localizar a nota depois.
- [ ] Liberadas pela conciliação (postar no G-Click quando a Fernanda decidir): 16 (422,87), 189 (634,31), 238 (609,54), 241 (2.403,15). 18 (42,00) e 177 (530,40) só conferidas por conta (2%), sem Portal. 173 (422,87, ISS fixo).
- [ ] **186 Lopes & Nadal:** cliente enviou os documentos em 03/10 → rodar Portal Nacional e DecWeb (prioridade logo após a Tacom); ISSQN sai junto com os demais impostos no G-Click. Em agosto a guia foi R$ 422,87 (fixo por profissional).
- [x] Portal Nacional rodado em 04/10 (`resultados.csv` recebido): 117, 247 (Montenegro/RS) e 258 deram `sem_movimento` em Emitidas e Recebidas nas duas rodadas (03/10 e 04/10); coerente com os recibos (258 receita 0,00; 117 mesmo padrão de jul/ago). Aceito, sem sinal de sessão vazada.
- [ ] 258 Set2026: guia ISSQN ainda em branco → propor `Sem movimento` (Fernanda confirma). 247 Set2026: declaração/guias em branco; Montenegro usa DMS/Livro Fiscal (não DecWeb); Portal sem notas → (?) lançar sem movimento após confirmação.
- [ ] **186 Lopes & Nadal — Portal 04/10:** Emitidas 5 notas (151 e 152 são de 08/2026, já declaradas em agosto; **09/2026 = 153 Tortelli R$ 2.500,00 + 154 Anderlise R$ 4.475,05 + 155 Ruy R$ 4.500,00 = R$ 11.475,05**, numeração 151–155 contínua, nenhuma cancelada). Recebidas: 2 notas Google (SP, ISS não retido; 288,28 de 08/2026 e 22,50 de 09/2026). Previsão da guia: ISS fixo R$ 422,87 (2 profissionais, igual a agosto). Falta rodar o DecWeb do 186 e conferir.

- [x] **186 DecWeb enviado em 04/10 às 11:26** (receita R$ 11.475,05, guia R$ 422,87, igual ao Portal e à previsão). Fernanda colou o TSV do 186.
- [ ] **G-Click 04/10 11:34:** Fernanda subiu 9 guias em lote (16, 18, 152, 173, 177, 186, 189, 238, 241 = R$ 5.949,70; o "R$ 8.388,07" dito antes estava errado). O log colado mostra só a atividade "Guia ISS" (upload); **falta ver "Envio ao cliente" com horário** para lançar `Enviado`. Fernanda disse "enviei agora"; TSV `Enviado` entregue condicionado à conferência do passo "Envio ao cliente".
- [ ] **186 — federais (atualizado 04/10 à tarde):** Domínio, Consulta Apuração 09/2026: ISS 422,87 (corrigido pela Fernanda; o Domínio mostra vencimento 09/10, mas a guia vale 13/10), PIS 74,59, COFINS 344,25 (batem com a previsão). IBS e CBS saldo 0,00 na consulta (informativos). **IRPJ (1.315,74) e CSLL (789,45) do 3º trimestre ficam PENDENTES** até o contábil liberar rendimentos financeiros e IRRF sobre aplicações (entram 100% na base de IRPJ/CSLL no Presumido, e o IRRF é dedutível); vencimento 30/10. Falta gerar o DARF de PIS/COFINS (vence 23/10) e preencher no FAT as linhas RENDIM. FINANCEIROS e IRRF S/RESGATES depois do retorno do contábil.
  - **Passo 1 (05/10): alimentar o FAT** `186_LOPES&NADAL_FAT2026` (Drive do cliente, aba 2026): digitar **11.475,05** em RECEITA SERVIÇOS/SETEMBRO (célula L4, vazia). O FAT usa receita por competência da NFS-e (agosto = 8.267,05 = notas 151+152 emitidas em 03/09). Conferir depois: PIS 74,59; COFINS 344,25; IRPJ mês 550,80; CSLL mês 330,48; 3º tri receita 27.411,35, IRPJ 1.315,74, CSLL 789,45 (soma dos meses dá 789,44, diferença de R$ 0,01 de arredondamento); adicional de IRPJ zero (base 8.771,63 < 60.000). DARF PIS/COFINS vence 23/10; IRPJ/CSLL 30/10. ISSQN profissional 422,87 já está no FAT. Fórmulas do FAT não verificadas (não alterei a planilha).

- [ ] **Planilha `CONTROLE | Rendimentos.xlsx` (Drive; uma aba por trimestre, colunas Cód. · Cliente · LIBERADO FISCAL · Observações; lista suspensa Sim/Não/NT/Pendente em C2:C30):** a aba `3ºTRIM 2026` tem 22 clientes (2, 16, 18, 26, 71, 117, 126, 155, 173, 177, 185, 186, 189, 197, 205, 209, 237, 241, 247, 257, 258, 261). **Faltam 227 PROGEST, 264 ZENITH PARACURU e 265 BELEM BRASIL HOLDING** (todos Presumido, com DARF IRPJ no Set2026). (?) 133 RFL e 238 REAT (Lucro Real) constavam no 4ºTrim 2025 e saíram dos blocos de 2026: confirmar com a Fernanda. Sem linha de IRPJ no Set2026 e fora da lista: 138, 248, 263 (Tacom, apurada pela matriz) e 152 (CRBM5, conselho). E-mail ao contábil pedindo informes de rendimentos e IRRF entregue em rascunho (prazo sugerido: sexta 16/10).

### DecWeb (ISSQN Porto Alegre) — 09/2026
- [ ] Rodar os **15 clientes restantes** de Porto Alegre: 2, 26, 152, 155, 173, 177, 186 (só depois dos documentos), 189, 205, 209, 237, 238, 241, 257, 258.
  Já fechados em 09/2026: 16, 18, 117, 133 (01/10) e Tacom 138 e 263 (02/10).
- [ ] **Senhas faltando no `clientes.csv`:** 26 (Raldi: sem CNPJ e sem senha na planilha) e 152 (Conselho: célula com várias linhas).
- [ ] Definir quais clientes estão **sem movimento** em setembro (`aceitar_avisos=sim`); candidatos de agosto: 2, 26, 117, 138, 152, 173, 209, 237, 238.
- [ ] **Lopes & Nadal (186):** prioridade; só roda **depois que a cliente enviar os documentos**; ISSQN sai junto com o restante dos impostos.

### Portal Nacional (NFS-e Emitidas/Recebidas) — 09/2026
- [ ] **Bloco 1:** 71, 117, 126, 152, 155, 189, 197. **Bloco 2:** 205, 237, 241, 247, 257, 258, 261, 264. Já baixados: 16 e 238.
- [ ] Conferir as planilhas do 16 salvas no Drive (quantidade de notas e competência); só a do 238 foi conferida.
- [ ] **Sem certificado neste PC (ficam de fora):** 2, 18, 26, 133, 138, 173, 177, 185, 209, 248, 263. A Tacom (138, 248, 263) precisa de outro caminho (acesso à máquina da cliente).
- [ ] (?) 173 está "PENDENTE DE CADASTRO"; 71, 197 e 261 estão "Em Transição (Prefeitura)": o Padrão Nacional já vale para eles?
- [ ] Ligar `conferencia = sim` no DecWeb quando houver Emitidas, para comparar Prestados × Emitidas.

### Cliente novo 265 — BELEM BRASIL HOLDING
- [x] 265 incluído no `clientes.csv` do DecWeb em 03/10/2026 (script `decweb/adicionar_cliente265.bat`, Fernanda confirmou "deu"). **Falta o `clientes.csv` do Portal Nacional** (sem senha) e trocar a senha do DecWeb.
- [ ] ISSQN do 265 nos meses seguintes: só a arquitetura (71.11-1-00) deve gerar ISS; aluguel e compra e venda de imóveis próprios ficam fora do ISS (?) confirmar. **Voltar `aceitar_avisos` do 265 para em branco** (o `sim` valeu só para 09/2026, receita zero confirmada pela Fernanda em 03/10).
- [ ] Apagar a mensagem do grupo de WhatsApp que expõe a senha do certificado. (A senha do DecWeb também foi digitada na sessão de 02/10/2026: considerar trocá-la.)

### Antigas (de agosto) e estruturais
- [ ] R-4010 do 189; PER/DCOMP do 133; conferência do 238.
- [ ] As 7 linhas "Não se aplica" fixas e as observações (aguardando a Fernanda avaliar).
- [ ] Dias de prazo de ISSQN dos demais municípios (hoje só Porto Alegre 13/10 e São Leopoldo 15/10).
- [ ] Possível gerador de TSV a partir dos PDFs que o robô baixa.
- [x] **`decweb/conciliacao.py` criado em 03/10/2026:** concilia Prestados×Emitidas, Tomados×Recebidas, declaração e guia (PDF) pela chave de acesso. Validado com dados reais do 155, 16 e 238. Falta rodar no PC do escritório (copiar o arquivo para `C:\Robos\decweb` e `pip install pypdf`) e conferir a leitura dos PDFs com `--ler-pdf`.

### Bloqueios do ambiente
- [x] BrasilAPI deu 404 para o 265 em 02/10 (CNPJ de 30/09, recente demais); dados vieram do Cartão CNPJ enviado em print.
- [x] ~~Consulta de CNPJ bloqueada pela rede~~ → em 02/10 a Fernanda liberou `brasilapi.com.br` em *Acesso à rede > Personalizado* do ambiente "TESTE" (mantida a lista padrão de gerenciadores de pacotes). **Vale só para sessões novas.**
- [ ] Se a BrasilAPI falhar numa sessão nova, liberar também `publica.cnpj.ws` e `receitaws.com.br`.

---

## RESOLVIDO

### Planilha Controle_Fiscal
- [x] Aba **Set2026** criada a partir da Ago2026 (320 linhas), com prazos em texto e contagem regressiva (183 prazos, 0 erros).
- [x] Linhas **DARF IRPJ/CSLL trimestral** inseridas para os Presumido (exceto 138, 152, 248, 263).
- [x] Fila de 01/10/2026 (16, 18, 117, 133) colada e processada.
- [x] Prazo do ISSQN de Porto Alegre corrigido no script: **13/10/2026** (estava 09/10; o prazo é o impresso na guia).

### DecWeb
- [x] Robô adaptado aos clientes da OfficeCont, instalado em `C:\Robos\decweb` e testado.
- [x] Correção: o aviso "Não foi informado serviço prestado/tomado" não bloqueia cliente que tem notas no Prestados baixado (commit 0c1c238).
- [x] 09/2026 fechados no DecWeb: 16, 18, 117, 133 (01/10) e Tacom 138 e 263 (02/10). Guia do 16 conferida; guias 16/18/263 lidas nos PDFs.
- [x] Guia do 263 (R$ 4.089,69, venc. 13/10) **enviada pelo G-Click** (comprovado em 02/10: guia 14:00, cliente 14:03, WhatsApp 14:14).

### Portal Nacional
- [x] Robô adaptado (saída na 003 do mês, período pela competência, `clientes.csv` robusto), instalado em `C:\Robos\portalnacional`; extensão instalada no perfil do robô.
- [x] **Bug de sessão corrigido:** o perfil compartilhado do Chrome mantinha a sessão do cliente anterior (a rodada inteira baixou o 238). Agora a sessão é apagada antes de cada login.
- [x] `logs\resultados.csv` da rodada com erro renomeado para `resultados_rodada_com_erro.csv` (os "sem movimento" dela não valem).
- [x] Teste com o 16 e depois o 238: troca de empresa correta, "empresa logada confirmada pelo CNPJ".
- [x] Certificados verificados: 18 válidos, 11 sem certificado neste PC.

### Cliente 265 (02/10/2026)
- [x] Cartão CNPJ lido: ATIVA desde 30/09/2026; CNAE principal 71.11-1-00; secundários 64.62-0-00, 68.10-2-02, 68.10-2-01; Av. Juca Batista, 8000, casa 802, Belém Novo, Porto Alegre/RS, CEP 91.781-200.
- [x] Prefeitura confirmada: **Porto Alegre**. Inscrição municipal **049298-2-9** feita; acesso ao DecWeb feito.

### Planilha em 03/10/2026
- [x] Script do 265 rodado: cadastro na linha 31; 12 linhas na Set2026 (322 a 333); verificação sem problemas.
- [x] `definirPrazosSet2026()` rodado com a versão nova: ISSQN/Declaração de Porto Alegre em 13/10 (22 linhas de cada; 1 de São Leopoldo em 15/10); `verificarPrazosSet2026()` sem problemas. A 1ª rodada tinha usado a versão antiga da planilha (09/10 em 44 linhas), já corrigida.
- [ ] Município sem prazo de ISS (Brasília, Rio de Janeiro, Novo Hamburgo, São Sebastião do Caí, Montenegro, Palhoça): cadastrar os dias (já era pendência).

### DecWeb — 265 em 09/2026 (03/10/2026)
- [x] Fase 1 sem envio: login na empresa certa, sem Prestados/Tomados. Fase T parou por pendência no cadastro (responsável não informado); Fernanda preencheu o responsável no site. Fase T de novo: **declaração ENVIADA às 08:42**, guia sem valor a recolher (não impressa), PDF `265_BelemBrasil_PortoAlegre_09.2026_DeclaraçãoMensal.pdf` baixado.
- [x] Fila Atualizações do 265 (Set2026) **colada e processada em 03/10 (08:56)**: DECLARAÇÃO PREFEITURA `Enviado` (linha 328), GUIA ISSQN `Sem movimento` (327), SERVIÇOS PRESTADOS `Sem movimento` (325), SERVIÇOS TOMADOS `Sem movimento` (324).
- [ ] Chamar atenção para: nome do arquivo do certificado A1 do 265 no Drive tem a senha escrita; a senha do DecWeb é a mesma. Renomear o arquivo e trocar as senhas.

### Portal Nacional — 265 em 09/2026 (03/10/2026)
- [x] Certificado A1 instalado (vence 01/10/2027), 265 incluído no `clientes.csv` do Portal (30 clientes). Rodada do 265: sessão anterior apagada, empresa logada confirmada pelo CNPJ, **Emitidas 0 notas** (09/2026 a 31/10), Recebidas geraram `265_BelemBrasil_PortoAlegre_09.2026_Recebidas.xlsx` na 003 de setembro.
- [x] Recibo da prefeitura conferido no PDF: declaração de Set/2026 recebida em 03/10/2026 às 08:42:47, receita bruta, imposto próprio e retido = R$ 0,00.
- [ ] **Out/2026 do 265:** o Recebidas traz 1 NFS-e tomada, nº 182232, de 01/10/2026 (competência 10/2026): SAFEWEB, certificado digital e-CNPJ A1, R$ 275,00, ISS 2% (R$ 5,50) não retido. Não é de 09/2026. Tratar no fechamento de outubro.

### DecWeb 09/2026 — rodada fase 1 de 03/10 (14 clientes, sem envio)
- [x] Declaração criada e dados baixados (ainda **não enviadas**) para: 2, 26, 155, 173, 177, 189, 209, 237, 238, 241, 257, 258. O 26 (Raldi) passou com a senha nova.
- [ ] **152 CRBM5 (Conselho de Biomedicina, insc. 276754-2-4): bloqueado.** O DecWeb não deixa abrir Set/2026 porque existe **Ago/2026 – Retificadora 1 – Aberta** (a Original de Ago foi enviada em 10/09/2026). Não era problema de senha. A Fernanda precisa decidir no site: concluir/enviar a retificadora (se for correção real) ou descartá-la (se foi aberta por engano). Ainda não sabemos quem a abriu.
- [ ] **205 L S BECKER: `login_falhou`** (usuário/senha do `clientes.csv`). Conferir na mão no DecWeb; evitar várias tentativas seguidas.
- [ ] Próximo: fase T nos 12 criados (com `aceitar_avisos` em branco: quem não tiver notas para com pendência e a Fernanda confirma receita zero), depois guias para o G-Click e TSV da fila.

### DecWeb 09/2026 — fase T de 03/10 (recibos lidos no Drive, 11:16 a 11:26)
- [x] **Declarações enviadas (recibo da prefeitura):** 2, 26, 155, 177, 189, 209, 237, 241, 257, 258.
- [x] Receita zero (sem guia): 2, 26, 209, 237, 258 (em 2 e 237 só há serviços tomados, sem ISS retido).
- [ ] **Guias a enviar pelo G-Click (venc. 13/10/2026), total R$ 10.909,88:** 155 Mainieri R$ 842,02 · 177 ILS R$ 530,40 · 189 Real Engenharia R$ 634,31 (Sociedade de Profissionais, 3 prof. × 35 UFM) · 241 Simples GPS R$ 2.403,15 · 257 B2B R$ 6.500,00 (ISS R$ 7.262,54 menos R$ 762,54 retidos pela Telefônica). Mais as de 16 (R$ 422,87) e 18 (R$ 42,00). Ficam `Pendente` até o envio comprovado.
- [ ] **173 Lopes & Martins e 238 REAT: NÃO enviados** (sem recibo). O 238 tem ISS **retido** nos tomados (R$ 609,54: Prime System e Primegrid), então não é sem movimento e gera guia; conferir também se a retenção sobre prestador do Simples (Prime System, 5%) está correta. Ver o log da rodada para o motivo da pendência.
- [ ] **Conferência com o Portal Nacional (chave de acesso é a mesma nos dois lados):** rodar o Portal para 155, 189, 237, 241, 257 e 258 (têm certificado). **Sem certificado neste PC:** 2, 26, 173, 177, 209 (conferir de outro modo). Cuidados: competência pela data da prestação (155 e 241 têm notas emitidas em 01/10 com prestação em 30/09); 155 tem 1 nota cancelada e 3 com valor 0; a retenção de R$ 762,54 do 257.
- [ ] Pendências remanescentes: 152 (retificadora de agosto aberta), 205 (login), 186 (documentos).

### Conciliação DecWeb × Portal Nacional — 09/2026 (03/10/2026, arquivos do Drive)
- [x] **155 Mainieri (Emitidas × Prestados): bate.** Portal competência 09/2026 = 108 notas (107 normais + 1 cancelada), R$ 21.051,25, ISS R$ 842,02; mesmas notas 876 a 983 do DecWeb. Recebidas do 155 ainda não baixadas.
- [x] **16 Centro Clínico: bate.** Emitidas 221 notas = R$ 142.642,60 (receita da declaração; ISS fixo R$ 422,87 por 2 profissionais); Recebidas 4 notas = R$ 753,49 (= Tomados do DecWeb). 6 notas de 10/2026 ficam de fora.
- [x] **238 REAT (Recebidas × Tomados): bate.** 7 notas de set. = R$ 15.730,90, ISS retido R$ 609,54 (Prime System e Primegrid); a 8ª nota do Portal (Castro Serralheria, R$ 450) é de 08/2026. Sem arquivo de Emitidas (0 notas). **A declaração do 238 ainda não foi enviada.**
- [x] 265: Emitidas 0; Recebidas 1 nota de 10/2026 (SAFEWEB, R$ 275,00).
- [ ] Alerta 155: 63 notas com competência 08/2026 foram geradas entre 31/08 e 03/09; a declaração de agosto foi recebida em 05/09 (R$ 22.477,87, ISS R$ 899,14), depois delas. Sem indício de furo, mas o mês inteiro não foi conferido.
- [ ] 238, pontos para REINF (15/10) e conferência: INSS retido R$ 1.295,45 (Prime System), IRRF R$ 17,75 e PIS/COFINS/CSLL retidos R$ 141,86 nas notas tomadas. Conferir se a retenção sobre prestador ME/EPP está correta.
- [ ] Falta baixar/conferir: 189, 237, 241, 257, 258 (Emitidas e Recebidas) e Recebidas do 155. Sem certificado: 2, 26, 173, 177, 209.

### Conciliação rodada no PC (`conciliacao.py 09/2026 --sem-pdf`, 03/10/2026) — nenhuma divergência
- [x] **Conciliados, sem divergência:** 16 (Prest. 221 notas R$ 142.642,60; Tom. 4 notas R$ 753,49), 155 (Prest. 107 notas R$ 21.051,25; Tom. 8 notas R$ 2.666,53), 189 (Prest. 2 notas R$ 2.868.189,79; Tom. 1 nota R$ 142.933,33), 237 (Tom. 1 nota R$ 1,60), 238 (Tom. 7 notas R$ 15.730,90, ISS retido R$ 609,54), 241 (Prest. 32 notas R$ 48.063,00; Tom. 5 notas R$ 6.261,84), 257 (Prest. 2 notas R$ 145.250,72, ISS retido R$ 762,54; Tom. 13 notas R$ 3.691,23), 265.
- [ ] **Sem planilha do Portal (sem certificado neste PC, não dá para conciliar):** 2 (Tom. 2 notas R$ 2.285,70), 18 (Prest. 1 nota R$ 2.100,00), 133 (Tom. 1 nota R$ 300,00), 138 (Tom. 9 notas R$ 28.980,50), 177 (Prest. 1 nota R$ 26.520,00), 263 (Prest. 9 notas R$ 81.793,56; Tom. 1 nota R$ 650,00). Os 26, 173, 209 e o 258 não apareceram (sem arquivos do DecWeb nem do Portal): o 258 tem certificado, rodar o Portal para confirmar que não há notas.
- [ ] Notas de outra competência no Portal, ignoradas (conferir no CSV `--csv-notas` se alguma tem ISS retido e se entrou na declaração do mês certo): 155 (63 de 08/2026 em Prestados; 1 de 10/2026 em Tomados), 16 (6 de 10/2026), 237 (1 de 08/2026), 238 (1 de 08/2026), 241 (3 de 08/2026), 257 (1 de 08/2026 e 1 de 10/2026).
- [ ] 155: 3 notas com valor zero e 1 cancelada (Prestados), iguais nos dois lados.

### Portal Nacional 09/2026 — situação da pasta 003 (03/10/2026, ~12:25)
- [x] **Com Emitidas e Recebidas:** 16, 71, 126, 155, 189, 241, 257, 261. **Só Recebidas** (Emitidas sem notas, provável): 152, 197, 237, 238, 264, 265. **Só Emitidas:** 205. **Sem nenhum arquivo:** 117, 247, 258 (zero nos dois, ou falha: ver `portalnacional\logs\resultados.csv`). **Não rodou:** 186 (aguarda documentos).
- [x] Clientes com certificado (19): 16, 71, 117, 126, 152, 155, 186, 189, 197, 205, 237, 238, 241, 247, 257, 258, 261, 264, 265. Sem certificado (11): 2, 18, 26, 133, 138, 173, 177, 185, 209, 248, 263.
- [ ] Previsão pelo Portal para o DecWeb (a conferir no resultado): **205** Prestados 17 notas normais, R$ 95.753,11, ISS 2% = R$ 1.915,06 (1 cancelada e 1 substituída fora; 5 notas de 10/2026 fora); **152** Tomados 59 notas, R$ 84.099,50, ISS R$ 1.920,13, **ISS retido R$ 568,44** em 14 notas (gera guia; 3 canceladas; 11 notas de 10/2026 e 1 de 08/2026 fora).

### DecWeb 09/2026 — situação após o `resultados.csv` (03/10/2026, ~12:30)
- [x] **205 L S Becker enviado** (recibo 03/10 12:26:41): receita R$ 95.753,11, ISS R$ 1.915,06, guia R$ 1.915,06 venc. 13/10 — **bateu exatamente com a previsão do Portal**.
- [x] Enviadas: 18 de 22 (2, 16, 18, 26, 117, 133, 138, 155, 177, 189, 205, 209, 237, 241, 257, 258, 263, 265).
- [ ] **Pendência (mesma mensagem nas 3):** 173 (11:19 e 12:26), 238 (11:24 e 12:27), 152 (12:25): "Não foi informado serviço prestado/tomado para esta escrituração". O Prestados baixado está vazio, então o robô só segue com `aceitar_avisos=sim` no `clientes.csv`. O 173 continuou parando às 12:26 mesmo após a confirmação da Fernanda: conferir se o `sim` foi salvo na linha dele. 238 e 152 também precisam do `sim` (receita própria zero confirmada pelo Portal: sem Emitidas).
- [ ] **O DecWeb importa o ISS retido dos tomados sozinho:** em agosto o 238 foi declarado com retido R$ 588,84 e o 152 com R$ 424,55. **Esperado em setembro:** 238 retido R$ 609,54 (tudo Porto Alegre); 152 retido total R$ 568,44, sendo **R$ 461,69 de Porto Alegre** (guia no DecWeb) e **R$ 106,75 de Estrela/RS** (2 notas, incidência em Estrela). Verificar nos PDFs depois do envio.
- [ ] **152, Estrela/RS:** em agosto houve um lançamento separado de R$ 25,63 para o Município de Estrela ("Declaração de Serviços Eventuais Tomados", competência 08/2026, venc. 23/09). Para setembro, pelas notas do Portal, esperar R$ 106,75; é feito no portal de Estrela, não no DecWeb. A Fernanda precisa fazer/confirmar.
- [ ] 186 Lopes & Nadal: aguarda documentos.

### DecWeb 09/2026 — rodada final de 03/10 (173, 152, 238 enviados às 14:02 a 14:04)
- [x] **21 de 22 enviadas** (falta só o 186, que aguarda documentos). Recibos: 152 às 14:02:14, 173 às 14:02:59, 238 às 14:03:48.
- [x] **Previsões do Portal confirmadas:** 238 ISS retido R$ 609,54 (guia R$ 609,54); 152 ISS retido R$ 461,69 de Porto Alegre (guia R$ 461,69); 205 R$ 95.753,11 / R$ 1.915,06.
- [x] **Correção:** o **173 NÃO é sem guia**. É Sociedade de Profissionais (2 profissionais × 35 UFM × R$ 6,0411): ISS fixo e **guia de R$ 422,87** (venc. 13/10), receita NFSE R$ 0,00. Eu havia dito "sem guia"; estava errado. (O mesmo profissional, Rodrigo Tavares Lopes, mesmo CPF, consta na declaração do 16 e na do 173: conferir se pode constar nas duas.)
- [ ] **Guias a enviar pelo G-Click (venc. 13/10), 11 guias, R$ 14.783,91:** 16 (422,87), 18 (42,00), 155 (842,02), 173 (422,87), 177 (530,40), 189 (634,31), 205 (1.915,06), 238 (609,54), 152 (461,69), 241 (2.403,15), 257 (6.500,00). Ficam `Pendente` até o envio comprovado.
- [ ] **152, Estrela/RS:** R$ 106,75 de ISS retido (2 notas com incidência em Estrela) a declarar no portal do Município de Estrela (em agosto foram R$ 25,63, venc. 23/09). Pelas notas do Portal; confirmar.
- [ ] **Voltar `aceitar_avisos` para em branco** em 173, 238, 152 (e 265, se ainda estiver `sim`).
- [ ] Conciliação: rodar de novo `conciliacao.py` com 152 e 205 (Portal já baixado).

### Cadastros do 265 (03/10/2026)
- [x] Capital resolvido: o contrato registrado na JUCISRS tem **R$ 5.980.000,00** (5.980.000 quotas de R$ 1,00; 2.990.000 para cada sócio, 50%); os R$ 5,95 mi eram só da proposta. Nome oficial "ARQUITETURA E PARTICIPACOES". Dados dos sócios (CPF/RG) lidos do contrato e entregues à Fernanda no chat; **não ficam neste repositório**.
- [x] Fernanda está finalizando o cadastro do 265 no Domínio (importando do 238).
- [ ] Pró-labore dos sócios: o contrato (cl. 13) permite, mas não fixa valor; definir com os sócios antes de abrir Folha.
- [ ] Bairro dos sócios no contrato é "Chapéu do Sol" e o da sede é "Belém Novo" (Cartão CNPJ e DecWeb usam Belém Novo).
- [x] 265 cadastrado **via extensão Claude in Chrome pela Fernanda** em 03/10 (o arquivo `INSTRUCOES_CHROME_265_SIEG_GCLICK.md` gerado pela agente estava incorreto e não foi usado; existe a skill `cadastro-cliente-sieg`). (?) confirmar se foram SIEG e G-Click, ou só o SIEG.

### Regras e memória registradas
- [x] Guia só vira `Enviado` com envio comprovado pelo G-Click; declaração da prefeitura é comprovada pelo recibo.
- [x] Tacom de Porto Alegre sempre primeiro (guia do ISSQN no dia 1); Lopes & Nadal (186) também prioridade, após os documentos.
- [x] `CLAUDE.md` e notas datadas no Drive criados.

---

## Como manter este documento
1. Ao fim de cada etapa: mover o item de PENDENTE para RESOLVIDO (com a data) ou ajustar o texto; acrescentar o que surgiu.
2. Salvar um snapshot `PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` na pasta do Drive e dar `git push` neste arquivo.
3. Nunca registrar senhas, CPFs completos ou certificados aqui.
