import pytest

from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 0, False, "renda invalida"),
        (-1, -1, True, "renda invalida"),
        (1,-2, False, "score invalido"),
        (1, 1100, False, "score invalido"),
        (2, 900, True, "reprovado"),
        (5, 300, False, "reprovado"),
        (3, 600, False, "aprovado padrao"),
        (4, 900, False, "aprovado premium")
    ]
)

def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado

@pytest.mark.parametrize(
     "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 1, True, "renda invalida"),
        (-1, 0, True, "renda invalida"),
        (200, 399, True, "reprovado"),
        (100, 400, False, "aprovado padrao"),
        (300, 699, False, "aprovado padrao"),
        (400, 700, False, "aprovado premium"),
        (100, 1000, False, "aprovado premium"),
        (100, 1001, False, "score invalido"),
     
    ]
)
def test_fronteira_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado
