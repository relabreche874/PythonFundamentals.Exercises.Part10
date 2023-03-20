class Person:  # Person class for defining customer
    last_name: object

    def __init__(self, id, first_name, last_name):
        self.id = id  # Customer ID
        self.first_name = first_name  # Customer first name
        self.last_name = last_name  # Customer last name


class Account:  # Account class for defining bank account
    def __init__(self, number, ac_type, owner):  # Define init method for Account class, self refers to class instance
        self.number = number  # The account number
        self.ac_type = ac_type  # The type of account
        self.owner = owner  # Owner of the account
        self.balance = 100  # Balance of the account


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, customer: Person):
        self.customers[customer.id] = customer.first_name + " " + customer.last_name

    def add_account(self, account: Account):
        self.accounts[account.number] = account

    def rem_account(self, number):
        del self.accounts[number]

    def deposit(self, number, amount):
        if number in self.accounts:
            dep_account = self.accounts.get(number)
            dep_account.balance += float(amount)

    def withdrawal(self, number, amount):
        if number in self.accounts:  #and amount < self.accounts.balance:
            with_account = self.accounts.get(number)
            with_account.balance -= float(amount)
        else:
            return "You do not have sufficient funds"

    def balance_inquiry(self, number):
        return self.accounts.get(number).balance
