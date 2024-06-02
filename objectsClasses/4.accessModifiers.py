class employee:
    def __init__(self):
        self.__name = "Dr.Sumit"
        
a = employee()
# print(a.__name) #cannot be accessed directly
print(a._employee__name) #can be acces indirectly

class Student:
    def __init__(self):
        self._name = "Sumit"

    def _funName(self):  # protected method
        return "WebWithSumit"
    
obj = Student()

# calling by object of Student class
print(obj._name)
print(obj._funName())