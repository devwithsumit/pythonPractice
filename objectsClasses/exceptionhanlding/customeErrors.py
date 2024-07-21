a = input("Enter number between 1 to 5 : ")
if int(a) < 1 or int(a) > 5:
    raise ValueError("Value is not in range of 1 to 5")

# Q.raise error the when the input is neither integer
# nor quit

# a = (input('Enter integer or type quit : '))
# if(a != 'quit'):
#     try:
#         a = int(a)
#     except ValueError:
#         raise ValueError()
