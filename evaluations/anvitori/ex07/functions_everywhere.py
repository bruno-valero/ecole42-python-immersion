import sys


def shrink(a: str) -> str:
    """
    Retorna os primeiros 8 caracteres da string fornecida.

    Se a string de entrada tiver menos de 8 caracteres, retorna a string original sem modificação.

    Args:
        a (str): A string a ser encurtada.

    Returns:
        str: Uma nova string contendo no máximo os 8 primeiros caracteres da string original.
    """
    return a[:8]


def enlarge(b: str) -> str:
    """
    Preenche a string com a letra 'Z' até que ela tenha pelo menos 8 caracteres.

    Se a string de entrada já tiver 8 ou mais caracteres, ela será retornada sem alterações.

    Args:
        b (str): A string a ser preenchida.

    Returns:
        str: Uma nova string com no mínimo 8 caracteres, preenchida com 'Z' à direita se necessário.
    """
    while len(b) < 8:
        b += "Z"
    return b


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            if len(item) > 8:
                print(shrink(item))
            elif len(item) == 8:
                print(item)
            else:
                print(enlarge(item))
    else:
        print(None)
