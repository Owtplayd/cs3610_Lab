from ZooFactoryMethod.IAnimalClass import IAnimal

"""
The Moose Concrete Class implements the IAnimal interface
"""


class Moose(IAnimal):
    def __init__(self):
        self.__name = "Moose"

    def saySomething(self) -> str:
        return f"{self.__name}: Snorting and grunting!"
