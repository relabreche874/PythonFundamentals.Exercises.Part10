# Python Object-Oriented Programming

# Method: A function associated with a class

# Class: A blueprint for creating instances



class Employee:
    def __init__(self, firstname, lastname, pay):  # This would be the constructor in Java
        self.first = firstname                                   #  < Class Attribute
        self.last = lastname                                     #  < Class Attribute
        self.pay = pay                                           #  < Class Attribute
        self.email = firstname + '.' + lastname + '@company.com' #  < Class Attribute

    def fullname(self):
         return f"{self.first} {self.last}"


# employee1 = Employee() is an instance of the Employee class

employee1 = Employee('Robert', 'LaBreche', 85000)


employee1.fullname()