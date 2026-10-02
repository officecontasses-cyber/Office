"""Lê config/configuracao.ini — o MESMO formato do robô DecWeb, para o escritório poder copiar o arquivo.

Estrutura de pastas do OfficeCont (confirmada no Drive):

    <raiz_fechamento> \\ 09_SETEMBRO \\ 003 ARQUIVOS PORTAL NACIONAL

Para testes, a variável de ambiente PORTAL_NACIONAL_CONFIG pode apontar para outro .ini.
"""
import configparser
import os
import sys
from pathlib import Path

ARQUIVO = Path(os.environ.get("PORTAL_NACIONAL_CONFIG") or (Path(__file__).parent / "config" / "configuracao.ini"))

SUB_NACIONAL = "003 ARQUIVOS PORTAL NACIONAL"
QUARENTENA = "_QUARENTENA_cnpj_divergente"

MESES_PASTA = {
    "01": "01_JANEIRO", "02": "02_FEVEREIRO", "03": "03_MARCO", "04": "04_ABRIL",
    "05": "05_MAIO", "06": "06_JUNHO", "07": "07_JULHO", "08": "08_AGOSTO",
    "09": "09_SETEMBRO", "10": "10_OUTUBRO", "11": "11_NOVEMBRO", "12": "12_DEZEMBRO",
}


def carregar() -> dict:
    if not ARQUIVO.exists():
        sys.exit(f"Falta o arquivo {ARQUIVO}.\nCopie config/configuracao.exemplo.ini para config/configuracao.ini e ajuste a pasta.")
    cp = configparser.ConfigParser(interpolation=None)
    cp.read(ARQUIVO, encoding="utf-8-sig")
    try:
        raiz = cp["pastas"]["raiz_fechamento"].strip().strip('"')
    except KeyError as e:
        sys.exit(f"{ARQUIVO}: falta a chave {e}. Veja config/configuracao.exemplo.ini.")
    if not raiz or "AJUSTAR" in raiz:
        sys.exit(f"Ajuste 'raiz_fechamento' em {ARQUIVO} (ainda está com o valor de exemplo).")
    return {"raiz_fechamento": raiz}


def pasta_nacional(cfg: dict, mes: str) -> Path:
    return Path(cfg["raiz_fechamento"]) / MESES_PASTA[mes] / SUB_NACIONAL
