"""
Conciliação de SERVIÇOS TOMADOS: Portal Nacional (Recebidas) x DecWeb (Serviços Tomados) x Domínio (Entradas)
==============================================================================================================

Roda sozinho, SEM abrir site. Lê os arquivos que já estão no Drive (pasta do mês):

  003 ARQUIVOS PORTAL NACIONAL   {n}_{apelido}_PortoAlegre_MM.AAAA_Recebidas.xlsx      (robô Portal Nacional)
  002 ARQUIVOS MUNICIPAIS        {n}_{apelido}_PortoAlegre_MM.AAAA_NFSE_ServTomados[.zip|pasta]   (robô DecWeb)
  008 ARQUIVOS DOMÍNIO           Entradas_{n}_MMAAAA.pdf   (relatório "Acompanhamento de Entradas" do Domínio)

Cada nota é casada pelo CNPJ do prestador + número da nota. Resultado por nota:
  OK            nas três fontes, mesmo valor
  ATENÇÃO       valor ou ISS retido diferente, ou nota só em uma fonte com explicação provável
                (ex.: Domínio tem a nota, o Portal foi exportado ANTES da emissão -> rodar o Portal de novo)
  FALTA         nota da competência no Portal e ausente no Domínio ou no DecWeb
  OUTRA COMP.   nota do Portal de outra competência (informativo)

Uso (na pasta do robô DecWeb, usa config/configuracao.ini; não lê senhas):
    python conciliacao_tomados_dominio.py 257 09/2026
    python conciliacao_tomados_dominio.py 257 09/2026 --csv tomados_257_09_2026.csv
    python conciliacao_tomados_dominio.py 257 09/2026 --portal "C:\\x\\Recebidas.xlsx" --decweb "C:\\x\\ServTomados.xlsx" --dominio "C:\\x\\Entradas_257_092026.pdf"
    python conciliacao_tomados_dominio.py 257 09/2026 --ver-texto      # mostra o texto lido do PDF do Domínio (para ajustar a leitura)
    python conciliacao_tomados_dominio.py 257 09/2026 --dominio-csv entradas.csv   # alternativa ao PDF: CSV ; com nota;cnpj;valor;emissao;entrada;nome

Requer: openpyxl e pypdf (pip install openpyxl pypdf).
"""

import argparse
import csv
import re
import sys
import zipfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import conciliacao as base            # reaproveita leitura/convenções do conciliacao.py
from conciliacao import so_digitos, para_float, brl, normaliza_competencia, _idx, _abre

TOL = 0.01
ESPECIES_SERVICO = {"39"}             # espécie 39 = NFS-e no Domínio (a 36 é NF-e)


@dataclass
class Nota:
    numero: int
    cnpj: str
    nome: str
    valor: float
    iss_retido: float = 0.0
    competencia: str = ""
    emissao: datetime | None = None
    chave: str = ""
    cancelada: bool = False


@dataclass
class Fonte:
    notas: list = field(default_factory=list)
    outras_comp: list = field(default_factory=list)   # só Portal
    gerado_em: datetime | None = None                 # só Portal


# ----------------------------------------------------------------------
# LEITURA
# ----------------------------------------------------------------------

def _data(v):
    if isinstance(v, datetime):
        return v
    m = re.search(r"(\d{2})/(\d{2})/(\d{4})(?:[ ,]+(\d{2}):(\d{2}):?(\d{2})?)?", str(v or ""))
    if not m:
        return None
    d, mo, a, h, mi, s = m.groups()
    return datetime(int(a), int(mo), int(d), int(h or 0), int(mi or 0), int(s or 0))


