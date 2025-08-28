import sys

def downcase_all(str: str) -> str:
    """
    Return the input string with all characters converted to lowercase.

    Args:
        text (str): The input string.

    Returns:
        str: The lowercase version of the input string.
    """
    return str.lower()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        [print(downcase_all(item)) for item in sys.argv[1:]]
    else:
        print(None)