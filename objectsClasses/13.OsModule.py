import os

files = os.listdir("objectsClasses")
a = 1
for i in files:
    if i.endswith('.png'):
        os.rename(f"objectsClasses/{i}", f"objectsClasses/{a}.png")
        a = a + 1
# print(files)
# os.rename("objectsClasses/hello.txt", "objectsClasses/file.txt")
