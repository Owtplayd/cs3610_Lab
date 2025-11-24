from abc import ABC, abstractmethod

"""The Product Interface"""


class IProduct(ABC):

    @abstractmethod
    def get_Price(self) -> int:
        """Return the price for this product"""
        pass

    @abstractmethod
    def get_Description(self) -> str:
        """Return a human readable description for this product"""
        pass
