from CustomerBuilderApp.WebAppBuilderClass import WebAppBuilder
from CustomerBuilderApp.MobileAppBuilderClass import MobileAppBuilder
from CustomerBuilderApp.DirectorClass import Director


def runCustomerBuilderDemo():

    print("=== Building Customer via WebAppBuilder (all fields) ===")
    web_builder = WebAppBuilder()
    director = Director(web_builder)

    customer1 = director.constructCustomer(
        "John",
        "A.",
        "Doe",
        "john.doe@example.com",
        "john.alt@example.com",
        "123-456-7890",
        "321-654-0987",
    )

    print(customer1)

    print("\n=== Building Customer via MobileAppBuilder (mandatory only) ===")
    mobile_builder = MobileAppBuilder()
    director = Director(mobile_builder)

    customer2 = director.constructCustomer(
        "Sarah",
        "",  # middleName ignored
        "Khan",
        "sarah@example.com",
        "",  # secondaryEmail ignored
        "222-333-4444",
        "",  # secondaryMobile ignored
    )

    print(customer2)


if __name__ == "__main__":
    runCustomerBuilderDemo()
