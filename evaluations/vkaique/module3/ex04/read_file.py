import sys

def main() -> None:
    """
    Lê e imprime o conteúdo de um arquivo passado como argumento.
    Tratamento de erros:
    - FileNotFoundError → "Erro: Arquivo não encontrado."
    - IsADirectoryError → "Erro: O argumento enviado é um diretório."
    - Qualquer outra exceção → "Erro inesperado: <NomeDaExceção>"
    """
    if len(sys.argv) != 2:
        print("usage: python3 read_file.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IsADirectoryError:
        print("Erro: O argumento enviado é um diretório.")
    except Exception as e:
        print(f"Erro inesperado: {type(e).__name__}")


if __name__ == "__main__":
    main()
