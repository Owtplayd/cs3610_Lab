from AbstractFactoryFood.PizzaClass import Pizza

"""Concrete Vegetarian Pizza"""

class VegPizza(Pizza):
    def __init__(self, price: int, cals: int, size: str, descr: str) -> None:
        super().__init__(price, cals, size, descr)

    def showVegPizzaAdver(self) -> str:
        return "Hot Veg Pizza – loaded with vegetables and cheese!"
