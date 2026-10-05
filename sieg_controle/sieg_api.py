#!/usr/bin/env python3
"""Validade dos certificados digitais cadastrados no SIEG (GET /api/v1/listar).

Atenção: certificado digital NÃO é certidão. Isto só avisa quais certificados da carteira estão
vencidos ou perto de vencer (sem certificado válido o HüB não consegue consultar nada do cliente).

Credenciais por variável de ambiente (nunca no código):
  SIEG_API_KEY, SIEG_CLIENT_ID, SIEG_SECRET_KEY

NÃO CONFIRMADO na documentação (conferir com o suporte SIEG antes de usar em produção):
  - os nomes dos headers do JWT: a página "Fluxo geral" cita X-Client-Id/X-Secret-Key e a página do
    JWT cita clientId/secretKey; use SIEG_JWT_HEADERS=clientId,secretKey para alternar;
  - se um cliente que só tem a Chave API consegue gerar o JWT.
"""
import argparse
import os
import sys
from datetime import datetime, timedelta, timezone

import requests

BASE = "https://api.sieg.com"
LIMITE_POR_PAGINA = 100  # documentado no artigo antigo; limite de 30 req/min


def jwt() -> str:
    c, s = os.environ["SIEG_CLIENT_ID"], os.environ["SIEG_SECRET_KEY"]
    h_cli, h_sec = (os.environ.get("SIEG_JWT_HEADERS") or "X-Client-Id,X-Secret-Key").split(",")
    r = requests.post(f"{BASE}/api/v1/create-jwt", headers={h_cli: c, h_sec: s}, timeout=30)
    r.raise_for_status()
    return r.json()["Token"]


def listar_certificados(token: str, ativos: bool = True):
    headers = {"Authorization": f"Bearer {token}", "X-API-Key": os.environ["SIEG_API_KEY"]}
    pagina = 0
    while True:
        r = requests.get(f"{BASE}/api/v1/listar", headers=headers,
                         params={"active": str(ativos).lower(), "pagina": pagina}, timeout=30)
        if r.status_code == 429:
            raise SystemExit("429: limite de 30 requisições/min excedido; tente de novo em 1 minuto.")
        r.raise_for_status()
        dados = r.json().get("Data") or []
        yield from dados
        if len(dados) < LIMITE_POR_PAGINA:
            return
        pagina += 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dias", type=int, default=30, help="avisar certificados que vencem em até N dias")
    ap.add_argument("--carteira", help="CSV com CNPJs; se omitido, lista todos os certificados da conta")
    args = ap.parse_args()

    faltando = [v for v in ("SIEG_API_KEY", "SIEG_CLIENT_ID", "SIEG_SECRET_KEY") if v not in os.environ]
    if faltando:
        print("Defina as variáveis de ambiente:", ", ".join(faltando), file=sys.stderr)
        return 1

    docs = None
    if args.carteira:
        from controle import carregar_carteira
        from pathlib import Path
        docs = set(carregar_carteira(Path(args.carteira))["documento"])

    limite = datetime.now(timezone.utc) + timedelta(days=args.dias)
    for c in listar_certificados(jwt()):
        doc = "".join(ch for ch in str(c.get("CnpjCpf", "")) if ch.isdigit())
        if docs is not None and doc not in docs:
            continue
        exp = datetime.fromisoformat(c["DataExpira"].replace("Z", "+00:00"))
        situacao = "VENCIDO" if exp < datetime.now(timezone.utc) else ("VENCE EM BREVE" if exp <= limite else "ok")
        if situacao != "ok":
            print(f"{situacao:15} {doc} {c.get('Nome', '')} expira em {exp:%d/%m/%Y}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
