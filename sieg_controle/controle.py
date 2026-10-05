#!/usr/bin/env python3
"""Controle de certidões, débitos e parcelamentos da carteira (a partir das exportações do HüB SIEG).

A API da SIEG não expõe certidões, débitos nem parcelamentos; esses dados saem do portal
(Pendências → Certidões / Diagnóstico Fiscal / Parcelamentos → "Exportar Todos").

Layout das exportações (conferido em 05/10/2026):
  Certidões:    Empresa, CNPJ, Data da Última Consulta, Visualização, Tipo, Situação, Data de Vencimento
  Diagnóstico:  Empresa, CNPJ, Data da Última Consulta, Visualização, Situação (Sim/Não)
  Parcelamentos: Empresa, CNPJ, Data da Última Consulta, Visualização, Data da Parcela, Situação,
                 Consulta em Atraso, Quitado
"""
import argparse
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd

FONTES = {
    "Certidões": "certidoes*",
    "Diagnóstico Fiscal": "diagnostico*",
    "Parcelamentos": "parcelamentos*",
}

# Certidões: situação -> nível. O que não estiver aqui é "ATENÇÃO" (ex.: "Outros").
CERT_IRREGULAR = {"irregular"}
CERT_OK = {"regular"}
# Diagnóstico Fiscal: valor da coluna Situação que indica irregularidade.
# INFERÊNCIA (não confirmada pela SIEG): "Não" = sem situação regular. Em 05/10/2026, 18 de 25 empresas com
# "Não" tinham CRFB-PGFN Irregular e 15 de 26 com "Sim" tinham Regular. Troque aqui se estiver invertido.
DIAG_IRREGULAR = {"nao"}
# Parcelamentos: situações tratadas como encerradas (sem acompanhamento) e como ativas.
PARC_ENCERRADO = ("encerrad", "liquidad")
PARC_ATIVO = ("em parcelamento", "deferida e consolidada")
PARC_ATENCAO = ("nao validado",)  # "Não validado – primeira parcela não paga"

NIVEL_ORDEM = {"IRREGULAR": 0, "ATENÇÃO": 1, "OK": 2}


def so_digitos(texto) -> str:
    return "".join(ch for ch in str(texto) if ch.isdigit())


def sem_acento(texto) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", str(texto)) if unicodedata.category(c) != "Mn").lower().strip()


def ler_tabela(caminho: Path) -> pd.DataFrame:
    if caminho.suffix.lower() in (".xlsx", ".xlsm", ".xls"):
        return pd.read_excel(caminho, dtype=str).fillna("")
    return pd.read_csv(caminho, dtype=str, sep=None, engine="python", encoding_errors="replace").fillna("")


