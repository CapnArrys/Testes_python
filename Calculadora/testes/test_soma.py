import pytest

from app.calculadora import soma

def teste_soma_positivo():
    assert soma(5, 5) == 10

def teste_soma_string():
    with pytest.raises(TypeError):
        soma("5", "5")

def teste_soma_negativo():
    assert soma(-5, -5) == -10

def teste_soma_decimal():
    assert soma(12.5, 12.5) == 25
