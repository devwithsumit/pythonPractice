def fun():
    try:
        l = ['zero','one','two']
        i = int(input("Enter index : "))
        print(l[int(i)])
        return 1
    except:
        print("Invalid input !")
        return 0
    finally:
        print('successful run')

x = fun()
# print(x)