def ler_portal(caminho, competencia: str) -> Fonte:
    wb = _abre(str(caminho))
    try:
        ws = wb.worksheets[0]
        rows = [list(r) for r in ws.iter_rows(values_only=True)]
    finally:
        wb.close()
    cab = [str(c or "").strip() for c in rows[0]]
    i = {n: _idx(cab, *nomes) for n, nomes in {
        "num": ("Número NFS-e", "Relação Número NFS-e"), "comp": ("Competência",),
        "cnpj": ("CNPJ/CPF Prestador",), "nome": ("Nome Prestador",), "val": ("Valor do Serviço (R$)",),
        "iss": ("Valor do ISSQN (R$)",), "ret": ("Retenção ISSQN",), "data": ("Data Geração",),
        "sit": ("Situação NFS-e",), "chave": ("Chave NFS-e",)}.items()}
    if i["num"] is None or i["val"] is None or i["cnpj"] is None:
        raise ValueError(f"{caminho}: não parece uma planilha Recebidas do Portal Nacional")
    f = Fonte()
    for r in rows[1:]:
        if r and any(str(c or "").strip().startswith("Gerado em") for c in r):
            f.gerado_em = _data(" ".join(str(c or "") for c in r))
        cel = str(r[i["num"]]).strip() if r and r[i["num"]] is not None else ""
        if not re.fullmatch(r"\d+(\.0)?", cel):
            continue   # linha de total/resumo
        r[i["num"]] = cel.split(".")[0]
        iss = para_float(r[i["iss"]]) if i["iss"] is not None else 0.0
        ret = str(r[i["ret"]] or "").strip()[:1] in ("2", "3")
        sit = str(r[i["sit"]] or "") if i["sit"] is not None else ""
        n = Nota(numero=int(so_digitos(r[i["num"]])), cnpj=so_digitos(r[i["cnpj"]]), nome=str(r[i["nome"]] or "")[:40],
                 valor=para_float(r[i["val"]]), iss_retido=iss if ret else 0.0,
                 competencia=normaliza_competencia(r[i["comp"]]), emissao=_data(r[i["data"]]) if i["data"] is not None else None,
                 chave=so_digitos(r[i["chave"]]) if i["chave"] is not None else "",
                 cancelada="cancel" in sit.casefold())
        if n.cancelada:
            continue
        (f.notas if n.competencia == competencia else f.outras_comp).append(n)
    # as duas últimas linhas do Portal trazem "Gerado em:" numa célula e a data em outra
    for r in rows:
        for k, c in enumerate(r):
            if str(c or "").strip().startswith("Gerado em") and k + 1 < len(r):
                f.gerado_em = _data(r[k + 1]) or f.gerado_em
    return f


def ler_decweb(origem) -> Fonte:
    wb = _abre(origem)
    try:
        rows = [list(r) for r in wb.worksheets[0].iter_rows(values_only=True)]
    finally:
        wb.close()
    f, cab = Fonte(), None
    for r in rows:
        p = str(r[0]).strip() if r and r[0] is not None else ""
        if p == "Número NFSE":
            cab = [str(c or "").strip() for c in r]
            i = {"data": _idx(cab, "Data Em. Nota"), "cnpj": _idx(cab, "CNPJ"), "nome": _idx(cab, "Nome Empresa"),
                 "val": _idx(cab, "Valor Serviços"), "ret": _idx(cab, "Val. ISS ret."), "sit": _idx(cab, "Situação.", "Situação"),
                 "chave": _idx(cab, "Chave Acesso")}
            continue
        if cab is None:
            continue
        if not p or any(str(c).strip().upper() == "TOTAL" for c in r if c is not None):
            break
        d = so_digitos(p)
        numero = int(d[5:]) if len(d) == 18 else int(d[-6:] or 0)     # 2026 1 + 13 dígitos = nº da nota
        sit = str(r[i["sit"]] or "") if i["sit"] is not None else ""
        if "cancel" in sit.casefold():
            continue
        f.notas.append(Nota(numero=numero, cnpj=so_digitos(r[i["cnpj"]]), nome=str(r[i["nome"]] or "")[:40],
                            valor=para_float(r[i["val"]]), iss_retido=para_float(r[i["ret"]]),
                            emissao=_data(r[i["data"]]), chave=so_digitos(r[i["chave"]]) if i["chave"] is not None else ""))
    return f


