import sys

def shrink(arg: str)-> str:
    """reduce str to 8 bytes"""
    return (arg[0: 8])

def enlarge(arg: str)-> str:
    """fill str with Z untill 8 bytes"""
    return (arg.ljust(8, 'Z'))

def main()-> int:
    """main function: converts the args to 8 bytes lenght, fill with Z original len is lower than 8"""
    if (len(sys.argv) < 2):
        print(None)
        return (0)
    for arg in range(1, len(sys.argv)):
        if (len(sys.argv[arg]) > 8):
            print(shrink(sys.argv[arg]))
        elif (len(sys.argv[arg]) < 8):
            print(enlarge(sys.argv[arg]))
        else:
            print(sys.argv[arg])
    return (0)

if __name__ == '__main__':
    sys.exit(main())