#!/usr/bin/env python3
"""Controle de certidões, débitos e parcelamentos da carteira (a partir das exportações do HüB SIEG).

A API da SIEG não expõe certidões, débitos nem parcelamentos; esses dados saem do portal
(Pendências → Certidões / Diagnóstico Fiscal / Parcelamentos → "Exportar Todos").
O script cruza essas planilhas com a lista de CNPJs da carteira e gera um relatório.

Como o layout das exportações não foi confirmado, o casamento é feito por CNPJ achado em
qualquer célula da linha, e a sinalização por palavras-chave (ver ALERTAS). Use --inspect
para ver as colunas reais e ajuste as palavras-chave se necessário.
"""
import argparse
import re
import sys
from pathlib import Path

import pandas as pd

# Fontes: nome do relatório -> padrão do arquivo dentro da pasta de exportações.
FONTES = {
    "Certidões": "certidoes*",
    "Diagnóstico Fiscal": "diagnostico*",
    "Parcelamentos": "parcelamentos*",
}

# Heurística: linha que contiver alguma dessas palavras (sem acento, minúsculas) é sinalizada.
ALERTAS = ("irregular", "positiva", "pendencia", "atraso", "vencid", "debito", "divida", "nao entregue")

CNPJ_RE = re.compile(r"(?<!\d)(\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2})(?!\d)")
CPF_RE = re.compile(r"(?<!\d)(\d{3}\.?\d{3}\.?\d{3}-?\d{2})(?!\d)")


def so_digitos(texto: str) -> str:
    return re.sub(r"\D", "", str(texto))


def sem_acento(texto: str) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn").lower()


def ler_tabela(caminho: Path) -> pd.DataFrame:
    if caminho.suffix.lower() in (".xlsx", ".xlsm", ".xls"):
        return pd.read_excel(caminho, dtype=str).fillna("")
    return pd.read_csv(caminho, dtype=str, sep=None, engine="python", encoding_errors="replace").fillna("")


def documento_da_linha(linha: pd.Series) -> str:
    texto = " | ".join(str(v) for v in linha.values)
    m = CNPJ_RE.search(texto) or CPF_RE.search(texto)
    return so_digitos(m.group(1)) if m else ""


def carregar_carteira(caminho: Path) -> pd.DataFrame:
    df = ler_tabela(caminho)
    col_doc = next((c for c in df.columns if re.search(r"cnpj|cpf|documento", sem_acento(c))), df.columns[0])
    col_nome = next((c for c in df.columns if re.search(r"nome|empresa|razao", sem_acento(c))), None)
    out = pd.DataFrame({"documento": df[col_doc].map(so_digitos)})
    out["nome"] = df[col_nome] if col_nome else ""
    out = out[out["documento"] != ""].drop_duplicates("documento")
    return out.reset_index(drop=True)


def localizar(pasta: Path, padrao: str) -> Path | None:
    achados = sorted(
        [p for p in pasta.glob(padrao + ".*") if p.suffix.lower() in (".xlsx", ".xls", ".csv")],
        key=lambda p: p.stat().st_mtime,
    )
    return achados[-1] if achados else None  # o mais recente


def analisar(df: pd.DataFrame, carteira: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    df = df.copy()
    df.insert(0, "documento", df.apply(documento_da_linha, axis=1))
    na_carteira = df[df["documento"].isin(carteira["documento"])].copy()
    texto = na_carteira.drop(columns="documento").astype(str).agg(" ".join, axis=1).map(sem_acento)
    na_carteira["alerta"] = texto.map(lambda t: ", ".join(a for a in ALERTAS if a in t))
    ausentes = sorted(set(carteira["documento"]) - set(na_carteira["documento"]))
    return na_carteira, ausentes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--carteira", default="carteira.csv", help="CSV/XLSX com CNPJs da carteira (coluna cnpj[,nome])")
    ap.add_argument("--exports", default="exports", help="pasta com as exportações do HüB SIEG")
    ap.add_argument("--saida", default="relatorio_carteira.xlsx")
    ap.add_argument("--inspect", action="store_true", help="só mostra as colunas e linhas de exemplo de cada exportação")
    args = ap.parse_args()

    pasta = Path(args.exports)
    if args.inspect:
        for nome, padrao in FONTES.items():
            arq = localizar(pasta, padrao)
            print(f"\n== {nome}: {arq or 'arquivo não encontrado (esperado ' + padrao + ')'}")
            if arq:
                df = ler_tabela(arq)
                print("colunas:", list(df.columns))
                print(df.head(3).to_string())
        return 0

    carteira = carregar_carteira(Path(args.carteira))
    if carteira.empty:
        print("Carteira vazia ou sem CNPJs reconhecíveis.", file=sys.stderr)
        return 1
    print(f"Carteira: {len(carteira)} documentos")

    resumo, abas = [], {}
    for nome, padrao in FONTES.items():
        arq = localizar(pasta, padrao)
        if not arq:
            resumo.append({"fonte": nome, "arquivo": "NÃO ENCONTRADO", "na_carteira": "", "sinalizados": "", "sem_registro": ""})
            continue
        dados, ausentes = analisar(ler_tabela(arq), carteira)
        abas[nome] = dados
        if ausentes:
            nomes = carteira.set_index("documento")["nome"]
            abas[f"{nome} - sem registro"] = pd.DataFrame({"documento": ausentes, "nome": [nomes[d] for d in ausentes]})
        resumo.append({
            "fonte": nome, "arquivo": arq.name, "na_carteira": dados["documento"].nunique(),
            "sinalizados": int((dados["alerta"] != "").sum()), "sem_registro": len(ausentes),
        })

    resumo_df = pd.DataFrame(resumo)
    print(resumo_df.to_string(index=False))
    with pd.ExcelWriter(args.saida) as xw:
        resumo_df.to_excel(xw, sheet_name="Resumo", index=False)
        for nome, df in abas.items():
            df.to_excel(xw, sheet_name=nome[:31], index=False)
    print(f"Relatório: {args.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
