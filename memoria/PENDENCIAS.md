# Pendências e resolvidos — OfficeCont (Fechamento Fiscal)

Documento vivo. **A cada rodada:** atualizar este arquivo (o que foi feito e o que falta), o log detalhado
`PROCESSO_FECHAMENTO_09-2026.md` e salvar o snapshot `PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` na pasta
`ARQUIVOS EXTENSÃO - CODE - CLAUDE` do Drive (regra da Fernanda, 02/10 e 04/10/2026).
Última atualização: **04/10/2026, noite.**

Convenção: `[ ]` pendente · `[x]` resolvido · `(?)` precisa de confirmação da Fernanda.
Nunca registrar aqui senhas, CPFs completos ou certificados.

**Situação em 04/10/2026 (noite):** agosto/2026 está **fechado** e o **SPED Contribuições de 08/2026 foi transmitido** (22 de 25;
faltam 117 e 227; o 002 foi transmitido às 13:51). Agora **volta o fechamento de 09/2026.**

---

## PENDENTE

- [ ] **126 Tatsch & Leite (São Leopoldo), ISS 09/2026 (04/10):** DMS (nº 1053665, ADN, 02/09/2026) e guia conferidos com o Portal Nacional: 209 notas, R$ 153.662,41, ISS **R$ 3.073,23**, batem centavo a centavo. Tomador: 16 notas, ISS 65,41, todas não retidas (nenhuma guia de tomador; 15 estão no Portal e a 16ª é o Facebook nº 14644240, R$ 1.703,92, comp. 30/09, fora do arquivo de Recebidas). Guia **liberada**: R$ 3.073,23, venc. 15/10/2026, Nosso Número 14400000001431673-7, salva no Drive (`..._09.2026_ISSQN.PDF`). **Confirmado pela Fernanda (04/10):** DECLARAÇÃO PREFEITURA `Enviado` (DMS). Print do G-Click (tarefa `ISSQN - São Leopoldo - SET/2026`): Guia ISS concluída e Envio ao cliente concluído em 04/10/2026 14:46 por fernanda.officecont (Guia ISS tomados: não se aplica). TSV entregue com a guia `Enviado` com base nesse print; falta ela colar e rodar `processarAtualizacoes()`. Fluxo documentado na skill `.claude/skills/sao-leopoldo-issqn/SKILL.md`.

- [ ] **SEGUNDA 05/10, PRIMEIRO HORÁRIO (lembrete):** enviar ao **257** o WhatsApp e o e-mail perguntando se a Lifecombr (nota 31, ISS R$ 6.500,00) deveria ter retido; textos em `memoria/RASCUNHOS_2026-10-05.md`. Também enviar o e-mail do **152** ao Gian sobre o ISS de Florianópolis (nota 6940, R$ 42,00; ISS 0,00 no Portal). Gian é interno da Officecont (responsável contábil nos cadastros de São Leopoldo), não contato do cliente.
- [ ] **152, Estrela/RS (R$ 106,75, ENGI PROJECT):** Fernanda e agente acessam juntas o portal de Estrela, para aprender a baixar as notas e fazer a declaração. Marcar horário.
- [ ] **205:** Fernanda confirmou (04/10) que a guia R$ 1.915,06 pode ser postada (nota 197 é a substituta); `conciliacao.py` corrigido (nota de substituição gerada conta como normal). Postar no G-Click.

