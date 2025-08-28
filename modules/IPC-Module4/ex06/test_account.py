import pytest
from account import Account
from utils import InsufficientBalance


def test_account(capsys: pytest.CaptureFixture[str]) -> None:
    acc = Account(123, "123.456.789-01")
    assert acc.__repr__() == "Account(123, '123.456.789-01')"
    assert acc.__str__() == "Account: 123\nBalance: [+] R$ 0,00"
    acc.deposit(1122200, "ATM deposit")
    acc.statement()
    captured = capsys.readouterr()
    assert captured.out == "[+] R$ 11.222,00 (ATM deposit)\nBalance: [+] R$ 11.222,00\n"


def test_insufficient_balance() -> None:
    with pytest.raises(InsufficientBalance, match="Insuffcient Ballance!!"):
        raise InsufficientBalance()
    with pytest.raises(InsufficientBalance, match="Some Error!!"):
        raise InsufficientBalance("Some Error!!")
