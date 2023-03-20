class Person:  # Person class for defining customer
    def __init__(self, id, first_name, last_name):
        self.id = id  # Customer ID
        self.first_name = first_name  # Customer first name
        self.last_name = last_name  # Customer last name


class Account:  # Account class for defining bank account
    def __init__(self, number, type, owner, balance):  # Define init method for Account class, self refers to class instance
        self.number = number  # The account number
        self.type = type  # The type of account
        self.owner = owner  # Owner of the account
        self.balance = balance # Balance of the account


class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

        def add_customer(self, customer):
            self.customers.append(customer)

        def add_account(self, account):
            self.accounts.append(account)

        def rem_account(self, account):
            self.accounts.remove(account)

        def deposit(account, amount):
            account.balance += amount

        def withdraw(self, account, amount):
            if account >= amount:
                account - amount
            else:
                return "You do not have sufficient funds"

        def account_balance(self, account):
            return account.balance
