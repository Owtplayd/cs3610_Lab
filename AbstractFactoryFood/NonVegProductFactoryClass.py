from AbstractFactoryFood.ProductFactoryClass import ProductFactory
from AbstractFactoryFood.BurgerClass import Burger
from AbstractFactoryFood.PizzaClass import Pizza
from AbstractFactoryFood.NonVegBurgerClass import NonVegBurger
from AbstractFactoryFood.NonVegPizzaClass import NonVegPizza

"""Concrete Factory that creates non-vegetarian burgers and pizzas"""

class NonVegProductFactory(ProductFactory):

    def createBurger(self, p: int, c: int, d: str) -> Burger:
        return NonVegBurger(p, c, d)

    def createPizza(self, p: int, c: int, s: str, d: str) -> Pizza:
        return NonVegPizza(p, c, s, d)
