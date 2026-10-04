"""Uso: python -m robo_issqn 09/2026"""
import sys

from .config import CLIENTE_126, Competencia


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Uso: python -m robo_issqn MM/AAAA")
        return 2
    comp = Competencia.parse(argv[1])
    c = CLIENTE_126
    print(f"Cliente {c.codigo} - {c.nome} (IM {c.inscricao_municipal})")
    print(f"Competência: {comp.mm_aaaa} | filtro do portal: {comp.portal} | ISS {c.aliquota_iss:.0%}")
    print("Etapa 1 concluída: nada foi acessado nem alterado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
