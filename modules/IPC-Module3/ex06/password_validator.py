import string


def is_valid_password(pss: str) -> bool:
    """Verifies if a password is valid"""
    min_chars_ok = len(pss) >= 8
    max_chars_ok = len(pss) <= 16
    has_lower = len([char for char in pss if char.islower()]) > 0
    has_upper = len([char for char in pss if char.isupper()]) > 0
    has_digit = len([char for char in pss if char.isdigit()]) > 0
    has_special = len([char for char in pss if char in string.punctuation]) > 0
    has_space = len([char for char in pss if char in " "]) > 0

    return (
        min_chars_ok
        and max_chars_ok
        and has_lower
        and has_upper
        and has_digit
        and has_special
        and not has_space
    )
