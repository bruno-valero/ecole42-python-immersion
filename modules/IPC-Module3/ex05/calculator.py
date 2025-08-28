from typing import Any


def add(n1: float, n2: float) -> float:
    """makes the sum of the two args"""
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    """makes the subtraction of the two args"""
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    """multiplies the two args"""
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    """makes the division of the two args. And handles division by zero"""
    try:
        return n1 / n2
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


def power(base: int, exponent: int) -> Any:
    """makes the sum of the two args"""
    return base**exponent
