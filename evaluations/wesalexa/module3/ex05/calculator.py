
def add(x: int, y: int) -> int:
    """get a sum of numbers and return it"""
    return x + y

def subtract(x: int, y: int) -> int:
    """get a sub of numbers and return it"""
    return x - y

def multiply(x: int, y: int) -> int:
    """get a mult of numbers and return it"""
    return x * y

def divide(x: float, y: float) -> float:
    """get a div of numbers and return it"""
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError ("Cannot divide by zero")

def power(x: int, y: int) -> any:
    """get a pow of numbers and return it"""
    return x ** y
