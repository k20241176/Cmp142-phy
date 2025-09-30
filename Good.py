class BankAccount:
    def __init__(self, owner: str, starting_balance: float = 0.0):
        self.owner = owner
        self._balance = float(starting_balance)  # _balance is "private"

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance
