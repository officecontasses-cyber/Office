"""
Automação Portal Nacional NFS-e (nfse.gov.br)
==================================================================

Robô que faz login no Portal Nacional da NFS-e com o certificado digital
do cliente e usa a extensão de Chrome "Baixar NFSe Nota Fiscal de Serviço
Eletrônica Emitidas e Recebidas" (Chrome Web Store, id
enehmclajcndmgefbmjhecccoegbdgea) pra baixar os relatórios "Completa" de
Emitidas e Recebidas do período, salvando com o nome padrão do escritório
na pasta de staging mensal.

ADAPTADO PARA A OFFICECONT (02/10/2026) a partir do pacote de outro escritório:
  - pasta de saída: <raiz_fechamento>\\<MM_MES>\\003 ARQUIVOS PORTAL NACIONAL (mesmo configuracao.ini do DecWeb);
  - período baixado: derivado da COMPETÊNCIA pedida (1º dia do mês dela até o último dia do mês seguinte),
    não mais "mês anterior + mês atual" relativo ao dia em que o robô roda;
  - clientes.csv: aceita BOM do Excel, linhas em branco e CNPJ com pontuação; confere as colunas.

FASE 1 (única fase por enquanto):
  1. Abre o Chrome com um PERFIL DEDICADO do robô (não o perfil pessoal),
     onde a extensão já precisa estar instalada uma vez (ver README).
  2. Vai em /EmissorNacional/Login e navega direto pro link de acesso via
     certificado digital (https://certificado.nfse.gov.br/EmissorNacional/
     Certificado) — isso dispara o seletor NATIVO de certificado do
     Windows/Chrome, que nenhuma automação de navegador consegue clicar.
     O robô PAUSA aqui e pede pra você escolher o certificado do cliente
     na janela que abrir.
  3. Depois de logado, abre a extensão direto pela URL dela
     (chrome-extension://.../popup.html) — não precisa clicar no ícone da
     barra de ferramentas.
  4. Pra cada tipo (Emitidas, Recebidas): seleciona o tipo, preenche o
     período no modelo "Mês Anterior e Atual" (do dia 1 do mês anterior
     até o último dia da competência pedida — igual ao atalho da própria
     extensão, pra não perder nota lançada com atraso) e clica "Completa".
     A extensão lê nota por nota (pode demorar minutos se tiver muitas
     notas) e no final dispara um download.
  5. Espera a mensagem final em #status ("Relação completa gerada com N
     nota(s)"). Se N=0, não tem nada pra baixar, segue pro próximo tipo.
     Se N>0, espera o .xlsx aparecer em <pasta_download_temp>/ (o Chrome
     salva com nome aleatório, ignorando o nome/subpasta que a extensão
     pede — não dá pra filtrar por nome) e move + renomeia pro padrão do
     escritório, dentro de 999 ROTINAS AUTOMÁTICAS/001 FECHAMENTO
     FISCAL/003 ARQUIVOS PORTAL NACIONAL/{MM}_{MÊS}/.

Nome final do arquivo: {numero}_{apelido}_{cidade}_MM.AAAA_{Emitidas|
Recebidas}.xlsx (ex.: 25_Lutecksolar_PortoAlegre_09.2026_Emitidas.xlsx) —
mesmo padrão {numero}_{apelido}_{cidade}_MM.AAAA_{TipoDocumento} que a
skill de realocação de documentos fiscais já reconhece.

✅ TESTADO DE PONTA A PONTA (07/09/2026), 2 clientes reais (15 -
Terceirizza, 23 - Escola da Licitocon), competência 09/2026 — login,
Emitidas, Recebidas, arquivo movido e renomeado certinho. Detalhes de
cada achado/correção no README (seção "Status atual").

Uso:
    pip install -r requirements.txt
    copie config/clientes.exemplo.csv para conferir o formato — o
    config/clientes.csv real já foi gerado a partir da base de clientes
    (999.../04 Controle de Clientes), filtrado por "Adesão Portal
    Nacional = SIM"
    python portal_nacional_download.py
"""

import argparse
import csv
import json
import logging
import os
import re
import shutil
import subprocess
import time
import unicodedata
from datetime import date, datetime
from pathlib import Path

try:
    import winreg  # só existe no Windows (seleção automática de certificado)
except ImportError:  # pragma: no cover
    winreg = None

import openpyxl

import portal_config

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# ----------------------------------------------------------------------
# CONFIGURAÇÃO
# ----------------------------------------------------------------------

URL_LOGIN = "https://www.nfse.gov.br/EmissorNacional/Login"
URL_CERTIFICADO = "https://certificado.nfse.gov.br/EmissorNacional/Certificado"

EXTENSAO_ID = "enehmclajcndmgefbmjhecccoegbdgea"
URL_EXTENSAO = f"chrome-extension://{EXTENSAO_ID}/popup.html"

RAIZ_PROJETO = Path(__file__).parent
ARQUIVO_CLIENTES = RAIZ_PROJETO / "config" / "clientes.csv"
PASTA_LOGS = RAIZ_PROJETO / "logs"

