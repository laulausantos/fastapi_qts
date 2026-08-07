from app.descontos.descontos import calcular_desconto

def test_valor_negativo():
    assert calcular_desconto(-2, True) == 0

def test_cliente_vip_valido():
    assert calcular_desconto(50, True) == 50 * 0.2

def test_cliente_nao_vip_valido():
    assert calcular_desconto(50, False) == 50 * 0.1

def test_valor_zero():
    assert calcular_desconto(0, True) == 0

def test_valor_pequeno():
    resultado = calcular_desconto(0.01, True)
    assert round(resultado, 3) == 0.002

def test_valor_maior():
    assert calcular_desconto(200, True) == 200 * 0.2
