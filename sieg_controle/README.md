# Controle da carteira (HüB SIEG)

Por que não é "só API": segundo o levantamento feito no portal em 05/10/2026, a API da SIEG cobre
XMLs e certificados digitais, **não** certidões, débitos nem parcelamentos. Esses dados só saem do
portal, por "Exportar Todos".

## Uso semanal (certidões, débitos, parcelamentos)

1. No HüB (iris.sieg.com → Pendências), exporte com **Exportar Todos** e salve em `exports/` com estes nomes:
   - `certidoes.xlsx` (Situação Fiscal → Certidões)
   - `diagnostico.xlsx` (Situação Fiscal → Diagnóstico Fiscal)
   - `parcelamentos.xlsx` (Parcelamentos)
2. Crie `carteira.csv` com a coluna `cnpj` (e, opcional, `nome`) da carteira da Fernanda.
   Hoje a Carteira do HüB só tem a de "GIAN"; a da Fernanda precisa ser criada lá ou mantida aqui.
3. Rode:

```bash
pip install pandas openpyxl requests
python controle.py --inspect   # confere colunas reais das exportações (rode na 1ª vez)
python controle.py             # gera relatorio_carteira.xlsx
```

O relatório tem as abas Resumo, Painel (uma linha por empresa) e uma aba por fonte, com as colunas `nivel` e `motivo`.

**Regras (por coluna, conferidas nas exportações de 05/10/2026):**
- Certidões: `Situação` = Irregular, ou `Data de Vencimento` já passada → IRREGULAR; vence em até `--dias` (padrão 30) ou situação diferente de Regular (ex.: "Outros", "Positiva com Efeitos de Negativa", "Indisponível para emissão") → ATENÇÃO.
- Diagnóstico Fiscal: `Situação` = "Não" → IRREGULAR. **Inferência não confirmada pela SIEG**: bate com os 19 irregulares do painel e com a CRFB-PGFN, mas confirme (constante `DIAG_IRREGULAR`).
- Parcelamentos: "Não validado – primeira parcela não paga" → ATENÇÃO; parcelamento ativo com `Data da Parcela` vencida e não quitado → IRREGULAR. A coluna `Data da Parcela` veio vazia nesta exportação, então o atraso de pagamento ainda não é detectado; `Consulta em Atraso` tem significado não confirmado e não gera alerta.
- A aba **Painel** traz uma linha por empresa, ordenada do pior para o melhor.
- Sem `carteira.csv`, o script usa todas as empresas das exportações (aviso na tela).

## Validade dos certificados digitais (API)

```bash
export SIEG_API_KEY=... SIEG_CLIENT_ID=... SIEG_SECRET_KEY=...
python sieg_api.py --carteira carteira.csv --dias 30
```

Ver ressalvas no cabeçalho de `sieg_api.py` (headers do JWT e credenciais ainda por confirmar com a SIEG).
Não commitar `carteira.csv`, `exports/` nem relatórios: contêm dados de clientes.
