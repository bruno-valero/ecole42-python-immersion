import pytest
from password_validator import is_valid_password

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_minus_8(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_bigger_16(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_has_upper(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_has_lower(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_has_digit(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_has_special_char(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect

@pytest.mark.parametrize("given, expect", 
[
    ("12345678901234567890123456789", False),
    ("A012345678901234", False), #16
    (" 012345678901@aA", False),  #16
    ("Aa@0123456789012", True), #16
    ("012345678901@aA", True),  #15
])
def test_password_has_space(given: str, expect: bool) -> None:
    assert  is_valid_password(given) == expect