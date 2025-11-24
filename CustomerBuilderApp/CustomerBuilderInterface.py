from abc import ABC, abstractmethod
from CustomerBuilderApp.CustomerProductClass import Customer


class CustomerBuilder(ABC):
    """Builder interface declaring all required steps."""

    @property
    @abstractmethod
    def product(self) -> Customer:
        """Return the final built product."""
        pass

    @abstractmethod
    def firstName(self, value: str):
        pass

    @abstractmethod
    def middleName(self, value: str):
        pass

    @abstractmethod
    def lastName(self, value: str):
        pass

    @abstractmethod
    def primaryEmail(self, value: str):
        pass

    @abstractmethod
    def secondaryEmail(self, value: str):
        pass

    @abstractmethod
    def primaryMobileNumber(self, value: str):
        pass

    @abstractmethod
    def secondaryMobileNumber(self, value: str):
        pass
