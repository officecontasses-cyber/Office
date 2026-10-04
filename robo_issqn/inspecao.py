"""Lê a estrutura da página aberta no Chrome do robô (campos, botões, links) para escrevermos os seletores.

Somente leitura: não clica, não digita, não envia nada.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .navegador import _pagina_visivel

JS_COLETA = """
() => {
  const rotulo = (el) => {
    if (el.id) { const l = document.querySelector(`label[for="${CSS.escape(el.id)}"]`); if (l) return l.innerText.trim(); }
    const p = el.closest('tr, div'); return p ? p.innerText.trim().slice(0, 60) : '';
  };
  const base = (el) => ({tag: el.tagName.toLowerCase(), id: el.id || '', name: el.name || '', type: el.type || '',
    classe: (el.className && el.className.toString().slice(0, 60)) || '', rotulo: rotulo(el)});
  const campos = [...document.querySelectorAll('input, select, textarea')].filter(e => e.type !== 'hidden').map(e => {
    const o = base(e); if (e.tagName === 'SELECT') o.opcoes = [...e.options].map(x => x.text.trim()); return o; });
  const botoes = [...document.querySelectorAll('button, input[type=button], input[type=submit], a')]
    .map(e => ({...base(e), texto: (e.innerText || e.value || '').trim().slice(0, 60), href: e.getAttribute('href') || ''}))
    .filter(b => b.texto || b.id);
  return {url: location.href, titulo: document.title, campos, botoes};
}
"""


def inspecionar(saida: Path, porta: int = 9222) -> Path:
    from playwright.sync_api import sync_playwright

    saida.mkdir(parents=True, exist_ok=True)
    arquivo = saida / f"inspecao_{datetime.now():%Y%m%d_%H%M%S}.txt"
    linhas: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{porta}")
        pagina = _pagina_visivel(browser.contexts[0])
        linhas.append(f"ABAS: {[pg.url for pg in browser.contexts[0].pages]}")
        for n, frame in enumerate(pagina.frames):
            try:
                d = frame.evaluate(JS_COLETA)
            except Exception as e:  # frame sem acesso
                linhas.append(f"\n== frame {n}: erro {e}")
                continue
            linhas.append(f"\n== frame {n}: {d['url']}  | título: {d['titulo']}")
            linhas.append("-- CAMPOS")
            for c in d["campos"]:
                linhas.append(f"  <{c['tag']} type={c['type']}> id={c['id']!r} name={c['name']!r} rótulo={c['rotulo']!r}")
                for o in c.get("opcoes", []):
                    linhas.append(f"       opção: {o}")
            linhas.append("-- BOTÕES / LINKS")
            for b in d["botoes"]:
                linhas.append(f"  <{b['tag']}> id={b['id']!r} texto={b['texto']!r} href={b['href'][:50]!r}")
        pagina.screenshot(path=str(arquivo.with_suffix(".png")), full_page=True)
        browser.close()  # só desconecta
    arquivo.write_text("\n".join(linhas), encoding="utf-8")
    return arquivo
