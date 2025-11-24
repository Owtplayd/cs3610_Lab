from abc import ABC, abstractmethod
from AbstractFactoryFood.BurgerClass import Burger
from AbstractFactoryFood.PizzaClass import Pizza

"""Abstract Factory for creating burgers and pizzas"""

class ProductFactory(ABC):

    @abstractmethod
    def createBurger(self, p: int, c: int, d: str) -> Burger:
        pass

    @abstractmethod
    def createPizza(self, p: int, c: int, s: str, d: str) -> Pizza:
        pass

