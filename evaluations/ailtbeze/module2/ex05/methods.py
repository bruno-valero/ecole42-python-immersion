import sys

def main()-> int:
    """main function: print if the input is upper, numeric, ascii and/or alpha"""
    print("São maíusculas?", sys.argv[1].isupper())
    print("É numérico?", sys.argv[1].isdigit())
    print("É ascii?", sys.argv[1].isascii())
    print("É alfanumérico?", sys.argv[1].isalnum())
    return (0)

if __name__ == '__main__':
    sys.exit(main())