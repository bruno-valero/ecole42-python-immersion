import sys

def is_positive(num: int) -> bool:
    """receive a int and return bool value"""
    return (num > 0)

def main()-> int:
    """main function: converts sys.argv[1] to int and calls is_positive"""
    if len(sys.argv) != 2:
        print("invalid input")
        return 1
    print(is_positive(int(sys.argv[1])))
    return 0

if __name__ == '__main__':
    sys.exit(main())