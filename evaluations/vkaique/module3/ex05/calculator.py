from typing import Any

def add(a: int, b: int) -> int:
    """Retorna a soma de dois números inteiros."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Retorna a subtração de dois números inteiros."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Retorna a multiplicação de dois números inteiros."""
    return a * b

def divide(a: int, b: int) -> float:
    """
    Retorna a divisão de dois números.
    Levanta ValueError se o divisor for zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base: int, exponent: int) -> Any:
    """
    Retorna base elevado ao expoente, que pode ser int ou float.
    """
    return base ** exponent