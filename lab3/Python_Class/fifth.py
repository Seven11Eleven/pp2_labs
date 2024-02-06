import datetime as dt
class Account:
    def __init__(self, owner = None, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, monthes, percent):
        self.balance += (percent/100) * self.balance
        print(f"Time now: {dt.datetime.now()}.\n{self.owner}, Your balance is {self.balance} tenge")

    def withdraw(self, withdrawal_amount):
        if self.balance <= 0:
            print(f"{self.owner}, you have a negative or zero balance, cannot withdraw money.")
        elif self.balance < withdrawal_amount:
            print(f"{self.owner}, your balance is less than the withdrawable amount, you cannot withdraw money.")
        elif withdrawal_amount < 0:
            print(f"{self.owner}, ha-ha, nice try but you cannot do that")
        else:
            self.balance -= withdrawal_amount
            print(f"{self.owner}, Take your money, have a nice day!\nYour balance now: {self.balance}")

    def show(self):
        print(f"{self.owner}, Your balance:{self.balance}")

proverka = Account("Yernur Toleukhan", 1337)
proverka.deposit(6, 10)
proverka.withdraw(-1337)
proverka.withdraw(1470.7)
proverka.withdraw(100)
proverka.show()

