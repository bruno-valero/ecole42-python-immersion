from typing import Any

def add(a: float, b: float ) -> float:
    """Return the sum of a and b."""
    return a + b

def subtract(a: float, b: float ) -> float:
    """Return the difference of a and b."""
    return a - b

def multiply(a: float, b: float ) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float ) -> float:
    """Return the division of a by b; raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
    
def power(base: int, exponent: int) -> Any:
    """Return base raised to the power of exponent."""
    return base ** exponent

