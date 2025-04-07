import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calculator = Calculator()

    def tearDown(self):
        """Clean up the Calculator instance after each test."""
        if hasattr(self.calculator, 'result'):
            del self.calculator.result

    def test_get_result_returns_none_before_addition(self):
        """Verifies that the `get_result()` method of the `Calculator` class returns `None`
        before any addition operations have been performed."""
        self.assertIsNone(self.calculator.get_result())

    def test_add_default(self):
        """Verifies that the `add()` method returns 0 when no values are provided
        (default values are used)."""
        result = self.calculator.add()
        self.assertEqual(result, 0)

    def test_add_custom_values(self):
        """Verifies that the `add()` method returns the correct sum when
        custom values are provided."""
        self.calculator.a = 2
        self.calculator.b = 3
        result = self.calculator.add()
        self.assertEqual(result, 5)

    def test_get_result_after_add(self):
        """Verifies that the `get_result()` method returns the correct result after an addition
        operation has been performed."""
        result = self.calculator.get_result()
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
