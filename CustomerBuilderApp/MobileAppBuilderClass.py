from CustomerBuilderApp.CustomerBuilderInterface import CustomerBuilder
from CustomerBuilderApp.CustomerProductClass import Customer


class MobileAppBuilder(CustomerBuilder):
    """Concrete Builder for Mobile App.
    Supports ONLY mandatory fields.
    Optional fields produce no effect.
    """

    def __init__(self) -> None:
        self._customer = Customer()

    def firstName(self, value: str):
        self._customer.firstName = value
        return self

    def lastName(self, value: str):
        self._customer.lastName = value
        return self

    # Unsupported field → ignore
    def middleName(self, value: str):
        return self

    def primaryEmail(self, value: str):
        self._customer.primaryEmail = value
        return self

    # Unsupported field → ignore
    def secondaryEmail(self, value: str):
        return self

    def primaryMobileNumber(self, value: str):
        self._customer.primaryMobileNumber = value
        return self

    # Unsupported field → ignore
    def secondaryMobileNumber(self, value: str):
        return self

    def build(self) -> Customer:
        return self._customer
