---
name: brasilia-issqn
description: Passo a passo do ISSQN de Brasília/DF (cliente 71 Conte e, a confirmar, 264 Zenith Paracuru) no ISSNet On-Line / Nota Control da Secretaria de Economia do DF: protocolo de Serviços Prestados, Declaração de Não Movimento de Contratados, guia, Livro Fiscal e conciliação com o Portal Nacional. Use no fechamento mensal de clientes com inscrição no DF.
---

# ISSQN Brasília/DF (ISSNet On-Line, sistema Nota Control), fluxo gravado em 04/10/2026 (competência 09/2026, cliente 71)

Fonte: 4 gravações de tela da Fernanda (04/10/2026 15:21 a 15:25), PDFs e CSV salvos no Drive, Portal Nacional.
Login e senha são da Fernanda (não vão ao chat nem ao repositório). Site: `iss.fazenda.df.gov.br/online`.

## O que é diferente
- Não existe guia quando todo o ISS foi **retido pelo tomador**: o protocolo de Prestados mostra o Quadro Resumo e a guia não é emitida.
- Brasília usa dois documentos: **Protocolo de Entrega: Serviços Prestados** (Relatório Fechamento Prestados) e **Declaração de Não Movimento** de Serviços Contratados (tomados), quando não há o que declarar.
- Cada empresa é escolhida no topo da tela (inscrição municipal 0817205500132 para o 71) e a competência também (Setembro 2026).

## Passo a passo (o que aparece nas gravações)
1. Entrar no ISSNet, escolher a empresa e a competência na barra superior ("Competência: Setembro 2026").
2. Menu **Declaração de Serviços Prestados**: o fechamento gera o **Protocolo de Entrega: Serviços Prestados** (tela `RelFechamentoPrestados.aspx`, botões Imprimir / Enviar por Email). Imprimir para PDF. Atenção: os cliques do fechamento em si não aparecem nas gravações (elas começam com o relatório pronto).
3. Menu **Declaração de Serviços Contratados**: sem serviços a declarar, sai a **Declaração de Não Movimento** (`DeclaracaoNaoMovimento.aspx`, texto "Declaramos que no mês de ... a empresa ... não teve movimento econômico"). Imprimir para PDF.
4. **Guias de Recolhimento > Emissão de Guia**: escolher o tipo da declaração (Serviços Contratados ou Serviços Prestados), mês e ano. A tela "Movimentação Mensal" lista as declarações do mês (data de geração, vencimento, status da guia, ícones de Não Movimento e Protocolo). Se não há ISS a pagar, não há guia (vencimento e status ficam em branco).
5. **Livro Fiscal > Emitir Livro Fiscal**: Tipo do documento Livro Fiscal, Serviços Prestados, Data Inicial 01/MM/AAAA e Data Final (último dia), Gerar e Exportar XLS, CSV ou TXT. O CSV traz por nota: tomador, valor, alíquota, imposto retido, tributado no município, PIS, COFINS, CSLL, IRRF, INSS e item da LC 116.

## Arquivos (Drive: 09_SETEMBRO > 002 ARQUIVOS MUNICIPAIS)
- `71_Conte_Brasília_MM.AAAA_DeclaraçãoMensalPrestados.pdf` (protocolo)
- `71_Conte_Brasília_MM.AAAA_DeclaraçãoMensalTomados.pdf` (não movimento)
- `71_Conte_Brasília_MM.AAAA_LivroFiscalPrestados.csv` (em 04/10 foi salvo sem extensão: `..._09.2026_LivroFiscalPrestados`; renomear com `.csv`)
- Os PDFs do Nota Control saem como imagem ("Impressão"): para ler, renderizar as páginas (pdftoppm) e olhar a imagem.

## Como ler o Quadro Resumo (página 2 do protocolo)
Colunas "Sem Retenção Na Fonte" e "Com Retenção Na Fonte", por "Tributado no Município" e "Tributado Fora do Município".
- Tudo em "Com Retenção" e "Sem Retenção" zerada: `Sem Recolhimento (Retenção Integral)`, valor 0,00, e o ISS apurado vai só na observação.
- Valor em "Sem Retenção": é o que o cliente paga; guia `Pendente` até a comprovação do G-Click.