### 1. Datas marcadas
- [ ] **Seg 05/10, antes das 11:00:** ligar para a Leidislaine (Tacom) e combinar o acesso à máquina dela (e-mail sem retorno até 03/10).
- [ ] **Qua 07/10: SPED Fiscal da Tacom** (10/2026) à Leidislaine, que transmite até 08/10. (?) vale para 138, 263 ou ambas?
- [ ] **13/10: ISSQN de Porto Alegre 09/2026** (o prazo é o impresso na guia, nunca o 09/10 do Domínio).
- [ ] **14/10: certificado A1 do 258 Nadal vence.** Conferir no OWA (Itens Enviados) se o e-mail ao Gian foi enviado; rascunho entregue em 03/10. Demais: 155 em 27/10, 71 em 13/11, 117 em 11/12, 126 em 16/12.
- [ ] **15/10: REINF de 09/2026** (186 já enviado; conferir os demais) e **002, 227 e 117 do SPED de 08/2026** (seção 2).
- [ ] **Sex 16/10 (sugerido): retorno do contábil** com rendimentos financeiros e IRRF do 3º trimestre.
- [ ] **23/10: DARF de PIS/COFINS de 09/2026. 30/10: IRPJ e CSLL do 3º trimestre. 16/11: SPED Contribuições de 09/2026.**
- [ ] **16 a 31/10: REAT HOLDING (238):** enviar à cliente o relatório de débitos ref. 06/2026 (Relatório Fiscal de 21/08, Júlia Rocha) + IRPJ e CSLL vencidos de meses anteriores. (?) quais meses.
- [ ] **238, retificação de junho/2026:** a FAT mostra guia complementar "A gerar" e pagamento "Pendente" (PIS R$ 38,96 + COFINS R$ 239,77 = R$ 278,73). Confirmar se foi gerada e paga.

### 2. SPED Contribuições 08/2026 (vence 15/10) — TRANSMITIDO em 04/10 (13:11 a 13:44)
- [x] **Transmitidos (Original, ReceitaNet, recibos lidos no Drive, `08_AGOSTO\010 EFD CONTRIBUIÇÕES`):** 016, 018, 026, 071, 126, 133, 155, 173, 177, 185, 186, 189, 205, 209, 237, 238, 241, 247, 257, 258, 261 e 264 (22 de 25). Valores dos recibos = arquivos conferidos (016 PIS 770,94 / COFINS 3.558,16; 126, 155, 185, 257 a recolher; 018, 071, 177, 189 cobertos por retenção; 205 a recolher 200,53 / 925,50; 241 a recolher 231,78 / 1.069,82; 133 e 238 Real: 11,55 / 53,22 e 576,15 / 2.655,03; zerados: 026, 173, 209, 237, 247, 258, 261, 264). O PVA aceitou os arquivos com registro 0120.
- [x] TSV `Enviado` da Ago2026 (SPED CONTRIBUIÇÕES) entregue em 04/10 para 186 (já colado) e para os outros 21 (a colar).
- [x] **002 RF Consultoria transmitido** em 04/10 às 13:51:44 (recibo conferido: PIS 142,86 / COFINS 659,34, iguais ao DARF de agosto); TSV `Enviado` entregue. Total transmitido: 23 clientes.
- [ ] **Ainda sem SPED de 08/2026:** **117** Tabajara (arquivo zerado gerado; sem procuração/certificado, baixa em andamento: propor `Não se aplica`, a confirmar) e **227** PROGEST (sem arquivo). 152 (autarquia) e 197 (dispensada) já estão `Não se aplica` na Controle.
- [ ] Observações a manter: 257 é contribuinte de ICMS e o arquivo só tem serviços (confirmar se a receita de R$ 126.223,13 inclui mercadoria); 018 com saldo de retenção sem uso nos registros 1300/1700 (conferir no Domínio).
- [ ] Linhas DARF PIS/COFINS de agosto ainda `Pendente` na Ago2026 (071, 133 COFINS, 237, 238, 241, 257, 258, 261): agosto está fechado; atualizar a planilha quando convier (071 `Retido`, 133 COFINS `Compensado` por PER/DCOMP, 237/258/261 `Sem movimento`).

