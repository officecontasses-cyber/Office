"""Testes da adaptação do robô DecWeb ao OfficeCont (tudo offline, planilhas sintéticas)."""
import io
import zipfile
from pathlib import Path

import openpyxl
import pytest

import conferencia_prestados as cp
import configuracao
import decweb_login as dl
from conftest import RAIZ_FECHAMENTO

CNPJ = "12.345.678/0001-90"
CLIENTE = {"numero": "177", "apelido": "ILS", "nome_painel": "ILS CONSULTORIA", "cnpj": "12345678000190"}


# ---------------------------------------------------------------- planilhas sintéticas

def xlsx_decweb(notas, competencia="09/2026 Original"):
    """notas: [(numero_com_prefixo, valor, situacao)] no layout real do ISSQNdec."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["ISSQNdec - Relação de Serviços Prestados"])
    ws.append(["Inscrição Municipal:", "000000-0-0"])
    ws.append(["Competência:", competencia])
    ws.append(["Nome da Empresa:", "EMPRESA TESTE"])
    ws.append(["CNPJ:", CNPJ])
    ws.append(["Número NFSE", "Data Em. Nota", "Nome Tomador", "Valor Serviços", "Situação."])
    for num, valor, sit in notas:
        ws.append([num, "01/09/2026", "TOMADOR", valor, sit])
    ws.append(["TOTAL", "TOTAL", "TOTAL", "TOTAL"])
    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue()


def xlsx_emitidas(notas, cnpj=CNPJ):
    """notas: [(numero, competencia, valor, situacao)] no layout real do Portal Nacional."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Relação"
    ws.append(["Número NFS-e", "Competência", "CNPJ/CPF Prestador", "Valor do Serviço (R$)", "Situação NFS-e", "Situação"])
    for num, comp, valor, sit in notas:
        ws.append([num, comp, cnpj, valor, "100 - NFS-e Gerada", sit])
    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue()


@pytest.fixture()
def pastas():
    mun = configuracao.pasta_municipais(configuracao.carregar(), "09")
    nac = configuracao.pasta_nacional(configuracao.carregar(), "09")
    mun.mkdir(parents=True, exist_ok=True)
    nac.mkdir(parents=True, exist_ok=True)
    for pasta in (mun, nac):
        for f in pasta.iterdir():
            if f.is_file():
                f.unlink()
            else:
                import shutil
                shutil.rmtree(f)
    return mun, nac


def grava_prestados_em_pasta(mun, conteudo):
    base = cp.nome_base_prestados(CLIENTE, "09", "2026")
    (mun / base).mkdir(exist_ok=True)
    (mun / base / "000000_202609_NFSE_ServPrestados.xlsx").write_bytes(conteudo)


# ---------------------------------------------------------------- configuração e caminhos

def test_pastas_primeiro_o_mes_depois_o_tipo():
    cfg = configuracao.carregar()
    assert configuracao.pasta_municipais(cfg, "09") == RAIZ_FECHAMENTO / "09_SETEMBRO" / "002 ARQUIVOS MUNICIPAIS"
    assert configuracao.pasta_nacional(cfg, "08") == RAIZ_FECHAMENTO / "08_AGOSTO" / "003 ARQUIVOS PORTAL NACIONAL"
    assert dl.pasta_download_da_competencia("09/2026") == str(configuracao.pasta_municipais(cfg, "09"))


def test_padroes_do_ini():
    cfg = configuracao.carregar()
    assert cfg["conferencia"] is False and cfg["sem_emitidas"] == "enviar"
    assert dl.CONFERENCIA_ATIVA is False


def test_nomes_de_arquivo_na_convencao_do_escritorio():
    c = {"numero": "205", "apelido": "L S Becker"}
    assert dl.nome_arquivo_padrao(c, "09/2026", "NFSE_ServPrestados", "zip") == "205_L S Becker_PortoAlegre_09.2026_NFSE_ServPrestados.zip"
    assert dl.nome_arquivo_padrao(c, "09/2026", "NFSE_ServTomados", "zip") == "205_L S Becker_PortoAlegre_09.2026_NFSE_ServTomados.zip"
    assert dl.nome_arquivo_padrao(c, "09/2026", "DeclaraçãoMensal", "pdf") == "205_L S Becker_PortoAlegre_09.2026_DeclaraçãoMensal.pdf"
    assert dl.nome_arquivo_padrao({"numero": "186", "apelido": "Lopes&Nadal"}, "09/2026", "ISSQN", "pdf") == "186_Lopes&Nadal_PortoAlegre_09.2026_ISSQN.pdf"


