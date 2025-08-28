import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg: str = sys.argv[1]
        print(f"São maíusculas? {arg.isupper()}")
        print(f"É númerico? {arg.isnumeric()}")
        print(f"É ascii? {arg.isascii()}")
        print(f"É alfanumérico? {arg.isalnum()}")