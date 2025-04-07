import pytest
from calculator import Calculator


def test_calculator_initialization():
    """
    Test the initialization of the Calculator with custom values.
    Ensures that the attributes 'a' and 'b' are set correctly.
    """
    calc = Calculator(5, 3)
    assert calc.a == 5
    assert calc.b == 3


def test_calculator_default_initialization():
    """
    Test the default initialization of the Calculator.
    Verifies that 'a' and 'b' are set to 0 when no arguments are provided.
    """
    calc = Calculator()
    assert calc.a == 0
    assert calc.b == 0


def test_calculator_add():
    """
    Test the add() method of the Calculator.
    Checks if the method correctly adds the values of 'a' and 'b'.
    """
    calc = Calculator(5, 3)
    result = calc.add()
    assert result == 8


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_calculator_add_parametrized(a, b, expected):
    """
    Parametrized test for the add() method.
    Tests multiple scenarios of addition with different input values.
    """
    calc = Calculator(a, b)
    assert calc.add() == expected


def test_calculator_add2_with_self_values():
    """
    Test the add2() method using values from self (a and b).
    Verifies that add2() correctly uses the instance attributes.
    """
    calc = Calculator(5, 3)
    result = calc.add2(calc.a, calc.b)
    assert result == 8


def test_calculator_add2_with_direct_arguments():
    """
    Test the add2() method with directly provided arguments.
    Ensures that add2() can work independently of instance attributes.
    """
    calc = Calculator()
    result = calc.add2(10, 20)
    assert result == 30


def test_get_result_before_add():
    """
    Test the get_result() method before any addition operation.
    Checks if it returns None when no calculation has been performed.
    """
    calc = Calculator()
    assert calc.get_result() is None


def test_get_result_after_add():
    """
    Test the get_result() method after an addition operation.
    Verifies that it returns the correct result of the last addition.
    """
    calc = Calculator(5, 3)
    calc.add()
    assert calc.get_result() == 8
