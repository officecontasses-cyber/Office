# Snapshot 29/10/2026 (quinta): fechamento fiscal 09/2026

Versão completa: `memoria/PENDENCIAS.md` e dossiês `memoria/CLIENTE_NNN_*.md`. Snapshot anterior: `PENDENCIAS_E_RESOLVIDOS_2026-10-28.md`.

**Repositório:** todo o trabalho foi levado para a branch **`main`** de `officecontasses-cyber/Office`. Qualquer conversa nova já abre com o CLAUDE.md, a memória e o painel de pendências.

## Guias entregues hoje (todas vencem 30/10, cota única)
| Nº | Cliente | CNPJ | DARF | Valor | G-Click |
|---|---|---|---|---|---|
| 247 | Porto Mais Alegre | 53290951000109 | 07.16.26302.4034482-1 | **4.309,37** (IRPJ 807,13 + CSLL 3.502,24) | 29/10 09:43/09:44 |
| 71 | Conte Arquitetura | 08307701000180 | 07.16.26302.4311001-5 | **174.386,85** (IRPJ 104.929,65 + CSLL 69.457,20) | 29/10 10:36/10:37 |
| 186 | Lopes & Nadal | 28516249000173 | 07.16.26302.4584488-1 | **2.337,93** (IRPJ 1.456,55 + CSLL 881,38) | 29/10 11:45 |
As seis linhas estão gravadas na fila `Atualizações` como `Enviado`, com memória de cálculo.

## Decisões e correções do dia
- **133 RFL (87828430000184):** contabilidade informou **prejuízo fiscal no 3ºTRIM** → DARF IRPJ e CSLL `Sem movimento`, sem guia. Pedir balancete/LALUR por escrito.
- **197 ASBBM (05164750000112): CSLL de 95,64 NÃO é devida.** Pesquisa no Lefisc: **IN RFB 1.700/2017, art. 13** — o caput isenta IRPJ e CSLL e o §1º exclui da isenção **apenas o IRPJ** sobre rendimento de aplicação financeira; §2º confirma o **IRRF definitivo** (o saldo credor de 79,60 do FAT **não existe**). Gravado `Não se aplica` nas duas linhas. Consulta formal ao Lefisc marcada para **03/11/2026**.
- **238 REAT (49252432000189):** fechamento de setembro entregue (guia de set enviada pelo Visão Cliente em 28/10 09:15). ENTRADAS e SERVIÇOS PRESTADOS gravados `Em andamento`: falta a apuração do Lucro Real bater no Domínio.
- **FATs corrigidos:** 247 e 186 aplicavam presunção de 32% sobre rendimento financeiro (agora entra 100% na base); 71 tinha a célula do 3ºTRIM do IRRF do Bradesco vazia (9,04). No 186 também foram lançados os rendimentos de resgate que faltavam (jul 657,62/7,32 e ago 362,93/4,92).
- **Rendimentos validados documento a documento:** 71 (Caixa, três extratos do fundo) e 186 (Invest Fácil e Fundo Simples Automático). Sem documento: Bradesco do 71 (vale centavos) e o resgate de 31/07 do 186 (653,00/6,51, calculado por cotas).

## Em aberto, por prazo
| Prazo | Nº | O quê |
|---|---|---|
| ■ vencido | 197 | **COFINS 4% sobre receita financeira: R$ 163,60 em 2026** (abril sozinho 116,15; 3ºTRIM 42,51), nenhuma guia paga. Decidir regularização com o Gian. |
| ■ vencido | 238 | DARFs de abr, mai e jun (9.405,48), pagamento não confirmado |
| ▲ 30/10 | 238 | Balancete de setembro no Livro Diário; relatório de débitos de 06/2026 à cliente |
| ▲ 09/11 | 261 | NFS-e de outubro para a Betha (falta o valor com a Jani); abatimento de 340,00 |
| ▲ 16/11 | todos | **SPED Contribuições 09/2026** — cerca de 25 clientes |
| ○ | 133 | Balancete/LALUR do 3ºTRIM por escrito |
| ○ | 261 | Comprovante do DARF e R-4020 da Betha |
| ○ | 197 | IRRF no Domínio (não pode estar em "a Recuperar"); ECF 2026 forma 9; rever ECF 2024 em LP e CSLL de 41,42 paga em 2025 |
| — | vários | Conciliações do Domínio: 126, 152, 177, 238, 248, 258, 261, 263, 264 |

## Alerta de segurança
E-mail de 04/03/2026 ("Cadastro e-mail contribuinte", Novo Hamburgo) traz **CNPJ e senha em texto aberto**. Conferir se a senha ainda vale, trocar e apagar a mensagem.

## Central (painel-artefato) e cruzamento G-Click x planilha x Drive — rodada da tarde

**Central confirmada como artefato.** Decisão da Fernanda: "a Central continua como artefato, segue alimentando". Não confundir com o que foi descartado hoje (artefato de pendências dentro do chat e mod ao lado do chat). A Central é `claude.ai/artifact/PYPKFYQgT9VNni3pZwg8G7`, abas Meu dia, Tarefas e Radar, estado no banco do artefato. Fonte principal: G-Click via API (somente GET); a Controle_Fiscal entra só com o que o G-Click não tem. Rotinas: G-Click 06:40, planilha 06:45, Meu dia 06:50, Radar 08:40. Código em `paineis/central-officecont-fernanda.html`.

