# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

import random
import string

def reverse(a):
    b = ""
    for i in a:
        b = i + b
    return b

def changeStr(a):
    start = "".join(random.choices(string.ascii_lowercase, k=3))
    end = "".join(random.choices(string.ascii_lowercase, k=3))
    if len(a) < 1:
        return a
    b = a[1:] + a[0]  # from 1 index to last add 0 index elem
    c = start + b + end
    return c

def removeStr(a, num=3):
    b = a[num:-num]
    c = b[-1] + b[:-1]  # add last elem to the 0 to -1 index
    return c

def code(a):
    b = a.split(" ")
    print("\nThe secret coded version : ", end="")
    for i in range(0, len(b)):
        if len(b[i]) <= 3:
            r = reverse(b[i])
            print(r, end=" ")
        else:
            r = changeStr(b[i])
            print(r, end=" ")

def decode(a):
    b = a.split(" ")
    print("\nThe decoded version : ", end="")
    for i in range(0, len(b)):
        if len(b[i]) <= 3:
            r = reverse(b[i])
            print(r, end=" ")
        else:
            r = removeStr(b[i])
            print(r, end=" ")


x = int(input('Press 1 to code or 0  to decode : '))
if x == 1:
    a = input("Enter your message to code : ")
    code(a)
elif x == 0:
    b = input("\nEnter your message to decode it : ")
    decode(b)
else:
    print("Invalid choice! Please enter either 1 or 0.")
