import conciliacao_tomados_dominio as c

TEXTO = ("138 09/09/2026 09/09/2026 165 900 39 16 SMARTSALES.ONE LTDA 62.079.320/0001-36 2-933 800 SC 400,00 0,00 "
         "1 140 07/10/2026 11/09/2026 347 900 39 6 GUINTER LUHRING 51.662.579/0001-99 BEM ESTAR 1-933 800 RS 1.300,00 0,00 "
         "126 18/09/2026 18/09/2026 11678 1 36 29 3C PLUS 20.287.691/0001-63 DA INFO 2-102 200 PR 417,90 ICMS 0,00")


def nota(num, cnpj, valor, comp="09/2026", emissao=None):
    return c.Nota(numero=num, cnpj=cnpj, nome="X", valor=valor, competencia=comp, emissao=emissao)


def test_leitura_dominio_so_nfse():
    f = c.ler_dominio_texto(TEXTO)
    assert [(n.numero, n.valor) for n in f.notas] == [(165, 400.0), (347, 1300.0)]   # NF-e (espécie 36) fica de fora


def test_nota_emitida_depois_do_export_do_portal():
    from datetime import datetime
    portal = c.Fonte(notas=[nota(165, "62079320000136", 400.0)], outras_comp=[nota(328, "51662579000199", 1300.0, "08/2026")],
                     gerado_em=datetime(2026, 10, 3, 11, 44))
    decweb = c.Fonte(notas=[nota(165, "62079320000136", 400.0)])
    dom = c.Fonte(notas=[nota(165, "62079320000136", 400.0), nota(347, "51662579000199", 1300.0, emissao=datetime(2026, 10, 7))])
    linhas = {l[1].numero: l for l in c.conciliar(portal, decweb, dom)}
    assert linhas[165][0] == "OK"
    assert linhas[347][0] == "ATENÇÃO" and "rodar o Portal de novo" in linhas[347][5] and "328" in linhas[347][5]
    assert linhas[328][0] == "OUTRA COMP."


def test_falta_no_dominio_e_valor_diferente():
    portal = c.Fonte(notas=[nota(1, "11", 100.0), nota(2, "22", 50.0)])
    decweb = c.Fonte(notas=[nota(1, "11", 100.0), nota(2, "22", 50.0)])
    dom = c.Fonte(notas=[nota(2, "22", 60.0)])
    linhas = {l[1].numero: l for l in c.conciliar(portal, decweb, dom)}
    assert linhas[1][0] == "FALTA"
    assert linhas[2][0] == "ATENÇÃO" and "valores diferentes" in linhas[2][5]
