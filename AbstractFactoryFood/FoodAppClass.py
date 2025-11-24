from typing import Dict, List
from AbstractFactoryFood.ProductFactoryClass import ProductFactory
from AbstractFactoryFood.VegProductFactoryClass import VegProductFactory
from AbstractFactoryFood.NonVegProductFactoryClass import NonVegProductFactory
from AbstractFactoryFood.IProductClass import IProduct

"""Client class that uses the Abstract Factory"""

class FoodApp:
    def __init__(self) -> None:
        # Available factories for each category
        # Dict {prodName : ProductFactory} as in the UML
        self.AvailableFood: Dict[str, ProductFactory] = {
            "veg": VegProductFactory(),
            "nonveg": NonVegProductFactory()
        }

    def makeOrder(self, prodNames: List[str]) -> List[IProduct]:
        """Create a list of products based on the order names.

        Supported names (case-insensitive, spaces ignored):
            'VegBurger', 'VegPizza', 'NonVegBurger', 'NonVegPizza'
        """
        ordered_products: List[IProduct] = []

        for name in prodNames:
            lower_name = name.lower().replace(" ", "")
            product = None

            if lower_name == "vegburger":
                factory = self.AvailableFood["veg"]
                product = factory.createBurger(
                    10,    # price
                    450,   # calories
                    "Crispy vegetarian burger"
                )
            elif lower_name == "vegpizza":
                factory = self.AvailableFood["veg"]
                product = factory.createPizza(
                    12,    # price
                    550,   # calories
                    "Medium",
                    "Classic veggie pizza"
                )
            elif lower_name == "nonvegburger":
                factory = self.AvailableFood["nonveg"]
                product = factory.createBurger(
                    14,
                    650,
                    "Juicy beef burger"
                )
            elif lower_name == "nonvegpizza":
                factory = self.AvailableFood["nonveg"]
                product = factory.createPizza(
                    16,
                    750,
                    "Large",
                    "Pepperoni and cheese pizza"
                )
            else:
                print(f"Product '{name}' is not available in the menu.")

            if product:
                ordered_products.append(product)

        return ordered_products

    def getOrderDescription(self, order: List[IProduct]) -> str:
        """Build a textual summary for the given order."""
        lines = []
        total_price = 0

        for idx, product in enumerate(order, start=1):
            price = product.get_Price()
            descr = product.get_Description()
            total_price += price
            lines.append(f"{idx}. {descr} - ${price}")

        lines.append(f"Total price: ${total_price}")
        return "\n".join(lines)