# O perfil do Chrome e a pasta de download temporária ficam em DISCO LOCAL
# (não no Drive de rede J:) — confirmado na prática (08/09/2026): o Chrome
# solta erros de sandbox ("Failed to grant sandbox access to cache
# directory ... Parâmetro incorreto") quando o perfil está numa unidade de
# rede, e isso causa instabilidade real (janela fechando sozinha, conexão
# resetando, extensão "desativada"/bloqueada). Só os arquivos do projeto
# (script, config, logs) ficam no Drive — o perfil do navegador, não.
# Caminho SEM ACENTO de propósito: com o perfil embaixo de
# "C:\Users\Usuário\..." o bash, o PowerShell e o Python discordavam sobre
# o que existia na pasta (o acento é decodificado de formas diferentes por
# cada um), o que gerou horas de diagnóstico enganoso em 08/09/2026.
PASTA_LOCAL_ROBO = Path(os.environ.get("PORTAL_NACIONAL_ROBO_DIR", r"C:\PortalNacionalRobo"))
PASTA_PERFIL_CHROME = PASTA_LOCAL_ROBO / "perfil_chrome_robo"
PASTA_DOWNLOAD_TEMP = PASTA_LOCAL_ROBO / "_downloads_temp"

# Pasta-raiz do fechamento (config/configuracao.ini, o mesmo do DecWeb). Os relatórios vão para
# <raiz>\\<MM_MES>\\003 ARQUIVOS PORTAL NACIONAL. Lida na primeira vez que é preciso (não no import).
_CFG: dict | None = None


def _cfg() -> dict:
    global _CFG
    if _CFG is None:
        _CFG = portal_config.carregar()
    return _CFG


TIMEOUT_LOGIN_SEGUNDOS = 180  # tempo pra escolher o certificado na janela nativa
TIMEOUT_RELACAO_SEGUNDOS = 1200  # "Completa" lê nota por nota: cliente 29 levou 5,5 min (08/09/2026)

PASTA_LOGS.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            PASTA_LOGS / f"execucao_{datetime.now():%Y%m%d_%H%M%S}.log",
            encoding="utf-8",
        ),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("portal_nacional")

COLUNAS_OBRIGATORIAS = ("numero", "apelido", "cnpj", "cidade")


# ----------------------------------------------------------------------
# LEITURA DA LISTA DE CLIENTES
# ----------------------------------------------------------------------

def _so_digitos(v) -> str:
    return re.sub(r"\D", "", str(v or ""))


def carregar_clientes() -> list[dict]:
    """Lê config/clientes.csv (UTF-8, com ou sem BOM do Excel). Ignora linhas em branco, tira espaços e deixa o
    CNPJ só com dígitos (14). Para o programa se faltar coluna ou se algum CNPJ não tiver 14 dígitos."""
    if not ARQUIVO_CLIENTES.exists():
        raise FileNotFoundError(
            f"Não encontrei {ARQUIVO_CLIENTES}.\n"
            "Copie config/clientes.exemplo.csv para config/clientes.csv e "
            "preencha uma linha por empresa."
        )
    with open(ARQUIVO_CLIENTES, encoding="utf-8-sig", newline="") as f:
        leitor = csv.DictReader(f)
        faltam = [c for c in COLUNAS_OBRIGATORIAS if c not in (leitor.fieldnames or [])]
        if faltam:
            raise ValueError(f"{ARQUIVO_CLIENTES.name}: faltam as colunas {', '.join(faltam)}.")
        clientes = []
        for linha in leitor:
            c = {k: (v or "").strip() for k, v in linha.items() if k}
            if not any(c.values()):
                continue
            c["cnpj"] = _so_digitos(c["cnpj"])
            if len(c["cnpj"]) != 14:
                raise ValueError(f"{ARQUIVO_CLIENTES.name}: cliente {c['numero']} ({c['apelido']}) com CNPJ inválido.")
            clientes.append(c)
    return clientes


# ----------------------------------------------------------------------
# CERTIFICADOS DIGITAIS (seleção automática — elimina a pausa manual)
# ----------------------------------------------------------------------
# O nome (CN) de cada certificado e-CNPJ traz o CNPJ: "RAZAO SOCIAL:CNPJ14".
# O robô lê o repositório do Windows (Usuário Atual), acha o certificado
# válido do CNPJ do cliente e grava, ANTES de abrir o Chrome daquele cliente,
# a política AutoSelectCertificateForUrls (HKCU, sem precisar de
# administrador) apontando só pra esse certificado. Como cada cliente roda
# num Chrome novo, a política vale sozinha pra ele. No fim (qualquer que
# seja o resultado) a política é apagada.

CHAVE_POLITICA_CERT = r"Software\Policies\Google\Chrome\AutoSelectCertificateForUrls"
PADRAO_URL_CERT = "https://certificado.nfse.gov.br"


def listar_certificados() -> list[dict]:
    """Certificados com chave privada do repositório Usuário Atual, que
    tenham CNPJ no CN. Retorna dicts: cn, cnpj, vence (date), thumb."""
    script = (
        "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; "
        "Get-ChildItem Cert:\\CurrentUser\\My | Where-Object { $_.HasPrivateKey } | "
        "ForEach-Object { [pscustomobject]@{ Subject = $_.Subject; "
        "NotAfter = $_.NotAfter.ToString('yyyy-MM-dd'); Thumb = $_.Thumbprint } } | "
        "ConvertTo-Json -Compress"
    )
    r = subprocess.run(
        ["powershell", "-NoProfile", "-Command", script],
        capture_output=True, encoding="utf-8", timeout=120,
    )
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError(f"Não consegui listar os certificados do Windows: {r.stderr.strip()[:300]}")
    dados = json.loads(r.stdout)
    if isinstance(dados, dict):
        dados = [dados]
    certs = []
    for d in dados:
        m = re.search(r'CN="?(.+?):(\d{14})"?(?:,|$)', d["Subject"])
        if not m:
            continue  # e-CPF ou certificado sem CNPJ no nome
        certs.append({
            "cn": f"{m.group(1)}:{m.group(2)}",
            "cnpj": m.group(2),
            "vence": date.fromisoformat(d["NotAfter"]),
            "thumb": d["Thumb"],
        })
    return certs


