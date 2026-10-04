"""Etapa B2: seleciona a transmissão da competência e baixa o Livro Fiscal Eletrônico (DMS).

Clica SOMENTE em 'Livro Fiscal Eletrônico (DMS)'. Não toca em 'Apuração de Imposto à recolher'
(que gera o faturamento).
"""
from __future__ import annotations

import re
import time
from pathlib import Path

from .config import Cliente, Competencia, nome_livro_dms
from .consulta import preencher_e_localizar

PREFIXO_TABELA = "form:dataTableConsultaDMS:dataTable:"
TIPO_TRANSMISSAO = "NFSe (ADN)"
TEXTO_LIVRO = "Livro Fiscal Eletrônico (DMS)"

JS_LINKS_TABELA = """
(prefixo) => [...document.querySelectorAll('a')].filter(a => a.id.startsWith(prefixo))
  .map(a => ({id: a.id, texto: (a.innerText || '').trim()}))
"""


def linhas_da_tabela(links: list[dict]) -> dict[int, list[dict]]:
    """Agrupa os links da tabela por número de linha (form:...:dataTable:<N>:...)."""
    linhas: dict[int, list[dict]] = {}
    for l in links:
        m = re.match(re.escape(PREFIXO_TABELA) + r"(\d+):", l["id"])
        if m:
            linhas.setdefault(int(m.group(1)), []).append(l)
    return linhas


def escolher_link_da_linha(links: list[dict], comp: Competencia) -> dict:
    """Acha a única linha 'NFSe (ADN)' da competência e devolve o link da competência nela."""
    candidatas = [
        ls for ls in linhas_da_tabela(links).values()
        if any(l["texto"] == TIPO_TRANSMISSAO for l in ls) and any(l["texto"] == comp.portal for l in ls)
    ]
    if len(candidatas) != 1:
        raise LookupError(
            f"Esperava 1 transmissão '{TIPO_TRANSMISSAO}' da competência {comp.portal}, achei {len(candidatas)}. "
            "Não vou escolher no escuro: confira a tela."
        )
    return next(l for l in candidatas[0] if l["texto"] == comp.portal)


def _nome_livre(destino: Path) -> Path:
    if not destino.exists():
        return destino
    n = 2
    while destino.with_name(f"{destino.stem}_{n}{destino.suffix}").exists():
        n += 1
    return destino.with_name(f"{destino.stem}_{n}{destino.suffix}")


def baixar_livro_fiscal(cliente: Cliente, comp: Competencia, saida: Path, porta: int = 9222,
                        tempo_limite_s: int = 45) -> Path:
    from playwright.sync_api import sync_playwright

    saida.mkdir(parents=True, exist_ok=True)
    destino = _nome_livre(saida / nome_livro_dms(cliente, comp))
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{porta}")
        contexto = browser.contexts[0]
        pagina, frame = preencher_e_localizar(browser, cliente, comp)

        link = escolher_link_da_linha(frame.evaluate(JS_LINKS_TABELA, PREFIXO_TABELA), comp)
        print(f"Selecionando a transmissão ({link['texto']})...")
        frame.locator(f"a[id='{link['id']}']").click()
        pagina.wait_for_timeout(2000)

        # captura o PDF seja por download, seja por resposta de rede (aba do visualizador)
        capturado: dict = {}
        paginas_antes = set(contexto.pages)

        def ao_baixar(download):
            download.save_as(str(destino))
            capturado["ok"] = "download"

        def ao_responder(resp):
            if capturado:
                return
            tipo = (resp.headers.get("content-type") or "").lower()
            if "application/pdf" in tipo and resp.status == 200:
                try:
                    corpo = resp.body()
                except Exception:
                    return
                if corpo[:4] == b"%PDF":
                    destino.write_bytes(corpo)
                    capturado["ok"] = "resposta"

        for pg in contexto.pages:
            pg.on("download", ao_baixar)
        contexto.on("page", lambda pg: pg.on("download", ao_baixar))
        contexto.on("response", ao_responder)

        print(f"Clicando em '{TEXTO_LIVRO}'...")
        frame.get_by_text(TEXTO_LIVRO, exact=True).click()
        limite = time.time() + tempo_limite_s
        while not capturado and time.time() < limite:
            pagina.wait_for_timeout(500)

        for pg in set(contexto.pages) - paginas_antes:  # fecha a aba do visualizador, se abriu
            try:
                pg.close()
            except Exception:
                pass
        browser.close()  # só desconecta

    if not capturado:
        raise RuntimeError(
            f"O PDF não chegou em {tempo_limite_s}s. Veja a janela do Chrome do robô e me conte o que apareceu."
        )
    if destino.read_bytes()[:4] != b"%PDF":
        raise RuntimeError(f"O arquivo salvo não parece um PDF: {destino}")
    print(f"PDF obtido por {capturado['ok']}: {destino.stat().st_size} bytes")
    return destino