### 3. Fechamento 09/2026 — Porto Alegre (DecWeb) — 22 de 22 declarações enviadas
**Guias ISSQN (venc. 13/10):**
- [x] Enviadas e já na Controle (TSV colado, G-Click 04/10 11:34): 16 (422,87), 18 (42,00), 152 (461,69), 173 (422,87), 177 (530,40), 186 (422,87), 189 (634,31), 238 (609,54), 241 (2.403,15); 263 Tacom (4.089,69, em 02/10).
- [ ] **155 (842,02): segurada, aguardando a Camila.**
- [ ] **257 (6.500,00): analisar na SEGUNDA 05/10 com o cliente.** ISS 7.262,54, retido só 762,54 (cliente costuma reter tudo). **Explicado (04/10):** a guia de 6.500,00 é o ISS (5%) da nota 31 LIFECOMBR TELECOMUNICACOES, R$ 130.000,00, item 10.05, `Não Retido` no Portal; a nota 32 TELEFONICA (R$ 15.250,72, ISS 762,54) veio retida. Perguntar ao cliente se a Lifecombr devia ter retido.
- [ ] **205 (1.915,06): provável OK (04/10):** a nota 196 está `Substituída` pela 197 (R$ 6.000, `NFS-e de Substituição Gerada`, Normal); a soma das normais do Portal (com a 197) = R$ 95.753,11 = DecWeb (17 notas). A divergência vem de como o `conciliacao.py` trata nota de substituição; ajustar o script e aguardar a confirmação da Fernanda para postar a guia. Texto anterior: **segurada.** DecWeb tem 1 nota de R$ 6.000,00 (ISS 120,00) que o Portal não tem; 3 canceladas no Portal x 2 no DecWeb. Rodar `findstr /I "Becker" notas_09_2026.csv`; se a nota estiver cancelada, retificar e refazer a guia.
- [x] **Fernanda confirmou `Sem movimento` na guia ISSQN de 09/2026 de 26, 209, 237 e 258 (04/10)**; TSV entregue. [ ] Segue em branco o **2 RF Consultoria** (não confirmado); 247 (Montenegro, DMS fora do DecWeb); 138, 117, 133 e 265 já `Sem movimento`.
- [ ] **152, Estrela/RS:** R$ 106,75 de ISS retido a declarar no portal de Estrela (em agosto foram R$ 25,63, venc. 23/09). Retido total 568,44 = 461,69 POA + 106,75 Estrela. A localizar a nota de R$ 42,00 que só o Portal tem.
- [ ] Voltar `aceitar_avisos` para em branco em 173, 238, 152 e 265.
- [ ] Rodar de novo `conciliacao.py` (já corrigido) para 152, 205 e 186. Reset do `aceitar_avisos` (173, 238, 152, 265): **feito pela Fernanda em 04/10**. **152 (04/10), comparado pela chave:** única nota só no Portal da 09/2026 é a LITORAL SERVICOS AUTOMOTIVOS nº 6940 (R$ 42,00, 01/09, incidência Florianópolis/SC, ISS 0,00: sem efeito na guia); ENGI PROJECT notas 1146 e 1218 (ISS retido 25,63 + 81,12 = **R$ 106,75, incidência Estrela/RS**): declarar/pagar no portal de Estrela. Notas de 10/2026 e 08/2026 no Portal são de outra competência (não entram).
- [ ] **227 PROGEST:** estava inativa; as entregas começam em 09/2026 (por isso sem SPED de 08/2026). **FAT do 186: feito.**
- [ ] Rodrigo Tavares Lopes (mesmo CPF) consta como profissional nos clientes 16 e 173: conferir.
- [ ] 155: 63 notas de 08/2026 geradas entre 31/08 e 03/09; sem indício de furo, mas agosto inteiro não foi conferido.
- [ ] Município sem prazo de ISS: Brasília, Rio de Janeiro, Novo Hamburgo, São Sebastião do Caí, Montenegro, Palhoça (já era pendência).

