import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            print(float(sys.argv[1]))
        except ValueError:
            print("conversion impossible")
