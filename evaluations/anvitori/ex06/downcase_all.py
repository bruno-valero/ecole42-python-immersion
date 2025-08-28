import sys

def downcase_it(a:str) -> str:
    """function to put arguments in lowercase """
    return str.lower(a)
    

if (__name__ == '__main__'):
    if len(sys.argv) > 1:    
        for item  in sys.argv[1 :]:
            print(downcase_it(item))
    else:
        print(None) 