# ---------------------------------------------------------------- clientes.csv

def test_csv_com_bom_linhas_em_branco_e_aceitar_avisos(tmp_path, monkeypatch):
    arq = tmp_path / "clientes.csv"
    arq.write_bytes(
        "﻿numero,apelido,nome_painel,cnpj,usuario,senha,aceitar_avisos\n"
        "177, ILS ,ILS CONSULTORIA,11.111.111/0001-91,111,x,\n"
        ",,,,,,\n"
        "173,Lopes&Martins,LOPES & MARTINS,22222222000191,222,y,SIM\n".encode("utf-8")
    )
    monkeypatch.setattr(dl, "ARQUIVO_CLIENTES", arq)
    clientes = dl.carregar_clientes()
    assert [c["numero"] for c in clientes] == ["177", "173"]
    assert clientes[0]["apelido"] == "ILS" and clientes[0]["cnpj"] == "11111111000191"
    assert clientes[0]["aceitar_avisos"] is False and clientes[1]["aceitar_avisos"] is True


def test_csv_sem_coluna_obrigatoria(tmp_path, monkeypatch):
    arq = tmp_path / "clientes.csv"
    arq.write_text("numero,apelido\n1,A\n", encoding="utf-8")
    monkeypatch.setattr(dl, "ARQUIVO_CLIENTES", arq)
    with pytest.raises(ValueError, match="faltam as colunas"):
        dl.carregar_clientes()


# ---------------------------------------------------------------- extração do zip

def test_extrai_zip_em_subpasta_e_mantem_o_zip(tmp_path):
    arq = tmp_path / "177_ILS_PortoAlegre_09.2026_NFSE_ServPrestados.zip"
    with zipfile.ZipFile(arq, "w") as z:
        z.writestr("28268024_202609_NFSE_ServPrestados.xlsx", b"conteudo")
    destino = dl.extrair_zip_na_pasta(arq)
    assert destino == tmp_path / "177_ILS_PortoAlegre_09.2026_NFSE_ServPrestados"
    assert (destino / "28268024_202609_NFSE_ServPrestados.xlsx").read_bytes() == b"conteudo"
    assert arq.exists()


def test_extracao_recusa_caminho_suspeito_no_zip(tmp_path):
    arq = tmp_path / "x.zip"
    with zipfile.ZipFile(arq, "w") as z:
        z.writestr("../fora.txt", b"mal")
    assert dl.extrair_zip_na_pasta(arq) is None
    assert not (tmp_path / "fora.txt").exists()


# ---------------------------------------------------------------- leitores e conferência

def test_leitor_decweb_ignora_canceladas_e_usa_6_ultimos_digitos():
    r = cp.ler_decweb_prestados(xlsx_decweb([
        ("202610000000001342", 1000.5, "Normal"),
        ("202610000000001343", 200.0, "Cancelada"),
    ]))
    assert r["competencia"] == "09/2026 Original"
    assert r["notas"] == {1342: {"valor": 1000.5, "situacao": "Normal"}}


def test_conferencia_ok_achando_a_emitidas_pelo_cnpj_e_nao_pelo_nome(pastas):
    mun, nac = pastas
    grava_prestados_em_pasta(mun, xlsx_decweb([("202610000000001342", 1000.5, "Normal")]))
    # nome de arquivo com razão social, como no Drive real, e outro cliente na mesma pasta
    (nac / "ILS CONSULTORIA EMPRESARIAL LTDA - Emitidas.xlsx").write_bytes(
        xlsx_emitidas([(1342, "09/2026", 1000.5, "Normal"), (1300, "08/2026", 50.0, "Normal")]))
    (nac / "OUTRA EMPRESA LTDA - Emitidas.xlsx").write_bytes(
        xlsx_emitidas([(9, "09/2026", 7.0, "Normal")], cnpj="99.999.999/0001-99"))
    sit, texto = cp.conferir_cliente(CLIENTE, "09/2026")
    assert sit == "ok", texto


