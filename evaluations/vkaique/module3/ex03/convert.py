import sys

def main() -> None:
    """
    Converte o argumento da linha de comando em float.
    - Imprime o número convertido, ou
    - "conversion impossible" se não puder converter.
    """
    if len(sys.argv) != 2:
        print("usage: python3 convert.py <number>")
        return

    arg: str = sys.argv[1]

    try:
        number: float = float(arg)
        print(number)
    except ValueError:
        print("conversion impossible")


if __name__ == "__main__":
    main()
