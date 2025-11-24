from CustomerBuilderApp.CustomerBuilderInterface import CustomerBuilder
from CustomerBuilderApp.CustomerProductClass import Customer


class Director:
    """Director class that enforces the required build sequence."""

    def __init__(self, builder: CustomerBuilder) -> None:
        self._builder = builder

    def constructCustomer(
        self,
        firstName: str,
        middleName: str,
        lastName: str,
        primaryEmail: str,
        secondaryEmail: str,
        primaryMobileNumber: str,
        secondaryMobileNumber: str,
    ) -> Customer:

        self._builder.firstName(firstName)
        self._builder.middleName(middleName)
        self._builder.lastName(lastName)
        self._builder.primaryEmail(primaryEmail)
        self._builder.secondaryEmail(secondaryEmail)
        self._builder.primaryMobileNumber(primaryMobileNumber)
        self._builder.secondaryMobileNumber(secondaryMobileNumber)

        return self._builder.product
