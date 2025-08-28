import sys


def shrink(str: str) -> str:
    """
    Return the input string unchanged if its length is less than 8.
    Otherwise, return only the first 8 characters.

    Args:
        text (str): The input string.

    Returns:
        str: The original string or the first 8 characters if it's longer.
    """
    return str[:8]


def enlarge(str: str) -> str:
    """
    Return the input string padded with 'Z' to make it exactly 8 characters long.
    If the string is longer than 8 characters, return only the first 8 characters.

    Args:
        text (str): The input string.

    Returns:
        str: A string of exactly 8 characters.
    """
    if len(str) > 8:
        return str[:8]
    return str + ("Z" * (8 - len(str)))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        [
            print(shrink(item) if len(item) > 8 else enlarge(item))
            for item in sys.argv[1:]
        ]
    else:
        print(None)
