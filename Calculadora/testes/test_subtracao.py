import pytest

from app.calculadora import subtracao

def teste_subtracao_positivo():
    assert subtracao(5, 5) == 0

def teste_subtracao_string():
    with pytest.raises(TypeError):
        subtracao("2", "1")

def teste_subtracao_negativo():
    assert subtracao(-5, -5) == 0

def teste_subtracao_decimal():
    assert subtracao(22.5, 12.5) == 10

def teste_subtracao_extra():
    assert subtracao(10, -10) == 20