def test_conferencia_divergencia_de_valor_e_de_nota(pastas):
    mun, nac = pastas
    grava_prestados_em_pasta(mun, xlsx_decweb([("202610000000001342", 1000.0, "Normal")]))
    (nac / "X - Emitidas.xlsx").write_bytes(xlsx_emitidas([(1342, "09/2026", 900.0, "Normal"), (1343, "09/2026", 5.0, "Normal")]))
    sit, texto = cp.conferir_cliente(CLIENTE, "09/2026")
    assert sit == "divergencia" and "1343" in texto and "valor diferente" in texto


def test_conferencia_le_o_decweb_tambem_do_zip(pastas):
    mun, nac = pastas
    base = cp.nome_base_prestados(CLIENTE, "09", "2026")
    with zipfile.ZipFile(mun / f"{base}.zip", "w") as z:
        z.writestr("a.xlsx", xlsx_decweb([("202610000000000012", 26520.0, "Normal")]))
    (nac / "X - Emitidas.xlsx").write_bytes(xlsx_emitidas([(12, "09/2026", 26520.0, "Normal")]))
    assert cp.conferir_cliente(CLIENTE, "09/2026")[0] == "ok"


def test_sem_emitidas_e_situacao_propria(pastas):
    mun, _nac = pastas
    grava_prestados_em_pasta(mun, xlsx_decweb([("202610000000001342", 1000.5, "Normal")]))
    sit, texto = cp.conferir_cliente(CLIENTE, "09/2026")
    assert sit == "sem_emitidas" and "1 nota" in texto
    # cliente sem movimento: sem zip no DecWeb e sem Emitidas
    assert cp.conferir_cliente({**CLIENTE, "numero": "999"}, "09/2026")[0] == "sem_emitidas"


def test_nacional_com_notas_e_sem_prestados_no_decweb_diverge(pastas):
    _mun, nac = pastas
    (nac / "X - Emitidas.xlsx").write_bytes(xlsx_emitidas([(1, "09/2026", 10.0, "Normal")]))
    assert cp.conferir_cliente(CLIENTE, "09/2026")[0] == "divergencia"


# ---------------------------------------------------------------- política de envio (_conferir_ou_bloquear)

def _com_conferencia(monkeypatch, ativa, situacao, politica="enviar"):
    monkeypatch.setattr(dl, "CONFERENCIA_ATIVA", ativa)
    monkeypatch.setattr(dl, "POLITICA_SEM_EMITIDAS", politica)
    monkeypatch.setattr(dl.cp, "conferir_cliente", lambda c, comp, cfg=None: (situacao, "texto"))


def test_conferencia_desligada_nao_bloqueia(monkeypatch):
    _com_conferencia(monkeypatch, False, "divergencia")
    c = {"nome_painel": "X", "_etapas": set()}
    dl._conferir_ou_bloquear(c, "09/2026")
    assert "conferido" not in c["_etapas"]


def test_conferencia_ok_marca_etapa(monkeypatch):
    _com_conferencia(monkeypatch, True, "ok")
    c = {"nome_painel": "X", "_etapas": set()}
    dl._conferir_ou_bloquear(c, "09/2026")
    assert "conferido" in c["_etapas"]


def test_divergencia_bloqueia(monkeypatch):
    _com_conferencia(monkeypatch, True, "divergencia")
    with pytest.raises(dl.PendenciaNoDecWeb):
        dl._conferir_ou_bloquear({"nome_painel": "X", "_etapas": set()}, "09/2026")


def test_sem_emitidas_envia_ou_bloqueia_conforme_a_politica(monkeypatch):
    _com_conferencia(monkeypatch, True, "sem_emitidas", "enviar")
    dl._conferir_ou_bloquear({"nome_painel": "X", "_etapas": set()}, "09/2026")
    _com_conferencia(monkeypatch, True, "sem_emitidas", "bloquear")
    with pytest.raises(dl.PendenciaNoDecWeb):
        dl._conferir_ou_bloquear({"nome_painel": "X", "_etapas": set()}, "09/2026")


# ---------------------------------------------------------------- avisos de receita zero (por cliente)

class _EsperaFalsa:
    def __init__(self, *a, **k):
        pass

    def until(self, cond, *a, **k):
        return True


