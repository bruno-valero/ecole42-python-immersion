import pytest
from person import Person


def test_person_initialization() -> None:
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30
    p.birthday()
    assert p.age == 31
    p.birthday()
    assert p.age == 32
