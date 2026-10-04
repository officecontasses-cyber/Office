import unittest
from decimal import Decimal

from robo_issqn.config import CLIENTE_126, Competencia


class TestCompetencia(unittest.TestCase):
    def test_formatos(self):
        for txt in ("09/2026", "2026-09", "2026/09"):
            c = Competencia.parse(txt)
            self.assertEqual((c.ano, c.mes), (2026, 9))
            self.assertEqual(c.mm_aaaa, "09.2026")
            self.assertEqual(c.portal, "2026/09")

    def test_invalida(self):
        for txt in ("13/2026", "9-2026", "abc"):
            with self.assertRaises(ValueError):
                Competencia.parse(txt)

    def test_cliente(self):
        self.assertEqual(CLIENTE_126.aliquota_iss, Decimal("0.02"))
        self.assertEqual(CLIENTE_126.inscricao_municipal, "445777")


if __name__ == "__main__":
    unittest.main()
