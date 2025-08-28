
import sys

if (__name__ == '__main__'):
    if len(sys.argv[1]) > 1:
        s = (str(sys.argv[1]))
        print(f'São maíusculas? {s.isupper()}')
        print(f'É númerico? {s.isdigit()}')
        print(f'É ascii? {s.isascii()}')
        print(f'É alfanumérico? {s.isalnum()}')