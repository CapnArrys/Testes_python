import pytest

from app.calculadora import divisao

def teste_divisao_positivo():
    assert divisao(6, 3) == 2

def teste_divisao_string():
    with pytest.raises(TypeError):
        divisao("5", 2)

def teste_divisao_zero():
    with pytest.raises(ZeroDivisionError):
        divisao(2, 0)

def teste_divisao_negativo():
    assert divisao(-6, 3) == -2

def teste_divisao_decimal():
    assert divisao(10, 2.5) == 4
