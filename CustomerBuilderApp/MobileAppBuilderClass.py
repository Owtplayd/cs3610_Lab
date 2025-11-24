from CustomerBuilderApp.CustomerBuilderInterface import CustomerBuilder
from CustomerBuilderApp.CustomerProductClass import Customer


class MobileAppBuilder(CustomerBuilder):
    """Concrete Builder: Mobile App only collects mandatory fields."""

    def __init__(self) -> None:
        self._customer = Customer()

    @property
    def product(self) -> Customer:
        return self._customer

    def firstName(self, value: str):
        self._customer.add("firstName", value)
        return self

    def middleName(self, value: str):
        # Optional field ignored
        return self

    def lastName(self, value: str):
        self._customer.add("lastName", value)
        return self

    def primaryEmail(self, value: str):
        self._customer.add("primaryEmail", value)
        return self

    def secondaryEmail(self, value: str):
        # Optional field ignored
        return self

    def primaryMobileNumber(self, value: str):
        self._customer.add("primaryMobileNumber", value)
        return self

    def secondaryMobileNumber(self, value: str):
        # Optional field ignored
        return self
