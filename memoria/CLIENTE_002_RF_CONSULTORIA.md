# Cliente 2 — RF CONSULTORIA: dossiê para o fechamento

**Gatilho (pedido da Fernanda, 17/10/2026):** quando ela disser "fechamento da empresa #2" (ou "fechar a 2"), ler este arquivo, conferir a Controle_Fiscal
do mês e apresentar o que está mapeado (Portal Nacional, prefeitura, particularidades) e o que falta. Atualizar este dossiê a cada fechamento.
Fontes deste dossiê: Cadastro_Clientes e abas Jul/Ago/Set2026 da Controle_Fiscal (export de 17/10/2026), `PENDENCIAS.md`, log `PROCESSO_FECHAMENTO_09-2026.md`
(seções 28k e outras) e `RASCUNHOS_2026-10-05.md` (item 4). Não li nenhum PDF/XML do cliente 2 nesta rodada: o que está abaixo vem das anotações já registradas.

## Cadastro
- Nº **002** (na Controle aparece como 2), RF CONSULTORIA, CNPJ 02.210.396/0001-27, Porto Alegre/RS.
- CNAE principal 6810202 (aluguel de imóveis próprios); sem CNAE secundário. **Lucro Presumido**; contribuinte de ICMS: NÃO; IE isento/N/A.
- Sócios no cadastro: Ricardo Fernandes da Silva (sócio-administrador; contato do cliente, "RFS") e Bruna Freire Fernandes (sócia menor, assistida/representada).
- Portal Nacional (NFS-e): "Obrigatório (Padrão Nacional)".

## Particularidades já mapeadas
- **Sem certificado digital no PC do escritório:** linha CERTIFICADO DIGITAL = "CLIENTE ENVIA AS NOTAS | NÃO TEMOS ACESSO AO CERTIFICADO DIGITAL". O robô do Portal Nacional **não roda** para o 2 (fica entre os 11 sem certificado); as notas dependem do cliente. (?) Em ago/2026 a linha SERVIÇOS PRESTADOS diz "Nenhuma nota de serviços prestados no Portal Nacional (08/2026)": confirmar de onde veio essa consulta.
- **Receita de aluguéis:** até 09/2026 foi **valor fixo** (jul/2026: R$ 21.978,00, `Importado`; PIS R$ 142,86 e COFINS R$ 659,34 em jul, ago e no SPED de 08 = 0,65% e 3% sobre R$ 21.978,00). **A partir de 10/2026 passa a ser o faturamento mensal** (Ricardo Fernandes confirmou por e-mail em 09/10/2026, "sim, exatamente"; a Fernanda perguntou). Regra: **não repetir o valor dos meses anteriores; pedir ao cliente o valor do mês** e conferir com notas/recibos antes de apurar (FAT, PIS/COFINS, IRPJ/CSLL). A mensagem original da Júlia e a imagem do e-mail não foram vistas pela agente: confirmar contrato e valor anterior.
- **ISSQN de Porto Alegre (DecWeb):** só serviços tomados, sem ISS retido; receita R$ 0,00 e imposto R$ 0,00 → **GUIA ISSQN = `Sem movimento`** (sem guia) e **DECLARAÇÃO PREFEITURA `Enviado`** com o recibo (set: recibo 03/10/2026 11:16:19; ago: 01/09 18:44).
- **Serviços tomados recorrentes (dados da prefeitura/Controle):** Officecont (nota mensal; jul e ago R$ 879,30, nº 987 em ago) e **Freire Administração e Serviços Prediais Ltda** (CNPJ 10.420.067/0001-39; ago R$ 1.318,68, ainda sem a nota; set: nº 14263 de 14/09 e nº 14320 de 28/09, R$ 1.142,85 cada, total R$ 2.285,70, sem ISS). Pontos em aberto com o cliente: as duas notas de set têm o mesmo valor (conferir se são serviços distintos) e se houve retenção (IRRF, PIS/COFINS/CSLL, INSS). Rascunho do e-mail em `RASCUNHOS_2026-10-05.md` item 4 (**não enviado**).
- **REINF:** envia-se R-2099 "sem retenção" **provisório** até chegarem as notas (set: 04/10/2026 16:24, recibo 12139055-06-2099-2609-12139055; ago: 09/09/2026 14:30, recibo 11973431-06-2099-2608-11973431). Se a Freire (ou outro prestador) tiver retido, retificar com R-4020/R-2010. Em jul/2026 há também uma linha "R 4010 0,01" `Enviado` (origem não analisada).
- **SPED Contribuições:** 08/2026 transmitido em 04/10/2026 13:51:44 (Original, PIS 142,86 e COFINS 659,34); antes disso estava "sem arquivo na pasta". 09/2026 vence 16/11.
- Cadastro de aluguel: a atividade é locação de imóveis próprios; a presunção de IRPJ/CSLL do aluguel e o tratamento do valor variável devem ser **confirmados na legislação vigente antes de apurar** (recomendo verificar; não afirmei percentuais).

