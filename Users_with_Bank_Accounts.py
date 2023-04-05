class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.account = BankAccount(0.02, 0)
        
    def display_info(self):
        print(f"First Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Bank Account Balance: {self.account.balance}")
            
    def make_deposit (self, amount):
        self.account.deposit (amount)
        
    def make_withdraw(self, amount):
        self.account.withdraw (amount)

    def display_user_balance (self):
        print(f"User: {self.name}")
        print(f"Account Balance: {self.account.balance}")


class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
        return self

    @classmethod
    def all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()



user1 = User("David", "DavidD@mail.com", 29)
user1.display_info()
user1.make_deposit(50)
user1.display_info()
user1.display_user_balance()