import utils


class Operation:
    cents: int
    operation_type: utils.OperationType
    description: str

    def __init__(self, cents: int, description: str) -> None:
        if not cents:
            raise ValueError("conts cannot be zero")
        self.cents = cents
        self.description = description
        self.operation_type = (
            utils.OperationType.CREDIT if cents > 0 else utils.OperationType.DEBIT
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(cents={self.cents}, operation_type='{self.operation_type}', description='{self.description}')"

    def __str__(self) -> str:
        return f"{utils.format_cents(self.cents)} ({self.description})"
