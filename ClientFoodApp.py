from AbstractFactoryFood.FoodAppClass import FoodApp

def runFoodApp():
    app = FoodApp()
    # Example order – you can change this in the notebook to test
    order_names = ["VegBurger", "VegPizza", "NonVegBurger", "NonVegPizza"]
    order = app.makeOrder(order_names)
    print(app.getOrderDescription(order))

if __name__ == "__main__":
    runFoodApp()
