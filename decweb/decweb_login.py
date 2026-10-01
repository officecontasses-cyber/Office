"""
Automação DECWEB - Porto Alegre (Declaração Eletrônica do ISSQN)
==================================================================

Fluxo baseado no POP - Fechamento Municipal de Porto Alegre (DecWeb).
Adaptado ao OfficeCont em 01/10/2026 a partir do pacote de outro escritório:
  - pastas: <raiz>\\<MM_MES>\\002 ARQUIVOS MUNICIPAIS (primeiro o mês, depois o tipo);
  - nomes de arquivo na convenção do escritório (zip + subpasta extraída ..._NFSE_ServPrestados/Tomados,
    ..._DeclaraçãoMensal.pdf, ..._ISSQN.pdf);
  - conferência com o Portal Nacional DESLIGADA por padrão (config/configuracao.ini) e, quando ligada,
    sem planilha Emitidas o robô pode enviar assim mesmo (opção sem_emitidas);
  - aceitar avisos de "receita zero" por cliente (coluna aceitar_avisos do clientes.csv).

O robô roda em TRÊS FASES, que podem ser rodadas separadas (1, 2, 3) ou
todas em sequência num único login (opção T = Tudo: cria/reaproveita a
declaração, baixa os zips, volta pra lista, ENVIA e imprime, sem pausa):

FASE 1 — preparar (automática):
  1. Login no CAS
  2. Tela "Relação de Declarantes" -> clica na lupa da empresa
  3. Tela "Relação de Declarações" -> clica "Nova Declaração", informa
     Mês/Ano da competência (e marca "Retificadora" se já existir uma
     declaração original pra essa competência), salva
  4. Abre a declaração recém-criada (link "NFSE Nota Fiscal Eletrônica")
  5. Baixa "Notas Serviços Prestados" (zip)
  6. Baixa "Notas Serviços Tomados" (zip)
  Para aí. A responsável revisa os valores no site antes de seguir pra Fase 2.

FASE 2 — enviar (automática, SEM pausa de confirmação — por decisão
explícita da responsável, o envio oficial é automatizado sem revisão humana
no meio):
  7. Se a declaração ainda estiver "Aberta": na própria "Relação de
     Declarações", clica no ícone de check (✔) da linha — abre o modal
     "Preparar Declaração para envio" — e clica "Preparar e Enviar" —
     isso ENVIA OFICIALMENTE a declaração (sem sair da tela da lista)
  Se já estiver enviada, não faz nada.

FASE 3 — imprimir (automática, roda depois que a declaração já foi
enviada — pela Fase 2 ou manualmente):
  8. Menu "Imprimir" -> modal "Impressão de documentos" -> marca
     Declaração + Recibo de Entrega (+ Guia Pagamento se houver ISSQN)
  9. Clica Imprimir e salva o(s) PDF(s) (Declaração e, se aplicável,
     Guia de Pagamento/ISSQN como arquivo separado)

Nome dos arquivos: segue o padrão do Painel de Fechamento —
{numero}_{apelido}_PortoAlegre_MM.AAAA_{sufixo}.{extensão}
(ex.: 23_EscolaLicitocon_PortoAlegre_08.2026_Prestados.zip)

STATUS DO TESTE REAL (cliente ESCOLA DA LICITOCON, última atualização 04/09/2026):
  ✅ Login, "Ir para declarações", "Nova Declaração" (original e
     Retificadora), abertura de "Valores da NFSE", download do zip de
     Notas Serviços Prestados/Tomados (com liberação de download via CDP),
     nomeação de arquivo no padrão do painel, e o clique no ícone de
     check + "Preparar e Enviar" (Fase 2) — confirmados contra a tela real.
  ✅ Fase 3 (impressão do PDF; Guia/ISSQN em rodada separada só quando
     há valor) — confirmada contra a tela real em 05/09/2026.
  ⏳ Ainda não testado: fluxo completo (T) de ponta a ponta — em especial
     a volta de 'Valores da NFSE' pra lista e a espera da linha virar
     'Enviada' antes de imprimir. Se travar, manda o log.

Uso:
    pip install -r requirements.txt
    copie config/clientes.exemplo.csv para config/clientes.csv e preencha
    python decweb_login.py
"""

import argparse
import csv
import logging
import re
import time
import zipfile
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import conferencia_prestados as cp

# ----------------------------------------------------------------------
# CONFIGURAÇÃO
# ----------------------------------------------------------------------

URL_DECWEB = "https://decwebapp.portoalegre.rs.gov.br/issqn-e/"
ARQUIVO_CLIENTES = Path(__file__).parent / "config" / "clientes.csv"
PASTA_LOGS = Path(__file__).parent / "logs"
TIMEOUT_SEGUNDOS = 30

# pasta-mãe onde ficam as pastas mensais dos arquivos municipais (confirmado
# contra a estrutura real: '08_AGOSTO', '09_SETEMBRO', '10_OUTUBRO', ... já
# existem ali). A pasta de download de cada cliente é calculada a partir
# daqui + da competência, em vez de vir fixa do clientes.csv — assim não
# precisa editar o CSV todo mês só pra trocar o mês.
import configuracao  # noqa: E402  (pastas e opções do escritório: config/configuracao.ini)

_CFG = configuracao.carregar()
MESES_PASTA = configuracao.MESES_PASTA


def pasta_download_da_competencia(competencia: str) -> str:
    """'09/2026' -> '<raiz>\\09_SETEMBRO\\002 ARQUIVOS MUNICIPAIS' (primeiro o mês, depois o tipo de
    arquivo — estrutura real do Drive do escritório). A pasta de Março ('03_MARCO') ainda não foi conferida
    contra a estrutura real — as demais (07 e 08) foram."""
    mes, _ano = competencia.split("/")
    return str(configuracao.pasta_municipais(_CFG, mes))

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
log = logging.getLogger("decweb")


# ----------------------------------------------------------------------
# LEITURA DA LISTA DE CLIENTES
# ----------------------------------------------------------------------

COLUNAS_OBRIGATORIAS = ("numero", "apelido", "nome_painel", "usuario", "senha")


def carregar_clientes() -> list[dict]:
    """Lê config/clientes.csv. Tolera BOM (UTF-8 com assinatura), espaços e linhas em branco. Colunas:
    numero, apelido, nome_painel, cnpj, usuario, senha, aceitar_avisos (cnpj e aceitar_avisos são opcionais).
    'aceitar_avisos' = sim só para cliente de receita zero confirmada (ver _confirmar_modal_preparar)."""
    if not ARQUIVO_CLIENTES.exists():
        raise FileNotFoundError(
            f"Não encontrei {ARQUIVO_CLIENTES}.\n"
            "Copie config/clientes.exemplo.csv para config/clientes.csv "
            "e preencha com os dados reais (esse arquivo NÃO deve ser "
            "compartilhado nem versionado — ele fica só na máquina do "
            "escritório)."
        )
    with open(ARQUIVO_CLIENTES, encoding="utf-8-sig", newline="") as f:
        leitor = csv.DictReader(f)
        faltando = [c for c in COLUNAS_OBRIGATORIAS if c not in [(h or "").strip() for h in (leitor.fieldnames or [])]]
        if faltando:
            raise ValueError(f"{ARQUIVO_CLIENTES}: faltam as colunas {', '.join(faltando)}.")
        clientes = []
        for linha in leitor:
            c = {(k or "").strip(): (v or "").strip() for k, v in linha.items() if k}
            if not c.get("numero"):
                continue  # linha em branco
            c["cnpj"] = re.sub(r"\D", "", c.get("cnpj", ""))
            c["aceitar_avisos"] = configuracao.eh_sim(c.get("aceitar_avisos"))
            clientes.append(c)
    return clientes


# ----------------------------------------------------------------------
# RESULTADOS POR CLIENTE (pro Painel de Fechamento) E DIAGNÓSTICO
# ----------------------------------------------------------------------
# logs/resultados.csv  -> histórico bruto, uma linha por cliente a cada vez
#                         que ele é processado (só cresce; não usar direto
#                         no Painel). Nunca grava usuário nem senha.
# logs/resumo_atual.csv -> uma linha por cliente da lista, pra competência
#                         pedida, sempre refeita (é o que o Painel lê).
# Etapas (acumuladas entre rodadas da mesma competência, já que as fases
# 1, 2 e 3 podem rodar em dias diferentes):
#   declaracao_criada | zips_baixados | conferido | enviada | pdf_baixado
ARQUIVO_RESULTADOS = PASTA_LOGS / "resultados.csv"
ARQUIVO_RESUMO = PASTA_LOGS / "resumo_atual.csv"
CAMPOS_RESULTADOS = ["timestamp", "competencia", "numero", "apelido", "cliente", "fase", "status", "etapas", "detalhe"]
CAMPOS_RESUMO = ["competencia", "numero", "apelido", "cliente", "status", "etapas", "detalhe", "timestamp"]
ETAPAS_ORDEM = ["declaracao_criada", "zips_baixados", "conferido", "enviada", "pdf_baixado"]

# Conferência DecWeb x Portal Nacional antes do envio (divergiu -> não envia). Vem de config/configuracao.ini
# (padrão: desligada); --com-conferencia liga e --sem-conferencia desliga numa execução.
CONFERENCIA_ATIVA = _CFG["conferencia"]
# Com a conferência ligada e SEM planilha Emitidas do cliente: 'enviar' (segue) ou 'bloquear'.
POLITICA_SEM_EMITIDAS = _CFG["sem_emitidas"]

