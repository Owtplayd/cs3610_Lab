from ZooFactoryMethod.IZooClass import IZoo
from ZooFactoryMethod.AnimalsFactoryClass import AnimalsFactory

"""
Toronto Zoo Concrete Class implements the IZoo base class
"""


class TorontoZoo(IZoo):
    def __init__(self) -> None:
        super().__init__()
        self._ourItinerary = (
            "Welcome to the Toronto Zoo! Our itinerary:\n"
            "1) African Savanna\n"
            "2) Tundra Trek\n"
        )

    def createAnimals(self) -> None:
        animals = ["lion", "elephant", "penguin", "white_bear"]
        myAnimals = list(map(AnimalsFactory.createAnimal, animals))

        for myAnimal in myAnimals:
            if myAnimal:
                self._animals.append(myAnimal)
