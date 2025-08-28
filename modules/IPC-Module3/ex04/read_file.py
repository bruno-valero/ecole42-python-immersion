import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
        except IsADirectoryError:
            print("Erro: O argumento enviado é um diretório.")
        except Exception as e:
            print(f"Erro inesperado: {type(e).__name__}.")
