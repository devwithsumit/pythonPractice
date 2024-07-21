a = (input("enter a number : "))

print(f"Table of {a} is :")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except Exception as e:
    print("Invalid input !")  # if typeof(input) == string || fraction || decimal
