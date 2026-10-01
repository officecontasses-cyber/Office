"""Lê config/configuracao.ini (pastas e opções do escritório).

Estrutura de pastas do OfficeCont (confirmada no Drive em 01/10/2026):

    <raiz_fechamento> \\ 09_SETEMBRO \\ 002 ARQUIVOS MUNICIPAIS
                                     \\ 003 ARQUIVOS PORTAL NACIONAL

ou seja: primeiro a pasta do mês, depois a pasta do tipo de arquivo.

Para testes, a variável de ambiente DECWEB_CONFIG pode apontar para outro .ini.
"""
import configparser
import os
import sys
from pathlib import Path

ARQUIVO = Path(os.environ.get("DECWEB_CONFIG") or (Path(__file__).parent / "config" / "configuracao.ini"))

SUB_MUNICIPAIS = "002 ARQUIVOS MUNICIPAIS"
SUB_NACIONAL = "003 ARQUIVOS PORTAL NACIONAL"

MESES_PASTA = {
    "01": "01_JANEIRO", "02": "02_FEVEREIRO", "03": "03_MARCO", "04": "04_ABRIL",
    "05": "05_MAIO", "06": "06_JUNHO", "07": "07_JULHO", "08": "08_AGOSTO",
    "09": "09_SETEMBRO", "10": "10_OUTUBRO", "11": "11_NOVEMBRO", "12": "12_DEZEMBRO",
}

_SIM = {"sim", "s", "1", "true", "verdadeiro", "yes", "y"}


def eh_sim(valor, padrao: bool = False) -> bool:
    """'sim'/'s'/'1'... -> True. Vazio ou None -> `padrao`."""
    if valor is None or str(valor).strip() == "":
        return padrao
    return str(valor).strip().lower() in _SIM


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

    opcoes = cp["opcoes"] if cp.has_section("opcoes") else {}
    sem_emitidas = str(opcoes.get("sem_emitidas", "enviar")).strip().lower()
    if sem_emitidas not in ("enviar", "bloquear"):
        sys.exit(f"{ARQUIVO}: 'sem_emitidas' deve ser 'enviar' ou 'bloquear' (veio {sem_emitidas!r}).")
    return {
        "raiz_fechamento": raiz,
        "conferencia": eh_sim(opcoes.get("conferencia"), padrao=False),
        "sem_emitidas": sem_emitidas,
    }


def pasta_mes(cfg: dict, mes: str) -> Path:
    return Path(cfg["raiz_fechamento"]) / MESES_PASTA[mes]


def pasta_municipais(cfg: dict, mes: str) -> Path:
    return pasta_mes(cfg, mes) / SUB_MUNICIPAIS


def pasta_nacional(cfg: dict, mes: str) -> Path:
    return pasta_mes(cfg, mes) / SUB_NACIONAL
