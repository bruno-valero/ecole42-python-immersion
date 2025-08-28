import sys

arg = sys.argv[1]

try:
    with open(arg, 'r') as file:
        conteudo = file.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Erro inesperado: PermissionError")
except IsADirectoryError:
    print("Argumento enviado é um diretório.")
except UnicodeDecodeError:
    print("Erro inesperado: UnicodeDecodeError")
except Exception as e:
    print(f"Erro inesperado: {type(e).__name__}")