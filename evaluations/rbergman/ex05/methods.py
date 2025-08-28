import sys
if __name__=='__main__':
    if len (sys.argv) > 1:
        x = (str(sys.argv[1]))
        print (f'São maíusculas? {x.isupper()}') 
        print (f'É númerico? {x.isnumeric()}')
        print (f'É ascii? {x.isascii()}')
        print (f'É alfanumérico? {x.isalnum()}')



