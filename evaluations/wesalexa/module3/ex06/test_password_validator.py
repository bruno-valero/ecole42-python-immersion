import pytest
from password_validator import is_valid_password

@pytest.mark.parametrize("input_test,expected",
                         [
                             ("12345Aa!678", True),
                             ("12345@iI145678", True),
                             ("a1237A@4567", True),
                             ("Aa@123456", True),
                             ("aaaaaaaaaaaaaaa", False),
                             ("a!a89aaAaa1", True),
                             ("@Aa12!456", True),
                             ("@Au492!49", True),
                             ("", False),
                             (" #45hjaAk3", False)
                         ]
                        )

def test_is_valid_password(input_test: any, expected: any) -> None:
    assert is_valid_password(input_test) == expected
