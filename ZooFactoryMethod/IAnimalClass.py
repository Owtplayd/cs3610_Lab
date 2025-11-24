from abc import ABC, abstractmethod

"""The Animal Interface (Product)"""


class IAnimal(ABC):

    @staticmethod
    @abstractmethod
    def saySomething() -> str:
        """Return the sound the animal makes"""
        pass
