class math:
    def __init__(self,num):
        self.num = num
    def addnum(self,n): #normal method
        print(f'adding {self.num} to {n}')
        self.num = self.num + n
        return self.num
    #static method doesn't require self parameter
    @staticmethod
    def add(a,b): 
        return a + b
    
result1 = math(8) #cannot acces math.addnum directly
print(result1.addnum(5))

result2 = math.add(1,6) #can be accessed directly using classname.methodName(a,b)
print(result2)

# a = math(1)
# print(a.num)
# a.addnum(5)
# print(a.num)