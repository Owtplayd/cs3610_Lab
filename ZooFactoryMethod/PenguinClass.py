from ZooFactoryMethod.IAnimalClass import IAnimal

"""
The Penguin Concrete Class implements the IAnimal interface
"""


class Penguin(IAnimal):
    def __init__(self):
        self.__name = "Penguin"

    def saySomething(self) -> str:
        return f"{self.__name}: Squawk, squawk!"
