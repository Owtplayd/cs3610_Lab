from ZooFactoryMethod.IZooClass import IZoo
from ZooFactoryMethod.AnimalsFactoryClass import AnimalsFactory

'''
Calgary Zoo Concrete Class implements the IZoo base class
'''

class CalgaryZoo(IZoo):
    def __init__(self) -> None:
        super().__init__()
        self._ourItinerary = (
            "Welcome to the Calgary Zoo! Our itinerary:\n"
            "1) Penguin Plunge\n"
            "2) Wild Canada\n"
        )

    def createAnimals(self) -> None:
        animals = ['grizzly_bear', 'moose', 'penguin']
        myAnimals = list(map(AnimalsFactory.createAnimal, animals))

        for myAnimal in myAnimals:
            if myAnimal:
                self._animals.append(myAnimal)
