import pytest

from app.calculadora import fatorial

def teste_fatorial_positivo():
    assert fatorial(5) == 120

def teste_fatorial_zero():
    assert fatorial(0) == 1

def teste_fatorial_maior_que_zero():
    assert fatorial(5) > 0

def teste_fatorial_nao_negativo():
    assert not fatorial(5) < 0

def teste_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-5)

def teste_fatorial_decimal():
    with pytest.raises(TypeError):
        fatorial(5.5)
