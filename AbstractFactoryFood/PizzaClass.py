from abc import ABC
from AbstractFactoryFood.IProductClass import IProduct

"""Abstract Pizza class implementing IProduct"""

class Pizza(IProduct, ABC):
    def __init__(self, price: int = 0, calories: int = 0,
                 size: str = "Small", descr: str = "") -> None:
        self._price = price
        self._calories = calories
        self._size = size
        self._descr = descr

    def get_Price(self) -> int:
        return self._price

    def get_Description(self) -> str:
        # Include size in the description to match the idea in the UML
        return f"{self._size} - {self._descr}"