RE_LINHA = re.compile(
    r"(?P<cod>\d{1,4})\s+(?P<emi>\d{2}/\d{2}/\d{4})\s+(?P<ent>\d{2}/\d{2}/\d{4})\s+(?P<nota>\d+)\s+(?P<serie>\w+)\s+"
    r"(?P<esp>\d{1,3})\s+(?P<codfor>\d+)\s+(?P<nome>.+?)\s+"
    r"(?P<cnpj>\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}|\d{3}\.\d{3}\.\d{3}-\d{2})\s+.*?"
    r"(?P<cfop>\d-\d{3})\s+(?P<ac>\d+)\s+(?P<uf>[A-Z]{2})\s+(?P<valor>\d{1,3}(?:\.\d{3})*,\d{2})")


def texto_pdf(caminho) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Instale o pypdf:  pip install pypdf")
    return "\n".join((p.extract_text() or "") for p in PdfReader(str(caminho)).pages)


def ler_dominio_texto(texto: str, todas: bool = False) -> Fonte:
    texto = re.sub(r"\s+", " ", texto)
    f = Fonte()
    for m in RE_LINHA.finditer(texto):
        if not todas and m["esp"] not in ESPECIES_SERVICO:
            continue
        f.notas.append(Nota(numero=int(m["nota"]), cnpj=so_digitos(m["cnpj"]), nome=m["nome"].strip()[:40],
                            valor=para_float(m["valor"]), emissao=_data(m["emi"]),
                            competencia=normaliza_competencia(m["ent"])))
    return f


def ler_dominio_csv(caminho) -> Fonte:
    f = Fonte()
    with open(caminho, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh, delimiter=";"):
            f.notas.append(Nota(numero=int(so_digitos(r["nota"])), cnpj=so_digitos(r["cnpj"]), nome=r.get("nome", "")[:40],
                                valor=para_float(r["valor"]), emissao=_data(r.get("emissao")),
                                competencia=normaliza_competencia(r.get("entrada"))))
    return f


# ----------------------------------------------------------------------
# LOCALIZAÇÃO
# ----------------------------------------------------------------------

def cliente(numero: str) -> dict:
    return next((c for c in base.carregar_clientes([numero])), {"numero": numero, "apelido": ""})


def achar_arquivos(cfg, numero, mes, ano):
    import configuracao
    pm = configuracao.pasta_mes(cfg, mes)
    c = cliente(numero)
    portal = None
    pn = configuracao.pasta_nacional(cfg, mes)
    if pn.exists():
        achados = sorted(p for p in pn.glob(f"{numero}_*_{mes}.{ano}_Recebidas.xlsx") if not p.name.startswith("~$"))
        portal = achados[0] if achados else None
    decweb = None
    pmun = configuracao.pasta_municipais(cfg, mes)
    b = f"{base.nome_base(c, mes, ano)}_NFSE_ServTomados"
    if pmun.exists():
        pasta = pmun / b
        if pasta.is_dir():
            x = sorted(p for p in pasta.glob("*.xlsx") if not p.name.startswith("~$"))
            decweb = str(x[0]) if x else None
        elif (pmun / f"{b}.zip").exists():
            with zipfile.ZipFile(pmun / f"{b}.zip") as z:
                x = [n for n in z.namelist() if n.lower().endswith(".xlsx")]
                decweb = z.read(x[0]) if x else None
    dom = None
    pd = pm / "008 ARQUIVOS DOMÍNIO"
    if pd.exists():
        achados = sorted(p for p in pd.glob("*.pdf") if "entrada" in p.name.casefold() and re.search(rf"(?<!\d){numero}(?!\d)", p.name))
        dom = achados[0] if achados else None
    return portal, decweb, dom