# Só liga com --aceitar-avisos (para a rodada inteira) ou com aceitar_avisos=sim na linha do cliente
# (ver _confirmar_modal_preparar).
ACEITAR_AVISOS = False
ACEITAR_AVISOS_CLIENTE = False


def marcar_etapa(cliente: dict, etapa: str) -> None:
    """Anota (no dict do cliente da rodada) que essa etapa foi concluída."""
    cliente.setdefault("_etapas", set()).add(etapa)


def registrar_resultado(competencia: str, cliente: dict, fase: str, resultado: dict) -> None:
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
            "apelido": cliente.get("apelido", ""),
            "cliente": cliente.get("nome_painel", ""),
            "fase": fase,
            "status": resultado["status"],
            "etapas": ";".join(resultado.get("etapas", [])),
            "detalhe": (resultado.get("detalhe") or "").replace("\n", " ")[:300],
        })


def atualizar_resumo(competencia: str, clientes: list[dict]) -> None:
    """Refaz logs/resumo_atual.csv: todos os clientes da lista, com a
    situação mais recente da competência ('pendente' se nunca processado)."""
    por_numero: dict[str, dict] = {}
    if ARQUIVO_RESULTADOS.exists():
        with open(ARQUIVO_RESULTADOS, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["competencia"] != competencia:
                    continue
                etapas = {e for e in (r.get("etapas") or "").split(";") if e}
                anterior = por_numero.get(r["numero"])
                if anterior:
                    etapas |= anterior["_etapas"]
                por_numero[r["numero"]] = {**r, "_etapas": etapas}

    PASTA_LOGS.mkdir(exist_ok=True)
    with open(ARQUIVO_RESUMO, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_RESUMO)
        w.writeheader()
        for c in sorted(clientes, key=lambda c: int(c["numero"])):
            r = por_numero.get(c["numero"])
            w.writerow({
                "competencia": competencia,
                "numero": c["numero"],
                "apelido": c.get("apelido", ""),
                "cliente": c.get("nome_painel", ""),
                "status": r["status"] if r else "pendente",
                "etapas": ";".join(e for e in ETAPAS_ORDEM if r and e in r["_etapas"]) if r else "",
                "detalhe": r["detalhe"] if r else "",
                "timestamp": r["timestamp"] if r else "",
            })


def salvar_diagnostico(driver, cliente: dict) -> None:
    """Quando algo falha, guarda print da tela e HTML em logs/diagnostico/ —
    pra investigar depois (ex.: o modal de impressão do For Behavior Pet,
    que deu timeout em 07/09/2026 sem ninguém ver a tela). Nunca derruba a
    rodada."""
    try:
        pasta = PASTA_LOGS / "diagnostico"
        pasta.mkdir(exist_ok=True)
        base = f"{datetime.now():%Y%m%d_%H%M%S}_{cliente.get('numero', 'x')}"
        driver.save_screenshot(str(pasta / f"{base}.png"))
        (pasta / f"{base}.html").write_text(driver.page_source, encoding="utf-8")
        log.info("Diagnóstico salvo em %s (%s.png / .html)", pasta, base)
    except Exception:
        pass


# ----------------------------------------------------------------------
# CHROME COM PASTA DE DOWNLOAD JÁ CONFIGURADA POR CLIENTE
# ----------------------------------------------------------------------

def montar_driver(pasta_download: str) -> webdriver.Chrome:
    Path(pasta_download).mkdir(parents=True, exist_ok=True)

    opcoes = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": str(Path(pasta_download).resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        # evita o Chrome abrir o PDF no visualizador interno em vez de baixar
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True,
    }
    opcoes.add_experimental_option("prefs", prefs)
    # comente a linha abaixo se quiser ver o navegador rodando (recomendado
    # enquanto ainda estamos ajustando a parte de downloads)
    # opcoes.add_argument("--headless=new")

    # achado em 07/09/2026: rodando vários clientes em sequência (fase T,
    # opção TODOS), o Chrome (ou o processo do chromedriver) caiu sozinho
    # no meio de mais de um cliente - uma vez como 'no such window: target
    # window already closed' e, no cliente seguinte, como falha total de
    # conexão com o driver (WinError 10061). Essas três flags são o padrão
    # recomendado pra reduzir esse tipo de crash em sessões automatizadas
    # longas no Windows.
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")
    opcoes.add_argument("--disable-gpu")

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=opcoes)

    # Chrome recente passou a bloquear/perguntar onde salvar em sessões
    # controladas por automação mesmo com as preferências acima — precisa
    # liberar explicitamente via protocolo do DevTools (confirmado contra
    # a tela real: sem isso aparecia a janela nativa "Salvar como").
    driver.execute_cdp_cmd(
        "Page.setDownloadBehavior",
        {"behavior": "allow", "downloadPath": str(Path(pasta_download).resolve())},
    )

    return driver


# ----------------------------------------------------------------------
# LOGIN NO CAS DA PREFEITURA DE PORTO ALEGRE
# ----------------------------------------------------------------------

def fazer_login(driver: webdriver.Chrome, usuario: str, senha: str, tentativas: int = 3) -> bool:
    """Faz login e retorna True se caiu na tela do DECWEB (login OK).

    Visto em 24/09/2026: o login falha de vez em quando com
    ReadTimeoutError de 120s (3 em ~10 execuções) e sempre passa na
    tentativa seguinte. Por isso: timeout de carregamento de 60s e até
    `tentativas` tentativas quando o erro for de tempo esgotado. Senha
    errada (volta False) NÃO repete — evita bloquear o usuário."""
    driver.set_page_load_timeout(60)
    for n in range(1, tentativas + 1):
        try:
            return _tentar_login(driver, usuario, senha)
        except Exception as exc:
            texto = f"{type(exc).__name__} {exc}".lower()
            if "timeout" not in texto and "timed out" not in texto or n == tentativas:
                raise
            log.warning("Login: tempo esgotado (%s) — tentativa %d/%d, esperando 10s.",
                        type(exc).__name__, n, tentativas)
            time.sleep(10)
    return False


def _tentar_login(driver: webdriver.Chrome, usuario: str, senha: str) -> bool:
    driver.get(URL_DECWEB)
    espera = WebDriverWait(driver, TIMEOUT_SEGUNDOS)

    # Tela padrão do CAS (Apereo CAS) usada pela Prefeitura de Porto Alegre:
    # campos com name/id "username" e "password"
    campo_usuario = espera.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    campo_senha = driver.find_element(By.ID, "password")

    campo_usuario.clear()
    campo_usuario.send_keys(usuario)
    campo_senha.clear()
    campo_senha.send_keys(senha)

    # o botão de entrar do CAS mudou em algum momento depois de 07/09/2026:
    # confirmado contra a tela real em 24/09/2026 que não é mais um
    # input name="submit" — agora é um botão de imagem name="envia"
    # (value="Entrar"). Tentamos os dois nomes conhecidos antes de cair
    # no fallback de ENTER no campo de senha, que se mostrou instável
    # (travou 120s numa tentativa real nesse mesmo dia).
    try:
        driver.find_element(By.NAME, "envia").click()
    except Exception:
        try:
            driver.find_element(By.NAME, "submit").click()
        except Exception:
            from selenium.webdriver.common.keys import Keys
            campo_senha.send_keys(Keys.RETURN)

    try:
        espera.until(
            lambda d: "cas/login" not in d.current_url.lower()
        )
    except Exception:
        return False

    if "cas/login" in driver.current_url.lower():
        return False  # provavelmente usuário/senha incorretos
    return True


def entrar_no_declarante(driver: webdriver.Chrome) -> None:
    """Da tela 'Relação de Declarantes' (logo após o login), clica no ícone
    'Ir para declarações' da empresa pra entrar em 'Relação de Declarações'
    (confirmado via tooltip contra a tela real)."""
    _clicar_xpath(driver, "//*[@title='Ir para declarações' or @alt='Ir para declarações']")


# ----------------------------------------------------------------------
# FASE 1 — CRIAR A DECLARAÇÃO DO MÊS E BAIXAR OS RELATÓRIOS (EXCEL)
# ----------------------------------------------------------------------

MESES_ABREV = {
    "01": "Jan", "02": "Fev", "03": "Mar", "04": "Abr",
    "05": "Mai", "06": "Jun", "07": "Jul", "08": "Ago",
    "09": "Set", "10": "Out", "11": "Nov", "12": "Dez",
}

MESES_COMPLETO = {
    "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
    "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
    "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro",
}


def competencia_para_rotulo(competencia: str) -> str:
    """'08/2026' -> 'Ago/2026' (é assim que a tela mostra a competência)."""
    mes, ano = competencia.split("/")
    return f"{MESES_ABREV[mes]}/{ano}"


def nome_arquivo_padrao(cliente: dict, competencia: str, sufixo: str, extensao: str) -> str:
    """Segue o padrão de nome do Painel de Fechamento / pasta 002 do OfficeCont:
    {numero}_{apelido}_PortoAlegre_MM.AAAA_{sufixo}.{extensao}
    ex.: 177_ILS_PortoAlegre_08.2026_NFSE_ServPrestados.zip | ..._DeclaraçãoMensal.pdf | ..._ISSQN.pdf"""
    mes, ano = competencia.split("/")
    return f"{cliente['numero']}_{cliente['apelido']}_PortoAlegre_{mes}.{ano}_{sufixo}.{extensao}"


