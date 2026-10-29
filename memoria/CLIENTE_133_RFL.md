# Cliente 133 — RFL SISTEMAS S/A (preparação 09/2026, 17/10/2026)

## Cadastro
- CNPJ 87.828.430/0001-84, Porto Alegre/RS, IM 525456-2-8, **Lucro Real**, não contribuinte de ICMS. CNAE 6203100; secundários 6204000 e 6810202 (aluguel de imóveis próprios). Sócios: Guilherme Guila Sebben (diretor) e Mario Guilherme Sebben (presidente). Grupo com CC&D (18) e ILS.
- **Sem certificado no PC** (cliente envia as notas; Portal Nacional não é baixado pelo robô). Atividade real: **aluguel de terreno em Pelotas/RS, R$ 700,00/mês** (CFOP 5-949) + rendimentos de CDB. Sem NFS-e de prestados.
- PIS/COFINS **não cumulativo** (aluguel 1,65%/7,6%; financeira 0,65%/4%), cód. 6912 (PIS) e 5856 (COFINS). Historicamente quitados por PER/DCOMP.

## Controle_Fiscal Set2026 (export 17/10 ~22:48)
CERTIFICADO `Não se aplica`; REINF `Enviado` (R-2099 12113783-10-2099-2609-12113783, 04/10); DECLARAÇÃO PREFEITURA `Enviado` (robô, 01/10); GUIA ISSQN `Sem movimento` 0 (06/10). **Em branco:** SERVIÇOS TOMADOS, SERVIÇOS PRESTADOS, DARF PIS, DARF COFINS, DARF IRPJ, DARF CSLL, SPED CONTRIBUIÇÕES (16/11).

## O que já existe (17/10)
- DCTFWeb 09/2026 entregue 14/10/2026 11:03 (recibo 0000050000538306277; o PDF não traz os valores no texto).
- FAT 133 (set): aluguel 700,00, financeira 1,38, IRRF s/ rendimentos 0,29; PIS 11,56 e COFINS 53,26 (conferem: 700 x 1,65% + 1,38 x 0,65% e 700 x 7,6% + 1,38 x 4%); observação de set em branco (compensação não lançada).
- Tomados (relação do DecWeb 09/2026): 1 NFS-e, nº 18, 11/09, Shaiane Pires Duarte Quincoses (MEI), R$ 300,00, ISS 0. Domínio ainda não salvo.
- Rendimentos (CONTROLE | Rendimentos, 3ºTRIM 2026): **133 não consta na aba** (já havia a dúvida em PENDENCIAS). FAT: IRRF s/ rendimentos jul 0,06 + ago 0,10 + set 0,29 = 0,45.

## Pontos de atenção
1. **Compensação:** aba Compensações só tem créditos até 10/2024 e o saldo é R$ 5,78 (COFINS 10/2024, após PERDCOMP 027). PIS 11,56 + COFINS 53,26 = 64,82 de set: ou há outro crédito, ou paga DARF (venc. 23/10).
2. **PIS 08/2026 (11,55, venc. 25/09):** a Controle (Ago2026) está `Pendente`; o FAT diz "COMPENSADO", mas o PERDCOMP 027 (20/09) lista só COFINS e usou 54,63 do crédito (60,41 - 5,78): não bate com 11,55 + 53,22. Confirmar se o PIS de agosto foi quitado.
3. **IRPJ/CSLL (Lucro Real) 3º tri:** sem Domínio/LALUR nesta rodada e sem informação de resultado dos tris anteriores na Controle; precisa balancete e apuração.
4. Movimento do cliente: `Movimento RFL 09-2026.zip` (Drive, 09/10) não aberto (extrato Banrisul do aluguel/CDB).

## Pedidos à Fernanda
Domínio de 09/2026 do 133 (Entradas, Saídas/Serviços, Resumo/Demonstrativo, balancete/apuração Lucro Real), confirmação do PIS de agosto e da fonte de crédito para setembro, e se o 133 entra no controle de Rendimentos.

