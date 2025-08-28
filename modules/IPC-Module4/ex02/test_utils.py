import pytest
from utils import format_cents


@pytest.mark.parametrize(
    "number, output",
    [
        (11_222_00, "[+] R$ 11.222,00"),
        (-11_222_00, "[-] R$ 11.222,00"),
        (235_779_841_15, "[+] R$ 235.779.841,15"),
        (-235_779_841_15, "[-] R$ 235.779.841,15"),
    ],
)
def test_format_cents(number: int, output: str) -> None:
    assert format_cents(number) == output