### 4. Fechamento 09/2026 — Domínio, federais e FAT
- [x] **186 conferido no Domínio (04/10):** prestados 11.475,05, entrada Google 22,50, IBS/CBS, retenções e IRPJ/CSLL do trimestre batem; ISS por profissional corrigido pela Fernanda (422,87); PIS 74,59 e COFINS 344,25 batem.
- [ ] **186: digitar R$ 11.475,05 no FAT** (RECEITA SERVIÇOS/SETEMBRO, célula L4 de `186_LOPES&NADAL_FAT2026`) e conferir PIS 74,59, COFINS 344,25, IRPJ 1.315,74, CSLL 789,45 (soma mensal 789,44: arredondamento).
- [ ] **186: IRPJ e CSLL do 3º trimestre pendentes** até o contábil liberar rendimentos financeiros e IRRF (entram 100% na base; IRRF dedutível). Linhas DARF IRPJ e DARF CSLL do 186 já `Pendente` na Set2026.
- [ ] **186: pergunta aberta sobre R-4010:** houve distribuição de lucros ou pagamento a pessoa física em setembro? Sem a resposta não se confirma "não se aplica".
- [ ] **186: SPED Contribuições de 09/2026** vence 16/11.
- [ ] **Conferência no Domínio dos demais clientes** (assim que a Fernanda importar e exportar para `008 ARQUIVOS DOMÍNIO`, `09_SETEMBRO`): começar por 152 e 205 (divergências), seguir a ordem de prioridade.
- [ ] **Acumuladores IBS/CBS (Domínio):** o do 186 foi ajustado (cClassTrib 200052/CST 200 nos prestados). Repetir só onde a atividade for a mesma; não replicar o 200052 para outras atividades sem conferir.
- [ ] **Planilha `CONTROLE | Rendimentos.xlsx` (aba `3ºTRIM 2026`):** incluir **227 PROGEST, 264 ZENITH PARACURU e 265 BELEM BRASIL HOLDING** (digitar nas linhas 24 a 26 e classificar A2:D26 pela coluna A). (?) 133 RFL e 238 REAT (Lucro Real) saíram dos blocos de 2026: confirmar. E-mail ao contábil entregue em rascunho (prazo sugerido 16/10).

### 5. Portal Nacional e robôs
- [x] Rodada de 09/2026 concluída em 02–04/10 (inclui 186; 117, 247 e 258 `sem_movimento` aceitos).
- [ ] Clientes **sem certificado** neste PC (2, 18, 26, 133, 138, 173, 177, 185, 209, 248, 263) ficam de fora; Tacom precisa de outro caminho (acesso à máquina da cliente).
- [ ] (?) 173 "PENDENTE DE CADASTRO"; 71, 197 e 261 "Em Transição (Prefeitura)": o Padrão Nacional já vale?
- [ ] `conciliacao.py`: copiar para `C:\Robos\decweb` e `pip install pypdf` (opcional) se ainda não foi feito.

### 6. Cliente 265 BELEM BRASIL HOLDING
- [ ] **Segurança:** trocar a senha do DecWeb (foi digitada no chat em 02/10); renomear o arquivo do certificado A1 no Drive (o nome contém a senha); apagar a mensagem do WhatsApp com a senha do certificado.
- [ ] ISSQN nos meses seguintes: só a arquitetura (71.11-1-00) gera ISS; aluguel e compra e venda de imóveis próprios ficam fora (?). Outubro: nota SAFEWEB 182232 (R$ 275,00, ISS 2% não retido) a tratar.
- [ ] Pró-labore dos sócios (cl. 13 do contrato não fixa valor); (?) confirmar se SIEG e G-Click foram ambos cadastrados.
- [ ] Incluir no Portal Nacional `clientes.csv` já feito; falta incluir 265 na planilha de rendimentos (ver seção 4).

### 7. Antigas e estruturais
- [ ] R-4010 do 189; PER/DCOMP do 133; conferência do 238; as 7 linhas "Não se aplica" fixas.
- [ ] Possível gerador de TSV a partir dos PDFs que o robô baixa.
- [ ] Se a BrasilAPI falhar em sessão nova, liberar `publica.cnpj.ws` e `receitaws.com.br` na rede do ambiente.

---