def situacao_certificado(cnpj: str, certs: list[dict]) -> tuple[str, dict | None]:
    """('OK', cert) | ('VENCIDO', cert_mais_recente) | ('SEM CERTIFICADO', None)."""
    do_cnpj = [c for c in certs if c["cnpj"] == cnpj]
    if not do_cnpj:
        return "SEM CERTIFICADO", None
    validos = [c for c in do_cnpj if c["vence"] >= date.today()]
    if validos:
        return "OK", max(validos, key=lambda c: c["vence"])
    return "VENCIDO", max(do_cnpj, key=lambda c: c["vence"])


def definir_politica_certificado(cn: str) -> None:
    """Grava a regra de seleção automática só pro certificado com esse CN."""
    if winreg is None:
        raise RuntimeError("Seleção automática de certificado só funciona no Windows.")
    regra = {"pattern": PADRAO_URL_CERT, "filter": {"SUBJECT": {"CN": cn}}}
    with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, CHAVE_POLITICA_CERT, 0, winreg.KEY_SET_VALUE) as k:
        winreg.SetValueEx(k, "1", 0, winreg.REG_SZ, json.dumps(regra, ensure_ascii=False))


def remover_politica_certificado() -> None:
    """Apaga a regra e as chaves que o robô criou (só se ficaram vazias)."""
    if winreg is None:
        return
    caminhos = [
        CHAVE_POLITICA_CERT,
        r"Software\Policies\Google\Chrome",
        r"Software\Policies\Google",
    ]
    for caminho in caminhos:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, caminho) as k:
                subchaves, valores, _ = winreg.QueryInfoKey(k)
            if caminho != CHAVE_POLITICA_CERT and (subchaves or valores):
                break  # tem coisa de outra pessoa: não mexe
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, caminho)
        except FileNotFoundError:
            continue
        except OSError:
            break