**Painel levado para a `main`** (commit `2c1277a`) e memória atualizada (`2ab5b24`). O painel estava só na branch `claude/bold-clarke-zxllnp`, que **não tinha nenhum commit em comum com a `main`** — nasceu da main antiga. Por isso a sessão da tarde rodou sem o CLAUDE.md e sem a `memoria/` e reconstruiu à mão coisas já escritas: foi assim que a 197 ASBBM foi analisada errado antes da correção.

**Cruzamento do fechamento 09/2026** (980 tarefas na janela jul–dez, 343 abertas, 26 vencidas), gravado na Central em três listas: 26 a dispensar (planilha em `Sem movimento`, `Retido` ou `Sem Recolhimento`), 7 a concluir (obrigação cumprida e comprovante no Drive; a 018 CC&D `93309631000178` sem DARF porque foi compensação) e 6 divergências. O prompt da extensão para fazer na tela proíbe enviar e-mail; o caminho de tela para **dispensar** ainda não está mapeado — a extensão deve descobrir e relatar.

### Divergências achadas
| Nº | Cliente | Divergência |
|---|---|---|
| 248 | TACOM PROJETOS FL SC (`01005845002003`) | ICMS de 09/2026 **dispensado no G-Click** (tarefa 4.7232) mas `Pendente` na planilha; ENTRADAS de 15,00 também `Pendente` |
| 197 | ASBBM (`05164750000112`) | **Nenhuma** tarefa de COFINS/PIS no G-Click, em competência alguma, havendo COFINS de 4% devida — falta a obrigação no perfil do cliente |
| 152 | CRBM5 (`13738204000176`) | "Confirmações - Retenções" vencida 15/10; checklist pede enviar ao CRBIO as retenções de ISSQN e federais — ação real, não dispensar |
| 126 | TATSCH & LEITE (`10914420000137`) | "Taxa de fiscalização anual" (comp 12/2026) vencida 15/10, checklist pede guia + envio ao cliente, **sem linha na planilha** |
| 126 | TATSCH & LEITE | Cotas 2 e 3 do IRPJ/CSLL com status `E` no G-Click (cota 1 `C`); significado do `E` não confirmado |
| 126 | TATSCH & LEITE | **Dois** DARFs de PIS/COFINS de 09/2026 no Drive (17/10 e outro de 27/10 com sufixo `_RE`) e uma linha só na planilha — conferir se é retificação ou complemento |

### Estrutura do Drive do fechamento (mapeada)
`1015_ROTINA AUTOMATICA / 001 FECHAMENTO FISCAL / 001_FECHAMENTO FISCAL / <MM_MÊS>`, só com 07_JULHO, 08_AGOSTO e 09_SETEMBRO; dentro, por tipo (001 REINF, 002 municipais, 003 Portal Nacional, 004 ICMS, 005 conferências, 006 XML, 007 SIEG, 008 Domínio, 009 impostos federais, 010 EFD Contribuições, 011 documentos de clientes). Nomenclatura `codigo_Cliente_Municipio_09.2026_Documento.pdf`; não existe arquivo com "DARF" no nome (são `PIS-COFINS` e `IRPJ-CSLL 3ºTRIM`, na 009). **A pasta 010 EFD CONTRIBUIÇÕES de setembro está vazia** — coerente com as ~25 linhas `Pendente` e as tarefas do G-Click para 13 e 16/11.

### Radar
Rodado no período 28–29/10, 22 linhas do roteiro. Com os domínios oficiais liberados na rede, dois itens passaram a **confirmados em fonte oficial**:
- **POAISS (Porto Alegre):** LC municipal 1.077 de 23/07/2026 + Decreto 23.895 de 28/07/2026. 95% à vista e 90% parcelado de multa e juros de ISS; adesão de 01/08 a 21/12/2026 em `adesaopoaiss.portoalegre.rs.gov.br`; parcela mínima de 80,00 PJ; última parcela até dezembro/2026; adesão importa confissão irrevogável e desistência de ações. Optante do Simples só pode aderir se o débito já foi transferido ao município (art. 2º, §4º).
- **Simples:** opção 2027 encerrada em 15/10; regularização de pendência de opção indeferida e adesão ao regime regular de IBS/CBS até **30/10** (notícias da RFB de 13/10 e 16/10).

Nota técnica para as próximas rodadas: nesta sessão o `WebFetch` ficou com DNS antigo e falha nos domínios liberados — as leituras oficiais saíram por `curl`. Dentro de `www8.receita.fazenda.gov.br` as páginas `TelaLegislacao.aspx`, `Agenda.aspx` e `TodasNoticias.aspx` derrubam a conexão, mas `NoticiaCompleta.aspx` abre; a listagem mensal em `www.gov.br/receitafederal` funciona. Falta liberar `consumo.tributos.gov.br`.
