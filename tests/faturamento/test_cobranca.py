import time
import pytest 
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso",
    [
        (-1,"BRONZE",0),
        (0,"BRONZE",10),
        (100,"OURO",-1),
    ]
)
def test_processar_cobranca_funcional(valor_base, plano, dias_atraso):
    assert processar_cobranca(valor_base, plano, dias_atraso) == -1.0

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso",
    [
        (100, "", 0),
        (100, "DIAMANTE", 0),
        (100, "BRONZE PREMIUM", 0),
    ]
)
def test_processar_cobranca_funcional(valor_base, plano, dias_atraso):
    assert processar_cobranca(valor_base, plano, dias_atraso) == -2.0

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, desconto",
    [
        (100,"BRONZE",0,100.0),
        (100,"PRATA",0,85.0),
        (100,"OURO",0,75.0),
    ]
)
def test_validacao_plano_funcional(valor_base, plano, dias_atraso, desconto):
    assert processar_cobranca(valor_base, plano, dias_atraso) == desconto

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, cobranca_atraso",
    [
        (100,"BRONZE",1,108.40),
        (100,"PRATA",10,96.40),
        (100,"OURO",20,89.00),
    ]
)
def test_atraso_moderado_funcional(valor_base, plano, dias_atraso, cobranca_atraso):
    assert processar_cobranca(valor_base, plano, dias_atraso) == cobranca_atraso

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, atraso_severo",
    [
        (100,"BRONZE",21,146.80),
        (100,"PRATA",30,135.40),
        (100,"OURO",40,129.00),
    ]
)
def test_atraso_severo_funcional(valor_base, plano, dias_atraso, atraso_severo):
    assert processar_cobranca(valor_base, plano, dias_atraso) == atraso_severo

def test_processar_cobranca_tempo_maximo():
    inicio = time.perf_counter()

    processar_cobranca(100, "PRATA", 10)

    fim = time.perf_counter()

    tempo_execucao = fim - inicio

    assert tempo_execucao <= 0.08
