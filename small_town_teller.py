from persistent_small_town_teller import PersistentUtils

class Person:  # Person class for defining customer
    #last_name: object

    def __init__(self, id, firstname, lastname):
        self.id = id  # Customer ID
        self.firstname = firstname  # Customer first name
        self.lastname = lastname  # Customer last name


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
        self.customers[customer.id] = customer.firstname + " " + customer.lastname

    def add_account(self, account: Account):
        self.accounts[account.number] = account

    def rem_account(self, number):
        del self.accounts[number]

    def deposit(self, number, amount):
        if number in self.accounts:
            dep_account = self.accounts.get(number)
            dep_account.balance += float(amount)

    def withdrawal(self, number, amount):
        if number in self.accounts:  # and amount < self.accounts.balance:
            with_account = self.accounts.get(number)
            with_account.balance -= float(amount)
        else:
            return "You do not have sufficient funds"

    def balance_inquiry(self, number):
        return self.accounts.get(number).balance

    def save_data(self):
        PersistentUtils.write_pickle("customers.pickle", self.customers)
        # Calls the write_pickle function from PersistentUtils, creates customers.pickle and writes customer dict to it
        PersistentUtils.write_pickle("accounts.pickle", self.accounts)
        # Calls the write_pickle function from PersistentUtils, creates accounts.pickle and writes accounts dict to it

    def load_data(self):
        PersistentUtils.load_pickle("customers.pickle")
        # Calls the load_pickle function from PersistentUtils, loads customers.pickle
        PersistentUtils.load_pickle("accounts.pickle")
        # Calls the load_pickle function from PersistentUtils, loads accounts.pickle