## Situação por competência (Controle_Fiscal, export de 17/10/2026)
| Linha | Jul/2026 | Ago/2026 | Set/2026 |
|---|---|---|---|
| REINF | Enviado | Enviado (R-2099) | Enviado (R-2099 provisório) |
| SERVIÇOS TOMADOS | Não Enviado (R$ 879,30) | Pendente (R$ 2.197,98: falta a Freire R$ 1.318,68) | em branco |
| SERVIÇOS PRESTADOS | Sem movimento | Sem movimento | em branco |
| RECEITA ALUGUEIS | Importado R$ 21.978,00 | Pendente | em branco |
| GUIA ISSQN | Sem movimento | Sem movimento | Sem movimento |
| DECLARAÇÃO PREFEITURA | Enviado | Enviado | Enviado |
| DARF PIS / COFINS | 142,86 / 659,34 Enviado | Enviado (venc. 25/09; G-Click 14/09) | em branco (venc. 23/10) |
| DARF IRPJ / CSLL | (trimestre) | n/a | em branco (venc. 30/10) |
| SPED CONTRIBUIÇÕES | Enviado | Enviado 04/10 | em branco (venc. 16/11) |
Observação: o log registra que há linhas de agosto ainda `Pendente` (2, entre outros): conferir se estão desatualizadas.

## Roteiro quando a Fernanda disser "fechamento da empresa #2" (próxima competência: 10/2026, feita em novembro)
1. Perguntar/pedir ao Ricardo: **valor do faturamento de aluguéis do mês** (regra nova), notas tomadas do mês (Officecont, Freire e outras), se houve retenção, notas emitidas pelo cliente (o Portal não é acessível sem certificado).
2. DecWeb Porto Alegre (robô, fases 1 a 3): declaração de tomados/prestados; receita zero → guia `Sem movimento`; usar a data impressa na guia se houver guia.
3. Conferir o que o Portal/prefeitura trazem de tomados (sem certificado, via relatório municipal da pasta `002 ARQUIVOS MUNICIPAIS`) e lançar/conciliar no Domínio antes de marcar Serviços Tomados `Importado` (regra de 06/10).
4. REINF: R-2099 só se não houver retenção; com retenção, R-4020 (e R-2010 se INSS) conforme a skill `conciliacao-retencoes-servicos-tomados`.
5. PIS/COFINS cumulativos sobre a receita do mês (0,65% e 3%): DARF dia 25 do mês seguinte (ago/2026 foi 25/09; confirmar o dia na guia); IRPJ/CSLL no fechamento do trimestre (próximo: 4º tri, vence em janeiro/2027); SPED Contribuições até o 10º dia útil... **conferir o prazo vigente** (09/2026 consta 16/11).
6. TSV de 7 colunas inline para a Controle; status só com confirmação; guia só `Enviado` com G-Click.
