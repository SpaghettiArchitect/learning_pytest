from employee import Employee


def test_give_default_raise():
    """Test if the default raise is added to the employee's salary."""
    new_employee = Employee("John", "Doe", 30_000)
    new_employee.give_raise()
    assert new_employee.annual_salary == 35_000


def test_give_custom_raise():
    """Test if a custom raise is added to the employee's salary."""
    new_employee = Employee("John", "Doe", 30_000)
    new_employee.give_raise(10_000)
    assert new_employee.annual_salary == 40_000
