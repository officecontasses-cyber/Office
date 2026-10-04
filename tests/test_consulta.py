import unittest

from robo_issqn.consulta import escolher_opcao

OPCOES = [
    "Nenhum",
    "DURIN COMERCIO DE PRODUTOS NATURAIS LTDA - ME [509815] - 509815",
    "TATSCH E LEITE CENTRO ODONTOLOGICO S/S [445777] - 445777",
]


class TestEscolherOpcao(unittest.TestCase):
    def test_acha_pela_inscricao(self):
        self.assertIn("TATSCH", escolher_opcao(OPCOES, "445777"))

    def test_nao_acha(self):
        with self.assertRaises(LookupError):
            escolher_opcao(OPCOES, "999999")

    def test_ambigua(self):
        with self.assertRaises(LookupError):
            escolher_opcao(OPCOES + ["OUTRA [445777] - 445777"], "445777")


if __name__ == "__main__":
    unittest.main()
