from AbstractFactoryFood.PizzaClass import Pizza

"""Concrete Non-Vegetarian Pizza"""

class NonVegPizza(Pizza):
    def __init__(self, price: int, cals: int, size: str, descr: str) -> None:
        super().__init__(price, cals, size, descr)
