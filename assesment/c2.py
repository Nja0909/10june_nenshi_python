# logic/customer.py

class Person:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

class Customer(Person):
    def __init__(self, name, mobile, customer_id, balance):
        super().__init__(name, mobile)
        self.customer_id = customer_id
        self.__balance = balance  # private field

    def get_balance(self):
        return self.__balance
