"""Etapa B (parte 1): preenche a Consulta DMS e clica em Localizar. Só consulta; não gera nada.

A tela fica num iframe (consultaDMSExterno.faces) dentro de programaAcessoExternoPortal.faces.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .config import Cliente, Competencia
from .inspecao import JS_COLETA

SEL_CONTRIBUINTE = "select[id='form:inscricaoResponsavel:select']"
SEL_COMP_DE = "input[id='form:competenciaIntervalo:fieldCaracter1:field']"
SEL_COMP_ATE = "input[id='form:competenciaIntervalo:fieldCaracter2:field']"
SEL_LOCALIZAR = "input[type=submit][value='Localizar']"

JS_TABELAS = """
() => [...document.querySelectorAll('table')].map((t, i) => ({
  i, id: t.id || '',
  linhas: [...t.querySelectorAll('tr')].map(tr => ({
    texto: [...tr.children].map(c => c.innerText.trim().replace(/\\s+/g, ' ')).join(' | ').slice(0, 220),
    acoes: [...tr.querySelectorAll('a, input[type=submit], input[type=button], button')]
      .map(e => `<${e.tagName.toLowerCase()} id=${e.id} texto=${(e.innerText || e.value || '').trim().slice(0, 40)}>`),
  })).filter(l => l.texto.replace(/[| ]/g, '')),
})).filter(t => t.linhas.length)
"""


def escolher_opcao(opcoes: list[str], inscricao: str) -> str:
    """Devolve a opção do Contribuinte que contém [inscrição]. Erro se não houver exatamente uma."""
    achadas = [o for o in opcoes if f"[{inscricao}]" in o]
    if len(achadas) != 1:
        raise LookupError(f"Esperava 1 contribuinte com [{inscricao}], achei {len(achadas)}: {achadas}")
    return achadas[0]


def achar_frame_dms(contexto):
    for pagina in contexto.pages:
        for frame in pagina.frames:
            if "consultaDMSExterno" in frame.url:
                return pagina, frame
    raise RuntimeError(
        "Não achei a tela Consulta DMS aberta no Chrome do robô. "
        "Abra Serviços > ... > 'Relatório, Apuração e guia Nota Fiscal Nacional' e tente de novo."
    )


def preencher_e_localizar(browser, cliente: Cliente, comp: Competencia):
    """Escolhe o contribuinte, preenche a competência e clica em Localizar. Retorna (pagina, frame)."""
    pagina, frame = achar_frame_dms(browser.contexts[0])

    opcoes = frame.locator(f"{SEL_CONTRIBUINTE} option").all_inner_texts()
    opcao = escolher_opcao([o.strip() for o in opcoes], cliente.inscricao_municipal)
    frame.select_option(SEL_CONTRIBUINTE, label=opcao)
    pagina.wait_for_timeout(1500)  # o portal pode recarregar o formulário ao trocar o contribuinte
    print(f"Contribuinte: {opcao}")

    for seletor in (SEL_COMP_DE, SEL_COMP_ATE):
        campo = frame.locator(seletor)
        campo.click()
        campo.fill("")
        campo.press_sequentially(comp.portal, delay=60)  # digitando, para respeitar máscaras do campo
    print(f"Competência: {comp.portal} a {comp.portal}")

    frame.locator(SEL_LOCALIZAR).first.click()
    try:
        pagina.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        pass
    pagina.wait_for_timeout(2000)
    return achar_frame_dms(browser.contexts[0])  # a tela pode ter sido recarregada


def consultar(cliente: Cliente, comp: Competencia, saida: Path, porta: int = 9222) -> Path:
    from playwright.sync_api import sync_playwright

    saida.mkdir(parents=True, exist_ok=True)
    marca = f"{datetime.now():%Y%m%d_%H%M%S}"
    relatorio = saida / f"consulta_{cliente.codigo}_{comp.mm_aaaa}_{marca}.txt"
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{porta}")
        pagina, frame = preencher_e_localizar(browser, cliente, comp)
        linhas = [f"CONSULTA {cliente.codigo} {comp.portal} | {frame.url}", ""]
        for t in frame.evaluate(JS_TABELAS):
            linhas.append(f"== tabela #{t['i']} id={t['id']!r}")
            for l in t["linhas"]:
                linhas.append(f"  {l['texto']}")
                for a in l["acoes"]:
                    linhas.append(f"      ação: {a}")
        d = frame.evaluate(JS_COLETA)
        linhas.append("\n== BOTÕES / LINKS APÓS LOCALIZAR")
        for b in d["botoes"]:
            linhas.append(f"  <{b['tag']}> id={b['id']!r} texto={b['texto']!r}")
        relatorio.write_text("\n".join(linhas), encoding="utf-8")
        pagina.screenshot(path=str(relatorio.with_suffix(".png")), full_page=True)
        browser.close()  # só desconecta
    return relatorio
