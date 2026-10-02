"""Testes offline do robô do Portal Nacional (CNPJs fictícios)."""
import fnmatch
import shutil
from datetime import date

import openpyxl
import pytest

import configuracao
import portal_nacional_download as pn
from conftest import RAIZ_FECHAMENTO

CNPJ = "12345678000190"
CLIENTE = {"numero": "177", "apelido": "ILS", "razao_social": "ILS CONSULTORIA", "cnpj": CNPJ, "cidade": "PortoAlegre"}


def xlsx(caminho, coluna, cnpjs):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Número NFS-e", coluna, "Valor do Serviço (R$)"])
    for i, c in enumerate(cnpjs, 1):
        ws.append([i, c, 100])
    wb.save(caminho)
    return caminho


# ---------------------------------------------------------------- período e nomes

@pytest.mark.parametrize("comp,esperado", [
    ("09/2026", ("2026-09-01", "2026-10-31")),
    ("11/2026", ("2026-11-01", "2026-12-31")),
    ("12/2026", ("2026-12-01", "2027-01-31")),
    ("01/2028", ("2028-01-01", "2028-02-29")),  # bissexto
])
def test_periodo_sai_da_competencia_e_nao_do_dia_de_hoje(comp, esperado):
    assert pn.periodo_da_competencia(comp) == esperado


def test_nome_do_arquivo_bate_com_a_busca_da_conferencia_do_decweb():
    nome = pn.nome_arquivo_padrao(CLIENTE, "09/2026", "Emitidas")
    assert nome == "177_ILS_PortoAlegre_09.2026_Emitidas.xlsx"
    assert fnmatch.fnmatch(nome, "177_*_09.2026_Emitidas.xlsx")  # padrão que o DecWeb procura


def test_pasta_vai_na_003_dentro_do_mes():
    assert pn.pasta_staging_mes("09/2026") == RAIZ_FECHAMENTO / "09_SETEMBRO" / "003 ARQUIVOS PORTAL NACIONAL"
    assert pn.pasta_quarentena("09/2026").parent == pn.pasta_staging_mes("09/2026")


def test_ini_de_exemplo_e_recusado(tmp_path, monkeypatch):
    ini = tmp_path / "x.ini"
    ini.write_text("[pastas]\nraiz_fechamento = C:\\AJUSTAR\\algo\n", encoding="utf-8")
    monkeypatch.setattr(configuracao, "ARQUIVO", ini)
    with pytest.raises(SystemExit):
        configuracao.carregar()


# ---------------------------------------------------------------- clientes.csv

def csv_em(tmp_path, monkeypatch, texto, bom=True):
    arq = tmp_path / "clientes.csv"
    arq.write_bytes((b"\xef\xbb\xbf" if bom else b"") + texto.encode("utf-8"))
    monkeypatch.setattr(pn, "ARQUIVO_CLIENTES", arq)


def test_csv_com_bom_linhas_em_branco_e_cnpj_com_mascara(tmp_path, monkeypatch):
    csv_em(tmp_path, monkeypatch,
           "numero,apelido,razao_social,cnpj,cidade\n177,ILS,ILS CONSULTORIA,12.345.678/0001-90,PortoAlegre\n,,,,\n")
    cs = pn.carregar_clientes()
    assert len(cs) == 1 and cs[0]["numero"] == "177" and cs[0]["cnpj"] == CNPJ


def test_csv_sem_coluna_obrigatoria(tmp_path, monkeypatch):
    csv_em(tmp_path, monkeypatch, "numero,apelido,cnpj\n177,ILS,12345678000190\n")
    with pytest.raises(ValueError, match="cidade"):
        pn.carregar_clientes()


def test_csv_com_cnpj_invalido_para(tmp_path, monkeypatch):
    csv_em(tmp_path, monkeypatch, "numero,apelido,razao_social,cnpj,cidade\n177,ILS,X,123,PortoAlegre\n")
    with pytest.raises(ValueError, match="CNPJ inválido"):
        pn.carregar_clientes()


# ---------------------------------------------------------------- conferência de CNPJ e quarentena

def test_cnpj_confere_mesmo_com_pontuacao_na_planilha(tmp_path):
    arq = xlsx(tmp_path / "e.xlsx", "CNPJ/CPF Prestador", ["12.345.678/0001-90"])
    pn.conferir_cnpj(arq, CLIENTE, "Emitidas")  # não levanta


def test_cnpj_divergente_levanta(tmp_path):
    arq = xlsx(tmp_path / "e.xlsx", "CNPJ/CPF Prestador", ["99999999000199"])
    with pytest.raises(ValueError, match="divergente"):
        pn.conferir_cnpj(arq, CLIENTE, "Emitidas")


def test_recebidas_confere_o_tomador(tmp_path):
    arq = xlsx(tmp_path / "r.xlsx", "CNPJ/CPF Tomador", [CNPJ])
    pn.conferir_cnpj(arq, CLIENTE, "Recebidas")


@pytest.fixture()
def pasta_limpa():
    base = RAIZ_FECHAMENTO
    if base.exists():
        shutil.rmtree(base)
    yield
    if base.exists():
        shutil.rmtree(base)


def test_arquivo_certo_vai_para_003_com_o_nome_padrao(tmp_path, pasta_limpa):
    arq = xlsx(tmp_path / "uuid.xlsx", "CNPJ/CPF Prestador", [CNPJ])
    destino = pn.mover_para_destino(arq, CLIENTE, "09/2026", "Emitidas")
    assert destino == pn.pasta_staging_mes("09/2026") / "177_ILS_PortoAlegre_09.2026_Emitidas.xlsx"
    assert destino.exists() and not arq.exists()


def test_arquivo_de_outro_cnpj_vai_para_quarentena_e_nao_para_a_003(tmp_path, pasta_limpa):
    arq = xlsx(tmp_path / "uuid.xlsx", "CNPJ/CPF Prestador", ["99999999000199"])
    with pytest.raises(ValueError):
        pn.mover_para_destino(arq, CLIENTE, "09/2026", "Emitidas")
    q = list(pn.pasta_quarentena("09/2026").glob("*.xlsx"))
    assert len(q) == 1
    assert not list(pn.pasta_staging_mes("09/2026").glob("*Emitidas*.xlsx"))  # a conferência nem enxerga


# ---------------------------------------------------------------- certificados

def certs():
    return [
        {"cn": f"ILS:{CNPJ}", "cnpj": CNPJ, "vence": date(2099, 1, 1), "thumb": "a"},
        {"cn": "VELHA:11111111000111", "cnpj": "11111111000111", "vence": date(2020, 1, 1), "thumb": "b"},
    ]


def test_situacao_do_certificado():
    assert pn.situacao_certificado(CNPJ, certs())[0] == "OK"
    assert pn.situacao_certificado("11111111000111", certs())[0] == "VENCIDO"
    assert pn.situacao_certificado("22222222000122", certs()) == ("SEM CERTIFICADO", None)
