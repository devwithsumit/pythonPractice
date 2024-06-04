from typing import Any


class employee:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is the name of this obj.str"

    def __repr__(self):
        return f"The name of the employee is {self.name} in this obj.repr"
    def __call__(self,):
        return f'you called this function'
        
a = employee("sumit", 11)
print(a)
print(str(a))
print(repr(a))
a()
