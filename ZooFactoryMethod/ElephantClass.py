from ZooFactoryMethod.IAnimalClass import IAnimal

"""
The Elephant Concrete Class implements the IAnimal interface
"""


class Elephant(IAnimal):
    def __init__(self):
        self.__name = "Elephant"

    def saySomething(self) -> str:
        return f"{self.__name}: Trumpeting!"
