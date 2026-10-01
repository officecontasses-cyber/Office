"""Prepara um ambiente falso (pastas e .ini temporários) ANTES de importar o robô, que lê a configuração
no import. Nenhum teste abre o navegador nem o DecWeb."""
import os
import sys
import tempfile
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROJETO))

_TMP = Path(tempfile.mkdtemp(prefix="decweb_teste_"))
RAIZ_FECHAMENTO = _TMP / "FECHAMENTO FISCAL"
INI = _TMP / "configuracao.ini"
INI.write_text(
    f"[pastas]\nraiz_fechamento = {RAIZ_FECHAMENTO}\n[opcoes]\nconferencia = nao\nsem_emitidas = enviar\n",
    encoding="utf-8",
)
os.environ["DECWEB_CONFIG"] = str(INI)
