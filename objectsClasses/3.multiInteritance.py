class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print(f'Name : {self.name}\nEmployee id :{self.id}')
    def intro(self):
        print(f'{self.name} is an employee')     
# interited class
class programmer(employee):
    def intro(self):
        print(f'{self.name} is now a programmer')

# Sub-interited class
class expert(programmer):
    def intro(self):
        print(self.name,"is now an advanced programmer\n"
              "Employee id is", self.id)
sumit = employee('Sumit',400)
asmit = expert('Asmit',340)
sumit.details()
sumit.intro()
asmit.intro()