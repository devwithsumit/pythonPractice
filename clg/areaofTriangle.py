import math


def area():
    s = (a * 3) / 2
    area = (math.sqrt(3) / 4) * a * a
    return area


def perimeter():
    return a * 3


a = int(input("Enter side of triangle : "))
print(f"Area : {area()}")
print(f"Perimeter : {perimeter()}")
