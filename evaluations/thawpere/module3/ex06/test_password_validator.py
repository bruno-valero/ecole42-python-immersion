import pytest
import password_validator

@pytest.mark.parametrize("input,expected", [
    ("Abcdef1!", True),
    ("StrongP@ssw0rd", True),
    ("A1b2C3d4!", True),
    ("A1b!", False),
    ("A1b2C3d4E5f6G7h8!", False),
    ("abcdef1!", False),
    ("ABCDEFG1!", False),
    ("0000000000", False),
    ("ABCDEF1!", False),
    ("Abcdefg!", False),
    ("Abcdefg1", False),
    ("Abc def1!", False),
    (" Abcdef1!", False),
    ("Abcdef1! ", False),
    ])

def test_valid_password(input: str, expected: bool) -> None:
    assert password_validator.is_valid_password(input) == expected
