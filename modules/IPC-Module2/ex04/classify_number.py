import sys

def is_positive(nbr: int) -> bool:
    """This function returns "True" if the given number is positive, otherwise, returns "False" """
    return (nbr > 0)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        print(is_positive(int(sys.argv[1])))