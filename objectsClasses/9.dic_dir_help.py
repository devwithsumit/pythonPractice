#dir() -> is function to return list of all attributes and methods
# for e.g : print(dir(e1))


#__dict__ -> is an attribute that returns a dictionary of
# an object's attributes
# for e.g : print(e1.__dict__)


#help() - > function used to get help documention of for an object
# for e.g : print(help(e1))

class employee:
    company = 'google'
    def __init__(self,name,age):
        self.name = name
        self.age = age

e1 = employee('sumit',20)
print(dir(e1))
print(e1.__dict__)
# print(help(e1))
