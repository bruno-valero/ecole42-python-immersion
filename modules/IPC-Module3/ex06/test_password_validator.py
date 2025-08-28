import pytest
from password_validator import is_valid_password


@pytest.mark.parametrize(
    "pss, output",
    [
        ("Ola12#", False),
        ("CavalosUp12#AndMoreCaracteres", False),
        ("CAVALOSUP12#", False),
        ("cavalosup12#", False),
        ("CavalosUpdigit#", False),
        ("CavalosUp123", False),
        ("Cavalos Up12#", False),
        ("CavalosUp12#", True),
        ("Ecole42@SP", True),
        ("IReside@Aruja1", True),
    ],
)
def test_is_valid_password(pss: str, output: bool) -> None:
    assert is_valid_password(pss) == output
