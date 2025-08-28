import pytest
from password_validator import is_valid_password

@pytest.mark.parametrize(
    "password,expected",
    [
        # senhas válidas
        ("Abcdef1!", True),
        ("Password123@", True),
        ("Qwerty9$", True),
        ("XyZ1#abc", True),
        # senhas inválidas
        ("abc", False),            # muito curta
        ("A" * 17, False),         # muito longa
        ("abcdefgh", False),        # só minúscula
        ("ABCDEFGH", False),        # só maiúscula
        ("12345678", False),        # só dígitos
        ("Abcdefgh", False),        # sem dígito e sem especial
        ("Abc12345", False),        # sem especial
        ("Abc!@#$%", False),        # sem dígito
        ("Abc 123!", False),        # contém espaço
    ]
)
def test_passwords(password: str, expected: bool) -> None:
    """Testa senhas válidas e inválidas."""
    assert is_valid_password(password) is expected
