from operation import Operation
import utils


class Account:
    account_id: int
    cpf: str
    __balance: int
    __operations: list[Operation]

    def __init__(self, account_id: int, cpf: str) -> None:
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self.__operations = []

    def deposit(self, amount: int, description: str) -> None:
        if not amount:
            raise ValueError("amount cannot be zero")
        self.__balance += amount
        self.__operations.append(Operation(amount, description))

    def withdraw(self, amount: int, description: str) -> None:
        if not amount:
            raise ValueError("amount cannot be zero")
        if self.__balance <= 0:
            raise Exception("Insuffcient Ballance!!")
        self.__balance -= amount
        self.__operations.append(Operation(-amount, description))

    def statement(self) -> None:
        [print(op) for op in self.__operations]
        print(f"Balance: {utils.format_cents(self.__balance)}")

    def __str__(self) -> str:
        return (
            f"Account: {self.account_id}\nBalance: {utils.format_cents(self.__balance)}"
        )

    def __repr__(self) -> str:
        return f"Account({self.account_id}, '{self.cpf}')"
