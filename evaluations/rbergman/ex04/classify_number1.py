import sys
def is_positive (number: int) -> bool:
    """
    Verifica se o número fornecido é positivo.

    Parâmetros:
    number (int): Número inteiro a ser avaliado.

    Retorna:
    bool: True se o número for maior que zero, False caso contrário.
    """
    return (number > 0)
if __name__ == "__main__":
    args = int(sys.argv[1])
    print(is_positive(args))
