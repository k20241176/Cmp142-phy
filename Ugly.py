GLOBAL_BALANCE = 0

class GodAccount:
    def __init__(self): pass

    def deposit_and_print(self):
        global GLOBAL_BALANCE
        amount = float(input("Enter deposit: "))   # direct I/O in class
        GLOBAL_BALANCE += amount
        print(f"New balance: {GLOBAL_BALANCE}")

    def withdraw_and_print(self):
        global GLOBAL_BALANCE
        amount = float(input("Enter withdraw: "))
        GLOBAL_BALANCE -= amount
        print(f"New balance: {GLOBAL_BALANCE}")
