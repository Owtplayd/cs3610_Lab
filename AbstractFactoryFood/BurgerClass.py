from abc import ABC
from AbstractFactoryFood.IProductClass import IProduct

"""Abstract Burger class implementing IProduct"""

class Burger(IProduct, ABC):
    def __init__(self, price: int = 0, calories: int = 0, descr: str = "") -> None:
        self._price = price
        self._calories = calories
        self._descr = descr

    def get_Price(self) -> int:
        return self._price

    def get_Description(self) -> str:
        return self._descr
