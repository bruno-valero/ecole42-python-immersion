from string import punctuation

def is_valid_password(password: str) -> bool:
    """ Check if it's a valid password """
    size = len(password)
    if not (size >= 8 and size <= 16):
        return False
    elif not any(c.isupper() for c in password):
        return False
    elif not any(c.islower() for c in password):
        return False
    elif not any(c.isdigit() for c in password):
        return False
    elif not any(c in punctuation for c in password):
        return False
    elif any(c.isspace() for c in password):
        return False
    return True
