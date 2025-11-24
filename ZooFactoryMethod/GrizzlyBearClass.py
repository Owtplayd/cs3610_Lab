from ZooFactoryMethod.IAnimalClass import IAnimal

"""
The GrizzlyBear Concrete Class implements the IAnimal interface
(used for the Calgary Zoo)
"""


class GrizzlyBear(IAnimal):
    def __init__(self):
        self.__name = "Grizzly Bear"

    def saySomething(self) -> str:
        return f"{self.__name}: Grrrr!"
