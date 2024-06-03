class employee:
    company = 'google'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def changeComp(cls,newcomp):
        cls.company = newcomp

e1 = employee('sumit',20)
e2 = employee('devraj',23)
print(e1.company,e2.company,end='\n')
e1.changeComp('apple')
# or
# employee.changeComp('apple')
print(e1.company,e2.company)
        
        