def normalizar(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza o documento (CNPJ 14 dígitos, CPF 11; o portal exporta sem zeros à esquerda só no CPF)."""
    df = df.copy()
    doc = df["CNPJ"].map(so_digitos)
    df["CNPJ"] = doc.map(lambda d: d.zfill(14) if len(d) > 11 else d.zfill(11))
    return df


def data_br(txt):
    try:
        return datetime.strptime(str(txt).strip(), "%d/%m/%Y").date()
    except ValueError:
        return None


def carregar_carteira(caminho: Path) -> pd.DataFrame:
    df = ler_tabela(caminho)
    col_doc = next((c for c in df.columns if any(k in sem_acento(c) for k in ("cnpj", "cpf", "documento"))), df.columns[0])
    col_nome = next((c for c in df.columns if any(k in sem_acento(c) for k in ("nome", "empresa", "razao"))), None)
    out = pd.DataFrame({"CNPJ": df[col_doc].map(so_digitos)})
    out["nome"] = df[col_nome] if col_nome else ""
    out["CNPJ"] = out["CNPJ"].map(lambda d: d.zfill(14) if len(d) > 11 else d.zfill(11))
    return out[out["CNPJ"].str.strip("0") != ""].drop_duplicates("CNPJ").reset_index(drop=True)


def localizar(pasta: Path, padrao: str) -> Path | None:
    achados = sorted(
        [p for p in pasta.glob(padrao + ".*") if p.suffix.lower() in (".xlsx", ".xls", ".csv")],
        key=lambda p: p.stat().st_mtime,
    )
    return achados[-1] if achados else None  # o mais recente


def nivel_certidao(linha: pd.Series, hoje: date, dias: int) -> tuple[str, str]:
    sit = sem_acento(linha["Situação"])
    venc = data_br(linha["Data de Vencimento"])
    if sit in CERT_IRREGULAR:
        return "IRREGULAR", f"{linha['Tipo']}: irregular"
    if venc and venc < hoje:
        return "IRREGULAR", f"{linha['Tipo']}: vencida em {venc:%d/%m/%Y}"
    if venc and venc <= hoje + timedelta(days=dias):
        return "ATENÇÃO", f"{linha['Tipo']}: vence em {venc:%d/%m/%Y}"
    if sit not in CERT_OK:
        return "ATENÇÃO", f"{linha['Tipo']}: {linha['Situação']}"
    return "OK", ""


def nivel_diagnostico(linha: pd.Series) -> tuple[str, str]:
    if sem_acento(linha["Situação"]) in DIAG_IRREGULAR:
        return "IRREGULAR", "Diagnóstico Fiscal: Situação = Não (provável pendência RFB/PGFN, a confirmar)"
    return "OK", ""


def nivel_parcelamento(linha: pd.Series, hoje: date) -> tuple[str, str]:
    sit = sem_acento(linha["Situação"])
    if any(sit.startswith(k) for k in PARC_ATENCAO):
        return "ATENÇÃO", f"Parcelamento: {linha['Situação']}"
    parcela = data_br(linha["Data da Parcela"])
    ativo = any(sit.startswith(k) for k in PARC_ATIVO)
    if ativo and parcela and parcela < hoje and sem_acento(linha["Quitado"]) != "sim":
        return "IRREGULAR", f"Parcelamento ativo com parcela vencida em {parcela:%d/%m/%Y}"
    return "OK", ""


def aplicar(df: pd.DataFrame, fn) -> pd.DataFrame:
    res = df.apply(fn, axis=1, result_type="expand")
    df = df.copy()
    df["nivel"], df["motivo"] = res[0], res[1]
    return df


def painel(carteira: pd.DataFrame, abas: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Uma linha por empresa: pior nível e motivos de cada fonte."""
    linhas = []
    for _, emp in carteira.iterrows():
        doc, motivos, pior = emp["CNPJ"], [], "OK"
        for nome, df in abas.items():
            sub = df[(df["CNPJ"] == doc) & (df["nivel"] != "OK")]
            for _, r in sub.iterrows():
                motivos.append(r["motivo"])
                if NIVEL_ORDEM[r["nivel"]] < NIVEL_ORDEM[pior]:
                    pior = r["nivel"]
        ativos = 0
        if "Parcelamentos" in abas:
            p = abas["Parcelamentos"]
            ativos = int(((p["CNPJ"] == doc) & p["Situação"].map(sem_acento).str.startswith(PARC_ATIVO)).sum())
        presente = any((df["CNPJ"] == doc).any() for df in abas.values())
        linhas.append({
            "CNPJ": doc, "Empresa": emp["nome"],
            "nível": pior if presente else "SEM REGISTRO",
            "parcelamentos ativos": ativos, "pendências": "; ".join(motivos),
        })
    out = pd.DataFrame(linhas)
    ordem = {"IRREGULAR": 0, "ATENÇÃO": 1, "OK": 2, "SEM REGISTRO": 3}
    return out.sort_values(by="nível", key=lambda s: s.map(ordem), kind="stable").reset_index(drop=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--carteira", default="carteira.csv",
                    help="CSV/XLSX com CNPJs da carteira (coluna cnpj[,nome]); se não existir, usa todas as empresas das exportações")
    ap.add_argument("--exports", default="exports", help="pasta com as exportações do HüB SIEG")
    ap.add_argument("--saida", default="relatorio_carteira.xlsx")
    ap.add_argument("--dias", type=int, default=30, help="avisar certidões que vencem em até N dias")
    ap.add_argument("--hoje", help="data de referência dd/mm/aaaa (padrão: hoje)")
    ap.add_argument("--inspect", action="store_true", help="só mostra as colunas e linhas de exemplo de cada exportação")
    args = ap.parse_args()
    hoje = data_br(args.hoje) if args.hoje else date.today()

    pasta = Path(args.exports)
    if args.inspect:
        for nome, padrao in FONTES.items():
            arq = localizar(pasta, padrao)
            print(f"\n== {nome}: {arq or 'não encontrado (esperado ' + padrao + ')'}")
            if arq:
                df = ler_tabela(arq)
                print("colunas:", list(df.columns))
                print(df.head(3).to_string())
        return 0

    dados = {}
    for nome, padrao in FONTES.items():
        arq = localizar(pasta, padrao)
        if arq:
            dados[nome] = (arq, normalizar(ler_tabela(arq)))
    if not dados:
        print(f"Nenhuma exportação encontrada em {pasta}/", file=sys.stderr)
        return 1

    cart_path = Path(args.carteira)
    if cart_path.exists():
        carteira = carregar_carteira(cart_path)
        print(f"Carteira: {len(carteira)} documentos ({cart_path})")
    else:
        todas = pd.concat([df[["CNPJ", "Empresa"]].rename(columns={"Empresa": "nome"}) for _, df in dados.values()])
        carteira = todas.drop_duplicates("CNPJ").reset_index(drop=True)
        print(f"AVISO: {cart_path} não existe; usando TODAS as {len(carteira)} empresas das exportações.")

    abas, resumo = {}, []
    regras = {
        "Certidões": lambda r: nivel_certidao(r, hoje, args.dias),
        "Diagnóstico Fiscal": nivel_diagnostico,
        "Parcelamentos": lambda r: nivel_parcelamento(r, hoje),
    }
    for nome in FONTES:
        if nome not in dados:
            resumo.append({"fonte": nome, "arquivo": "NÃO ENCONTRADO"})
            continue
        arq, df = dados[nome]
        df = df[df["CNPJ"].isin(carteira["CNPJ"])]
        df = aplicar(df, regras[nome]) if len(df) else df.assign(nivel="", motivo="")
        abas[nome] = df
        resumo.append({
            "fonte": nome, "arquivo": arq.name, "empresas na carteira": df["CNPJ"].nunique(),
            "linhas": len(df), "irregulares": int((df["nivel"] == "IRREGULAR").sum()),
            "atenção": int((df["nivel"] == "ATENÇÃO").sum()),
        })

    pn = painel(carteira, abas)
    resumo_df = pd.DataFrame(resumo)
    print(resumo_df.to_string(index=False))
    print(pn["nível"].value_counts().to_string())

    with pd.ExcelWriter(args.saida) as xw:
        resumo_df.to_excel(xw, sheet_name="Resumo", index=False)
        pn.to_excel(xw, sheet_name="Painel", index=False)
        for nome, df in abas.items():
            df.to_excel(xw, sheet_name=nome[:31], index=False)
    print(f"Relatório: {args.saida} (referência {hoje:%d/%m/%Y})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
