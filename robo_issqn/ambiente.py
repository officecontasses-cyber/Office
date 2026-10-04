"""Leitura simples do arquivo .env (sem dependências). Nunca guarda senha: o login é por certificado."""
from __future__ import annotations

import os
from pathlib import Path


def ler_env(caminho: str | Path = ".env") -> dict[str, str]:
    valores: dict[str, str] = {}
    p = Path(caminho)
    if p.exists():
        for linha in p.read_text(encoding="utf-8").splitlines():
            linha = linha.strip()
            if not linha or linha.startswith("#") or "=" not in linha:
                continue
            chave, _, valor = linha.partition("=")
            valores[chave.strip()] = valor.strip().strip('"').strip("'")
    # variáveis do sistema têm prioridade sobre o arquivo
    for chave in list(valores) + [k for k in os.environ if k.startswith("ISSQN_")]:
        if chave in os.environ:
            valores[chave] = os.environ[chave]
    return valores
