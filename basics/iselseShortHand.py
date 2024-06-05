a = 2
b = 23
print(a) if a < b else ""
print("A") if a > b else print("=") if a == b else print("B")

c = a if a > b else b  # most useful case
print(c)
