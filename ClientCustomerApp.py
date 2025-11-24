from CustomerBuilderApp.WebAppBuilderClass import WebAppBuilder
from CustomerBuilderApp.MobileAppBuilderClass import MobileAppBuilder
from CustomerBuilderApp.DirectorClass import Director


def runCustomerBuilderDemo():

    print("=== Building Customer (Web App) ===")
    web_builder = WebAppBuilder()
    director = Director(web_builder)

    customer1 = director.constructCustomer(
        "John",
        "Anthony",
        "Doe",
        "john@example.com",
        "john.alt@example.com",
        "123-456-7890",
        "987-654-3210",
    )

    customer1.showCustomer()

    print("\n=== Building Customer (Mobile App) ===")
    mobile_builder = MobileAppBuilder()
    director = Director(mobile_builder)

    customer2 = director.constructCustomer(
        "Sarah",
        "",
        "Khan",
        "sarah@example.com",
        "",
        "222-333-4444",
        "",
    )

    customer2.showCustomer()


if __name__ == "__main__":
    runCustomerBuilderDemo()