def _elemento_visivel(driver: webdriver.Chrome, xpath: str):
    """Entre TODOS os elementos que casam com `xpath`, devolve o primeiro
    que estiver realmente visível e habilitado na tela — confirmado
    contra a tela real que o DecWeb costuma ter cópias escondidas do
    mesmo texto/botão (ex.: uma versão da seção 'Legal' ao lado da
    'Nacional' visível, ambas com o mesmo rótulo). Pegar só o primeiro
    resultado do XPath, sem checar visibilidade, arrisca clicar/esperar
    numa cópia escondida que nunca fica clicável. Devolve False se
    nenhuma cópia estiver visível ainda (uso como condição de espera)."""
    for candidato in driver.find_elements(By.XPATH, xpath):
        try:
            if candidato.is_displayed() and candidato.is_enabled():
                return candidato
        except StaleElementReferenceException:
            continue
    return False


def _clicar_xpath(driver: webdriver.Chrome, xpath: str, timeout: int = TIMEOUT_SEGUNDOS, tentativas: int = 3):
    """Localiza (a cópia visível, ver `_elemento_visivel`) e clica um
    elemento por XPath, tentando de novo se a página mudar entre localizar
    e clicar (StaleElementReferenceException) ou se um resquício de
    modal/máscara ainda estiver por cima na hora do clique
    (ElementClickInterceptedException) — comum logo após uma navegação ou
    o fechamento de um modal, enquanto a tela ainda está se ajustando. Na
    última tentativa, cai pra um clique via JavaScript, que ignora
    sobreposição visual."""
    ultimo_erro = None
    for tentativa in range(tentativas):
        try:
            elemento = WebDriverWait(driver, timeout).until(
                lambda d: _elemento_visivel(d, xpath)
            )
            if tentativa == tentativas - 1:
                driver.execute_script("arguments[0].click();", elemento)
            else:
                elemento.click()
            return elemento
        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
            ElementNotInteractableException,
        ) as exc:
            ultimo_erro = exc
            time.sleep(0.5)
    raise ultimo_erro


def _clicar_por_texto(driver: webdriver.Chrome, texto: str, timeout: int = TIMEOUT_SEGUNDOS):
    """Clica no primeiro elemento cujo texto visível OU atributo 'value'
    seja `texto` — o DecWeb mistura links/spans com texto normal e
    <input value="..."> estilizados como botão."""
    xpath = f"//*[contains(text(), '{texto}')] | //input[@value='{texto}']"
    return _clicar_xpath(driver, xpath, timeout)


def criar_nova_declaracao(driver: webdriver.Chrome, competencia: str, retificadora: bool = False) -> None:
    """Clica em 'Nova Declaração', preenche Mês/Ano (e marca 'Retificadora'
    se já existir uma declaração original pra essa competência) e salva.

    Confirmado contra a tela real: modal 'Nova Declaração' com dois
    dropdowns — Mês (nome por extenso, ex.: 'Agosto') e Ano (numérico,
    ex.: '2026') — e um checkbox 'Retificadora' que, ao menos pra esse
    cliente de teste, não abriu nenhum campo extra (motivo, número da
    declaração original, etc.) — só marca e segue direto pro Salvar."""
    espera = WebDriverWait(driver, TIMEOUT_SEGUNDOS)
    mes, ano = competencia.split("/")
    mes_nome = MESES_COMPLETO[mes]

    _clicar_por_texto(driver, "Nova Declaração")
    espera.until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Informe a competência')]"))
    )

    # a tela de fundo (Relação de Declarações) também tem um dropdown de
    # mês, no filtro "Todos os meses" — por isso NÃO dá pra procurar o
    # select por "tem a opção Janeiro" na página inteira (pega o filtro de
    # fundo, não o campo do modal). Restringimos a busca ao container do
    # próprio modal, identificado pelo texto único 'Informe a competência'.
    modal = driver.find_element(
        By.XPATH, "//*[contains(text(), 'Informe a competência')]/ancestor::*[.//select][1]"
    )
    campo_mes, campo_ano = modal.find_elements(By.TAG_NAME, "select")[:2]
    Select(campo_mes).select_by_visible_text(mes_nome)
    Select(campo_ano).select_by_visible_text(ano)

    if retificadora:
        checkbox_retificadora = modal.find_element(
            By.XPATH,
            ".//*[contains(normalize-space(text()), 'Retificadora')]"
            "/ancestor::*[self::tr or self::div][1]//input[@type='checkbox']",
        )
        if not checkbox_retificadora.is_selected():
            checkbox_retificadora.click()
        log.info("Criando como RETIFICADORA (já existe declaração original para essa competência)")

    _clicar_por_texto(driver, "Salvar")
    # espera o modal fechar de vez (senão a máscara dele pode atrapalhar o
    # próximo clique, mesmo já "invisível")
    espera.until(
        EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(), 'Informe a competência')]"))
    )


def abrir_valores_nfse(driver: webdriver.Chrome, rotulo_competencia: str) -> None:
    """Clica no link 'NFSE Nota Fiscal Eletrônica' da competência recém-
    criada, abrindo a tela 'Valores da NFSE'.

    Essa linha fica numa SUB-linha, fora da linha onde aparece o texto da
    competência (confirmado contra a tela real) — por isso usamos
    'following::' a partir do texto da competência em vez de restringir à
    mesma linha/ancestor: o bloco da competência (linha + sub-linha) fica
    todo em sequência no documento, então o primeiro link 'NFSE Nota
    Fiscal Eletrônica' que aparece depois já é o certo."""
    xpath = (
        f"(//*[contains(normalize-space(text()), '{rotulo_competencia}')])[1]"
        "/following::*[contains(text(), 'NFSE Nota Fiscal Eletrônica')][1]"
    )
    _clicar_xpath(driver, xpath)


def extrair_zip_na_pasta(arquivo_zip: Path) -> Path | None:
    """Extrai o zip numa subpasta de mesmo nome (sem '.zip'), como o escritório já organiza a pasta
    002 ARQUIVOS MUNICIPAIS: o zip fica ao lado e a subpasta traz o .xlsx nota a nota. Reexecutar sobrescreve
    o conteúdo. NUNCA derruba a rodada: se falhar, só avisa."""
    destino = arquivo_zip.with_suffix("")
    try:
        destino.mkdir(exist_ok=True)
        raiz = destino.resolve()
        with zipfile.ZipFile(arquivo_zip) as z:
            for membro in z.infolist():
                alvo = (destino / membro.filename).resolve()
                if alvo != raiz and raiz not in alvo.parents:
                    raise ValueError(f"caminho suspeito dentro do zip: {membro.filename!r}")
            z.extractall(destino)
        log.info("Zip extraído em %s", destino.name)
        return destino
    except Exception as exc:
        log.warning("Não consegui extrair %s (%s) — o zip continua na pasta.", arquivo_zip.name, exc)
        return None


def _baixar_notas_excel(
    driver: webdriver.Chrome, tipo: str, pasta_download: str, nome_arquivo: str
) -> None:
    """Clica no link 'Notas Serviços {tipo}' da linha 'Nota Nacional' (ex.:
    tipo='Prestados' ou 'Tomados'), espera o modal com a lista de notas,
    clica em Download, espera o Excel cair na pasta, renomeia, e fecha o
    modal antes de voltar.

    Confirmado contra a tela real: existem DOIS links com o mesmo texto
    'Notas Serviços {tipo}' na página — um na linha 'Nota Legal' (sempre
    zerada) e outro na linha 'Nota Nacional' (com os valores de verdade,
    é o que o POP manda usar). Por isso ancoramos no texto 'Nota Nacional'
    em vez de simplesmente procurar o texto do link direto.

    Quando o cliente não teve nenhuma nota no mês (sem movimento), a tela
    mostra só o aviso 'Nenhuma NFSE foi encontrada para os critérios
    informados', com botão 'Fechar' e SEM botão 'Download' nenhum — sem
    tratar isso, o robô ficava esperando um Download que nunca aparece até
    estourar em erro (confirmado pela responsável em 06/09/2026, achado real:
    isso vai acontecer com frequência em produção, cliente sem movimento
    no mês não é caso raro)."""
    xpath_link = (
        "//*[contains(text(), 'Nota Nacional')]"
        "/ancestor::*[self::tr or self::div][1]"
        f"//*[contains(text(), 'Notas Serviços {tipo}')]"
    )
    _clicar_xpath(driver, xpath_link)

    # essa consulta busca as notas contra um serviço externo (NFS-e) e pode
    # demorar bem mais que os outros passos — por isso 90s aqui. Espera por
    # QUALQUER um dos dois resultados possíveis, o que aparecer primeiro:
    # o aviso 'sem movimento' (só 'Fechar', sem Download) ou a lista com
    # dados de verdade (com botão 'Download'). Esperar só pelo texto do
    # título do modal se mostrou pouco confiável: provavelmente existe
    # mais de uma cópia dele no HTML, uma escondida.
    def _resultado(d):
        if _elemento_visivel(d, "//*[contains(text(), 'Nenhuma NFSE foi encontrada')]"):
            return "vazio"
        if _elemento_visivel(d, "//*[contains(text(), 'Download')] | //input[@value='Download']"):
            return "dados"
        return False

    if WebDriverWait(driver, 90).until(_resultado) == "vazio":
        log.info("Sem %s no mês (nenhuma NFSE encontrada) — nada a baixar", tipo)
        _clicar_por_texto(driver, "Fechar")
        return

    pasta = Path(pasta_download)
    existentes = _snapshot_pasta(pasta)
    _clicar_por_texto(driver, "Download")

    # confirmado contra a tela real: o DecWeb baixa um .zip (não .xls
    # direto) com o nome já vindo pronto do site, tipo
    # '90269624_202608_NFSE_ServPrestados_NotaNacional.zip'
    try:
        arquivo = esperar_download_e_renomear(pasta, existentes, nome_arquivo, padrao="*.zip")
        log.info("Excel (zip) baixado: %s", nome_arquivo)
        extrair_zip_na_pasta(arquivo)
    except TimeoutError as exc:
        log.error(str(exc))

    try:
        _clicar_por_texto(driver, "Fechar")
    except Exception:
        pass


