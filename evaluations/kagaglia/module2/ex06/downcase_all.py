import sys

def down_case(string : str ) -> None:
    print(string.lower())
    '''Prints the lowercase version of the given string.

    Args:
        string (str): The input string to convert to lowercase.'''


if __name__ == '__main__':
   
   i = 1
   if len(sys.argv) > 1:
       while(len(sys.argv) > i):
        down_case(sys.argv[i])
        i += 1
   else: 
       print("None")