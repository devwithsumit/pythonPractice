try:
    a = int(input("Enter a :"))
    arr = [23, 88, 2]
    print(arr[a])
except ValueError:
    print("Number entered is invalid")
except IndexError:
    print("Invalid Index")  # if input -3 > input | 2 < input