def relatorio_certificados(clientes: list[dict]) -> list[dict]:
    """Situação do certificado de cada cliente (imprime e salva em
    logs/certificados_status.csv, pro Painel)."""
    certs = listar_certificados()
    linhas = []
    for c in sorted(clientes, key=lambda c: int(c["numero"])):
        sit, cert = situacao_certificado(re.sub(r"\D", "", c["cnpj"]), certs)
        linhas.append({
            "numero": c["numero"], "apelido": c["apelido"], "situacao": sit,
            "vence": cert["vence"].strftime("%d/%m/%Y") if cert else "",
        })
    PASTA_LOGS.mkdir(exist_ok=True)
    with open(PASTA_LOGS / "certificados_status.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["numero", "apelido", "situacao", "vence"])
        w.writeheader()
        w.writerows(linhas)
    return linhas


# ----------------------------------------------------------------------
# CHROME COM PERFIL DEDICADO (onde a extensão já está instalada)
# ----------------------------------------------------------------------

def montar_driver() -> webdriver.Chrome:
    PASTA_PERFIL_CHROME.mkdir(parents=True, exist_ok=True)
    PASTA_DOWNLOAD_TEMP.mkdir(parents=True, exist_ok=True)

    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument(f"--user-data-dir={PASTA_PERFIL_CHROME.resolve()}")

    # A extensão precisa estar instalada pela Chrome Web Store NESTE perfil
    # (uma vez só — ver README). Tentamos carregar uma cópia descompactada
    # com --load-extension, mas o Chrome estável recusa: "--load-extension
    # is not allowed in Google Chrome, ignoring" (confirmado 08/09/2026).
    opcoes.add_experimental_option("excludeSwitches", ["disable-extensions"])

    prefs = {
        "download.default_directory": str(PASTA_DOWNLOAD_TEMP.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    opcoes.add_experimental_option("prefs", prefs)

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=opcoes)

    # O timeout HTTP padrão do cliente Selenium (120s) é menor que o tempo
    # que alguém pode levar pra escolher o certificado na janela nativa —
    # a página fica "carregando" (do ponto de vista do Selenium) até a
    # escolha ser feita, e sem isso o driver.get() estoura com
    # ReadTimeoutError antes da pessoa conseguir clicar (confirmado na
    # prática: 07/09/2026).
    driver.command_executor.set_timeout(max(TIMEOUT_LOGIN_SEGUNDOS + 60, 300))

    # Sobrescreve em nível de BROWSER (não só da aba) pra tentar valer
    # também pros downloads disparados pela extensão — ver aviso no
    # docstring do módulo, isso ainda não foi confirmado na prática.
    try:
        driver.execute_cdp_cmd(
            "Browser.setDownloadBehavior",
            {"behavior": "allow", "downloadPath": str(PASTA_DOWNLOAD_TEMP.resolve())},
        )
    except Exception:
        log.warning("Não consegui setar Browser.setDownloadBehavior via CDP.")

    return driver


# ----------------------------------------------------------------------
# LOGIN COM CERTIFICADO DIGITAL (pausa manual pro seletor nativo)
# ----------------------------------------------------------------------

TENTATIVAS_PORTAL = 3
PAUSA_ENTRE_TENTATIVAS_SEGUNDOS = 20


def _portal_indisponivel(driver: webdriver.Chrome) -> bool:
    """O certificado.nfse.gov.br às vezes devolve uma página 503 com o texto
    'The service is unavailable.' (instabilidade do portal do governo,
    observada em 08/09/2026)."""
    try:
        corpo = driver.execute_script("return document.body ? document.body.innerText : '';")
    except WebDriverException:
        return False
    return "service is unavailable" in (corpo or "").lower()


def _navegar_com_retentativa(
    driver: webdriver.Chrome, url: str, apelido_cliente: str,
    timeout_pagina: int | None = None,
) -> bool:
    """driver.get() tolerante ao portal: ERR_CONNECTION_RESET, 503 e página
    que nunca termina de carregar (timeout_pagina, em segundos). Tenta
    TENTATIVAS_PORTAL vezes com pausa. Retorna False se o portal continuar
    fora do ar (aí o cliente é pulado, sem traceback).

    timeout_pagina só faz sentido pra páginas que NÃO dependem de clique
    humano — no certificado.nfse.gov.br a página fica "carregando" de
    propósito até a pessoa escolher o certificado, então lá NÃO se usa."""
    if timeout_pagina:
        driver.set_page_load_timeout(timeout_pagina)
    for tentativa in range(1, TENTATIVAS_PORTAL + 1):
        try:
            driver.get(url)
            if not _portal_indisponivel(driver):
                return True
            motivo = "portal respondeu 'The service is unavailable' (503)"
        except TimeoutException:
            # Página de login que não termina de carregar (5 min sem
            # resposta, cliente 58, 08/09/2026) — o portal engasgou.
            motivo = f"página não carregou em {timeout_pagina}s"
        except WebDriverException as e:
            msg = str(e).splitlines()[0] if str(e) else type(e).__name__
            if "net::ERR_" not in msg:
                raise  # não é erro de rede, não mascarar
            motivo = msg
        if tentativa < TENTATIVAS_PORTAL:
            log.warning(
                "Cliente %s: %s (tentativa %d/%d) — esperando %ds e tentando de novo.",
                apelido_cliente, motivo, tentativa, TENTATIVAS_PORTAL,
                PAUSA_ENTRE_TENTATIVAS_SEGUNDOS,
            )
            time.sleep(PAUSA_ENTRE_TENTATIVAS_SEGUNDOS)
        else:
            log.error(
                "Cliente %s: portal fora do ar depois de %d tentativas (%s). "
                "Pulando — rode de novo mais tarde.",
                apelido_cliente, TENTATIVAS_PORTAL, motivo,
            )
    return False


def fazer_login_certificado(driver: webdriver.Chrome, apelido_cliente: str, cliente: dict | None = None) -> bool:
    """Navega pro link de acesso via certificado e PAUSA pra escolha manual
    do certificado na janela nativa do Windows/Chrome. Retorna True se caiu
    de volta autenticado no Portal Contribuinte."""
    # Página de login: sem clique humano, 90s é mais que suficiente quando o
    # portal está saudável — se estourar, é engasgo dele, tenta de novo.
    limpar_sessao_portal(driver)
    if not _navegar_com_retentativa(driver, URL_LOGIN, apelido_cliente, timeout_pagina=90):
        return False

    log.info(
        "Cliente %s: abrindo o acesso via certificado digital — "
        "ESCOLHA O CERTIFICADO na janela que vai aparecer e confirme.",
        apelido_cliente,
    )
    # Certificado: a página fica carregando até a pessoa escolher. O timeout
    # aqui é o tempo pra escolher (TIMEOUT_LOGIN_SEGUNDOS); se estourar,
    # reabre a janela do certificado (até TENTATIVAS_PORTAL vezes) em vez de
    # morrer com ReadTimeoutError depois de 5 min.
    if not _navegar_com_retentativa(
        driver, URL_CERTIFICADO, apelido_cliente, timeout_pagina=TIMEOUT_LOGIN_SEGUNDOS
    ):
        return False

    espera = WebDriverWait(driver, TIMEOUT_LOGIN_SEGUNDOS)
    try:
        espera.until(lambda d: "/EmissorNacional/Dashboard" in d.current_url
                     or "/EmissorNacional/Notas" in d.current_url
                     or "/EmissorNacional/" == d.current_url.split("nfse.gov.br")[-1])
    except TimeoutException:
        log.error(
            "Cliente %s: não caiu no Portal Contribuinte depois de "
            "%ss — certificado não escolhido a tempo, ou não é o "
            "certificado certo para esse cliente.",
            apelido_cliente, TIMEOUT_LOGIN_SEGUNDOS,
        )
        return False

    log.info("Cliente %s: login com certificado OK.", apelido_cliente)
    if cliente is not None:
        quem = conferir_empresa_logada(driver, cliente)
        if quem is True:
            log.info("Cliente %s: empresa logada confirmada pelo CNPJ na página.", apelido_cliente)
        elif quem is False:
            log.warning("Cliente %s: a página do portal mostra CNPJ(s), mas NÃO o do cliente — "
                        "possível sessão de outra empresa. Confira os arquivos desse cliente.", apelido_cliente)
        else:
            log.info("Cliente %s: a página não mostra CNPJ; a empresa será conferida pelo CNPJ dentro da planilha.",
                     apelido_cliente)
    return True


# ----------------------------------------------------------------------
# ISOLAMENTO DE SESSÃO ENTRE CLIENTES
# ----------------------------------------------------------------------
# Visto em 02/10/2026: o robô abre um Chrome novo por cliente, MAS todos usam o MESMO perfil
# (perfil_chrome_robo). O cookie de sessão do portal ficou no perfil, o cliente seguinte "logou" em 1 segundo
# ainda como o cliente anterior e a rodada inteira baixou os dados do 238. A conferência de CNPJ barrou os
# arquivos (nada errado foi arquivado), mas "0 notas / sem movimento" não passa por conferência nenhuma:
# era a sessão do 238, não do cliente. Por isso a sessão do portal é apagada ANTES de cada login.

ORIGENS_PORTAL = ("https://www.nfse.gov.br", "https://certificado.nfse.gov.br", "https://nfse.gov.br")


def limpar_sessao_portal(driver: webdriver.Chrome) -> None:
    """Apaga cookies, cache e armazenamento do portal no perfil do robô (via DevTools), para o login do
    cliente começar do zero. A extensão não depende deles: ela usa a sessão que o login cria."""
    comandos = [("Network.clearBrowserCookies", {}), ("Network.clearBrowserCache", {})]
    comandos += [("Storage.clearDataForOrigin", {"origin": o, "storageTypes": "all"}) for o in ORIGENS_PORTAL]
    falhas = []
    for nome, args in comandos:
        try:
            driver.execute_cdp_cmd(nome, args)
        except Exception as e:  # noqa: BLE001 - qualquer falha do CDP vira aviso
            falhas.append(f"{nome}: {str(e).splitlines()[0] if str(e) else type(e).__name__}")
    if falhas:
        log.warning("Não consegui limpar toda a sessão do portal (%s).", "; ".join(falhas))
    else:
        log.info("Sessão anterior do portal apagada.")


_CNPJ_FORMATADO = re.compile(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}")


def conferir_empresa_logada(driver: webdriver.Chrome, cliente: dict) -> bool | None:
    """Tenta confirmar, pela própria página do portal, que a sessão é da empresa certa.
    True = o CNPJ do cliente aparece na página; False = aparecem CNPJs, mas não o do cliente (suspeito);
    None = a página não mostra CNPJ nenhum (não dá para saber). Só informa no log: quem barra é a
    conferência de CNPJ do arquivo e a limpeza de sessão."""
    try:
        corpo = driver.execute_script("return document.body ? document.body.innerText : '';") or ""
    except WebDriverException:
        return None
    esperado = _so_digitos(cliente["cnpj"])
    achados = {_so_digitos(m) for m in _CNPJ_FORMATADO.findall(corpo)}
    if esperado in achados or esperado in _so_digitos(corpo):
        return True
    return False if achados else None


# ----------------------------------------------------------------------
# EXTENSÃO — GERAR E BAIXAR A RELAÇÃO "COMPLETA"
# ----------------------------------------------------------------------

def gerar_relacao(
    driver: webdriver.Chrome, tipo: str, data_inicial: str, data_final: str
) -> int:
    """tipo: 'Emitidas' ou 'Recebidas'. Datas no formato AAAA-MM-DD (o que
    <input type="date"> espera)."""
    # Abrir numa aba NOVA em branco e só então navegar pra URL da extensão
    # (em vez de driver.get() direto na aba que acabou de vir do portal) —
    # confirmado na prática (08/09/2026) que navegar a mesma aba pode dar
    # ERR_BLOCKED_BY_CLIENT em sessão controlada por automação, mesmo com a
    # extensão funcionando normalmente fora da automação.
    driver.switch_to.new_window("tab")
    driver.get(URL_EXTENSAO)
    espera = WebDriverWait(driver, 30)
    espera.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nfse-type-btn")))

    # "Emitidas"/"Recebidas" são <a class="nfse-type-btn" href="..." target="_blank">.
    # O clique real deles (visto no código-fonte popup.js) faz preventDefault()
    # e manda o background navegar "a aba ativa" pro link — mas como aqui a
    # própria aba da extensão É a aba ativa, isso navega ela embora, perdendo
    # a UI (confirmado na prática: 07/09/2026). A extensão só precisa mesmo
    # do atributo `data-nfse-type` no <body> (é só o que gerarRelacao() lê,
    # visto em popup.js) — então setamos direto, sem clicar no link.
    driver.execute_script(
        """
        const tipo = arguments[0];
        document.querySelectorAll('.nfse-type-btn').forEach(b => b.classList.remove('selected'));
        const alvo = [...document.querySelectorAll('.nfse-type-btn')]
            .find(b => b.textContent.includes(tipo));
        if (alvo) alvo.classList.add('selected');
        document.body.setAttribute('data-nfse-type', tipo);
        """,
        tipo,
    )

    # Campos de data confirmados via dump real do DOM: #dateStart / #dateEnd
    campo_inicial = driver.find_element(By.ID, "dateStart")
    campo_final = driver.find_element(By.ID, "dateEnd")
    driver.execute_script("arguments[0].value = arguments[1];", campo_inicial, data_inicial)
    driver.execute_script("arguments[0].value = arguments[1];", campo_final, data_final)
    for campo in (campo_inicial, campo_final):
        driver.execute_script(
            "arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", campo
        )

    botao_completa = espera.until(
        EC.element_to_be_clickable((By.ID, "relacaoCompletaBtn"))
    )
    botao_completa.click()

    log.info(
        "Gerando relação Completa (%s, %s a %s) — a extensão lê nota por "
        "nota, pode demorar.",
        tipo, data_inicial, data_final,
    )

    # A extensão escreve o resultado final em #status (confirmado via dump
    # real do DOM: "✅ Relação completa gerada com N nota(s). Salva em
    # NFSe/RELATORIOS/." — inclusive quando N=0, caso em que NENHUM arquivo
    # é baixado). Espera essa mensagem em vez de só esperar o botão
    # reabilitar, pra saber com certeza quantas notas vieram.
    fim = time.time() + TIMEOUT_RELACAO_SEGUNDOS
    texto_status = ""
    while time.time() < fim:
        status = driver.execute_script(
            "const el = document.getElementById('status');"
            "return el ? {texto: el.innerText, classe: el.className} : {texto: '', classe: ''};"
        ) or {}
        texto_status = status.get("texto") or ""
        classe = status.get("classe") or ""
        m = re.search(r"gerada com (\d+) nota", texto_status)
        if m:
            return int(m.group(1))
        # Sem movimento: a extensão NÃO diz "gerada com 0 nota(s)" — ela mostra
        # "❌ Nenhuma nota encontrada para o período selecionado..." em
        # vermelho (visto no cliente 27, 08/09/2026). É 0 nota, não erro.
        if "nenhuma nota encontrada" in texto_status.lower():
            return 0
        # A extensão marca avisos com showStatus(..., 'error') -> classe
        # "error" no #status (e ⚠️ no texto). Ex.: "Faça login no portal
        # NFS-e primeiro!" — sem isso o robô esperaria os 10 min à toa
        # (08/09/2026). Falha na hora, com a mensagem da extensão.
        if "error" in classe.split() or "⚠" in texto_status:
            raise RuntimeError(f"A extensão parou com aviso: {texto_status.strip()!r}")
        time.sleep(3)

    raise TimeoutError(
        f"A extensão não terminou de gerar a relação de {tipo} em "
        f"{TIMEOUT_RELACAO_SEGUNDOS}s. Último #status: {texto_status.strip()!r}"
    )


def esperar_download(tipo: str, apos: datetime, timeout_segundos: int = 120) -> Path:
    """Espera aparecer um .xlsx novo em _downloads_temp/, gerado depois do
    instante `apos`. Levanta TimeoutError se não achar — nesse caso,
    verifique se não ficou uma janela nativa 'Salvar como' esperando clique
    manual (ver aviso no docstring do módulo).

    Confirmado na prática (07/09/2026): a extensão pede pra salvar em
    'NFSe/RELATORIOS/<nome com Empresa/Tipo/Completa/data>.xlsx', mas o
    Chrome ignora o subcaminho/nome sugeridos e salva com um nome
    aleatório (UUID) direto na raiz da pasta de download — por isso não dá
    pra filtrar pelo nome, só pela data de modificação (um arquivo por vez,
    já que cada chamada processa Emitidas e Recebidas em sequência)."""
    fim = time.time() + timeout_segundos
    while time.time() < fim:
        candidatos = [
            p for p in PASTA_DOWNLOAD_TEMP.glob("*.xlsx")
            if datetime.fromtimestamp(p.stat().st_mtime) >= apos
        ]
        if candidatos:
            candidatos.sort(key=lambda p: p.stat().st_mtime, reverse=True)
            return candidatos[0]
        time.sleep(2)
    raise TimeoutError(
        f"Não encontrei nenhum .xlsx novo em {PASTA_DOWNLOAD_TEMP} depois "
        f"de {timeout_segundos}s (esperando o relatório de {tipo}). "
        "Verifique se não ficou uma janela nativa 'Salvar como' esperando "
        "clique manual."
    )


# ----------------------------------------------------------------------
# NOME E DESTINO FINAL DO ARQUIVO
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# LOG ESTRUTURADO DE RESULTADOS (pro Painel de Fechamento)
# ----------------------------------------------------------------------
# Um CSV consolidado, uma linha por cliente+tipo, sobrevive a várias
# execuções (cada cliente roda como um processo Python separado — os logs
# de texto em logs/execucao_*.log ficam espalhados um por rodada, isso
# aqui é o que dá pra importar direto num painel.
ARQUIVO_RESULTADOS = PASTA_LOGS / "resultados.csv"
CAMPOS_RESULTADOS = [
    "timestamp", "competencia", "numero", "apelido", "razao_social",
    "cidade", "tipo", "status", "qtd_notas", "arquivo", "detalhe",
]


def registrar_resultado(
    competencia: str, cliente: dict, tipo: str, status: str,
    qtd_notas: int | None = None, arquivo: Path | None = None, detalhe: str = "",
) -> None:
    """status: 'baixado' | 'sem_movimento' | 'erro' | 'login_falhou'."""
    PASTA_LOGS.mkdir(exist_ok=True)
    novo = not ARQUIVO_RESULTADOS.exists()
    with open(ARQUIVO_RESULTADOS, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_RESULTADOS)
        if novo:
            w.writeheader()
        w.writerow({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "competencia": competencia,
            "numero": cliente["numero"],
            "apelido": cliente["apelido"],
            "razao_social": cliente.get("razao_social", ""),
            "cidade": cliente.get("cidade", ""),
            "tipo": tipo,
            "status": status,
            "qtd_notas": qtd_notas if qtd_notas is not None else "",
            "arquivo": arquivo.name if arquivo else "",
            "detalhe": detalhe,
        })


def nome_arquivo_padrao(cliente: dict, competencia: str, tipo: str) -> str:
    """{numero}_{apelido}_{cidade}_MM.AAAA_{Emitidas|Recebidas}.xlsx"""
    mes, ano = competencia.split("/")
    return f"{cliente['numero']}_{cliente['apelido']}_{cliente['cidade']}_{mes}.{ano}_{tipo}.xlsx"


def pasta_staging_mes(competencia: str) -> Path:
    mes, _ano = competencia.split("/")
    return portal_config.pasta_nacional(_cfg(), mes)


def pasta_quarentena(competencia: str) -> Path:
    """Dentro da 003 do mês: quem procura um arquivo errado olha ali, e o glob da conferência do DecWeb
    (só a pasta, sem subpastas) não enxerga a quarentena."""
    return pasta_staging_mes(competencia) / portal_config.QUARENTENA


def conferir_cnpj(arquivo: Path, cliente: dict, tipo: str) -> None:
    """Abre o .xlsx recém-baixado e confere se o CNPJ do
    Prestador (Emitidas) ou Tomador (Recebidas) bate com o do cliente
    esperado. Levanta ValueError se não bater.

    Existe porque isso já aconteceu na prática (09/09/2026): o cliente 3
    (Casa Clara) rodou bem depois do cliente 1 (EW Transportes) na mesma
    sessão, mas o "Recebidas" saiu com as notas da EW — o Portal
    provavelmente ainda estava autenticado no CNPJ anterior quando a
    extensão exportou. O robô não tinha como perceber isso sozinho antes
    desta checagem; o erro foi achado revisando o arquivo."""
    coluna_alvo = "Prestador" if tipo == "Emitidas" else "Tomador"
    wb = openpyxl.load_workbook(arquivo, read_only=True, data_only=True)
    try:
        ws = wb.worksheets[0]
        linhas = ws.iter_rows(values_only=True)
        cabecalho = [str(h or "") for h in next(linhas)]
        try:
            idx = next(
                i for i, h in enumerate(cabecalho)
                if "CNPJ" in h and coluna_alvo in h
            )
        except StopIteration:
            return  # planilha sem essa coluna (formato mudou?) — não bloqueia
        cnpjs_no_arquivo = {
            re.sub(r"\D", "", str(linha[idx]))
            for linha in linhas
            if linha and linha[idx]
        }
    finally:
        wb.close()

    if not cnpjs_no_arquivo:
        return  # nenhuma nota com CNPJ pra conferir (não deveria chegar aqui com 0 notas, mas por segurança)

    if _so_digitos(cliente["cnpj"]) not in cnpjs_no_arquivo:
        raise ValueError(
            f"CNPJ divergente: esperava {cliente['cnpj']} ({cliente['apelido']}) "
            f"na coluna {coluna_alvo}, achei {sorted(cnpjs_no_arquivo)} — "
            f"provavelmente sessão do portal ainda autenticada no cliente "
            f"anterior. Arquivo NÃO movido."
        )


def mover_para_destino(arquivo_baixado: Path, cliente: dict, competencia: str, tipo: str) -> Path:
    try:
        conferir_cnpj(arquivo_baixado, cliente, tipo)
    except ValueError:
        # Não deixa na pasta de download temp (pode confundir a próxima
        # busca por arquivo novo) nem descarta (preserva pra investigar).
        quarentena = pasta_quarentena(competencia)
        quarentena.mkdir(parents=True, exist_ok=True)
        destino_quarentena = quarentena / f"{datetime.now():%Y%m%d_%H%M%S}_{arquivo_baixado.name}"
        shutil.move(str(arquivo_baixado), str(destino_quarentena))
        log.warning("Arquivo movido pra quarentena: %s", destino_quarentena)
        raise

    destino_pasta = pasta_staging_mes(competencia)
    destino_pasta.mkdir(parents=True, exist_ok=True)
    destino = destino_pasta / nome_arquivo_padrao(cliente, competencia, tipo)
    # shutil.move, não Path.replace: o download cai em C: e o destino é o
    # Drive J: — os.replace não atravessa volumes (WinError 17, 08/09/2026).
    shutil.move(str(arquivo_baixado), str(destino))
    log.info("Movido para %s", destino)
    return destino


# ----------------------------------------------------------------------
# FASE 1 — UM CLIENTE, UMA COMPETÊNCIA
# ----------------------------------------------------------------------

def _ultimo_dia_mes(mes: str, ano: int) -> int:
    ultimo_dia = {
        "01": 31, "02": 28, "03": 31, "04": 30, "05": 31, "06": 30,
        "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31,
    }[mes]
    if mes == "02" and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        ultimo_dia = 29
    return ultimo_dia


def periodo_da_competencia(competencia: str) -> tuple[str, str]:
    """Período a baixar para a competência MM/AAAA: do dia 1 dela até o último dia do mês SEGUINTE.

    Antes era 'mês anterior + mês atual' relativo ao dia em que o robô roda: rodando em dezembro para
    setembro, as notas de setembro ficavam de fora. Incluir o mês seguinte mantém o que o atalho da
    extensão fazia (pegar nota lançada com atraso); quem filtra a competência é a conferência.
    Ex.: 09/2026 -> ('2026-09-01', '2026-10-31')."""
    mes, ano = competencia.split("/")
    m, a = int(mes), int(ano)
    m2, a2 = (1, a + 1) if m == 12 else (m + 1, a)
    return f"{a}-{m:02d}-01", f"{a2}-{m2:02d}-{_ultimo_dia_mes(f'{m2:02d}', a2):02d}"


def processar_cliente(driver: webdriver.Chrome, cliente: dict, competencia: str) -> None:
    data_inicial, data_final = periodo_da_competencia(competencia)

    if not fazer_login_certificado(driver, cliente["apelido"], cliente):
        log.error("Pulando cliente %s — login não confirmado.", cliente["apelido"])
        for tipo in ("Emitidas", "Recebidas"):
            registrar_resultado(competencia, cliente, tipo, "login_falhou")
        return

    for tipo in ("Emitidas", "Recebidas"):
        inicio = datetime.now()
        try:
            try:
                qtd_notas = gerar_relacao(driver, tipo, data_inicial, data_final)
            except RuntimeError as e:
                # Visto em 30/09/2026 (cliente 15, logo depois de uma Emitidas
                # de 97s): a extensão devolveu "Faça login no portal NFS-e
                # primeiro!" — a sessão do portal caiu. Refaz o login (a
                # política de certificado ainda vale nesse Chrome) e tenta
                # esse tipo mais uma vez.
                if "login" not in str(e).lower():
                    raise
                log.warning("Cliente %s: sessão do portal caiu antes de %s — refazendo o login.",
                            cliente["apelido"], tipo)
                if not fazer_login_certificado(driver, cliente["apelido"], cliente):
                    raise
                inicio = datetime.now()
                qtd_notas = gerar_relacao(driver, tipo, data_inicial, data_final)
            if qtd_notas == 0:
                log.info(
                    "Cliente %s: %s sem movimento em %s (0 notas) — nada "
                    "pra baixar, seguindo.",
                    cliente["apelido"], tipo, competencia,
                )
                registrar_resultado(competencia, cliente, tipo, "sem_movimento", qtd_notas=0)
                continue
            arquivo = esperar_download(tipo, apos=inicio, timeout_segundos=TIMEOUT_RELACAO_SEGUNDOS)
            destino = mover_para_destino(arquivo, cliente, competencia, tipo)
            registrar_resultado(competencia, cliente, tipo, "baixado", qtd_notas=qtd_notas, arquivo=destino)
        except Exception as e:
            log.exception("Falhou %s para o cliente %s", tipo, cliente["apelido"])
            registrar_resultado(competencia, cliente, tipo, "erro", detalhe=str(e)[:200])


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------

def main() -> None:
    global TIMEOUT_LOGIN_SEGUNDOS
    ap = argparse.ArgumentParser(description="Download Emitidas/Recebidas do Portal Nacional NFS-e")
    ap.add_argument("--competencia", help="MM/AAAA (se omitido, pergunta)")
    ap.add_argument("--clientes", help="números separados por vírgula, ou 'todos' (se omitido, pergunta)")
    ap.add_argument("--manual", action="store_true",
                    help="modo antigo: pausa pra você escolher o certificado na janela do Windows")
    ap.add_argument("--verificar-certificados", action="store_true",
                    help="só lista a situação do certificado de cada cliente e sai")
    args = ap.parse_args()

    try:
        clientes = carregar_clientes()
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return
    print(f"{len(clientes)} clientes carregados de {ARQUIVO_CLIENTES.name}.\n")

    if args.verificar_certificados:
        linhas = relatorio_certificados(clientes)
        for l in linhas:
            print(f"{l['numero']:>3}  {l['apelido']:<42} {l['situacao']:<16} {l['vence']}")
        print(f"\nSalvo em {PASTA_LOGS / 'certificados_status.csv'}")
        return

    competencia = (args.competencia or input("Competência (MM/AAAA): ")).strip()
    if not re.fullmatch(r"(0[1-9]|1[0-2])/20\d\d", competencia):
        print(f"Competência inválida: {competencia!r}. Use MM/AAAA, por exemplo 09/2026.")
        return

    if args.clientes is not None:
        numero = "" if args.clientes.strip().lower() == "todos" else args.clientes.strip()
    else:
        numero = input(
            "Número do cliente (do config/clientes.csv), vários separados por "
            "vírgula, ou ENTER pra rodar todos: "
        ).strip()

    _cfg()  # falha cedo, antes de abrir o Chrome, se o configuracao.ini estiver faltando ou com o valor de exemplo

    if numero:
        pedidos = [n.strip() for n in numero.split(",") if n.strip()]
        selecionados = [c for c in clientes if c["numero"] in pedidos]
        faltando = [n for n in pedidos if n not in {c["numero"] for c in selecionados}]
        if faltando:
            print(f"Cliente(s) não encontrado(s) em {ARQUIVO_CLIENTES.name}: {', '.join(faltando)}.")
            return
    else:
        selecionados = clientes

    auto_cert = not args.manual
    certs = []
    if auto_cert:
        certs = listar_certificados()
        log.info("Seleção automática de certificado ligada (%d certificados com CNPJ no Windows).", len(certs))
        # Sem clique humano a página do certificado responde em segundos: se
        # a política não valer e a janela do Windows aparecer, não adianta
        # esperar 3 min por tentativa.
        TIMEOUT_LOGIN_SEGUNDOS = 60

    # Um Chrome NOVO por cliente — o Chrome lembra o certificado escolhido
    # pra um site durante toda a sessão do processo, então reaproveitar o
    # mesmo navegador entre clientes faria o cliente 2 (e os seguintes)
    # serem processados com o certificado do cliente 1, sem avisar
    # (confirmado como risco real, não hipotético: 07/09/2026).
    try:
        for cliente in selecionados:
            log.info("=== Cliente %s - %s ===", cliente["numero"], cliente["apelido"])
            if auto_cert:
                sit, cert = situacao_certificado(re.sub(r"\D", "", cliente["cnpj"]), certs)
                if sit != "OK":
                    motivo = (
                        f"certificado digital vencido em {cert['vence']:%d/%m/%Y}"
                        if sit == "VENCIDO" else "sem certificado digital neste computador"
                    )
                    log.error("Cliente %s: %s — pulando.", cliente["apelido"], motivo)
                    for tipo in ("Emitidas", "Recebidas"):
                        registrar_resultado(competencia, cliente, tipo, "login_falhou", detalhe=motivo)
                    continue
                definir_politica_certificado(cert["cn"])
                log.info("Cliente %s: certificado %s (vence %s) selecionado automaticamente.",
                         cliente["apelido"], cert["cn"], cert["vence"])
            driver = montar_driver()
            try:
                processar_cliente(driver, cliente, competencia)
            finally:
                driver.quit()
                if auto_cert:
                    remover_politica_certificado()
    finally:
        if auto_cert:
            remover_politica_certificado()


if __name__ == "__main__":
    main()
