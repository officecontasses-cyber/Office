"""Uso:
    python -m robo_issqn 09/2026          mostra os dados (não acessa nada)
    python -m robo_issqn abrir            etapa A: abre o portal no Chrome (somente leitura)
"""
import sys
from pathlib import Path

from .ambiente import ler_env
from .config import CLIENTE_126, Competencia


def abrir() -> int:
    env = ler_env()
    url = env.get("ISSQN_PORTAL_URL")
    if not url:
        print("Defina ISSQN_PORTAL_URL no arquivo .env (copie de .env.example).")
        return 2
    from .navegador import abrir_portal

    arquivo = abrir_portal(
        url,
        perfil=Path(env.get("ISSQN_PERFIL_NAVEGADOR", "perfil_navegador")),
        saida=Path(env.get("ISSQN_PASTA_SAIDA", "saida")),
        chrome_path=env.get("ISSQN_CHROME_PATH") or None,
        porta=int(env.get("ISSQN_PORTA_CONTROLE", "9222")),
    )
    print(f"Print salvo em: {arquivo}")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[1] == "abrir":
        return abrir()
    if len(argv) != 2:
        print("Uso: python -m robo_issqn MM/AAAA | abrir")
        return 2
    comp = Competencia.parse(argv[1])
    c = CLIENTE_126
    print(f"Cliente {c.codigo} - {c.nome} (IM {c.inscricao_municipal})")
    print(f"Competência: {comp.mm_aaaa} | filtro do portal: {comp.portal} | ISS {c.aliquota_iss:.0%}")
    print("Etapa 1 concluída: nada foi acessado nem alterado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
