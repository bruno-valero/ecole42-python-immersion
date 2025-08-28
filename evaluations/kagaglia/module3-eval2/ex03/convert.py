import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 convert.py <number>")
        sys.exit(1)

    arg = sys.argv[1]

    try:
        valor = float(arg)
        print(valor)
    except ValueError:
        print("conversion impossible")

if __name__ == "__main__":
    sys.exit(main())