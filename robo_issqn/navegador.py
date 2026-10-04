"""Etapa A: abre o Chrome como um Chrome normal (perfil próprio) e se conecta a ele para o robô trabalhar.

Por que assim: o login da SEMFA usa a extensão Lacuna Web PKI, que não instala num Chrome aberto pelo
Playwright (muitas opções de automação). Aqui o Chrome é iniciado sem elas, com apenas uma porta de controle.
O Chrome continua aberto ao final, então o login feito nele vale para as próximas etapas.

Somente leitura: não clica em nada do portal. Salva um print para conferirmos a tela.
"""
from __future__ import annotations

import os
import subprocess
import time
import urllib.request
from datetime import datetime
from pathlib import Path

CANDIDATOS_WINDOWS = (
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
)


def _porta_ativa(porta: int) -> bool:
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{porta}/json/version", timeout=1).close()
        return True
    except Exception:
        return False


def _achar_chrome(chrome_path: str | None) -> str:
    if chrome_path:
        return chrome_path
    for c in CANDIDATOS_WINDOWS:
        if Path(c).exists():
            return c
    raise FileNotFoundError("Chrome não encontrado. Defina ISSQN_CHROME_PATH no .env.")


def iniciar_chrome(perfil: Path, chrome_path: str | None = None, porta: int = 9222) -> bool:
    """Garante um Chrome com porta de controle aberta. Retorna True se este chamado o iniciou."""
    if _porta_ativa(porta):
        return False
    perfil.mkdir(parents=True, exist_ok=True)
    args = [
        _achar_chrome(chrome_path),
        f"--user-data-dir={perfil.resolve()}",
        f"--remote-debugging-port={porta}",
        "--no-first-run",
        "--no-default-browser-check",
    ]
    if os.name != "nt" and hasattr(os, "geteuid") and os.geteuid() == 0:
        args.append("--no-sandbox")  # só em Linux como root (ambiente de teste)
    subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(40):
        if _porta_ativa(porta):
            return True
        time.sleep(0.5)
    raise RuntimeError(
        "O Chrome não respondeu na porta de controle. Feche TODAS as janelas do Chrome do robô "
        "(as que usam a pasta perfil_navegador) e rode de novo."
    )


def _pagina_visivel(contexto):
    paginas = contexto.pages
    for pg in reversed(paginas):
        try:
            if pg.evaluate("document.visibilityState") == "visible":
                return pg
        except Exception:
            continue
    return paginas[-1]


def abrir_portal(url: str, perfil: Path, saida: Path, chrome_path: str | None = None,
                 porta: int = 9222, espera_ms: int = 3000) -> Path:
    """Abre `url`, aguarda o usuário (certificado/login) e salva um print. Retorna o caminho do print."""
    from playwright.sync_api import sync_playwright  # só quem usa o navegador precisa instalar

    saida.mkdir(parents=True, exist_ok=True)
    novo = iniciar_chrome(perfil, chrome_path, porta)
    print("Chrome do robô iniciado." if novo else "Chrome do robô já estava aberto: reaproveitando.")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{porta}")
        contexto = browser.contexts[0]
        pagina = contexto.pages[0] if contexto.pages else contexto.new_page()
        pagina.goto(url, wait_until="domcontentloaded")
        pagina.wait_for_timeout(espera_ms)
        print(f"Título da página: {pagina.title()!r}")
        print(f"Endereço atual: {pagina.url}")
        input("Se pediu certificado/login, faça agora no Chrome. Quando a tela estiver pronta, tecle Enter aqui... ")
        for i, pg in enumerate(contexto.pages, 1):
            print(f"  aba {i}: {pg.url}")
        alvo = _pagina_visivel(contexto)
        print(f"Endereço da aba em uso: {alvo.url}")
        arquivo = saida / f"tela_{datetime.now():%Y%m%d_%H%M%S}.png"
        alvo.screenshot(path=str(arquivo), full_page=True)
        browser.close()  # só desconecta: o Chrome continua aberto
        return arquivo
