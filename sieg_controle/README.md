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

O relatório tem uma aba de resumo, uma aba por fonte (só empresas da carteira, com a coluna `alerta`)
e uma aba "sem registro" com CNPJs da carteira que não aparecem na exportação.

**Limitação:** o layout das exportações não foi confirmado. O casamento usa o CNPJ/CPF encontrado em
qualquer célula da linha, e o `alerta` é heurístico (palavras `ALERTAS` em `controle.py`). Confira a
primeira saída contra o portal e ajuste as palavras-chave.

## Validade dos certificados digitais (API)

```bash
export SIEG_API_KEY=... SIEG_CLIENT_ID=... SIEG_SECRET_KEY=...
python sieg_api.py --carteira carteira.csv --dias 30
```

Ver ressalvas no cabeçalho de `sieg_api.py` (headers do JWT e credenciais ainda por confirmar com a SIEG).
Não commitar `carteira.csv`, `exports/` nem relatórios: contêm dados de clientes.
