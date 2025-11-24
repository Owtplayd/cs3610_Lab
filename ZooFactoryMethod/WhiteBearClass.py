from ZooFactoryMethod.IAnimalClass import IAnimal

"""
The WhiteBear Concrete Class implements the IAnimal interface
(used for the Toronto Zoo)
"""


class WhiteBear(IAnimal):
    def __init__(self):
        self.__name = "White Bear"

    def saySomething(self) -> str:
        return f"{self.__name}: *deep growl*"
