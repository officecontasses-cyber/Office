"""Monta config\\clientes.csv do robô DecWeb a partir da planilha "Clientes Simples - Dados_Completos".

Uso (no PC do colaborador, dentro de C:\\Robos\\decweb):
    python colaborador\\montar_clientes.py "C:\\Robos\\temp\\Clientes Simples - Dados_Completos.csv"

A planilha (exportada em CSV) tem as senhas do DecWeb. Este script:
  - só lê o arquivo exportado e grava config\\clientes.csv (local, fora do Meu Drive);
  - nunca imprime senha, nem grava senha em log;
  - só inclui as empresas de Porto Alegre listadas em CLIENTES abaixo (DecWeb só atende Porto Alegre);
  - confere os dígitos do CNPJ e avisa quem está sem senha ou com a senha "-".
Depois de conferir o resultado, APAGUE o CSV exportado (use --apagar-origem para o script apagar).
"""
import argparse
import csv
import datetime
import re
import shutil
import sys
import unicodedata
from pathlib import Path

# numero: (apelido, nome_painel, cnpj com 14 dígitos). Sem senha aqui.
CLIENTES = {
    "1": ("FPVanzetto", "FP VANZETTO", "01390758000146"),
    "11": ("StarCeo", "STARCEO", "04435328000191"),
    "34": ("EFSConsulting", "EFS CONSULTING", "06171291000167"),
    "75": ("VCTAudiodub", "VCT AUDIODUB", "08779486000110"),
    "79": ("HomeroZenker", "HOMERO ZENKER", "01058895000188"),
    "85": ("BergmannMassaro", "BERGMANN & MASSARO", "09147917000198"),
    "92": ("RFS", "RFS", "09040365000114"),
    "93": ("Flaviarte", "FLAVIARTE", "91545038000103"),
    "115": ("Projeta", "PROJETA", "08220031000160"),
    "148": ("ARS", "ARS", "16651383000106"),
    "158": ("Joga", "JOGA", "19722575000146"),
    "164": ("PorticoJobLeite", "PORTICO - JOB E LEITE", "12931519000172"),
    "167": ("BMSoft", "BMSOFT", "21734194000129"),
    "169": ("DMSouza", "DM SOUZA", "22575008000119"),
    "176": ("BelaVistaSul", "BELA VISTA SUL", "24286521000115"),
    "199": ("F8Gestao", "F8 GESTÃO", "31571815000154"),
    "210": ("OfficeCont", "OFFICECONT", "35743878000100"),
    "213": ("GCL", "GCL", "04610510000131"),
    "222": ("RCBertoglio", "RC BERTOGLIO ARQUITETURA", "42265639000149"),
    "226": ("LDG", "LDG", "44763907000188"),
    "230": ("FRB", "FRB", "45687570000130"),
    "236": ("PeludosDaMontanha", "PELUDOS DA MONTANHA", "34040879000117"),
}
CABECALHO = ["numero", "apelido", "nome_painel", "cnpj", "usuario", "senha", "aceitar_avisos"]
SENHA_VAZIA = {"", "-", "\\-", "–", "—"}


def norm(txt: str) -> str:
    txt = unicodedata.normalize("NFKD", txt or "")
    txt = "".join(c for c in txt if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", txt).strip().upper()


def cnpj_valido(c: str) -> bool:
    if len(c) != 14 or not c.isdigit() or len(set(c)) == 1:
        return False
    n = [int(x) for x in c]

    def dv(base, pesos):
        r = sum(a * b for a, b in zip(base, pesos)) % 11
        return 0 if r < 2 else 11 - r

    d1 = dv(n[:12], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    d2 = dv(n[:12] + [d1], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    return n[12] == d1 and n[13] == d2


def achar_coluna(cabecalho, *opcoes):
    mapa = {norm(h): i for i, h in enumerate(cabecalho)}
    for o in opcoes:
        if norm(o) in mapa:
            return mapa[norm(o)]
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planilha_csv", help="CSV exportado da planilha de clientes")
    ap.add_argument("--saida", default=str(Path(__file__).resolve().parent.parent / "config" / "clientes.csv"))
    ap.add_argument("--apagar-origem", action="store_true", help="apaga o CSV exportado ao terminar sem erro")
    args = ap.parse_args()

    origem = Path(args.planilha_csv)
    if not origem.is_file():
        print(f"Não achei o arquivo: {origem}")
        return 1
    with origem.open(encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.reader(f))
    if not linhas:
        print("Arquivo vazio.")
        return 1
    cab = linhas[0]
    c_num = 0
    c_cnpj = achar_coluna(cab, "CNPJ")
    c_login = achar_coluna(cab, "LOGIN PREF.", "LOGIN PREF")
    c_senha = achar_coluna(cab, "SENHA PREF.", "SENHA PREF")
    c_cidade = achar_coluna(cab, "CIDADE/ESTADO")
    if None in (c_cnpj, c_login, c_senha):
        print("Não achei as colunas CNPJ, LOGIN PREF. e SENHA PREF. no arquivo. Exporte a aba certa da planilha.")
        return 1

    achados, ignorados = {}, []
    for lin in linhas[1:]:
        if not lin or not lin[c_num].strip():
            continue
        num = lin[c_num].strip().lstrip("0")
        if num in CLIENTES:
            achados[num] = lin
        else:
            cidade = lin[c_cidade].strip() if c_cidade is not None and c_cidade < len(lin) else "?"
            ignorados.append((num, lin[1].strip() if len(lin) > 1 else "", cidade))

    saida_linhas, sem_senha, erros = [], [], []
    for num in sorted(CLIENTES, key=int):
        apelido, painel, cnpj_modelo = CLIENTES[num]
        lin = achados.get(num)
        if lin is None:
            erros.append(f"{num} {apelido}: não está na planilha exportada")
            continue
        cnpj = re.sub(r"\D", "", lin[c_cnpj]).zfill(14)
        if cnpj != cnpj_modelo or not cnpj_valido(cnpj):
            erros.append(f"{num} {apelido}: CNPJ da planilha ({cnpj}) diferente do esperado ({cnpj_modelo}) ou inválido")
            continue
        usuario = re.sub(r"\D", "", lin[c_login]) or cnpj
        senha = lin[c_senha].strip()
        if senha in SENHA_VAZIA:
            sem_senha.append(f"{num} {apelido}")
            continue
        saida_linhas.append([num, apelido, painel, cnpj, usuario, senha, ""])

    saida = Path(args.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    if saida.exists():
        bak = saida.with_name(saida.name + ".bak_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
        shutil.copy2(saida, bak)
        print(f"Cópia de segurança do arquivo anterior: {bak.name}")
    with saida.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(CABECALHO)
        w.writerows(saida_linhas)

    print(f"\nclientes.csv gravado em {saida} com {len(saida_linhas)} empresas (senhas NÃO exibidas).")
    if sem_senha:
        print("\nFicaram FORA por falta de senha na planilha (peça à Fernanda e inclua depois):")
        for s in sem_senha:
            print("  -", s)
    for e in erros:
        print("ERRO:", e)
    if ignorados:
        print("\nLinhas da planilha que não entram (fora de Porto Alegre ou não listadas):")
        for n, nome, cid in ignorados:
            print(f"  - {n} {nome} ({cid})")
    if erros:
        print("\nHá erros acima: confira antes de rodar o robô.")
        return 2
    if args.apagar_origem:
        origem.unlink()
        print(f"\nArquivo exportado apagado: {origem}")
    else:
        print(f"\nLEMBRETE: apague agora o arquivo exportado ({origem}); ele tem senhas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
