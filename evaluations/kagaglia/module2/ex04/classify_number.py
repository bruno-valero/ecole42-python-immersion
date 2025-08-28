import sys

def is_positive(number: int) -> bool:
    '''Checks if the given number is positive.'''
    return number > 0
    
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Many arguments.")
    else:
        print(is_positive(int(sys.argv[1])))