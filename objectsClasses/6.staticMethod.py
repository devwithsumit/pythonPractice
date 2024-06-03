class math:
    def __init__(self,num):
        self.num = num
    def addnum(self,n): #normal method
        print(f'adding {self.num} to {n}')
        self.num = self.num + n
    #static method doesn't require self parameter
    @staticmethod
    def add(a,b): 
        return a + b
result = math.add(1,6) #can be accessed directly using classname.methodName(a,b)
print(result)

# a = math(1)
# print(a.num)
# a.addnum(5)
# print(a.num)