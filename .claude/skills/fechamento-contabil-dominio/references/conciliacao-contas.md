# Conciliação conta a conta (Etapa 5)

Apoia a Etapa 5 do `SKILL.md`. Conciliar é provar o saldo de cada conta com um suporte que não seja o
próprio razão. Use o que as etapas anteriores já juntaram — não peça de novo o que está no pacote da
Etapa 1, no mapa ou nas planilhas de controle.

## Ordem dos grupos e suporte de cada um

Siga esta ordem: os grupos de cima alimentam a conferência dos de baixo (ex.: o banco conciliado ajuda a
explicar fornecedores e tributos pagos). Pule o grupo que o cliente não tem, dizendo que não tem.

| # | Grupo | Suporte (fonte) | O que precisa bater / o que olhar |
|---|---|---|---|
| 1 | **Integridade** | Balancete; mapa (aba `Saldos`) | D = C; sintéticas = soma das analíticas; saldo invertido explicado; abertura = saldo final do mês anterior no mapa |
| 2 | **Bancos e aplicações** | Extratos (pacote, item A); extrato/informe da aplicação | Saldo contábil = saldo final do extrato em cada conta. A Etapa 3 já fechou o movimento — aqui confirma o saldo e acha lançamento que entrou depois (integração, ajuste) |
| 3 | **Caixa** | Não há extrato | Saldo negativo é erro; saldo alto e parado é ponto a perguntar ao colaborador |
| 4 | **Clientes** | Relatório de saídas/serviços (item F); recebimentos no banco; relação de títulos em aberto, se o cliente tiver | Saldo = notas emitidas ainda não recebidas. Saldo antigo sem movimento, saldo credor (adiantamento ou recebimento sem nota) → `conciliacao-clientes` |
| 5 | **Tributos a recuperar / compensar** | GATILHO da REINF (retenções sofridas); notas com retenção; apuração (item F) | Retenção sofrida lançada como ativo e depois compensada; crédito de PIS/COFINS (Real) com origem; saldo que só cresce sem compensação é ponto a explicar |
| 6 | **Imobilizado** | Relatório do patrimônio do Domínio; notas de compra/venda de bens (pacote) | Saldo de bens e de depreciação acumulada = relatório do patrimônio; aquisição/baixa do mês registrada → `ativo-imobilizado-depreciacao` |
| 7 | **Fornecedores** | Relatório de entradas/serviços tomados (item F); pagamentos no banco | Saldo = notas recebidas ainda não pagas; saldo devedor (adiantamento ou pagamento sem nota) → `conciliacao-fornecedores` |
| 8 | **Obrigações trabalhistas** | Folha do DP (`003_FOPAG`: relação da folha, FGTS); comprovantes (item B) | Salários e pró-labore a pagar zerados depois do pagamento; INSS, IRRF e FGTS a recolher = guias da competência; provisões de férias e 13º geradas |
| 9 | **Tributos a recolher** | Apuração do Domínio (item F); comprovantes (item B) | Em aberto só o da competência atual (vence no mês seguinte); saldo de competência antiga = não pago ou pago sem baixa — descobrir qual |
| 10 | **Retenções a recolher** | GATILHO da REINF (detalhe com códigos e valores); comprovantes (item B) | Competência `COM RETENÇÃO` com as retenções no passivo e depois pagas; `SEM MOVIMENTO` com retenção no contábil é divergência a explicar |
| 11 | **Parcelamentos e débitos** | Situação fiscal federal, estadual e municipal (itens C, D, E) | Todo parcelamento/débito dos relatórios está no passivo e vice-versa; parcela do mês paga e baixada; saldo do parcelamento coerente com o relatório |
| 12 | **Empréstimos e financiamentos** | Contrato e extrato/demonstrativo do banco (item G) | Saldo devedor = demonstrativo do banco; juros do mês em despesa; separar curto e longo prazo se o cliente fizer assim |
| 13 | **Sócios, mútuo e lucros** | Aba Lucros distribuídos do artefato Controle Contábil (planilha DIST LUCROS); banco | Lucros pagos no banco = lucros registrados; mútuo com saldo explicado; pagamento a sócio sem classificação definida é ponto a perguntar |
| 14 | **Patrimônio líquido** | Contrato social (pasta `CADASTRO`) | Capital social = contrato; movimento de lucros/prejuízos acumulados explicado |
| 15 | **Transitórias / "a regularizar"** | Mapa (aba `Saldos`, alertas); pendências das Etapas 3 e 4 | Devem zerar; o que sobrar precisa da pendência explicada |
| 16 | **Resultado do período** | Balancete do mês anterior e do mesmo mês do ano anterior; relatórios do fiscal | Receita já cruzada na Etapa 4; despesa recorrente que faltou ou duplicou; variação grande com explicação ou pergunta |

