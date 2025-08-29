from account import Account
from utils import DuplicatedAccount, AccountNotFount, InvalidInput

class Bank:
    __accounts: list[Account]

    def __init__(self) -> None:
        self.__accounts = []

    def __len__(self) -> int:
        return len(self.__accounts)

    def __getitem__(self, acc_id: int) -> Account:
        def account_exists(acc: Account) -> bool:
            return acc.account_id == acc_id

        exists: list[Account] = list(filter(account_exists, self.__accounts))
        if not len(exists):
            raise AccountNotFount()
        return exists[0]

    def __contains__(self, item: Account | int | str) -> bool:
        exists: list[Account] = []
        if isinstance(item, Account):

            def account_exists(acc: Account) -> bool:
                return acc.account_id == item.account_id and acc.cpf == item.cpf

            exists = list(filter(account_exists, self.__accounts))
        elif isinstance(item, str):

            def cpf_exists(acc: Account) -> bool:
                return acc.cpf == item

            exists = list(filter(cpf_exists, self.__accounts))
        elif isinstance(item, int):

            def id_exists(acc: Account) -> bool:
                return acc.account_id == item

            exists = list(filter(id_exists, self.__accounts))
        else:
            return False
        return len(exists) > 0

    def add_account(self, account: Account) -> None:
        if not account:
            raise InvalidInput()
        if account in self:
            raise DuplicatedAccount()
        self.__accounts.append(account)

    def get_account_by_cpf(self, cpf: str) -> Account:
        if not cpf:
            raise InvalidInput()
        account = list(filter(lambda acc: acc.cpf == cpf, self.__accounts))
        if not len(account):
            raise AccountNotFount()
        return account[0]

    def get_account_by_id(self, account_id: int) -> Account:
        if not account_id:
            raise InvalidInput()
        account = list(
            filter(lambda acc: acc.account_id == account_id, self.__accounts)
        )
        if not len(account):
            raise AccountNotFount()
        return account[0]

    def transfer(
        self,
        source_account: int,
        destination_account: int,
        value: int,
        description: str,
    ) -> None:
        if (
            not source_account
            or not destination_account
            or not value
            or not description
            or source_account == destination_account
        ):
            raise InvalidInput()
        if source_account not in self or destination_account not in self:
            raise AccountNotFount()
        source = list(
            filter(lambda x: x.account_id == source_account, self.__accounts)
        )[0]
        destination = list(
            filter(lambda x: x.account_id == destination_account, self.__accounts)
        )[0]
        source.withdraw(value, description)
        destination.deposit(value, description)
