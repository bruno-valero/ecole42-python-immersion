import cowsay

def greeting(name: str='42') -> None:
    """receives a name and prints a greeting"""
    cowsay.cow(f'Hello {name}')
    