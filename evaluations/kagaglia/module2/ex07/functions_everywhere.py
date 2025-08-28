import sys

def shirnk(text: str) -> str:
    '''Return the first eight characters of the given string.

    Args:
        text (str): Input string.

    Returns:
        str: Truncated string.'''
    return text[:8]

def enlarge(text: str) -> str:
    '''Pad the given string with 'Z' until it reaches 8 characters.

    Args:
        text (str): Input string.

    Returns:
        str: Padded string.'''
    return text + ('Z' * max(0, 8 - (len(text))))

if __name__ == '__main__':

    i = 1
    if len(sys.argv) == 1:
        print("None")
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                print(shirnk(arg))
            elif len(arg) < 8:
                print(enlarge(arg))
            else:
                print(arg)
            i += 1