def _lista_de_declaracoes_carregada(driver: webdriver.Chrome) -> None:
    """Espera a tela 'Relação de Declarações' terminar de carregar (o botão
    'Nova Declaração' fica visível) antes de ler as linhas — logo após o
    clique em 'Ir para declarações' a lista ainda pode não estar na tela."""
    WebDriverWait(driver, TIMEOUT_SEGUNDOS).until(
        lambda d: _elemento_visivel(
            d, "//*[contains(text(), 'Nova Declaração')] | //input[@value='Nova Declaração']"
        )
    )


def _existe_declaracao_aberta(driver: webdriver.Chrome, rotulo_competencia: str) -> bool:
    """True se a lista já tem alguma declaração dessa competência ainda
    incompleta — 'Aberta' OU 'Preparada' (confirmado contra a tela real:
    uma declaração Original vira 'Preparada' antes de 'Enviada', um
    estado intermediário que também precisa ser reaproveitado, não
    recriado). Ex.: sobra de uma rodada anterior que falhou no meio. Não
    espera pela linha nem levanta erro se não houver nenhuma."""
    _lista_de_declaracoes_carregada(driver)
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
    )
    return any(
        "Aberta" in linha.text or "Preparada" in linha.text
        for linha in driver.find_elements(By.XPATH, xpath)
    )


def _ja_enviada_hoje(driver: webdriver.Chrome, rotulo_competencia: str) -> bool:
    """True se a linha mais recente da competência já foi enviada HOJE.

    Achado confirmado por revisão em 05/09/2026: se o fluxo T falha DEPOIS
    do envio (ex.: máscara de modal interceptando o clique de imprimir,
    como aconteceu de fato), rodar T de novo não encontrava nenhuma linha
    'Aberta' e criava + ENVIAVA outra declaração retificadora idêntica —
    um protocolo oficial duplicado na prefeitura só por causa de uma falha
    na impressão. Essa checagem evita isso: se já foi enviada hoje, pula
    reto pra impressão em vez de criar/enviar de novo."""
    _lista_de_declaracoes_carregada(driver)
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
    )
    linhas = driver.find_elements(By.XPATH, xpath)
    if not linhas:
        return False
    hoje = datetime.now().strftime("%d/%m/%Y")
    texto = linhas[0].text
    return "Enviada" in texto and hoje in texto


def _existe_declaracao_enviada(driver: webdriver.Chrome, rotulo_competencia: str) -> bool:
    """True se a lista já tem uma declaração dessa competência 'Enviada'."""
    _lista_de_declaracoes_carregada(driver)
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
    )
    return any("Enviada" in linha.text for linha in driver.find_elements(By.XPATH, xpath))


def _criar_ou_reaproveitar_declaracao(
    driver: webdriver.Chrome, competencia: str, rotulo_competencia: str, nome_cliente: str,
    retificadora: bool, cliente: dict | None = None,
) -> None:
    """Cria a declaração da competência — ou, se já existir uma 'Aberta',
    reaproveita (evita criar duplicata ao rodar de novo depois de uma
    falha no meio do caminho).

    Se a competência JÁ TEM declaração enviada e o robô não foi avisado
    (--retificadora), para com uma PENDÊNCIA em vez de criar outra
    'Original' por engano: quem decide retificar é a responsável. Caso real
    a observar: a de 09/2026 do Rodrigo Simmi (47) foi enviada em 24/09,
    antes do fim do mês."""
    if _existe_declaracao_aberta(driver, rotulo_competencia):
        log.info(
            "[%s] Já existe declaração de %s incompleta (Aberta/Preparada) — "
            "reaproveitando em vez de criar outra",
            nome_cliente, rotulo_competencia,
        )
    else:
        if not retificadora and _existe_declaracao_enviada(driver, rotulo_competencia):
            raise PendenciaNoDecWeb(
                f"{rotulo_competencia} já tem declaração ENVIADA — se for preciso "
                "retificar, rode de novo com --retificadora"
            )
        criar_nova_declaracao(driver, competencia, retificadora=retificadora)
    if cliente is not None:
        marcar_etapa(cliente, "declaracao_criada")


def _baixar_excels(driver: webdriver.Chrome, competencia: str, cliente: dict) -> None:
    """Na tela 'Valores da NFSE', baixa os zips de Serviços Prestados e
    Tomados já com o nome do padrão do Painel de Fechamento."""
    pasta_download = cliente["pasta_download"]
    _baixar_notas_excel(
        driver, "Prestados", pasta_download,
        nome_arquivo_padrao(cliente, competencia, "NFSE_ServPrestados", "zip"),
    )
    _baixar_notas_excel(
        driver, "Tomados", pasta_download,
        nome_arquivo_padrao(cliente, competencia, "NFSE_ServTomados", "zip"),
    )


def _voltar_para_relacao_de_declaracoes(driver: webdriver.Chrome) -> None:
    """De dentro da declaração ('Valores da NFSE') volta pra lista pelo
    breadcrumb 'Relação de Declarantes' + 'Ir para declarações' — o mesmo
    caminho já confirmado logo após o login. Se o breadcrumb não estiver
    na tela, recomeça pela página inicial do DecWeb (a sessão continua
    logada)."""
    try:
        _clicar_por_texto(driver, "Relação de Declarantes", timeout=10)
    except Exception:
        driver.get(URL_DECWEB)
    entrar_no_declarante(driver)


def preparar_declaracao_e_baixar_excels(
    driver: webdriver.Chrome, competencia: str, cliente: dict, retificadora: bool = False,
) -> None:
    """FASE 1: cria a declaração do mês (original ou retificadora — ou
    reaproveita uma que já esteja Aberta) e baixa os relatórios de Serviços
    Prestados e Tomados. Para aqui: as Fases 2 e 3 (ou o fluxo completo T)
    fazem o envio e a impressão."""
    rotulo = competencia_para_rotulo(competencia)
    nome_cliente = cliente["nome_painel"]

    entrar_no_declarante(driver)
    _criar_ou_reaproveitar_declaracao(driver, competencia, rotulo, nome_cliente, retificadora, cliente)
    abrir_valores_nfse(driver, rotulo)
    _baixar_excels(driver, competencia, cliente)
    marcar_etapa(cliente, "zips_baixados")

    log.info(
        "[%s] Zips baixados. Revise os valores no site e rode a Fase 2 (enviar, "
        "com --enviar) e a Fase 3 (imprimir) — ou o fluxo completo (T, com --enviar).",
        nome_cliente,
    )


# ----------------------------------------------------------------------
# FASE 2 — ENVIAR (SE PRECISO) E IMPRIMIR A DECLARAÇÃO (PDF)
# ----------------------------------------------------------------------

def declaracao_esta_aberta(driver: webdriver.Chrome, rotulo_competencia: str) -> bool:
    """Confere se a declaração ainda precisa ser enviada — checa a
    AUSÊNCIA de 'Enviada' na linha, em vez de procurar 'Aberta'
    especificamente, porque uma declaração Original passa por um estado
    intermediário 'Preparada' (nem Aberta, nem Enviada) — sobra do antigo
    caminho pelos ícones da lista — que também precisa do envio
    completado."""
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
    )
    linha = WebDriverWait(driver, TIMEOUT_SEGUNDOS).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return "Enviada" not in linha.text


def _icone_da_linha(driver: webdriver.Chrome, rotulo_competencia: str, acao: str):
    """Acha o ícone `acao` ('prepararDeclaracao' ou 'enviarDeclaracao') na
    linha da competência, ou False se ele não estiver na tela.

    SEGURANÇA: ancora no id exato do ícone ('::prepararDeclaracao'), nunca
    na posição dele na linha nem no arquivo de imagem. A MESMA linha tem o
    ícone '::excluirDeclaracao' (delete3.png, com confirm() 'Deseja
    realmente excluir a Declaração...'), então um seletor frouxo — por
    ordem ou por <input type=image> genérico — apagaria a declaração do
    cliente em vez de enviá-la. Os dois pontos duplos fazem parte do id
    real gerado pelo JSF e evitam casar com 'excluirDeclaracao'."""
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
        f"//input[@type='image'][contains(@id, '::{acao}')]"
    )
    return _elemento_visivel(driver, xpath)


class PendenciaNoDecWeb(Exception):
    """A declaração não pode ser fechada pelo robô porque o próprio DecWeb
    apontou pendências no modal de preparar (cadastro do responsável
    desatualizado, escrituração sem serviço informado, etc.).

    Nesses casos o site NÃO mostra o botão de confirmar — só 'Cancelar' —
    então não há o que automatizar: precisa de alguém resolver a pendência
    na mão. Por decisão da responsável (24/09/2026), o robô apenas registra o
    que está pendente e segue pro próximo cliente, em vez de insistir."""


def _pendencias_do_modal(driver: webdriver.Chrome) -> list[str]:
    """Lê as mensagens de erro/aviso que o modal de preparar lista por
    escrituração, pra o log dizer exatamente o que precisa ser resolvido."""
    texto = ""
    for bloco in driver.find_elements(
        By.XPATH, "//*[contains(@id, 'mpPrepararDeclaracaoContentDiv')]"
    ):
        try:
            if bloco.is_displayed():
                texto = bloco.text
                break
        except StaleElementReferenceException:
            continue

    interessantes = ("necessária", "necessario", "necessário", "Não foi informado", "deve", "inválid")
    return [
        linha.strip()
        for linha in texto.splitlines()
        if linha.strip() and any(p.lower() in linha.lower() for p in interessantes)
    ]


