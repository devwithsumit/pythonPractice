class animal:
    def __init__(self, name, specie) -> None:
        self.name = name
        self.specie = specie

    def makeSound(self):
        print("Sound made by the animal")

class dog(animal):
    def __init__(self, name, specie):
        animal.__init__(self, name, specie)

    def makeSound(self):
        print("woof... !")

obj1 = dog("sheru", "dog")
obj1.makeSound()

obj2 = animal("nandu", "cat")
obj2.makeSound()
