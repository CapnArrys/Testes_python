import pytest

from app.calculadora import multiplicacao

def teste_multiplicacao_positivo():
    assert multiplicacao(2, 3) == 6

def teste_multiplicacao_string():
    with pytest.raises(TypeError):
        multiplicacao("5", 2)

def teste_multiplicacao_negativo():
    assert multiplicacao(-2, 3) == -6

def teste_multiplicacao_decimal():
    assert multiplicacao(12.5, 2) == 25