## DecWeb retificadora 1 + Domínio (18/10/2026 ~10:30, conferido)
- **DecWeb (fase T --retificadora --enviar, rodada ~10:25):** `52545628_202609_NFSE_ServTomados.xlsx` agora diz `Competência 09/2026 Retificadora 1` com **2 notas tomadas, R$ 1.552,35, ISS 0**: nº 18 (11/09, Shaiane Pires Duarte Quincoses, MEI, R$ 300,00, fora do município) e **nº 1051 (05/10, Officecont, R$ 1.252,35, Simples, tributação no município, sem retenção)**. Antes (original) só a nº 18. O zip foi atualizado. **O PDF `DeclaraçãoMensal` retificado NÃO apareceu no Drive** (o do Drive é o original de 01/10 17:37, 7.530 bytes): conferir a pasta local do robô / sincronização e o recibo da retificadora.
- **Domínio Saídas:** 701,38 = aluguel 700,00 (CFOP 5-949, clientes diversos) + 1,38 rendimento (BANCO): = FAT.
- **Domínio Entradas (NFS-e, esp. 39, acum. 800):** só a **1051 Officecont R$ 1.252,35** (entrada 30/09). **A nº 18 (MEI, R$ 300,00) não está no Domínio**: DecWeb 1.552,35 x Domínio 1.252,35 = 300,00.
- **Resumo:** PIS 11,56 + COFINS 53,26 = 64,82 (= FAT); IBS, CBS e ISS zerados.
- Serviços_133 (relatório do Domínio) e balancete/LALUR (Lucro Real) não foram salvos.

## NFS-e nº 18 (Shaiane, MEI) — localizada na pasta do cliente (18/10/2026)
`Movimento RFL 09-2026` (001): `Shaiane NF 18.pdf` (DANFSe) e `Comprovante Shaiane NF 18.pdf` (recibo Banrisul). **Nota real e paga:** NFS-e 18, emitida 11/09/2026, chave 43144072250455947000165000000000001826090455843397 (= a do DecWeb), prestador 50.455.947 Shaiane Pires Duarte Quincoses (MEI, Pelotas/RS), tomador RFL Sistemas S/A, CNAE/serv. 07.01.04, "Levantamento de todo hospital para projeto arquitetônico", R$ 300,00, ISS não retido (local Pelotas), sem IBS/CBS. Pagamento: Banrisul PIX/transferência 14/09/2026 18:23, "PGTO NF 18", R$ 300,00, NSU 20260914001960240786.
**Conclusão:** despesa real da RFL, falta lançar no Domínio (Entradas/Serviços tomados, acumulador 800, R$ 300,00); depois o Domínio fecha em 1.552,35 = DecWeb retificadora. Classificação contábil (despesa x custo do projeto) é decisão da Fernanda.

## Pasta `_133` e dados para lançar a NFS-e 18 (18/10/2026)
Criada `_133` em `007 ARQUIVOS SIEG` (id 1FTDUA311NpqBf9WmDbihK4masg9ShjhN, ao lado da `_71`; não existia pasta "importações _133") com cópias de `Shaiane NF 18.pdf` e `Comprovante Shaiane NF 18.pdf` (as originais continuam em `Movimento RFL 09-2026`). Dados do lançamento: NFS-e 18, emissão 11/09/2026, fornecedor 50.455.947/0001-65 (Shaiane Pires Duarte Quincoses, MEI, Pelotas/RS, IBGE 4314407), valor contábil 300,00, CFOP 1-933, acumulador 800, ISS 0 não retido, sem IBS/CBS, sem crédito de PIS/COFINS (mesmo tratamento da 1051).

## Conferência após lançar a NFS-e 18 (18/10/2026 10:39)
- **Entradas (10:39):** cód. 13 NFS-e 18 (11/09, série 70000, esp. 39, Shaiane, CFOP 1-933, acum. 800, R$ 300,00, ISS/IRRF/CRF 0) + cód. 12 NFS-e 1051 Officecont (R$ 1.252,35) = **1.552,35 = DecWeb retificadora 1**. SIEG: CNPJ do 133 só tem a pasta `Servico Tomado` (sem `Entrada`): sem NF-e de produtos.
- **Saídas (10:39):** 701,38 (700,00 + 1,38) inalterado = FAT.
- **Declaração mensal (PDF baixado):** `Retificadora 1`, recebida 18/10/2026 10:27:59, autenticação 6A BC E9 BB 66 CE 34 F1 7D A4 98 A7 FE 4B 6A 9C, base 0, total a recolher 0,00 (ISS zero, bate).
- **Resumo (`Empresa 133`, 10:25) é anterior ao lançamento**: PIS 11,56 / COFINS 53,26, IBS/CBS/ISS 0. Esperado inalterado (sem crédito); regerar para confirmar.
- Pendentes: PIS 08/2026, crédito/pagamento de set (PIS 11,56 + COFINS 53,26, venc. 23/10), IRPJ/CSLL (Lucro Real), Serviços_133, rendimentos, SPED 16/11.