def _modal(monkeypatch, pendencias, aceitar_global=False, aceitar_cliente=False):
    """Simula o modal 'Preparar' de uma declaração nova: só 'Preparar' (idCbPrep) e 'Cancelar', com avisos."""
    cliques = []
    monkeypatch.setattr(dl, "WebDriverWait", _EsperaFalsa)
    monkeypatch.setattr(dl, "_elemento_visivel",
                        lambda d, xp: ("idCbPrep" in xp) and True or False)
    monkeypatch.setattr(dl, "_pendencias_do_modal", lambda d: pendencias)
    monkeypatch.setattr(dl, "_clicar_xpath", lambda d, xp, *a, **k: cliques.append(xp))
    monkeypatch.setattr(dl, "ACEITAR_AVISOS", aceitar_global)
    monkeypatch.setattr(dl, "ACEITAR_AVISOS_CLIENTE", aceitar_cliente)
    return cliques


AVISO = "Não foi informado serviço prestado na escrituração 09/2026"


def test_aviso_de_receita_zero_sem_permissao_bloqueia(monkeypatch):
    _modal(monkeypatch, [AVISO])
    with pytest.raises(dl.PendenciaNoDecWeb):
        dl._confirmar_modal_preparar(object())


def test_aviso_de_receita_zero_com_permissao_do_cliente_prepara(monkeypatch):
    cliques = _modal(monkeypatch, [AVISO], aceitar_cliente=True)
    assert dl._confirmar_modal_preparar(object()) is True
    assert any("idCbPrep" in c for c in cliques)
    assert not any("idCbSalvarNovo" in c for c in cliques)  # nunca 'Preparar e Enviar' por esse caminho


def test_outra_pendencia_continua_bloqueando_mesmo_com_permissao(monkeypatch):
    _modal(monkeypatch, [AVISO, "Cadastro do responsável é necessário"], aceitar_global=True, aceitar_cliente=True)
    with pytest.raises(dl.PendenciaNoDecWeb):
        dl._confirmar_modal_preparar(object())


# ---------------------------------------------------------------- aviso com movimento no mês
# O DecWeb dá a MESMA mensagem para quem não teve nota nenhuma e para quem só emite por NFS-e
# (a escrituração manual fica vazia). O relatório de Prestados que o robô acabou de baixar desempata.

def _modal_com_cliente(monkeypatch, pendencias, **kw):
    cliques = _modal(monkeypatch, pendencias, **kw)
    monkeypatch.setattr(dl, "CLIENTE_ATUAL", {**CLIENTE, "_etapas": set()})
    monkeypatch.setattr(dl, "COMPETENCIA_ATUAL", "09/2026")
    return cliques


def test_aviso_com_notas_no_prestados_segue_sem_precisar_de_permissao(monkeypatch, pastas):
    mun, _ = pastas
    grava_prestados_em_pasta(mun, xlsx_decweb([("NFSE 000123", 1500.0, "Normal")]))
    cliques = _modal_com_cliente(monkeypatch, [AVISO])
    assert dl._confirmar_modal_preparar(object()) is True
    assert any("idCbPrep" in c for c in cliques)
    assert not any("idCbSalvarNovo" in c for c in cliques)  # nunca 'Preparar e Enviar'
    assert "aviso_escrituracao_aceito" in dl.CLIENTE_ATUAL["_etapas"]


def test_aviso_com_prestados_vazio_continua_bloqueando_e_explica(monkeypatch, pastas):
    mun, _ = pastas
    grava_prestados_em_pasta(mun, xlsx_decweb([]))
    _modal_com_cliente(monkeypatch, [AVISO])
    with pytest.raises(dl.PendenciaNoDecWeb, match="receita zero"):
        dl._confirmar_modal_preparar(object())


def test_sem_relatorio_baixado_continua_bloqueando(monkeypatch, pastas):
    _modal_com_cliente(monkeypatch, [AVISO])
    with pytest.raises(dl.PendenciaNoDecWeb):
        dl._confirmar_modal_preparar(object())


def test_outra_pendencia_bloqueia_mesmo_com_notas(monkeypatch, pastas):
    mun, _ = pastas
    grava_prestados_em_pasta(mun, xlsx_decweb([("NFSE 000123", 1500.0, "Normal")]))
    _modal_com_cliente(monkeypatch, [AVISO, "Cadastro do responsável é necessário"])
    with pytest.raises(dl.PendenciaNoDecWeb):
        dl._confirmar_modal_preparar(object())
