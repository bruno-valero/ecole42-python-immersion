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
        super().__init__(f"Insuffcient Ballance!!" if not message else message)


class OperationType(Enum):
    CREDIT = 1
    DEBIT = 2
