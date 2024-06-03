class employee:
    company = 'Apple' #class varible
    def __init__(self,name):
        self.name = name
    def details(self):
        print(f'Name : {self.name} , company : {self.company}')
        
sumit = employee('Sumit')
sumit.details()

asmit = employee('Asmit')
asmit.company = 'Google' #instance variable (given)
asmit.details()
# asmit.details()
# asmit.intro()