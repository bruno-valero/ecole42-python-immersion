def is_positive (number: int) -> bool:
    """
Verifica se um número inteiro é positivo.

    Parâmetros:
    number (int): O número a ser verificado.

    Retorna:
    bool: True se o número for maior que zero, False caso contrário
"""
    return (number > 0)

print("3:", is_positive(3))
print("50:", is_positive(50))
print("-4:", is_positive(-4))
print("0:", is_positive(0))


