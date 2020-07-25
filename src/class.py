"""
Класс, который реализует
базовые возможности
банковского счета.
"""

class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0


my_account = BankAccount(55)
my_account.withdraw(50)
my_account.deposit(10)
print(my_account.balance, my_account.overdrawn())
