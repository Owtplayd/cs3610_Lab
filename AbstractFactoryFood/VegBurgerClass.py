from AbstractFactoryFood.BurgerClass import Burger

"""Concrete Vegetarian Burger"""

class VegBurger(Burger):
    def __init__(self, price: int, cals: int, descr: str) -> None:
        super().__init__(price, cals, descr)

    def showVegBurgerAdver(self) -> str:
        return "Try our fresh Veg Burger packed with veggies!"
