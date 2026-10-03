# Pendências e resolvidos — OfficeCont (Fechamento Fiscal)

Documento vivo. **Atualizar a cada etapa** e salvar um snapshot datado na pasta `ARQUIVOS EXTENSÃO - CODE - CLAUDE` do Drive,
para não perdermos contexto. Última atualização: **03/10/2026** (sessão 2: cliente 265 cadastrado e com 09/2026 fechado; falta o restante do fechamento de 09/2026).

Convenção: `[ ]` pendente · `[x]` resolvido · `(?)` precisa de confirmação da Fernanda.

---

## PENDENTE

### Com data marcada
- [ ] **Tacom — SPED Fiscal (10/2026):** enviar os arquivos à Leidislaine Ribeiro **até quarta 07/10** (ela transmite até quinta 08/10; entra de férias).
  Acesso à máquina dela na **segunda 05/10, antes das 11:00** (a Fernanda não consegue nesse horário; conferir se ela confirmou). (?) vale para 138, 263 ou ambas?
- [ ] **ISSQN Porto Alegre 09/2026 vence 13/10.** Rodar o DecWeb nos clientes restantes antes disso (ver abaixo).
- [ ] **REAT HOLDING (238) — 2ª quinzena de outubro (16 a 31/10):** enviar à cliente o **relatório de débitos ref. 06/2026** (Relatório Fiscal de 21/08, Júlia Rocha)
  **+ IRPJ e CSLL vencidos de meses anteriores.** (?) quais meses estão vencidos. Fila sugerida (Pendente) para DARF IRPJ e DARF CSLL do 238 na Set2026: não confirmado que foi colada.
- [ ] **Certificados que vencem:** 258 Nadal (14/10/2026), 155 Mainieri (27/10), 71 Conte (13/11), 117 Tabajara (11/12), 126 Tatsch Leite (16/12). Providenciar renovação.
- [ ] **SPED Contribuições 09/2026:** prazo 16/11 (na planilha). Pendência de agosto: SPED Contribuições 15/10.

### Fila da Controle_Fiscal (aba Atualizações) — a confirmar que foi colada e processada
- [ ] Tacom 09/2026: 263 declaração Enviado; 263 guia Enviado R$ 4.089,69 (G-Click comprovado em 02/10); 138 declaração Enviado. (?) 138 guia: lançar `Sem movimento`?
- [ ] Corrigir observações das guias do 16 e do 18 (dizem "Venc. 09/10"; o correto é **13/10/2026**).
- [ ] Guias do 16 (R$ 422,87) e do 18 (R$ 42,00): continuam `Pendente` até o envio comprovado no G-Click; depois `Enviado`.

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
