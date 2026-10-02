"""Ambiente falso (pastas, .ini e clientes.csv temporários) ANTES de importar o robô, que lê a configuração
sob demanda. Nenhum teste abre o navegador nem o portal."""
import os
import sys
import tempfile
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROJETO))

_TMP = Path(tempfile.mkdtemp(prefix="portal_teste_"))
RAIZ_FECHAMENTO = _TMP / "FECHAMENTO FISCAL"
INI = _TMP / "configuracao.ini"
INI.write_text(f"[pastas]\nraiz_fechamento = {RAIZ_FECHAMENTO}\n", encoding="utf-8")
os.environ["PORTAL_NACIONAL_CONFIG"] = str(INI)
