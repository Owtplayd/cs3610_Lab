from ZooFactoryMethod.IAnimalClass import IAnimal

"""
The Lion Concrete Class implements the IAnimal interface
"""


class Lion(IAnimal):
    def __init__(self):
        self.__name = "Lion"

    def saySomething(self) -> str:
        return f"{self.__name}: Roaring!"
