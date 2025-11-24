class Customer:
    """Product class: represents the final Customer object."""

    def __init__(self) -> None:
        self.firstName: str = ""
        self.lastName: str = ""
        self.middleName: str = ""
        self.primaryEmail: str = ""
        self.secondaryEmail: str = ""
        self.primaryMobileNumber: str = ""
        self.secondaryMobileNumber: str = ""

    def __str__(self) -> str:
        return (
            f"Customer(\n"
            f"  firstName='{self.firstName}',\n"
            f"  middleName='{self.middleName}',\n"
            f"  lastName='{self.lastName}',\n"
            f"  primaryEmail='{self.primaryEmail}',\n"
            f"  secondaryEmail='{self.secondaryEmail}',\n"
            f"  primaryMobileNumber='{self.primaryMobileNumber}',\n"
            f"  secondaryMobileNumber='{self.secondaryMobileNumber}'\n"
            f")"
        )