def _confirmar_modal_preparar(driver: webdriver.Chrome) -> bool:
    """Se o modal 'Preparar Declaração para envio' tiver aberto, confirma
    nele e devolve True. Devolve False quando o modal não apareceu.

    Confirmado no HTML real (24/09/2026): o botão de confirmar do modal é
    'Preparar' (id ...formPrepararDeclaracao:idCbSalvarEdicao) — NÃO
    'Preparar e Enviar', que não existe em lugar nenhum da página. O
    ícone de check também pode preparar direto, sem abrir modal nenhum
    (o onclick dele traz um 'false ? mostrar : esconder' embutido), que é
    o caso 'Declaração preparada sem modal' visto nos logs de 07/09."""
    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Preparar Declaração para envio')]")
            )
        )
    except Exception:
        return False

    # Quando o DecWeb aponta pendências (cadastro do responsável
    # desatualizado, escrituração sem serviço informado...), ele NÃO
    # renderiza o botão de confirmar — o modal fica só com 'Cancelar'.
    # Confirmado na tela real em 24/09/2026 com o R & J ODONTOLOGIA.
    # Antes disso o robô ficava 30s tentando clicar num botão que nunca
    # existiu e morria com um timeout sem explicação.
    # 01/10/2026: no modal de uma declaração nova (ainda sem edição) os botões
    # têm outros ids — 'Preparar e Enviar' (idCbSalvarNovo) e 'Preparar'
    # (idCbPrep) — e aparecem MESMO com avisos de "Não foi informado serviço
    # prestado/tomado" (cliente de receita zero). O robô só procurava
    # idCbSalvarEdicao e tratava isso como "DecWeb não liberou o envio".
    # Com --aceitar-avisos, aceita ESSES avisos (e só eles) clicando em
    # 'Preparar' (nunca em 'Preparar e Enviar': o envio continua nos ícones).
    # Qualquer outra pendência ("necessária", "inválid", cadastro...) segue
    # bloqueando como antes.
    if not _elemento_visivel(driver, "//input[contains(@id, 'idCbSalvarEdicao')]"):
        pendencias = _pendencias_do_modal(driver)
        so_avisos_de_receita_zero = bool(pendencias) and all(
            re.search(r"não foi informado serviço (prestado|tomado)", p, re.I) for p in pendencias
        )
        if (
            (ACEITAR_AVISOS or ACEITAR_AVISOS_CLIENTE)
            and so_avisos_de_receita_zero
            and _elemento_visivel(driver, "//input[contains(@id, 'formPrepararDeclaracao:idCbPrep')]")
        ):
            log.warning("Avisos aceitos (--aceitar-avisos / aceitar_avisos=sim no clientes.csv): %s", "; ".join(pendencias))
            _clicar_xpath(driver, "//input[contains(@id, 'formPrepararDeclaracao:idCbPrep')]")
            return True
        try:
            _clicar_xpath(driver, "//input[contains(@id, 'idCbCancelar')]", timeout=8)
        except Exception:
            pass
        raise PendenciaNoDecWeb(
            "o DecWeb não liberou o envio — resolver na mão: "
            + ("; ".join(pendencias) if pendencias else "ver o modal 'Preparar Declaração para envio'")
        )

    _clicar_xpath(driver, "//input[contains(@id, 'idCbSalvarEdicao')]")
    return True


def _aceitar_confirm_se_aparecer(driver: webdriver.Chrome) -> None:
    """Aceita a caixa nativa de confirmação, se o clique tiver disparado
    uma (vários ícones dessa tela usam confirm() do navegador).

    SEGURANÇA: recusa qualquer confirmação que fale em excluir. Os ícones
    de exclusão dessa tela perguntam 'Deseja realmente excluir a
    Declaração/Escrituração...' — se uma dessas aparecer aqui, alguma
    coisa clicou no lugar errado, e aceitar apagaria o trabalho do mês.
    Nesse caso cancela e levanta erro em vez de seguir em frente."""
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
    except Exception:
        return

    alerta = driver.switch_to.alert
    texto = alerta.text or ""
    if "exclu" in texto.lower():
        alerta.dismiss()
        raise RuntimeError(
            f"Apareceu uma confirmação de EXCLUSÃO no meio do envio ({texto!r}) — "
            "cancelada. Confira a tela antes de rodar de novo."
        )
    alerta.accept()


def _conferir_ou_bloquear(cliente: dict, competencia: str) -> None:
    """Confere os Serviços Prestados do DecWeb contra as Emitidas do Portal
    Nacional (ver conferencia_prestados.py). Divergência, ou falta de um dos
    arquivos, BLOQUEIA o envio com uma PENDÊNCIA explicando o que diverge."""
    if not CONFERENCIA_ATIVA:
        log.info("[%s] Conferência DecWeb x Nacional DESLIGADA — enviando sem conferir.", cliente["nome_painel"])
        return
    situacao, texto = cp.conferir_cliente(cliente, competencia, _CFG)
    if situacao == "ok":
        log.info("[%s] Conferência com o Portal Nacional OK — %s", cliente["nome_painel"], texto)
        marcar_etapa(cliente, "conferido")
        return
    if situacao == "sem_emitidas" and POLITICA_SEM_EMITIDAS == "enviar":
        log.warning("[%s] Sem planilha Emitidas para conferir — seguindo e enviando assim mesmo (%s)",
                    cliente["nome_painel"], texto)
        return
    raise PendenciaNoDecWeb(f"envio BLOQUEADO pela conferência com o Portal Nacional — {texto}")


def enviar_por_icones(
    driver: webdriver.Chrome, rotulo_competencia: str, nome_cliente: str
) -> None:
    """Envia a declaração pelos ÍCONES da linha, na 'Relação de
    Declarações' (assume que a página já está nessa tela). Isso ENVIA
    OFICIALMENTE a declaração pra prefeitura, sem pausa de confirmação,
    por decisão da responsável.

    Caminho restaurado em 24/09/2026: era assim que o robô enviava de
    verdade (confirmado nos logs de 07/09/2026, envios bem-sucedidos). Foi
    trocado pelo menu 'Preparar/Enviar' a pedido da responsável, mas esse
    menu simplesmente NÃO EXISTE na tela — o robô travava esperando por
    ele. Ver o diagnóstico no README.

    São DOIS passos, não um: 'Preparar' leva de Aberta → Preparada, e só
    então aparece o ícone de enviar, que leva de Preparada → Enviada. Os
    três casos já vistos na tela real estão tratados abaixo."""
    # Esperar por UM dos dois ícones antes de decidir o que fazer. Olhar
    # uma vez só não serve: no fluxo T isso roda logo depois de voltar da
    # declaração pra lista, com a tela ainda se redesenhando via AJAX — o
    # ícone de preparar existia, mas ainda não estava visível, e o robô
    # concluía "já está Preparada" e travava esperando um ícone de enviar
    # que nunca vinha, porque a declaração seguia Aberta (visto no R & J
    # ODONTOLOGIA em 24/09/2026). Na Fase 2 o bug não aparecia porque a
    # checagem de declaracao_esta_aberta já dava esse tempo.
    def _icone_disponivel(d):
        if _icone_da_linha(d, rotulo_competencia, "prepararDeclaracao"):
            return "prepararDeclaracao"
        if _icone_da_linha(d, rotulo_competencia, "enviarDeclaracao"):
            return "enviarDeclaracao"
        return False

    try:
        acao = WebDriverWait(driver, TIMEOUT_SEGUNDOS).until(_icone_disponivel)
    except Exception:
        raise RuntimeError(
            f"A linha de {rotulo_competencia} não mostrou nem o ícone de preparar "
            "nem o de enviar — confira o estado dela na tela."
        )

    if acao == "prepararDeclaracao":
        log.info("[%s] Preparando a declaração de %s...", nome_cliente, rotulo_competencia)
        _clicar_xpath(
            driver,
            f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
            "/ancestor::*[self::tr or self::div][1]"
            "//input[@type='image'][contains(@id, '::prepararDeclaracao')]",
        )
        _aceitar_confirm_se_aparecer(driver)
        if _confirmar_modal_preparar(driver):
            log.info("[%s] Confirmado no modal 'Preparar Declaração para envio'", nome_cliente)
        else:
            log.info("[%s] Preparada direto, sem modal (caso Original)", nome_cliente)
    else:
        log.info(
            "[%s] %s já está Preparada — indo direto pro envio",
            nome_cliente, rotulo_competencia,
        )

    # o ícone de enviar só existe depois que a declaração está 'Preparada',
    # e a lista se redesenha via AJAX — por isso esperamos ele aparecer em
    # vez de procurar uma vez só
    try:
        WebDriverWait(driver, TIMEOUT_SEGUNDOS).until(
            lambda d: _icone_da_linha(d, rotulo_competencia, "enviarDeclaracao")
        )
    except Exception:
        raise RuntimeError(
            f"A declaração de {rotulo_competencia} não mostrou o ícone de enviar "
            "depois de preparada — confira a linha na tela (o estado dela deve "
            "estar 'Preparada')."
        )

    log.info("[%s] Enviando declaração para a prefeitura...", nome_cliente)
    _clicar_xpath(
        driver,
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
        "//input[@type='image'][contains(@id, '::enviarDeclaracao')]",
    )
    _aceitar_confirm_se_aparecer(driver)
    _confirmar_modal_preparar(driver)
    log.info("[%s] Declaração ENVIADA oficialmente à prefeitura.", nome_cliente)