## PIS/COFINS 09/2026 do 133 — compensação parcial e guia (18/10/2026 ~11:00, conferido)
- **PER/DCOMP** `29817.01875.181026.1.3.04-9972` (PDF `DEC PERDCOMP 027.pdf` na pasta de compensações, mas é a **028**; a 027 é de 20/09): crédito COFINS 10/2024 (DARF 07.01.24311.6620518-4, cód. 5856-01, pago 11/11/2024, R$ 180,53; crédito inicial 114,00), saldo original 5,78, Selic 25,44% = **7,25**, saldo do crédito = 0,00. Débito: COFINS 09/2026 (5856-01, venc. 23/10), DCTFWeb recibo 050000540031181 (18/10).
- **Guia** `133_RFL_PortoAlegre_09.2026_PIS-COFINS.pdf`: doc 07.16.26291.8027591-4, venc. 23/10, **COFINS 46,01 (5856) + PIS 11,56 (6912) = 57,57** (recibo declaração 50000540031241). COFINS 53,26 - 7,25 = 46,01 = FAT. G-Click `Darf Pis / Cofins` concluída 18/10/2026 10:58 (fernanda.officecont).
- **FAT:** na aba Compensações a linha 028 repete o nº da 027 (`38252.90637.200926.1.3.04-0560`): o correto é `29817.01875.181026.1.3.04-9972`. A observação de set diz "COMPENSADO PARTE DO COFINS" (PIS não foi compensado).
- **Crédito de 10/2024 esgotado:** outubro/2026 e seguintes viram DARF cheio (~R$ 64,8/mês) salvo novo crédito.
- PIS de agosto (11,55): a DEC da 027 (20/09) não está na pasta; crédito usado 60,41 < débitos de agosto (53,22 + 11,55 = 64,77): conferir.

## IRPJ/CSLL do 3ºTRIM — análise de 29/10/2026 (véspera do vencimento)
- **Controle_Fiscal (Set2026):** DARF IRPJ e DARF CSLL `Pendente`, **sem valor**, observação "Lucro Real: aguarda a contabilidade liberar a apuração do 3º trimestre. Venc. 30/10/2026". Todo o resto de setembro está fechado: Declaração Prefeitura `Enviado` (retificadora 1), ISSQN `Sem movimento`, PIS 11,56 e COFINS 46,01 `Enviado` (guia 07.16.26291.8027591-4, G-Click 18/10 10:58). Falta só o SPED (16/11).
- **Busca no Drive em 29/10: não existe balancete, LALUR nem apuração de IRPJ/CSLL do 133 em 2026.** Também não há guia de IRPJ/CSLL de trimestres anteriores de 2026 no Drive.
- **O FAT do 133 não tem seção de IRPJ/CSLL** (é Lucro Real: o imposto sai do balancete/LALUR, não do FAT). O FAT só controla aluguel, receita financeira e PIS/COFINS não cumulativo.
- **Resumo dos Impostos do Domínio (18/10 10:57):** só PIS 11,56 e COFINS 46,01; IBS, CBS e ISS zerados. **Nada de IRPJ/CSLL** — o módulo fiscal não apura Lucro Real.
- **Ordem de grandeza:** receita do trimestre = aluguel 700,00 × 3 = 2.100,00 + receita financeira (jul 0,40 + ago 0,54 + set 1,38 = 2,32) = **2.102,32**; despesas conhecidas: NFS-e tomadas 1.552,35 no mês de setembro (Officecont 1.252,35 + Shaiane 300,00) e os meses anteriores. Com esse porte, o resultado do trimestre pode ser **prejuízo ou lucro muito pequeno** — mas isso **só o balancete diz**.
- **Conclusão:** é pendência da **contabilidade**, não do fiscal, e não há documento nenhum para apurar daqui.
- **29/10/2026 (decisão da Fernanda):** DARF IRPJ e DARF CSLL do 3ºTRIM gravados na fila como **`Em andamento`** (pós-fechamento), aguardando a contabilidade. Sem valor, com o contexto na observação. Cobrar o balancete/LALUR do 3º trimestre; se o resultado for prejuízo, pedir confirmação por escrito e registrar sem guia.
