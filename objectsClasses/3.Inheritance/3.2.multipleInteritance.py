#multiple inheritace means inheritance from more than one class
class animal:
    def __init__(self, name, specie) -> None:
        self.name = name
        self.specie = specie

    def makeSound(self):
        print("Sound made by the animal")

class bird:
    def __init__(self, name, specie) -> None:
        self.name = name
        self.specie = specie

    def makeSound(self):
        print("Sound made by the bird")

#multiple inheritance
class aves(animal, bird):
    def __init__(self, name, specie, size):
        super().__init__(name, specie)
        self.size = size

obj1 = aves("sheru", "dog", "avg")
obj1.makeSound()
print(obj1.__dict__)
# print(aves.mro())
