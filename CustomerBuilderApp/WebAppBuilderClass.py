from CustomerBuilderApp.CustomerBuilderInterface import CustomerBuilder
from CustomerBuilderApp.CustomerProductClass import Customer


class WebAppBuilder(CustomerBuilder):
    """Concrete Builder: Web App collects ALL fields."""

    def __init__(self) -> None:
        self._customer = Customer()

    @property
    def product(self) -> Customer:
        return self._customer

    def firstName(self, value: str):
        self._customer.add("firstName", value)
        return self

    def middleName(self, value: str):
        self._customer.add("middleName", value)
        return self

    def lastName(self, value: str):
        self._customer.add("lastName", value)
        return self

    def primaryEmail(self, value: str):
        self._customer.add("primaryEmail", value)
        return self

    def secondaryEmail(self, value: str):
        self._customer.add("secondaryEmail", value)
        return self

    def primaryMobileNumber(self, value: str):
        self._customer.add("primaryMobileNumber", value)
        return self

    def secondaryMobileNumber(self, value: str):
        self._customer.add("secondaryMobileNumber", value)
        return self
