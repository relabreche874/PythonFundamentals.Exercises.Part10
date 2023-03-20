class Person:  # Person class for defining customer
    def __init__(self, id, first_name, last_name):
        self.id = id  # Customer ID
        self.first_name = first_name  # Customer first name
        self.last_name = last_name  # Customer last name


class Account:  # Account class for defining bank account
    def __init__(self, number, type, owner):  # Define init method for Account class, self refers to class instance
        self.number = number  # The account number
        self.type = type  # The type of account
        self.owner = owner  # Owner of the account
        self.balance = 100  # Balance of the account


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

    def deposit(self, account, amount):
        self.accounts.balance += int(amount)

    def withdraw(self, account, amount):
        if int(account) >= int(amount):
            self.accounts.balance - amount
        else:
            return "You do not have sufficient funds"

    def balance_inquiry(self, account):
        return self.accounts.balance
