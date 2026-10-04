"""Etapa A: abre o Chrome com perfil próprio e deixa o login por certificado acontecer.

Somente leitura: não clica em nada do portal. Salva um print para conferirmos a tela.
"""
from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path


def abrir_portal(url: str, perfil: Path, saida: Path, chrome_path: str | None = None,
                 espera_ms: int = 5000) -> Path:
    """Abre `url`, aguarda o usuário (certificado/login) e salva um print. Retorna o caminho do print."""
    from playwright.sync_api import sync_playwright  # importado aqui: só quem usa o navegador precisa instalar

    perfil.mkdir(parents=True, exist_ok=True)
    saida.mkdir(parents=True, exist_ok=True)
    # No Windows o Chrome roda com sandbox normal (evita a faixa "--no-sandbox"); em Linux/root desligado.
    opcoes = dict(user_data_dir=str(perfil), headless=False, accept_downloads=True, no_viewport=True,
                  chromium_sandbox=(os.name == "nt"))
    if chrome_path:
        opcoes["executable_path"] = chrome_path
    else:
        opcoes["channel"] = "chrome"  # Chrome instalado no PC: usa o repositório de certificados do Windows

    with sync_playwright() as p:
        contexto = p.chromium.launch_persistent_context(**opcoes)
        try:
            pagina = contexto.pages[0] if contexto.pages else contexto.new_page()
            pagina.goto(url, wait_until="domcontentloaded")
            pagina.wait_for_timeout(espera_ms)
            print(f"Título da página: {pagina.title()!r}")
            print(f"Endereço atual: {pagina.url}")
            input("Se pediu certificado/login, faça agora no Chrome. Quando a tela estiver pronta, tecle Enter aqui... ")
            print(f"Endereço depois do login: {pagina.url}")
            arquivo = saida / f"tela_{datetime.now():%Y%m%d_%H%M%S}.png"
            pagina.screenshot(path=str(arquivo), full_page=True)
            return arquivo
        finally:
            contexto.close()
