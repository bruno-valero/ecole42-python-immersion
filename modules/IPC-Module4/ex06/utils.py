from enum import Enum


def format_cents(cents: int) -> str:
    value = cents * -1 if cents < 0 else cents
    brl = value / 100
    str_cents: str = (
        f"[{'+' if cents >= 0 else '-'}] R$ {brl:,.2f}".replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
    return str_cents


class InsufficientBalance(Exception):
    def __init__(self, message: str = ""):
        super().__init__("Insuffcient Ballance!!" if not message else message)


class DuplicatedAccount(Exception):
    def __init__(self, message: str = ""):
        super().__init__("This account already exists!!" if not message else message)


class AccountNotFount(Exception):
    def __init__(self, message: str = ""):
        super().__init__("Account not found!!" if not message else message)


class InvalidInput(Exception):
    def __init__(self, message: str = ""):
        super().__init__("Invalid input!!" if not message else message)


class OperationType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'
