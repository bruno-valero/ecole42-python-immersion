import sys


if __name__=="__main__":
    try:
        name_archive = str(sys.argv[1])
        open_archive = open(name_archive)
        read_archive = open_archive.read()
        print(read_archive)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IsADirectoryError:
        print("Erro: O argumento enviado é um diretório.")
    except Exception as e:
        print(f'Erro inesperado: {type(e).__name__}.')
