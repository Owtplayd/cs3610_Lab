from ZooFactoryMethod.IAnimalClass import IAnimal

from typing import Type
from abc import abstractmethod

"""
The Zoo Interface / Base Class (Creator in Factory Method)
"""


class IZoo:
    def __init__(self) -> None:
        self._animals: list[Type[IAnimal]] = []
        self._ourItinerary: str = ""

    @abstractmethod
    def createAnimals(self) -> None:
        pass

    def askEachAnimalSaySomething(self) -> None:
        for myAnimal in self._animals:
            print(myAnimal.saySomething())

    def startVisit(self) -> None:
        """Template method: create animals, show itinerary, then let them speak"""
        self.createAnimals()
        print(self._ourItinerary)
        self.askEachAnimalSaySomething()
