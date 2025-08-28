import pytest
from operation import Operation
from account import Account
from bank import Bank
from utils import (
    InvalidInput,
    AccountNotFount,
)


def test_bank(capsys: pytest.CaptureFixture[str]) -> None:
    bank = Bank()
    ac1 = Account(123, "123.456.789-01")
    ac2 = Account(456, "234.567.890-12")
    bank.add_account(ac1)
    bank.add_account(ac2)
    assert len(bank) == 2
    assert (123 in bank) == True
    assert bank[123].__repr__() == "Account(123, '123.456.789-01')"
    bank[123].deposit(10000, "Initial deposit")
    bank.transfer(123, 456, 5000, "Payment")
    bank[456].statement()
    captured = capsys.readouterr()
    assert captured.out == "[+] R$ 50,00 (Payment)\nBalance: [+] R$ 50,00\n"


def test_invalid_input() -> None:
    bank = Bank()
    ac1 = Account(124, "123.456.789-01")
    ac2 = Account(457, "234.567.890-12")
    bank.add_account(ac1)
    bank.add_account(ac2)
    bank[124].deposit(10000, "Initial deposit")
    bank.transfer(124, 457, 5000, "Payment")

    with pytest.raises(InvalidInput, match="Invalid input!!"):
        bank.get_account_by_cpf("")
    with pytest.raises(InvalidInput, match="Invalid input!!"):
        bank.get_account_by_id(0)
    with pytest.raises(InvalidInput, match="Invalid input!!"):
        bank.transfer(123, 456, 5000, "")
    with pytest.raises(InvalidInput, match="Invalid input!!"):
        bank.transfer(13, 456, 5000, "")


def test_account_not_found() -> None:
    bank = Bank()
    ac1 = Account(125, "123.456.789-01")
    ac2 = Account(458, "234.567.890-12")
    bank.add_account(ac1)
    bank.add_account(ac2)
    bank[125].deposit(10000, "Initial deposit")
    bank.transfer(125, 458, 5000, "Payment")

    with pytest.raises(AccountNotFount, match="Account not found!!"):
        bank.get_account_by_id(28)
