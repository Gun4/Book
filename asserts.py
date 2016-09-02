import unittest
from Pytest_book.calculate import Calculate

b = []

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual("HelloWorld", self.calc.add("Hello", "World"))