# ----------------------------------------------------------------------
# CONCILIAÇÃO
# ----------------------------------------------------------------------

def conciliar(portal: Fonte, decweb: Fonte, dominio: Fonte):
    linhas = []
    usados_portal_outras = set()

    def chave(n):
        return (n.cnpj, n.numero)

    P = {chave(n): n for n in portal.notas}
    D = {chave(n): n for n in decweb.notas}
    M = {chave(n): n for n in dominio.notas}
    O = {chave(n): n for n in portal.outras_comp}
    for k in sorted(set(P) | set(D) | set(M), key=lambda x: (x[0], x[1])):
        p, d, m = P.get(k), D.get(k), M.get(k)
        ref = p or d or m
        obs, status = [], "OK"
        if p and m and d:
            if abs(p.valor - m.valor) > TOL or abs(p.valor - d.valor) > TOL:
                status = "ATENÇÃO"; obs.append(f"valores diferentes (Portal {brl(p.valor)} | DecWeb {brl(d.valor)} | Domínio {brl(m.valor)})")
            if abs(p.iss_retido - d.iss_retido) > TOL:
                status = "ATENÇÃO"; obs.append(f"ISS retido diferente (Portal {brl(p.iss_retido)} | DecWeb {brl(d.iss_retido)})")
        else:
            if p and not m:
                status = "FALTA"; obs.append("no Portal e NÃO no Domínio (lançar)")
            if p and not d:
                status = "FALTA" if status != "FALTA" else status; obs.append("no Portal e NÃO no DecWeb (declarar/retificar)")
            if m and not p:
                status = "ATENÇÃO"
                if m.emissao and portal.gerado_em and m.emissao > portal.gerado_em:
                    obs.append(f"emitida em {m.emissao:%d/%m/%Y}, depois do export do Portal ({portal.gerado_em:%d/%m/%Y}): rodar o Portal de novo")
                elif k in O:
                    obs.append(f"no Portal só com competência {O[k].competencia}")
                else:
                    obs.append("no Domínio e não no Portal")
                par = next((o for o in portal.outras_comp if o.cnpj == m.cnpj and abs(o.valor - m.valor) <= TOL and chave(o) != k), None)
                if par:
                    obs.append(f"mesmo prestador e valor da nota {par.numero} do Portal (comp. {par.competencia}): conferir número/data")
            if d and not m and not p:
                status = "ATENÇÃO"; obs.append("só no DecWeb")
            if d and not m and p:
                pass
            if m and p and not d:
                pass
        linhas.append((status, ref, p, d, m, "; ".join(obs)))
    for k, o in O.items():
        if k not in M and k not in D:
            linhas.append(("OUTRA COMP.", o, o, None, None, f"competência {o.competencia}: não entra nesta competência"))
    return linhas


ICONES = {"OK": "✅", "ATENÇÃO": "⚠️ ", "FALTA": "❌", "OUTRA COMP.": "ℹ️ "}


