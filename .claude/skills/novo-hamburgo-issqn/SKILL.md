---
name: novo-hamburgo-issqn
description: Passo a passo do ISSQN de Novo Hamburgo/RS (clientes 261 Giatech e 197 ASBBM) no Atende.Net / IPM Escrita Fiscal (WEF): protocolar Serviços Prestados e Tomados, emitir o carnê e conciliar com o Portal Nacional. Use no fechamento mensal de clientes com inscrição em Novo Hamburgo.
---

# ISSQN Novo Hamburgo/RS (IPM Atende.Net, Escrita Fiscal WEF), fluxo validado em 04/10/2026 (competência 09/2026, cliente 261)

Fonte: gravação de tela da Fernanda (04/10/2026, 2m55s) + PDFs salvos no Drive + planilhas do Portal Nacional.
Login = CNPJ da empresa + senha própria de cada cliente (a Fernanda digita; nunca no chat nem no repositório).

## Diferença para Porto Alegre e São Leopoldo
Aqui **não vem nada pronto**: a declaração do mês fica `Em Digitação` e a Fernanda precisa **Protocolar** (Prestados e Tomados). O protocolo é o recibo oficial da prefeitura (vale como DECLARAÇÃO PREFEITURA `Enviado`). A guia só vira `Enviado` com envio comprovado pelo G-Click.

## Passo a passo
1. `nfse-novohamburgo.atende.net/autoatendimento/servicos/nfse` > Login (CNPJ + senha) > **Acessar** (iPM fiscal) > Painel do Gestor (Escrita Fiscal).
2. **Declaração de Serviços Prestados** > Exercício 2026 > Consultar. A competência do mês aparece `Em Digitação` (valor contábil e ISS já preenchidos a partir das NFS-e emitidas).
3. Marcar a linha da competência > **Protocolar** > conferir a aba "ISS Novo Hamburgo" (serviço, alíquota, base e valor do ISS) > **Protocolar** > modelo do recibo **Detalhado** > Confirmar. Abre o PDF "Protocolo de Entrega - Serviços Prestados" (identificador WEF..., carimbo "Emitido por ... data hora"). Baixar.
4. Com a linha ainda marcada: **Emissão do Carnê > Carnê do ISSQN** > PDF Report.pdf (boleto Caixa com QR Code PIX). Baixar.
5. **Declaração de Serviços Tomados** > mesma consulta > competência `Em Digitação` > Protocolar. Abas: "ISS Retido Novo Hamburgo", "ISS Outros Municípios", "Sem Tributação". Sem retenção em Novo Hamburgo = sem guia ("Sem Recolhimento"). O ISS de outros municípios aparece só informativo (quem recolhe é o prestador). Confirmar > baixar o recibo (Recibo de Entrega > Imprimir).
6. Se o mês não teve nota, a competência fica "Sem Movimento" e não gera guia (ex.: 261 em agosto).

## Arquivos (Drive: 09_SETEMBRO... pasta 002 ARQUIVOS MUNICIPAIS)
- `261_Giatech_NovoHamburgo_MM.AAAA_DeclaraçãoMensalPrestados.pdf`
- `261_Giatech_NovoHamburgo_MM.AAAA_ISSQN.pdf` (carnê)
- `261_Giatech_NovoHamburgo_MM.AAAA_DeclaraçãoMensalTomados.pdf`
- Portal Nacional: `..._Emitidas.xlsx` e `..._Recebidas.xlsx` (pasta 003).

## Conciliação com o Portal Nacional (antes de liberar a guia)
- Prestados: nota a nota (número, valor, ISS 2%, tomador, data) = Emitidas (Situação normal, competência do mês). Guia = ISS total do protocolo.
- Tomados: notas do protocolo = Recebidas da competência. Atenção: nota de prestador de outra cidade pode estar no protocolo e não no Portal (a nota municipal de São Paulo, por exemplo), ou o contrário (nota do Portal com competência do mês anterior). Verificar número, data e valor.
- ISS de Outros Municípios = soma do ISS das Recebidas com incidência fora (Google SP 2,27 + Ecustomize Brasília 3,30 = 5,57), todas "Não Retido".
- Ler também no Emitidas as retenções federais (IRRF, PIS, COFINS, CSLL) para a apuração federal.

## Resultado 261 Giatech, 09/2026
- Prestados: 1 nota (nº 10, BETHA SISTEMAS LTDA, 25/09/2026, R$ 34.000,00, ISS 2% = R$ 680,00, não retido) = Portal = protocolo = **guia R$ 680,00**, venc. **20/10/2026**, documento 1017590/2026, Nosso Número 14/260000000894448-5.
- Tomados: 3 notas, R$ 483,40, ISS retido em Novo Hamburgo R$ 0,00, ISS outros municípios R$ 5,57.
- Federal (nota 10): IRRF R$ 510,00 e contribuições sociais retidas R$ 1.241,00 (PIS 221,00 + COFINS 1.020,00), conforme o Portal.

## Registro na Controle_Fiscal (TSV de 7 colunas, inline, aba Atualizações)
- DECLARAÇÃO PREFEITURA: `Enviado` com os protocolos de Prestados e Tomados (recibo da prefeitura comprova o envio).
- GUIA ISSQN: `Pendente` com o valor do carnê até haver G-Click.
- Se a aba tiver linhas SERVIÇOS PRESTADOS/TOMADOS: `Pendente` com o valor do documento, até a conferência XML x Domínio. Confirmar com a Fernanda quais linhas existem. Status só com confirmação explícita.
