import sys

def shrink(str : str ) -> str:   
    """
    Reduz uma string para os primeiros 8 caracteres.

    Parâmetros:
    str (str): A string original.

    Retorna:
    str: Uma nova string contendo apenas os primeiros 8 caracteres da original.
    """
    return (str[:8])
def enlarge(str : str) -> str:
    """
    Aumenta uma string para 8 caracteres, preenchendo com 'Z' à direita se necessário.

    Parâmetros:
    str (str): A string original.

    Retorna:
    str: Uma nova string com exatamente 8 caracteres, preenchida com 'Z' se for menor.
    """
    return str.ljust(8, 'Z')

    # return (str + ('Z' * (8 - len(str))))
if __name__=='__main__':
    if len (sys.argv) > 1:
        for arg in (sys.argv [1:]):
            if len(arg) > 8:
                print(shrink(arg))
            else:
                print(enlarge(arg))

    


 