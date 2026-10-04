# Plano para agilizar o fechamento de 10/2026 (registrado em 04/10/2026)

Objetivo da Fernanda: no fechamento de outubro, fazer tudo com agilidade. Base: o que foi aprendido no fechamento de 09/2026.

## Ordem sugerida do mês (primeira semana útil)
1. **Dia 1:** Tacom (138 e 263 ISSQN POA, regra de 02/10) e DecWeb dos demais de POA em lote (`decweb_login.py --fase T --enviar`); 186 só depois que a cliente enviar os documentos.
2. **Dia 1 a 2:** Portal Nacional em lote para os clientes com certificado (`portal_nacional_download.py`), depois `conciliacao.py` (já corrigido para nota de substituição). Rodar também para os que não geraram planilha, e conferir no log `Emitidas/Recebidas sem movimento` (sempre com login confirmado pelo CNPJ).
3. **Dia 2 a 3:** prefeituras fora do DecWeb com as skills: `sao-leopoldo-issqn` (126), `novo-hamburgo-issqn` (261 e 197), `brasilia-issqn` (71 e 264); Montenegro (247), Rio (185), PROGEST (227) e São Paulo (a gravar/mapear).
4. **Federais:** retenções nas Recebidas e Emitidas do Portal (IRRF, contribuições, INSS) para REINF e DARF; REINF vence dia 15.
5. **TSV para a Controle:** um bloco só por município, com evidência (recibo, DMS, print do G-Click).

## O que pedir ao cliente antes de fechar
- Clientes sem certificado A1 neste PC (2, 18, 26, 133, 138, 173, 177, 185, 209, 248, 263): relação das notas recebidas do mês e se houve retenção federal (só federal). Mandar nos dias 1 e 2 do mês, não no meio da semana.
- 186: documentos do mês (dispara DecWeb e federais juntos).
- 257: confirmar retenção das notas de maior valor antes de gerar a guia.

## Ganhos já prontos para usar
- Skills por município (acima) com os valores de conferência e o TSV padrão.
- Agente de apoio para ler várias planilhas do Portal ao mesmo tempo (levantamento de retenção federal em minutos).
- Regras fixas: DMS de São Leopoldo e protocolos de Novo Hamburgo/Brasília valem como Declaração Prefeitura `Enviado`; guia só `Enviado` com G-Click.

## A melhorar em outubro
- Gravar São Paulo, Montenegro, Rio e PROGEST uma vez e virar skill (menos conversa, mais execução).
- Renomear o Livro Fiscal de Brasília com `.csv` ao salvar.
- Instalar/renovar certificados A1 antes do dia 1 (258 vence em 14/10; 155 em 27/10; 71 em 13/11).
- Salvar logs do robô no Drive (sem senhas) para eu conferir sem pedir `resultados.csv`.
- Atualizar o memória a cada rodada (PENDENCIAS, PROCESSO e snapshot no Drive).
