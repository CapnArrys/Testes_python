import pytest

from app.calculadora import exponenciacao

def teste_exponenciacao_positivo():
    assert exponenciacao(2, 3) == 8

def teste_exponenciacao_string():
    with pytest.raises(TypeError):
        exponenciacao(2, "3")

def teste_exponenciacao_negativo():
    assert exponenciacao(5, -1) == 0.2

def teste_exponenciacao_decimal():
    assert exponenciacao(4, 0.5) == 2
