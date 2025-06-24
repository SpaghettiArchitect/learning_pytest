import pytest
from employee import Employee


@pytest.fixture
def new_employee():
    """An employee that will be available to other tests."""
    new_employee = Employee("John", "Doe", 30_000)
    return new_employee


def test_give_default_raise(new_employee):
    """Test if the default raise is added to the employee's salary."""
    new_employee.give_raise()
    assert new_employee.annual_salary == 35_000


def test_give_custom_raise(new_employee):
    """Test if a custom raise is added to the employee's salary."""
    new_employee.give_raise(10_000)
    assert new_employee.annual_salary == 40_000
