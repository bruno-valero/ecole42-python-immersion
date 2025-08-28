import pytest
from operation import Operation
from account import Account
from utils import format_cents


def test_account(capsys: pytest.CaptureFixture[str]) -> None:
    acc = Account(123, "123.456.789-01")
    assert acc.__repr__() == "Account(123, '123.456.789-01')"
    assert acc.__str__() == "Account: 123\nBalance: [+] R$ 0,00"
    acc.deposit(1122200, "ATM deposit")
    acc.statement()
    captured = capsys.readouterr()
    assert captured.out == "[+] R$ 11.222,00 (ATM deposit)\nBalance: [+] R$ 11.222,00\n"
