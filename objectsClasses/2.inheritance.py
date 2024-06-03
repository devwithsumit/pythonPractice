class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print(f'Name : {self.name}, Employee id :{self.id}')
# interited class
class programmer(employee):
    def intro(self):
        print(f'{self.name} is a programmer')
sumit = employee('Sumit',400)
asmit = programmer('Asmit',340)
sumit.details()
asmit.details()
asmit.intro()
