import pytest
from operation import Operation
from utils import format_cents


def test_operation() -> None:
    op = Operation(15_000_00, "test")
    assert op.cents == 15_000_00
    assert op.description == "test"
    assert op.operation_type == "credit"
    assert (
        op.__repr__()
        == "Operation(cents=1500000, operation_type='credit', description='test')"
    )
    assert op.__str__() == "[+] R$ 15.000,00 (test)"


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
