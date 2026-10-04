---
name: sao-leopoldo-issqn
description: Passo a passo do ISSQN de São Leopoldo/RS (cliente 126 Tatsch & Leite): conferir o DMS gerado pelo ADN, gerar o faturamento, imprimir a guia e conciliar com o Portal Nacional. Use no fechamento mensal do 126 ou de outro cliente com inscrição em São Leopoldo.
---

# ISSQN São Leopoldo/RS (SEMFA), fluxo validado em 04/10/2026 (competência 09/2026)

Fonte: gravação de tela da Fernanda (04/10/2026) + DMS/guia de 08/2026 e 09/2026 no Drive. Cliente 126 TATSCH & LEITE CENTRO ODONTOLOGICO S/S, CNPJ 10.914.420/0001-37, contribuinte 445777, Lucro Presumido, ISS 2% por nota (código 04.12.01).
Nunca digitar senhas no chat nem gravá-las no repositório. O login é da Fernanda no próprio Chrome.

## Como funciona
- Não existe envio manual da declaração. A **DMS é gerada sozinha pela integração com o ADN** (Portal Nacional): aparece como transmissão "NFSe (ADN)" com data no início do mês (09/2026: nº 1053665, 02/09/2026).
- O que a Fernanda faz é **gerar o faturamento** (apuração do imposto a recolher) e **imprimir a guia** (Carnê Consolidado ISS).
- Regra de 17/09/2026: o Livro Fiscal Eletrônico (DMS) salvo na pasta 002 é a evidência da linha DECLARAÇÃO PREFEITURA (`Enviado`). A GUIA ISSQN só vira `Enviado` com envio comprovado pelo G-Click.

## Passo a passo no portal da prefeitura
1. Portal da prefeitura > Serviços > Empresa > ISSQN - Prestadores > **NFS-E Padrão Nacional** > card **"Relatório, Apuração e guia Nota Fiscal Nacional"**. Abre a tela **Consulta DMS** (grp.saoleopoldo.rs.gov.br).
2. Contribuinte: TATSCH E LEITE [445777]. Competência `2026/09` a `2026/09`. **Localizar**.
3. Clicar na linha da transmissão (competência 2026/09, "NFSe (ADN)"). Aparecem 3 botões: Declaração Mensal de Serviços - DMS, Apuração de Imposto à recolher, Livro Fiscal Eletrônico (DMS).
4. **Apuração de Imposto à recolher** > Tipo **Prestador** > marcar "Selecionar todos os registros" (sem marcar dá o erro "Selecione pelo menos uma nota para realizar o faturamento") > **Gerar faturamento** > confirmar "Confirma a geração de faturamento para N notas?" > Sim.
5. Abre a Declaração Mensal de Serviços - DMS, aba Imposto: linha `ISSV(02)-2026/9-0 (R)`, vencimento 15/10/2026, base de cálculo, valor, situação `Lançado`. Conferir com o Portal.
6. Ícone de impressora > **Carnê Consolidado ISS** > Data de pagamento (o vencimento) > **Imprimir** > baixar o PDF da guia.
7. Tipo **Tomador**: se não houver retenção aparece "Sem notas fiscais para gerar faturamento". Não há guia de tomador (as notas tomadas vêm marcadas N, não retido: o prestador recolhe).
8. **Livro Fiscal Eletrônico (DMS)**: PDF de 12 páginas, com "Valores Totais" do prestador e do tomador. Baixar.

## Arquivos (Drive: 09_SETEMBRO > 002 ARQUIVOS MUNICIPAIS)
- `126_Tatsch&Leite_SãoLeopoldo_MM.AAAA_NFSE_Prest_Tomad.PDF` (Livro Fiscal DMS)
- `126_Tatsch&Leite_SãoLeopoldo_MM.AAAA_ISSQN.PDF` (guia)

## Conciliação com o Portal Nacional (antes de liberar a guia)
- Emitidas do mês (competência MM/AAAA, Situação normal): quantidade, valor bruto e ISS 2% devem bater com "Valores Totais" do prestador no DMS. Notas do mês seguinte ficam fora.
- Recebidas: só ISS **retido** gera obrigação; no 126 todas vêm "Não Retido".
- Valor da guia = Valor ISS do prestador no DMS (bater centavo a centavo).
- 09/2026: Portal e DMS batem em 209 notas, R$ 153.662,41, ISS R$ 3.073,23. Guia R$ 3.073,23, venc. 15/10/2026, Nosso Número 14400000001431673-7 (`ISSV 2026: 9/0`).
- 08/2026 (referência): 182 notas, R$ 109.035,74, guia R$ 2.180,70.

## Registro na Controle_Fiscal (TSV de 7 colunas, inline, aba Atualizações)
- DECLARAÇÃO PREFEITURA: `Enviado`, obs. `Livro Fiscal DMS (SEMFA) <data de geração> — relatório do que consta na Prefeitura.`
- GUIA ISSQN: `Pendente` com o valor da guia até haver G-Click; obs. `Guia gerada, sem G-Click/print de envio — confirmar com a Fernanda.`
- Status só com confirmação explícita dela.
