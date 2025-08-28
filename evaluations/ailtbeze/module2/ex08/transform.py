import sys

def square_even_numbers(numbers: list[int])-> list[int]:
    """receives a list and return a new list of squares for even numbers"""
    return ([x**2 for x in numbers if x % 2 == 0])

def main()-> int:
    """receives a list and then shows the square root of even numbers"""
    int_array = list(map(int, sys.argv[1].split(' ')))
    print("Squared evens:", square_even_numbers(int_array))   
    return (0)

if __name__ == '__main__':
    sys.exit(main())
