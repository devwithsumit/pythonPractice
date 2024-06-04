#The super() keyword in Python is used to refer to the
# parent class. It is especially useful when a class 
# inherits from multiple parent classes and you want
# to call a method from one of the parent classes.
# class parent:
#     def parentMethod(self):
#         print("parent method")
# class child(parent):
#     def childMethod(self):
#         print('child method')
#         super().parentMethod() #calling parent's method inside child's method
        
# obj = child()
# obj.childMethod()


class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id) #calling parent's construction function
        self.lang = lang
rohan = Employee("Rohan Das", "420")
print(rohan.__dict__)
Sumit = Programmer("Sumit", "2345", "Python")
print(Sumit.__dict__)