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
