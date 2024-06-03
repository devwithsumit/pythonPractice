# class method as alternative constructor
class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def split_method(self,string):
    #     return self(string.split(',')[0],string.split(',')[1])
    @classmethod
    def split_str(cls,string):
        print(string)
        print(string.split(','))
        return cls(string.split(',')[0],string.split(',')[1])

nameAge1 = 'sumit,20'
nameAge2 = 'devraj,21'
e1 = employee.split_str(nameAge1)
# e2 = employee.split_str(nameAge2)
# e1 = employee(nameAge[0],nameAge[1])
# nameAge.split(',')
print(e1.name)
# print(e2.name)
# print(e1.name,e1.age)    
