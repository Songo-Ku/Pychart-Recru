# from typing import List


class Calculator:
    def __init__(self, a: int = 0, b: int = 0):
        self.a = a
        self.b = b
        self.result = None

    def add(self) -> float:
        self.result = self.a + self.b
        return self.result

    def add2(self, a: int, b: int) -> float:
        return a + b

    def get_result(self) -> float:
        """Retrieve the result of the last addition."""
        return getattr(self, 'result', None)

# user_name = 'John Doe'
# # Example usage
# calculator = Calculator(1, 2)
# print(calculator.add())
