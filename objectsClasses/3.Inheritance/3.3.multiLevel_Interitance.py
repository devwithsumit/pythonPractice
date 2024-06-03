#parent class
class employee:
    def __init__(self, name):
        self.name = name
        self.id = id

    def details(self):
        print(f"Name : {self.name}")

    def intro(self):
        print(f"{self.name} is an employee")

# interited class
class programmer(employee):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def details(self):
        super().details()
        print(f"Id : {self.id}")

    def intro(self):
        print(f"{self.name} is a programmer")

# Sub-interited class
class expert(programmer):

    def __init__(self, name, id, company):
        super().__init__(name, id)
        self.company = company

    def details(self):
        super().details()
        print(f"Company : {self.company}")

    def intro(self):
        print(f"{self.name} is an advanced programmer")


sumit = expert("Sumit", 123, "Apple")
sumit.details()