Notas por regime: no Simples, os tributos a recolher do grupo 9 são o DAS (mais o INSS patronal
quando o anexo exigir, ver `Perfil`); no Presumido, PIS/COFINS mensais e IRPJ/CSLL trimestrais; no Real,
PIS/COFINS não cumulativos e as estimativas ou o balanço de IRPJ/CSLL. A conferência do valor em si
desses tributos é da Etapa 6 — aqui se concilia o saldo da conta (apurado − pago = em aberto).

## Diferenças: onde corrigir

Toda diferença ≠ 0 entra no papel de trabalho. O colaborador decide o que aceitar; você não descarta
diferença por achar pequena.

| Causa | Onde corrigir |
|---|---|
| Erro de módulo (nota, folha, bem, acumulador) | Etapa 4: corrigir no módulo e reintegrar |
| Erro na importação bancária | Etapa 3: corrigir a linha e reimportar |
| Lançamento que falta e não é de módulo | Planilha `AJUSTES {NNN} {MM-AAAA}.xlsx` (a mesma da Etapa 4), com histórico e motivo |
| Documento que não existe | Pendência com o cliente (`pendencias-fechamento-cliente`) |
| Diferença que vem de mês já fechado | Pendência herdada — não lance correção de período anterior sem decisão do colaborador (e do revisor, se for o caso) |

## Papel de trabalho

`CONCILIACAO {NNN} {MM-AAAA}.xlsx`, em `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}`. Uma aba `Contas`, uma
linha por conta com saldo ou movimento:

| Coluna | Conteúdo |
|---|---|
| Grupo | Um dos grupos da tabela acima |
| Código Domínio / Conta | Código reduzido e nome |
| Saldo contábil | Saldo final no balancete da competência |
| Saldo do suporte | O que o suporte mostra |
| Diferença | Saldo contábil − suporte |
| Suporte | Documento e onde está (ex.: "extrato Banco X set/2026, 001/09_SETEMBRO") |
| Status | `Conciliada` · `Divergente` · `Pendência aceita` · `Sem suporte` |
| Explicação | Causa da diferença ou por que está sem suporte |
| Ação | O que fazer e onde (Etapa 3, Etapa 4, AJUSTES, cliente) |

Uma aba `Resultado` com as variações relevantes do período e a explicação de cada uma, e uma aba
`Rodadas` registrando cada rodada de correção (data, contas reconferidas, o que mudou). A Etapa 6
acrescenta a aba `Tributos` no mesmo arquivo.

`Sem suporte` não é o mesmo que conciliada: é conta cujo saldo ninguém consegue provar com documento —
vira pendência para o revisor ver.

## Checklist de saída da Etapa 5

- [ ] Balancete íntegro e abertura = saldos finais do mês anterior (ou diferença registrada como pendência herdada)
- [ ] Todos os grupos aplicáveis conciliados, na ordem, com a fonte do suporte de cada conta
- [ ] Nenhuma conta `Divergente`; `Pendência aceita` sempre com motivo
- [ ] Transitórias zeradas ou explicadas
- [ ] Variações relevantes do resultado explicadas ou perguntadas
- [ ] Ajustes importados e balancete final exportado depois da última rodada
- [ ] Papel de trabalho salvo em `005_CONTABIL RELATORIOS/{MM_MÊS}` do cliente
