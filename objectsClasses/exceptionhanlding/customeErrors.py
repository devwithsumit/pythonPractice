
a = input("Enter number between 1 to 5 : ")
if(a < 1 or a > 5):
    raise ValueError("Value is not in range of 1 to 10")

# Q.raise error the when the input is neither integer
# nor quit
# a = (input('Enter integer or type quit : '))

# if(a != 'quit'):
#     try:
#         a = int(a)
#     except ValueError:
#         raise ValueError()