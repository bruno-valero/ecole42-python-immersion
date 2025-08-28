import sys
def downcase_all (value : str) -> str:
    """
    Converte todos os caracteres de uma string para minúsculas.

    Parâmetros:
    value (str): A string que será convertida.

    Retorna:
    str: A mesma string com todos os caracteres em minúsculo.
    """
    return (value.lower())
if __name__=='__main__':
    if len(sys.argv) >= 2:
        for arg in (sys.argv [1:]):
            print(downcase_all(arg))
    else:
        print ("None")


    


