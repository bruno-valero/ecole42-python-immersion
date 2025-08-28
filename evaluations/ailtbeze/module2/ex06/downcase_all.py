import sys

def downcase_it(arg: str)-> str:
    """receive a str and returns a lowercase version of the argument"""
    return (arg.lower())

def main()-> int:
    """main function: verify args len, prints None if lower than 2 or aply dowcase_it func"""
    argc = len(sys.argv)

    if (argc < 2):
        print(None)
    else:
        for arg in range(1, argc):
            print(downcase_it(sys.argv[arg]))
    return (0)

if __name__ == '__main__':
    sys.exit(main())