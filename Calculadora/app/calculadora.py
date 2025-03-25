def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para numeros negativos")
    if not isinstance(n, int):
        raise TypeError("Fatorial só é definido para números")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
def soma(n, n2):
    if not isinstance(n, (int, float)) or not isinstance(n2, (int, float)):
        raise TypeError("é necessário somente numeros para somar")
    
    else:
        return n + n2

def subtracao(n, n2):
    if not isinstance(n, (int, float)) or not isinstance(n2, (int, float)):
        raise TypeError("é necessário somente numeros para somar")
    
    else:
        return n - n2

def multiplicacao(n, n2):
    if not isinstance(n, (int, float)) or not isinstance(n2, (int, float)):
        raise TypeError("é necessário somente numeros para multiplicar")
    
    else:
        return n * n2
    
def divisao(n, n2):
    if not isinstance(n, (int, float)) or not isinstance(n2, (int, float)):
        raise TypeError("É necessário somente números para dividir")
    if n2 == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    else:
        return n / n2

def exponenciacao(n, n2):
    if not isinstance(n, (int, float)) or not isinstance(n2, (int, float)):
        raise TypeError("É necessário somente números para exponenciação")
    else:
        return n ** n2
