from typing import Any

def add(nbr1: int, nbr2: int) -> int:
    """ Add two numbers """
    return nbr1 + nbr2

def subtract(nbr1: int, nbr2: int) -> int:
    """ Subtract two numbers """
    return nbr1 - nbr2

def multiply(nbr1: int, nbr2: int) -> int:
    """ Multiply two numbers """
    return nbr1 * nbr2

def divide(nbr1: int, nbr2: int) -> float:
    """ Divide two numbers """
    try:
        result = nbr1 / nbr2
        return result
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")

def power(base: int, exponent: int) -> Any:
    """ Power of base at exponent """
    return base ** exponent


