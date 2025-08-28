import sys

def methods(string : str ) -> None:
    print(f"Is alphabetic? {string.isalpha()}")
    print(f"Is numeric? {string.isnumeric()}")
    print(f"Is ASCII?  {string.isascii()}")
    print(f"Is alphanumeric? {string.isalnum()}")
    ''' Display various string method checks for the given input.

    Args:
        string (str): The input string to be evaluated.

    Prints:
        - Whether the string contains only alphabetic characters.
        - Whether the string is numeric.
        - Whether the string contains only ASCII characters.
        - Whether the string is alphanumeric.'''


if __name__ == '__main__':
   if len(sys.argv) > 1:
       methods(sys.argv[1])
   else: 
       print("Missing arguments.")

    