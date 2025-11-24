class Customer:
    """Product class built step-by-step by a Builder."""

    def __init__(self) -> None:
        self._components = []  # List of ("fieldName", value)

    def add(self, fieldName: str, value: str) -> None:
        """Add a field/value pair to the customer object."""
        print(f"Adding component: {fieldName} = {value}")
        self._components.append((fieldName, value))

    def showCustomer(self) -> None:
        """Display final components."""
        print("\n=== Final Customer Object ===")
        for field, value in self._components:
            print(f"{field}: {value}")

    def __str__(self) -> str:
        """Pretty print for debugging."""
        output = "Customer(\n"
        for field, value in self._components:
            output += f"  {field} = {value}\n"
        output += ")"
        return output
