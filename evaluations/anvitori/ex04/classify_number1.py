
import sys

def is_positive(a: int) -> bool:
    """ function to see if the number is positive """
    return a > 0

if (__name__ == '__main__'):
    n = (int(sys.argv[1]))
    print(is_positive(n))

