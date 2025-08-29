import sys

if __name__ == "__main__":
    try:
        x = float(sys.argv[1])
        print(x)
    except ValueError:
        print("conversion impossible")