## RESOLVIDO (resumo por data)

### 04/10/2026
- [x] **SPED Contribuições de 08/2026 transmitido para 22 clientes** (13:11 a 13:44; Original, ReceitaNet): 016, 018, 026, 071, 126, 133, 155, 173, 177, 185, 186, 189, 205, 209, 237, 238, 241, 247, 257, 258, 261 e 264; recibos lidos e conferidos com os arquivos; TSV de registro entregue.
- [x] **186 (Lopes & Nadal) fechado até onde depende só da casa:** documentos chegaram; Portal (5 emitidas, 2 recebidas); DecWeb enviado às 11:26 (receita 11.475,05, guia 422,87); guia enviada pelo G-Click; PIS/COFINS (418,84, venc. 23/10) subidos e `Enviado`; REINF R-2099 enviado (recibo 12122144-09-2099-2609-12122144); Domínio conferido; auditoria da Controle feita e TSV colado (prestados, tomados, REINF, IRPJ/CSLL pendentes).
- [x] **SPED Contribuições 08/2026 do 186 transmitido** (13:11:36, recibo na Ago2026); pasta do Drive renomeada para `010 EFD CONTRIBUIÇÕES`.
- [x] Portal 117, 247 e 258 sem movimento; 9 guias ISSQN enviadas; 138 guia `Sem movimento`; correção do PIS do 016 em agosto (770,94, não 771,31).
- [x] Conciliação Portal x DecWeb de 03/10 analisada (sem divergências, exceto 152 e 205); soma correta das guias liberadas: R$ 5.949,70 (o R$ 8.388,07 dito antes estava errado).

### 03/10/2026
- [x] DecWeb 09/2026: 22 de 22 enviadas, 186 em 04/10 (recibos lidos). 173 NÃO é sem guia: Sociedade de Profissionais, guia 422,87.
- [x] Portal Nacional rodado para os 19 clientes com certificado; `conciliacao.py` criado e rodado (sem divergência em 16, 155, 189, 237, 238, 241, 257, 265).
- [x] 265: declaração enviada e fila processada; capital resolvido (R$ 5.980.000,00); cadastro via extensão do Chrome.
- [x] Prazos de ISSQN de Porto Alegre corrigidos para 13/10 (46 linhas); `verificarPrazosSet2026` sem problemas.

### 01–02/10/2026
- [x] DecWeb: 16, 18, 117, 133 (01/10) e Tacom 138 e 263 (02/10); guia do 263 (R$ 4.089,69) enviada pelo G-Click com comprovação.
- [x] Bug de sessão do Portal Nacional corrigido; `portal_config.py` renomeado; certificados verificados (19 com, 11 sem).
- [x] Aba Set2026 criada (320 linhas) com prazos em texto e linhas de IRPJ/CSLL trimestral.

### Regras e memória registradas
- [x] Guia só vira `Enviado` com envio comprovado pelo G-Click; declaração da prefeitura é comprovada pelo recibo.
- [x] Tacom de Porto Alegre sempre primeiro; Lopes & Nadal (186) após os documentos, ISSQN junto com os demais impostos quando possível.
- [x] Domínio considera a **data de saída** das notas (não a de emissão): notas emitidas em setembro com saída em agosto ficam em agosto.
- [x] Registrar a memória a cada rodada: este arquivo + `PROCESSO_FECHAMENTO_09-2026.md` + snapshot datado no Drive.

---

## Como manter este documento
1. Ao fim de cada rodada: mover o item de PENDENTE para RESOLVIDO (com a data) ou ajustar o texto; acrescentar o que surgiu.
2. Atualizar o log detalhado em `PROCESSO_FECHAMENTO_09-2026.md`.
3. Salvar o snapshot `PENDENCIAS_E_RESOLVIDOS_AAAA-MM-DD.md` na pasta do Drive e dar `git push`.
4. Conferir a planilha Controle_Fiscal antes de repetir uma pendência (a Fernanda pode já ter colado o TSV).
