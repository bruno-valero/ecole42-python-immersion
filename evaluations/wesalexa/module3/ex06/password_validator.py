import string

def len_password(psswd1: str) -> bool:
    """get a len of a string"""
    x = 0
    for i in psswd1:
        x += 1
    if x >= 8 and x <= 16:
        return True
    else:
        return False

def is_space(psswd1: str) -> bool:
    """check if have a space in a string and convert for a return"""
    return not (any(c.isspace() for c in psswd1))

def is_valid_password(psswd1: any) -> bool:
    """get a password (any type) and check your security and return a boolean"""
    pss = str(psswd1)

    if (any(c.isdigit() for c in pss)
    and len_password(pss)
    and any(c.isupper() for c in pss)
    and any(c.islower() for c in pss)
    and any(c in string.punctuation for c in pss)
    and is_space(pss)):
        return True
    else:
        return False
