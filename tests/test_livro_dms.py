import unittest

from robo_issqn.config import CLIENTE_126, Competencia, nome_guia, nome_livro_dms
from robo_issqn.livro_dms import escolher_link_da_linha, linhas_da_tabela

P = "form:dataTableConsultaDMS:dataTable:"


def linha(n, comp="2026/09", tipo="NFSe (ADN)"):
    return [
        {"id": f"{P}{n}:j_id_f3:j_id_f4", "texto": "1053665"},
        {"id": f"{P}{n}:j_id_fr:j_id_fs", "texto": comp},
        {"id": f"{P}{n}:j_id_fz:j_id_g0", "texto": tipo},
    ]


class TestNomes(unittest.TestCase):
    def test_padrao_da_pasta_002(self):
        c = Competencia.parse("09/2026")
        self.assertEqual(nome_livro_dms(CLIENTE_126, c), "126_Tatsch&Leite_SãoLeopoldo_09.2026_NFSE_Prest_Tomad.PDF")
        self.assertEqual(nome_guia(CLIENTE_126, c), "126_Tatsch&Leite_SãoLeopoldo_09.2026_ISSQN.PDF")


class TestEscolherLinha(unittest.TestCase):
    comp = Competencia.parse("09/2026")

    def test_uma_linha(self):
        l = escolher_link_da_linha(linha(0), self.comp)
        self.assertEqual(l["texto"], "2026/09")
        self.assertTrue(l["id"].startswith(P + "0:"))

    def test_ignora_outra_competencia(self):
        links = linha(0, comp="2026/08") + linha(1)
        self.assertTrue(escolher_link_da_linha(links, self.comp)["id"].startswith(P + "1:"))

    def test_nenhuma_ou_duas_param(self):
        with self.assertRaises(LookupError):
            escolher_link_da_linha(linha(0, comp="2026/08"), self.comp)
        with self.assertRaises(LookupError):
            escolher_link_da_linha(linha(0) + linha(1), self.comp)

    def test_agrupa(self):
        self.assertEqual(sorted(linhas_da_tabela(linha(0) + linha(3))), [0, 3])


if __name__ == "__main__":
    unittest.main()
