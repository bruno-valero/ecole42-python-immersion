import pytest
import calculator

def test_add() -> None:
    """
    Testa a função add para somas de números positivos e negativos.
    """
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract() -> None:
    """
    Testa a função subtract para subtração de números positivos e negativos.
    """
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 15) == -5

def test_multiply() -> None:
    """
    Testa a função multiply para multiplicação de números positivos e negativos.
    """
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10

def test_divide() -> None:
    """
    Testa a função divide para divisões normais, incluindo resultado float.
    """
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 4) == 2.25

def test_divide_by_zero() -> None:
    """
    Verifica se a função divide lança ValueError quando o divisor é zero.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

def test_power() -> None:
    """
    Testa a função power para diferentes cenários:
    - expoentes positivos
    - expoentes zero
    - expoentes negativos
    - base negativa com expoente positivo
    """
    # expoentes positivos
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1

    # expoentes negativos
    assert calculator.power(2, -2) == 0.25
    assert calculator.power(4, -1) == 0.25

    # base negativa
    assert calculator.power(-2, 3) == -8
    assert calculator.power(-2, 2) == 4
