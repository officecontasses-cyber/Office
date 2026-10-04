"""Dados fixos do cliente e parâmetros da competência (etapa 1).

Valores extraídos da skill sao-leopoldo-issqn (fluxo validado em 04/10/2026).
Nenhuma credencial é lida ou guardada aqui.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Cliente:
    codigo: str
    nome: str
    nome_arquivo: str  # trecho usado no nome dos PDFs
    cnpj: str
    inscricao_municipal: str  # "contribuinte" no portal da SEMFA
    regime: str
    aliquota_iss: Decimal
    cidade_arquivo: str = "SãoLeopoldo"


CLIENTE_126 = Cliente(
    codigo="126",
    nome="TATSCH & LEITE CENTRO ODONTOLOGICO S/S",
    nome_arquivo="Tatsch&Leite",
    cnpj="10.914.420/0001-37",
    inscricao_municipal="445777",
    regime="Lucro Presumido",
    aliquota_iss=Decimal("0.02"),
)


@dataclass(frozen=True)
class Competencia:
    ano: int
    mes: int

    @classmethod
    def parse(cls, texto: str) -> "Competencia":
        """Aceita 'MM/AAAA' ou 'AAAA-MM' (também 'AAAA/MM')."""
        t = texto.strip()
        m = re.fullmatch(r"(\d{1,2})/(\d{4})", t) or None
        if m:
            mes, ano = int(m.group(1)), int(m.group(2))
        else:
            m = re.fullmatch(r"(\d{4})[-/](\d{1,2})", t)
            if not m:
                raise ValueError(f"Competência inválida: {texto!r} (use MM/AAAA)")
            ano, mes = int(m.group(1)), int(m.group(2))
        if not 1 <= mes <= 12:
            raise ValueError(f"Mês inválido em {texto!r}")
        return cls(ano, mes)

    @property
    def mm_aaaa(self) -> str:
        return f"{self.mes:02d}.{self.ano}"

    @property
    def portal(self) -> str:
        """Formato do filtro da tela Consulta DMS (ex.: 2026/09)."""
        return f"{self.ano}/{self.mes:02d}"