def imprimir(linhas, portal, decweb, dominio, competencia, sem_emoji=False):
    ic = {k: f"[{k[:3]}]" for k in ICONES} if sem_emoji else ICONES
    print(f"\nTOMADOS {competencia}: Portal x DecWeb x Domínio\n")
    print(f"{'':3} {'Prestador':32} {'Nota':>9} {'Portal':>11} {'DecWeb':>11} {'Domínio':>11}  Obs.")
    print("-" * 120)
    for st, ref, p, d, m, obs in linhas:
        def v(x):
            return brl(x.valor).replace("R$ ", "") if x else "—"
        print(f"{ic[st]:3} {ref.nome[:32]:32} {ref.numero:>9} {v(p):>11} {v(d):>11} {v(m):>11}  {obs}")
    print("-" * 120)
    tp = sum(n.valor for n in portal.notas); td = sum(n.valor for n in decweb.notas); tm = sum(n.valor for n in dominio.notas)
    print(f"{'TOTAL (competência)':>46} {brl(tp):>11} {brl(td):>11} {brl(tm):>11}")
    print(f"{'notas':>46} {len(portal.notas):>11} {len(decweb.notas):>11} {len(dominio.notas):>11}")
    cont = {k: sum(1 for l in linhas if l[0] == k) for k in ICONES}
    total = sum(v for k, v in cont.items() if k != "OUTRA COMP.") or 1
    barra = int(10 * cont["OK"] / total)
    print(f"\nPlacar: {'#' * barra}{'.' * (10 - barra)} {cont['OK']}/{total} conferem | atenção {cont['ATENÇÃO']} | falta {cont['FALTA']} | outra competência {cont['OUTRA COMP.']}")
    if portal.gerado_em:
        print(f"Portal exportado em {portal.gerado_em:%d/%m/%Y %H:%M}")


def gravar_csv(linhas, caminho):
    with open(caminho, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["status", "cnpj_prestador", "prestador", "nota", "portal", "decweb", "dominio", "observacao"])
        for st, ref, p, d, m, obs in linhas:
            w.writerow([st, ref.cnpj, ref.nome, ref.numero] + [f"{x.valor:.2f}".replace(".", ",") if x else "" for x in (p, d, m)] + [obs])


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Conciliação de serviços tomados: Portal x DecWeb x Domínio.")
    ap.add_argument("cliente", help="número do cliente (ex.: 257)")
    ap.add_argument("competencia", help="MM/AAAA")
    ap.add_argument("--portal"); ap.add_argument("--decweb"); ap.add_argument("--dominio"); ap.add_argument("--dominio-csv")
    ap.add_argument("--csv"); ap.add_argument("--ver-texto", action="store_true")
    ap.add_argument("--todas-especies", action="store_true", help="não filtra a espécie 39 (NFS-e) do Domínio")
    ap.add_argument("--sem-emoji", action="store_true")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"(0[1-9]|1[0-2])/\d{4}", a.competencia):
        ap.error("competência deve ser MM/AAAA")
    mes, ano = a.competencia.split("/")
    portal_a, decweb_a, dom_a = a.portal, a.decweb, a.dominio
    if not (portal_a and decweb_a and (dom_a or a.dominio_csv)):
        import configuracao
        cfg = configuracao.carregar()
        p, d, m = achar_arquivos(cfg, a.cliente, mes, ano)
        portal_a, decweb_a, dom_a = portal_a or p, decweb_a or d, dom_a or m
    faltam = [n for n, x in (("Portal Recebidas", portal_a), ("DecWeb ServTomados", decweb_a)) if not x]
    if not (dom_a or a.dominio_csv):
        faltam.append("Domínio Entradas (PDF ou CSV)")
    if faltam:
        print("Não encontrei: " + ", ".join(faltam) + ". Use --portal / --decweb / --dominio para informar o caminho.")
        return 1
    if a.ver_texto and dom_a:
        print(texto_pdf(dom_a)); print("\n--- notas lidas ---")
    portal = ler_portal(portal_a, a.competencia)
    decweb = ler_decweb(decweb_a if isinstance(decweb_a, (bytes, bytearray)) else str(decweb_a))
    dominio = ler_dominio_csv(a.dominio_csv) if a.dominio_csv else ler_dominio_texto(texto_pdf(dom_a), a.todas_especies)
    if not dominio.notas:
        print("Nenhuma nota lida do Domínio. Rode com --ver-texto para ver o texto do PDF ou use --dominio-csv.")
        return 1
    linhas = conciliar(portal, decweb, dominio)
    imprimir(linhas, portal, decweb, dominio, a.competencia, a.sem_emoji)
    if a.csv:
        gravar_csv(linhas, a.csv); print(f"CSV gravado em {a.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