def _esperar_confirmacao_envio(driver: webdriver.Chrome, rotulo_competencia: str, nome_cliente: str) -> None:
    """Depois de mandar enviar (e já de volta na 'Relação de
    Declarações'), espera a linha mostrar 'Enviada' — a lista se
    redesenha depois do envio, então demora um pouco."""
    espera = WebDriverWait(driver, 60, ignored_exceptions=(StaleElementReferenceException,))
    try:
        espera.until(EC.invisibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Preparar Declaração para envio')]")
        ))
        espera.until(lambda d: _competencia_consta_como_enviada(d, rotulo_competencia))
    except Exception:
        log.warning(
            "[%s] A linha de %s não apareceu como 'Enviada' em 60s — seguindo mesmo assim",
            nome_cliente, rotulo_competencia,
        )


def _xpath_botao_imprimir(rotulo_competencia: str) -> str:
    """XPath do ícone de impressão da linha cuja competência é
    `rotulo_competencia` (ex.: 'Ago/2026'). Sobe da célula de texto até a
    linha e procura o ícone cujo id contém 'declaracao' (visto no
    DevTools: ...:declaracao:0::imp). Quando há várias linhas da mesma
    competência (Original, Retificadora 1, 2...), a primeira visível é a
    mais recente — é essa que queremos."""
    return (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
        "//img[contains(@id, 'declaracao')]"
    )


def _achar_checkbox_por_rotulo(driver: webdriver.Chrome, rotulo: str, timeout: int = TIMEOUT_SEGUNDOS):
    """Acha (sem marcar/desmarcar) o checkbox da linha cujo texto é
    `rotulo`, dentro do modal 'Impressão de documentos' (o checkbox e o
    texto ficam em células/blocos irmãos, não um do lado do outro
    diretamente — por isso sobe até a linha em comum, mesmo padrão usado
    pra achar a linha da competência)."""
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo}')]"
        "/ancestor::*[self::tr or self::div][1]"
        "//input[@type='checkbox']"
    )
    return WebDriverWait(driver, timeout).until(lambda d: _elemento_visivel(d, xpath))


def _definir_checkbox(driver: webdriver.Chrome, rotulo: str, marcar: bool, timeout: int = TIMEOUT_SEGUNDOS) -> bool:
    """Marca ou desmarca o checkbox de `rotulo` conforme `marcar`. Retorna
    se o checkbox está habilitado (a Guia Pagamento, por exemplo, fica
    desabilitada quando não há ISSQN a recolher). Tenta de novo se o
    checkbox ainda não estiver interagível (comum logo depois de fechar o
    aviso 'Mensagem', enquanto o modal ainda está se ajustando)."""
    ultimo_erro = None
    for _ in range(3):
        checkbox = _achar_checkbox_por_rotulo(driver, rotulo, timeout=timeout)
        try:
            if checkbox.is_enabled() and checkbox.is_selected() != marcar:
                checkbox.click()
            return checkbox.is_enabled()
        except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException) as exc:
            ultimo_erro = exc
            time.sleep(0.5)
    raise ultimo_erro


def _fechar_aviso_mensagem(driver: webdriver.Chrome) -> None:
    """Fecha o popup 'Mensagem' que às vezes aparece junto do modal de
    impressão (ex.: 'Guia de Pagamento só é impressa quando o valor for
    superior a R$0,00'), se ele aparecer."""
    try:
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Mensagem')]"))
        )
        _clicar_por_texto(driver, "Ok")
    except Exception:
        pass  # não apareceu dessa vez, segue normal


def _abrir_modal_impressao(driver: webdriver.Chrome, rotulo_competencia: str) -> None:
    """Clica no ícone de impressão da linha (relocaliza toda vez — a
    referência antiga pode ficar inválida depois de abrir/fechar abas) e
    espera o modal 'Impressão de documentos' abrir."""
    # via _clicar_xpath: logo após um envio a lista ainda se redesenha e a
    # máscara do modal de impressão ('mpImpressaoDiv') intercepta o clique
    # — visto em 05/09/2026; com retentativa + clique via JavaScript passa
    _clicar_xpath(driver, _xpath_botao_imprimir(rotulo_competencia))
    WebDriverWait(driver, TIMEOUT_SEGUNDOS).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Impressão de documentos')]"))
    )
    _fechar_aviso_mensagem(driver)


def _imprimir_e_esperar_pdf(driver: webdriver.Chrome, pasta: Path, nome_final: str) -> Path:
    """Clica 'Imprimir' no modal já configurado, espera o PDF cair na pasta
    e renomeia pro nome final. Confirmado contra a tela real: com a
    liberação de download (CDP, em montar_driver) o Chrome baixa o PDF
    sozinho — abre uma aba em branco ('about:blank') e salva como
    'guia_recibo*.pdf'. A aba extra é fechada depois que o arquivo chega."""
    existentes = _snapshot_pasta(pasta)
    aba_original = driver.current_window_handle
    _clicar_xpath(driver, "//button[contains(text(),'Imprimir')] | //input[@value='Imprimir']")

    try:
        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
    except Exception:
        pass  # nem sempre sobra aba aberta quando o download é direto

    arquivo = esperar_download_e_renomear(pasta, existentes, nome_final)

    for aba in [h for h in driver.window_handles if h != aba_original]:
        driver.switch_to.window(aba)
        driver.close()
    driver.switch_to.window(aba_original)
    return arquivo


def _guia_pagamento_tem_valor(driver: webdriver.Chrome) -> bool:
    """Chamar com 'Guia Pagamento' já marcado (isso revela os campos de
    valor). Confere se há de fato algo a pagar — confirmado contra a tela
    real que o checkbox fica clicável mesmo com ISSQN = R$0,00 (não dá
    pra confiar em is_enabled()); nesse caso o Imprimir fica sem efeito."""
    campo = WebDriverWait(driver, TIMEOUT_SEGUNDOS).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//*[contains(text(), 'Valor a Ser Considerado na Guia de Pagamento')]/following::input[1]",
        ))
    )
    valor = (campo.get_attribute("value") or "0").strip()
    return valor not in ("", "0", "0,00", "0.00")


def _fechar_modal_impressao_se_aberto(driver: webdriver.Chrome) -> None:
    """Depois de um Imprimir, o modal pode continuar aberto na aba
    principal; clica em Cancelar se ainda estiver visível, pra poder
    reabrir do zero."""
    try:
        if _elemento_visivel(driver, "//*[contains(text(), 'Impressão de documentos')]"):
            _clicar_por_texto(driver, "Cancelar", timeout=5)
    except Exception:
        pass


def imprimir_declaracao(
    driver: webdriver.Chrome, rotulo_competencia: str, pasta: Path, nome_declaracao: str, nome_issqn: str
) -> tuple[Path, Path | None]:
    """Imprime a declaração em DUAS rodadas separadas, sempre a partir da
    tela 'Relação de Declarações' (sem abrir a declaração) — confirmado
    contra a tela real que marcar Guia Pagamento junto de Declaração +
    Recibo de Entrega muda o layout do modal e o botão Imprimir para de
    responder. Por isso:
      1ª rodada — só Declaração + Recibo de Entrega (Guia nunca é tocada)
      2ª rodada — reabre o modal do zero, marca só a Guia Pagamento e olha
      o valor revelado: se for R$0,00, clica Cancelar (nada a imprimir);
      se houver valor, clica Imprimir. Assim não precisa desmarcar a Guia
      nunca (desmarcar se mostrou instável contra a tela real).
    Retorna (arquivo_declaracao, arquivo_issqn_ou_None), já renomeados."""
    _abrir_modal_impressao(driver, rotulo_competencia)
    _definir_checkbox(driver, "Declaração", True)
    try:
        _definir_checkbox(driver, "Recibo de Entrega", True, timeout=5)
    except Exception:
        # confirmado contra a tela real (07/09/2026): um cliente sem
        # movimento no mês pode ter um modal só com 'Declaração', sem
        # 'Recibo de Entrega' nenhum — opcional, não trava esperando
        log.info("Sem checkbox de Recibo de Entrega nesse modal — seguindo só com Declaração")
    arquivo_declaracao = _imprimir_e_esperar_pdf(driver, pasta, nome_declaracao)

    _fechar_modal_impressao_se_aberto(driver)

    arquivo_issqn = None
    _abrir_modal_impressao(driver, rotulo_competencia)
    _definir_checkbox(driver, "Guia Pagamento", True)
    if _guia_pagamento_tem_valor(driver):
        arquivo_issqn = _imprimir_e_esperar_pdf(driver, pasta, nome_issqn)
    else:
        log.info("Guia de Pagamento sem valor a recolher — não será impressa")
        _clicar_por_texto(driver, "Cancelar")

    return arquivo_declaracao, arquivo_issqn


def _snapshot_pasta(pasta: Path) -> set[str]:
    """Nomes dos arquivos que já existem na pasta — tirar ANTES de clicar em
    Download/Imprimir, pra depois só aceitar arquivo novo. Importante
    porque a pasta de download é compartilhada entre vários clientes e
    guarda arquivos antigos (inclusive de rodadas anteriores do robô)."""
    return {p.name for p in pasta.iterdir()} if pasta.exists() else set()


