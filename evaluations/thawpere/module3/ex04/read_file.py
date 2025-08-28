import sys

def read_file(file: str) -> None:
    """ Read content file """
    with open(file) as f:
        print(f.read())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("One argument only, please.")
        sys.exit(1)
    try:
        read_file(sys.argv[1])
    except FileNotFoundError:
        print("Error: File not found.")
    except IsADirectoryError:
        print("Error: The argument provided is a directory.")
    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}")

