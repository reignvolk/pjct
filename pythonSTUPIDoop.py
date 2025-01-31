#object = a "bundle" of related attributes (variables) and methods (functions)
# ex. phone, cup, book
# you need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of the object

# Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals
# and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Accepted, balance is now {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Funds Unavailable"
        else:
            self.balance -= amount
            return f"Withdrawal Accepted, balance is now {self.balance}"

acct1 = Account("Crazy", 100)

print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(500))
print(acct1.balance)