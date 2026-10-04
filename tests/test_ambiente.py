import os
import tempfile
import unittest
from pathlib import Path

from robo_issqn.ambiente import ler_env


class TestEnv(unittest.TestCase):
    def test_le_arquivo_e_ignora_comentarios(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / ".env"
            f.write_text('# c\nISSQN_PORTAL_URL="https://x.test"\n\nA=1\n', encoding="utf-8")
            v = ler_env(f)
            self.assertEqual(v["ISSQN_PORTAL_URL"], "https://x.test")
            self.assertEqual(v["A"], "1")

    def test_sistema_tem_prioridade(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / ".env"
            f.write_text("ISSQN_X=arquivo\n", encoding="utf-8")
            os.environ["ISSQN_X"] = "sistema"
            try:
                self.assertEqual(ler_env(f)["ISSQN_X"], "sistema")
            finally:
                del os.environ["ISSQN_X"]

    def test_arquivo_inexistente(self):
        self.assertEqual(ler_env("nao_existe.env"), {})


if __name__ == "__main__":
    unittest.main()
