class Employee:
    """Store information about an employee."""

    def __init__(self, first_name: str, last_name: str, annual_salary: float):
        """Stores name and salary information."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount: float = 5_000):
        """Add the given amount to the annual salary."""
        self.annual_salary += amount