## Conciliação com o Portal Nacional
- Prestados: nº de notas, valor bruto e ISS do protocolo = Emitidas do mês (normais). Separar "no município" (Brasília/DF) e "fora" (demais).
- Recebidas: só vale ISS marcado "Retido pelo Tomador" (esse o cliente recolhe, ao município de incidência). Notas de prestadores do DF com ISS "não retido" conferir se a lei do DF exige retenção.
- Retenções federais (IRRF e contribuições) saem nas notas e no Livro Fiscal; levar para a apuração federal.

## Resultado 71 Conte, 09/2026
- Protocolo: 42 notas, R$ 1.091.077,54 = Portal. Tributado no município (DF): R$ 972.981,50, ISS R$ 46.949,88; fora do município: R$ 118.096,04, ISS R$ 5.603,74 (Portal 5.603,75, 1 centavo de arredondamento). Total ISS R$ 52.553,62. Tudo com retenção (tomador Caixa Econômica Federal); sem retenção R$ 0,00. Sem guia.
- Tomados (DF): Declaração de Não Movimento. Mas o 71 retém ISS de R$ 39,43 de uma nota de prestador de fora (RIPA Arquitetura nº 153, R$ 1.971,36, 2%): a Fernanda emitiu a guia de **Jundiaí/SP** (GISS Online, nº 00026073855, competência 09/2026, venc. 26/10/2026) e salvou como `71_Conte_Jundiaí_09.2026_ISSQNTomados.pdf`. Atenção: o Portal mostra "Município de Incidência: São Paulo/SP" nessa nota, e o código da chave de acesso (3525904) é de Jundiaí; conferir onde o serviço foi executado (item 7.11, decoração) antes de dar o assunto por encerrado.
- Federais pelas notas: IRRF R$ 52.371,72 e contribuições retidas R$ 10.910,78.

## Registro na Controle_Fiscal (TSV de 7 colunas, inline, aba Atualizações)
- SERVIÇOS TOMADOS: `Sem movimento`, 0,00, `Declaração de Não Movimentação (Contratados) <data>.`
- SERVIÇOS PRESTADOS: `Pendente`, valor total do protocolo, `... (42 notas) — falta conferência XML x Domínio.`
- GUIA ISSQN: `Sem Recolhimento (Retenção Integral)`, 0,00, ISS apurado como prestador (DF e fora) só na observação.
- GUIA ISSQN FORA MUNICÍPIO: é a guia que o próprio cliente paga como **tomador** de prestador de fora (ex.: Jundiaí R$ 39,43). `Pendente` com o valor da guia até o G-Click. Não confundir com o ISS que os tomadores dele retêm nas notas emitidas por ele (esse vai na observação da GUIA ISSQN).
- DECLARAÇÃO PREFEITURA: `Enviado` com o protocolo de Prestados e a Não Movimento, depois da confirmação explícita da Fernanda (regra a registrar aqui quando ela confirmar).

## Cliente 264 Zenith Paracuru (sem notas emitidas), 09/2026
Quando o Portal não tem Emitidas, gerar no ISSNet as duas **Declarações de Não Movimento** (Serviços Prestados e Serviços Contratados), salvar como `264_Zenith_Brasília_MM.AAAA_DeclaraçãoMensalPrestados.pdf` e `..._Tomados.pdf`. TSV: SERVIÇOS TOMADOS `Sem movimento` 0,00; DECLARAÇÃO PREFEITURA `Enviado` (Não Movimentação Contratados/Prestados, data); GUIA ISSQN `Sem movimento` 0,00 ("Sem movimento econômico declarado (Tomados e Prestados) — sem guia gerada."). Regra confirmada pelo registro de agosto (05/09/2026) e de setembro (04/10/2026).
