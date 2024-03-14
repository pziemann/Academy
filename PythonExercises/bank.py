class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry not enough funds!")
    
    def statement(self):
        print("Your balance: ${}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)
    def __str__(self):
        return "{} Current account balance: {}$".format(self.name, self.balance)
class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 100)
    def __str__(self):
        return "{} savings account balance: {}$".format(self.name, self.balance)
x = Current("Pawel", 500)
y = Savings("Tom", 8000)
print(y)
y.withdrawal(1700)
print(y)
