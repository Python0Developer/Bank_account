# 2. Write a Python class named BankAccount with two attributes, owner and balance, and two methods, deposit and withdraw.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of {amount} accepted. New balance is {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of {amount} accepted. New balance is {self.balance}"
        else:
            return "Funds unavailable!"

# Example usage
my_account = BankAccount("John", 1000)
print(my_account.owner)  # Output: John
print(my_account.balance)  # Output: 1000

print(my_account.deposit(500))  # Output: Deposit of 500 accepted. New balance is 1500
print(my_account.withdraw(200))  # Output: Withdrawal of 200 accepted. New balance is 1300
print(my_account.withdraw(2000))  # Output: Funds unavailable!

