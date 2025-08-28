import sys

def square_even_numbers (lista:list[int]) -> list[int]:
    """
    Retorna uma lista contendo os quadrados dos números pares da lista fornecida.

    Parâmetros:
    lista (list[int]): Lista de números inteiros.

    Retorna:
    list[int]: Lista com os quadrados dos números pares encontrados na lista original.
    """
    return [x**2 for x in lista if x % 2 == 0]
if __name__=='__main__':
    args = sys.argv[1]
    Lista: list[int] = list(map(int, args.split()))
    print("Squared Evens:", square_even_numbers(Lista))