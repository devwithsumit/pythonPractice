class student:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name = n
        self.occ = o
    # def greet():
    #     print("hello")
    def info(self):
        print(f"{self.name} is a {self.occ}")

        
a = student("sumit","student")
b = student("amit","berozgar")
a.info()
b.info()
a.name = 'divya'
a.occupation = ''
a.info()

def greet():
    print('Hello World')
greet()