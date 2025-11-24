from AbstractFactoryFood.ProductFactoryClass import ProductFactory
from AbstractFactoryFood.BurgerClass import Burger
from AbstractFactoryFood.PizzaClass import Pizza
from AbstractFactoryFood.VegBurgerClass import VegBurger
from AbstractFactoryFood.VegPizzaClass import VegPizza

"""Concrete Factory that creates vegetarian burgers and pizzas"""

class VegProductFactory(ProductFactory):

    def createBurger(self, p: int, c: int, d: str) -> Burger:
        return VegBurger(p, c, d)

    def createPizza(self, p: int, c: int, s: str, d: str) -> Pizza:
        return VegPizza(p, c, s, d)
