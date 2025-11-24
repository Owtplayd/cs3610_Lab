from ZooFactoryMethod.IAnimalClass import IAnimal
from ZooFactoryMethod.LionClass import Lion
from ZooFactoryMethod.ElephantClass import Elephant
from ZooFactoryMethod.PenguinClass import Penguin
from ZooFactoryMethod.WhiteBearClass import WhiteBear
from ZooFactoryMethod.GrizzlyBearClass import GrizzlyBear
from ZooFactoryMethod.MooseClass import Moose


class AnimalsFactory:
    """Factory that creates concrete Animal objects."""

    @staticmethod
    def create_animal(kind: str) -> IAnimal | None:
        try:
            k = kind.lower()
            if k == "lion":
                return Lion()
            elif k == "elephant":
                return Elephant()
            elif k == "penguin":
                return Penguin()
            elif k == "white_bear":
                return WhiteBear()
            elif k == "grizzly_bear":
                return GrizzlyBear()
            elif k == "moose":
                return Moose()
            else:
                raise Exception(f"I don't know how to create an animal '{kind}'")
        except Exception as e:
            print(e)
        return None
