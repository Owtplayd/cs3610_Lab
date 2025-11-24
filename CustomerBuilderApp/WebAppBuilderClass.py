from CustomerBuilderApp.CustomerBuilderInterface import CustomerBuilder
from CustomerBuilderApp.CustomerProductClass import Customer


class WebAppBuilder(CustomerBuilder):
    """Concrete Builder for Web Application.
    Supports ALL fields (mandatory + optional).
    """

    def __init__(self) -> None:
        self._customer = Customer()

    def firstName(self, value: str):
        self._customer.firstName = value
        return self

    def lastName(self, value: str):
        self._customer.lastName = value
        return self

    def middleName(self, value: str):
        self._customer.middleName = value
        return self

    def primaryEmail(self, value: str):
        self._customer.primaryEmail = value
        return self

    def secondaryEmail(self, value: str):
        self._customer.secondaryEmail = value
        return self

    def primaryMobileNumber(self, value: str):
        self._customer.primaryMobileNumber = value
        return self

    def secondaryMobileNumber(self, value: str):
        self._customer.secondaryMobileNumber = value
        return self

    def build(self) -> Customer:
        return self._customer