def _limpar_lixo_do_chrome(pasta: Path) -> None:
    """Junto com cada download do DecWeb (zip ou PDF), o Chrome deixa na
    pasta uma página 'downloads.htm' (visto na pasta real) — lixo que só
    atrapalha. Remove o que conseguir, inclusive um '.crdownload' órfão
    de rodada anterior; se o Chrome ainda estiver gravando (arquivo em
    uso), deixa pra próxima vez — a limpeza NUNCA pode derrubar a rodada
    (foi exatamente isso que aconteceu em 05/09/2026)."""
    for p in pasta.glob("downloads*.htm*"):
        try:
            p.unlink()
        except OSError:
            pass


def esperar_download_e_renomear(
    pasta: Path, existentes: set[str], novo_nome: str, timeout: int = 60, padrao: str = "*.pdf"
) -> Path:
    """Espera aparecer um arquivo NOVO (que não estava em `existentes`, sem
    .crdownload pendente) na pasta, que bata com `padrao`, e renomeia pro
    nome final (substituindo se já existir um com esse nome — rerodar
    gera uma cópia fresca). Levanta TimeoutError se não baixar a tempo."""
    destino = pasta / novo_nome
    _limpar_lixo_do_chrome(pasta)
    inicio = time.time()
    while time.time() - inicio < timeout:
        # só espera por download parcial NOSSO (novo, e que não seja o
        # 'downloads.htm' do Chrome): um .crdownload órfão de rodada
        # anterior, ou o lixo do Chrome ainda gravando, não pode travar aqui
        parciais = [
            p for p in pasta.glob("*.crdownload")
            if p.name not in existentes and not p.name.startswith("downloads")
        ]
        novos = [p for p in pasta.glob(padrao) if p.name not in existentes and p.name != novo_nome]
        if novos and not parciais:
            novos.sort(key=lambda p: p.stat().st_mtime, reverse=True)
            novos[0].replace(destino)
            _limpar_lixo_do_chrome(pasta)
            return destino
        time.sleep(1)
    raise TimeoutError(f"Download não concluiu em {timeout}s (pasta: {pasta})")


def _enviar_se_aberta(
    driver: webdriver.Chrome, rotulo_competencia: str, nome_cliente: str, cliente: dict | None = None,
    competencia: str | None = None,
) -> None:
    """Assume estar na 'Relação de Declarações'. Se a declaração ainda
    precisar ser enviada, envia pelos ícones da própria linha (ver
    enviar_por_icones) e confere o resultado. Se já estiver enviada, não
    faz nada.

    Os ícones ficam na lista, então NÃO se entra mais em 'Valores da
    NFSE' aqui — era o que o caminho antigo pelo menu exigia."""
    if not declaracao_esta_aberta(driver, rotulo_competencia):
        log.info("[%s] Declaração de %s já estava enviada — nada a fazer", nome_cliente, rotulo_competencia)
        if cliente is not None:
            marcar_etapa(cliente, "enviada")
        return

    if cliente is not None and competencia is not None:
        _conferir_ou_bloquear(cliente, competencia)
    enviar_por_icones(driver, rotulo_competencia, nome_cliente)
    _esperar_confirmacao_envio(driver, rotulo_competencia, nome_cliente)
    if cliente is not None:
        marcar_etapa(cliente, "enviada")


def _competencia_consta_como_enviada(driver: webdriver.Chrome, rotulo_competencia: str) -> bool:
    """True quando a PRIMEIRA linha da competência (a mais recente) já
    aparece como 'Enviada em ...' e sem 'Aberta'. False se a lista ainda
    estiver se redesenhando (linha ausente)."""
    xpath = (
        f"//*[contains(normalize-space(text()), '{rotulo_competencia}')]"
        "/ancestor::*[self::tr or self::div][1]"
    )
    linhas = driver.find_elements(By.XPATH, xpath)
    if not linhas:
        return False
    texto = linhas[0].text
    return "Enviada" in texto and "Aberta" not in texto


def enviar_declaracao_se_aberta(driver: webdriver.Chrome, competencia: str, cliente: dict) -> None:
    """FASE 2: se a declaração dessa competência ainda estiver 'Aberta',
    envia automaticamente. Se já estiver enviada, não faz nada."""
    entrar_no_declarante(driver)
    _enviar_se_aberta(driver, competencia_para_rotulo(competencia), cliente["nome_painel"], cliente, competencia)


def _imprimir_e_salvar(driver: webdriver.Chrome, competencia: str, cliente: dict) -> None:
    """Na lista: imprime (Declaração + Recibo de Entrega, e Guia de
    Pagamento/ISSQN só se houver valor) e deixa os PDFs na pasta com o
    nome do padrão do Painel de Fechamento."""
    rotulo = competencia_para_rotulo(competencia)
    nome_cliente = cliente["nome_painel"]
    pasta = Path(cliente["pasta_download"])
    nome_declaracao = nome_arquivo_padrao(cliente, competencia, "DeclaraçãoMensal", "pdf")
    nome_issqn = nome_arquivo_padrao(cliente, competencia, "ISSQN", "pdf")

    arquivo_declaracao, arquivo_issqn = imprimir_declaracao(
        driver, rotulo, pasta, nome_declaracao, nome_issqn
    )
    log.info("[%s] Declaração baixada: %s", nome_cliente, arquivo_declaracao.name)
    if arquivo_issqn:
        log.info("[%s] Guia de Pagamento (ISSQN) baixada: %s", nome_cliente, arquivo_issqn.name)
    marcar_etapa(cliente, "pdf_baixado")


def imprimir_declaracao_enviada(driver: webdriver.Chrome, competencia: str, cliente: dict) -> None:
    """FASE 3: baixa o PDF final de uma declaração já enviada (pela Fase 2
    ou manualmente)."""
    entrar_no_declarante(driver)
    _imprimir_e_salvar(driver, competencia, cliente)


def fluxo_completo(
    driver: webdriver.Chrome, competencia: str, cliente: dict, retificadora: bool = False,
) -> None:
    """TUDO (T): Fases 1 + 2 + 3 em sequência, num único login — cria (ou
    reaproveita) a declaração, baixa os zips, volta pra lista, ENVIA (pelos
    ícones da linha — ver enviar_por_icones) e imprime. Sem pausa de
    revisão no meio, por decisão da responsável (o envio é oficial
    e irreversível)."""
    rotulo = competencia_para_rotulo(competencia)
    nome_cliente = cliente["nome_painel"]

    entrar_no_declarante(driver)

    if _ja_enviada_hoje(driver, rotulo):
        log.warning(
            "[%s] %s já foi ENVIADA hoje (provável rerodada de T após falha "
            "numa etapa anterior) — pulando criação/download/envio, indo "
            "direto pra impressão pra não protocolar outra declaração",
            nome_cliente, rotulo,
        )
        marcar_etapa(cliente, "enviada")
        _imprimir_e_salvar(driver, competencia, cliente)
        return

    _criar_ou_reaproveitar_declaracao(driver, competencia, rotulo, nome_cliente, retificadora, cliente)
    abrir_valores_nfse(driver, rotulo)
    _baixar_excels(driver, competencia, cliente)
    marcar_etapa(cliente, "zips_baixados")
    # os ícones de preparar/enviar ficam na LISTA, então voltamos pra ela
    # antes de enviar (o caminho antigo pelo menu enviava de dentro da
    # declaração, o que não existe na tela real)
    _conferir_ou_bloquear(cliente, competencia)
    _voltar_para_relacao_de_declaracoes(driver)
    enviar_por_icones(driver, rotulo, nome_cliente)
    _esperar_confirmacao_envio(driver, rotulo, nome_cliente)
    marcar_etapa(cliente, "enviada")
    _imprimir_e_salvar(driver, competencia, cliente)


# ----------------------------------------------------------------------
# EXECUÇÃO
# ----------------------------------------------------------------------

def processar_cliente(cliente: dict, competencia: str, fase: str, retificadora: bool = False) -> dict:
    global ACEITAR_AVISOS_CLIENTE
    nome = cliente["nome_painel"]
    ACEITAR_AVISOS_CLIENTE = bool(cliente.get("aceitar_avisos"))
    # a pasta do clientes.csv é ignorada de propósito — a pasta de download
    # é sempre a do mês da competência (ver pasta_download_da_competencia)
    cliente = {**cliente, "pasta_download": pasta_download_da_competencia(competencia), "_etapas": set()}
    resultado = {"cliente": nome, "status": "erro", "detalhe": "", "etapas": []}
    driver = None
    try:
        driver = montar_driver(cliente["pasta_download"])
        logado = fazer_login(driver, cliente["usuario"], cliente["senha"])
        if not logado:
            resultado["status"] = "login_falhou"
            resultado["detalhe"] = "Falha no login (checar usuário/senha)"
            log.error("[%s] %s", nome, resultado["detalhe"])
            return resultado

        log.info("[%s] Login OK", nome)

        if fase == "T":
            fluxo_completo(driver, competencia, cliente, retificadora=retificadora)
        elif fase == "1":
            preparar_declaracao_e_baixar_excels(driver, competencia, cliente, retificadora=retificadora)
        elif fase == "2":
            enviar_declaracao_se_aberta(driver, competencia, cliente)
        else:
            imprimir_declaracao_enviada(driver, competencia, cliente)

        resultado["status"] = "ok"

    except PendenciaNoDecWeb as exc:
        # não é erro do robô: é o site dizendo que falta resolver algo na
        # mão. Fica separado de 'erro' pra não virar ruído no resumo e pra
        # a responsável achar rápido quem precisa dela.
        resultado["status"] = "PENDÊNCIA"
        resultado["detalhe"] = str(exc)
        log.warning("[%s] Não dá pra fechar automaticamente: %s", nome, exc)
        if driver is not None:
            salvar_diagnostico(driver, cliente)
    except Exception as exc:
        resultado["detalhe"] = str(exc)
        log.exception("[%s] Erro inesperado", nome)
        if driver is not None:
            salvar_diagnostico(driver, cliente)
    finally:
        ACEITAR_AVISOS_CLIENTE = False
        resultado["etapas"] = [e for e in ETAPAS_ORDEM if e in cliente["_etapas"]]
        if driver is not None:
            time.sleep(2)  # dá tempo de qualquer download em andamento
            driver.quit()
            time.sleep(3)  # dá tempo do processo do Chrome liberar memória
            # antes de abrir o próximo (ver _sessao_do_driver_caiu)

    return resultado


