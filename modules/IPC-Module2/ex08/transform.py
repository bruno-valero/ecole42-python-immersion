import sys


def square_even_numbers(list: list[int]) -> list[int]:
    """
    Return a new list containing the square of each even number from the input list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: A list with the squared values of the even integers from the input list.
    """
    return f"Squared evens: {[nbr**2 for nbr in list if nbr % 2 == 0]}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(square_even_numbers([int(number) for number in sys.argv[1].split()]))
    else:
        print(None)
