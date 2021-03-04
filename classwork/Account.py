class Account:
    def __init__(self, account_number, balance = 0):
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


gt_account = Account("1234567890")
gt_account.deposit(100)
gt_account.withdraw(10)