def _sessao_do_driver_caiu(detalhe: str) -> bool:
    """True se `detalhe` (a mensagem de erro guardada em resultado['detalhe'])
    indica que o processo do Chrome/chromedriver caiu sozinho no meio do
    trabalho, em vez de um problema na própria tela do DecWeb (timeout
    normal, elemento não encontrado etc.) — casos em que vale tentar esse
    cliente de novo do zero, com login e navegador novos.

    Confirmado nos logs de 07/09/2026: aconteceu tanto como 'no such
    window: target window already closed' (a janela fechou sozinha) quanto
    como falha total de conexão HTTP com o driver local (WinError 10061),
    depois de rodar vários clientes em sequência na mesma execução. Repetir
    esse cliente é seguro mesmo se o crash tiver acontecido logo depois do
    envio: _ja_enviada_hoje / _existe_declaracao_aberta já evitam recriar
    ou reenviar uma declaração que já foi enviada ou está em andamento."""
    texto = detalhe.lower()
    return any(s in texto for s in (
        "no such window", "target window already closed",
        "invalid session id", "chrome not reachable",
        "failed to establish a new connection", "connection refused",
        "disconnected: not connected to devtools",
        "read timed out", "readtimeouterror",
    ))


def main():
    ap = argparse.ArgumentParser(
        description="DecWeb Porto Alegre: criar declaração, baixar relatórios, enviar e imprimir.",
        epilog=(
            "O ENVIO OFICIAL (fases 2 e T) só roda com --enviar. Sem --enviar, "
            "use a fase 1 (cria a declaração e baixa os zips, sem enviar)."
        ),
    )
    ap.add_argument("--competencia", help="MM/AAAA (se omitido, pergunta)")
    ap.add_argument("--fase", choices=["1", "2", "3", "T", "t", "C", "c"],
                    help="1 = criar + baixar zips (não envia) | 2 = enviar | 3 = baixar PDF | T = tudo | "
                         "C = só conferir DecWeb x Portal Nacional (sem abrir o site)")
    ap.add_argument("--sem-conferencia", action="store_true",
                    help="desliga a conferência com o Portal Nacional antes do envio (já é o padrão do ini)")
    ap.add_argument("--com-conferencia", action="store_true",
                    help="liga a conferência com o Portal Nacional antes do envio (divergiu -> não envia)")
    ap.add_argument("--clientes", help="números separados por vírgula, ou 'todos' (se omitido, pergunta)")
    ap.add_argument("--retificadora", action="store_true",
                    help="criar como Retificadora (a competência já tem declaração enviada)")
    ap.add_argument("--enviar", action="store_true",
                    help="autoriza o ENVIO OFICIAL à prefeitura (fases 2 e T)")
    ap.add_argument("--aceitar-avisos", action="store_true",
                    help="aceita os avisos 'Não foi informado serviço prestado/tomado' do modal de preparar "
                         "(cliente de receita zero confirmado). Outras pendências continuam bloqueando.")
    args = ap.parse_args()
    interativo = args.fase is None
    global CONFERENCIA_ATIVA, ACEITAR_AVISOS
    if args.com_conferencia and args.sem_conferencia:
        log.error("Use só um: --com-conferencia ou --sem-conferencia — encerrando.")
        return
    if args.com_conferencia:
        CONFERENCIA_ATIVA = True
    if args.sem_conferencia:
        CONFERENCIA_ATIVA = False
    if args.aceitar_avisos:
        ACEITAR_AVISOS = True

    competencia = (args.competencia or input("Competência a processar (MM/AAAA): ")).strip()
    if not re.fullmatch(r"\d{2}/\d{4}", competencia):
        log.error("Competência inválida: %r (esperado formato MM/AAAA, ex.: 09/2026) — encerrando.", competencia)
        return

    fase = args.fase or input(
        "1 = criar declaração + baixar Excel (NÃO envia) | "
        "2 = ENVIAR se ainda estiver Aberta | "
        "3 = baixar PDF de declaração já enviada | "
        "T = Tudo (criar + baixar + ENVIAR + imprimir, sem pausa) | "
        "C = só conferir com o Portal Nacional  [1/2/3/T/C]: "
    )
    fase = fase.strip().upper()
    if fase not in ("T", "1", "2", "3", "C"):
        # confirmado em 07/09/2026: texto sobrando/colado no terminal fez a
        # fase vir corrompida (ex.: "TPYTHON DECWEB_LOGIN.PY"); como isso
        # não batia com "T"/"1"/"2", o código antigo caía silenciosamente
        # na Fase 3 (senão de tudo) — tentou imprimir uma declaração que
        # nunca foi criada. Agora trava com erro claro em vez de adivinhar.
        log.error("Fase inválida: %r (esperado 1, 2, 3, T ou C) — encerrando.", fase)
        return

    envia = fase in ("T", "2")
    if envia and not interativo and not args.enviar:
        log.error(
            "A fase %s ENVIA a declaração oficialmente à prefeitura. Rode de novo com "
            "--enviar para confirmar (ou use --fase 1, que só cria e baixa os zips).", fase,
        )
        return

    retificadora = args.retificadora
    if fase in ("T", "1") and interativo and not retificadora:
        resposta = input(
            "Já existe uma declaração original pra essa competência "
            "(precisa ser Retificadora)? [s/N]: "
        ).strip().lower()
        retificadora = resposta == "s"

    todos = carregar_clientes()

    # confirmado em 05/09/2026: sem essa pergunta, o script processava TODOS
    # os clientes do CSV mesmo quando a intenção era só testar um — perigoso
    # com Fase T/2 (envio oficial). Agora precisa pedir TODOS de propósito.
    if args.clientes is not None:
        filtro = args.clientes.strip()
    else:
        filtro = input(
            f"Digite o número do cliente (coluna 'numero' do CSV, {len(todos)} cadastrados) "
            "pra rodar só ele (vários separados por vírgula), ou digite TODOS pra rodar a lista inteira: "
        ).strip()
    if filtro.upper() == "TODOS":
        clientes = todos
    else:
        pedidos = [n.strip() for n in filtro.split(",") if n.strip()]
        clientes = [c for c in todos if c["numero"] in pedidos]
        faltando = [n for n in pedidos if n not in {c["numero"] for c in clientes}]
        if not clientes or faltando:
            log.error("Cliente(s) sem correspondência em 'numero' no CSV: %s — nada feito.",
                      ", ".join(faltando) or filtro)
            return

    if envia and interativo:
        print(f"\nATENÇÃO: isso vai ENVIAR OFICIALMENTE {len(clientes)} declaração(ões) de {competencia} "
              "à prefeitura, sem pausa e sem volta.")
        if input("Digite ENVIAR para confirmar: ").strip() != "ENVIAR":
            log.info("Envio não confirmado — encerrando sem fazer nada.")
            return

    log.info(
        "Processando %d cliente(s) de %s | Fase %s%s%s | Conferência com o Nacional: %s",
        len(clientes), ARQUIVO_CLIENTES, fase,
        " | Retificadora" if retificadora else "",
        " | ENVIO OFICIAL" if envia else " | sem envio",
        ("LIGADA (sem Emitidas: %s)" % POLITICA_SEM_EMITIDAS) if CONFERENCIA_ATIVA else "DESLIGADA",
    )

    resultados = []
    for cliente in clientes:
        if fase == "C":
            # só local: não abre navegador nem o site
            situacao, texto = cp.conferir_cliente(cliente, competencia, _CFG)
            resultado = {
                "cliente": cliente["nome_painel"],
                "status": "ok" if situacao == "ok" else "PENDÊNCIA",
                "etapas": ["conferido"] if situacao == "ok" else [],
                "detalhe": texto,
            }
            resultados.append(resultado)
            registrar_resultado(competencia, cliente, fase, resultado)
            atualizar_resumo(competencia, todos)
            continue
        resultado = processar_cliente(cliente, competencia, fase, retificadora=retificadora)
        if resultado["status"] == "erro" and _sessao_do_driver_caiu(resultado["detalhe"]):
            log.warning(
                "[%s] O navegador caiu no meio do trabalho (%s) — esperando um "
                "pouco e tentando esse cliente de novo, do zero",
                resultado["cliente"], resultado["detalhe"],
            )
            time.sleep(5)
            etapas_antes = set(resultado["etapas"])
            resultado = processar_cliente(cliente, competencia, fase, retificadora=retificadora)
            resultado["etapas"] = [e for e in ETAPAS_ORDEM if e in (etapas_antes | set(resultado["etapas"]))]
        resultados.append(resultado)
        registrar_resultado(competencia, cliente, fase, resultado)
        atualizar_resumo(competencia, todos)

    log.info("=" * 60)
    log.info("RESUMO DA EXECUÇÃO")
    for r in resultados:
        log.info("  %-40s %-12s %-40s %s", r["cliente"], r["status"], ";".join(r["etapas"]), r["detalhe"])
    log.info("Resumo atualizado em %s", ARQUIVO_RESUMO)


if __name__ == "__main__":
    main()
