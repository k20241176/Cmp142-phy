class AccountData:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # public data

def deposit(account: AccountData, amount):
    account.balance += amount

def withdraw(account: AccountData, amount):
    account.balance -= amount
