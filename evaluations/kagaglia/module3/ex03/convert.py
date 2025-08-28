import sys

if len(sys.argv) < 2:
    sys.exit
arg = sys.argv[1]

try:
    valor = float(arg)
    print(valor)
except ValueError:
    print("Conversion impossible")