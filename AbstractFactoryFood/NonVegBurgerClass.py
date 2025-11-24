from AbstractFactoryFood.BurgerClass import Burger

"""Concrete Non-Vegetarian Burger"""


class NonVegBurger(Burger):
    def __init__(self, price: int, cals: int, descr: str) -> None:
        super().__init__(price, cals, descr)
