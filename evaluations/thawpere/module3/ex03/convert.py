import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("One argument only, please")
        sys.exit(1)
    try:
        converted = float(sys.argv[1])
        print(converted)
    except ValueError:
        print("Conversion impossible")
