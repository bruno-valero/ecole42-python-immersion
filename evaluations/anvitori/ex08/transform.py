import sys


def square_even_numbers(my_list: list[int]) -> list[int]:
    """
    Retorna uma nova lista contendo os quadrados dos números pares da lista fornecida.

    Parâmetros:
        my_list (list[int]): Lista de números inteiros.

    Retorna:
        list[int]: Lista com os quadrados dos números pares presentes em `my_list`.

    Exemplo:
        >>> square_even_numbers([1, 2, 3, 4])
        [4, 16]
    """
    return [m**2 for m in my_list if m % 2 == 0]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        values: list[int] = []
        for value in sys.argv[1].split():
            values.append(int(value))
        print(square_even_numbers(values))
