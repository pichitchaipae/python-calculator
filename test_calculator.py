import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3, 3), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(9, 5), 45)

    #source from https://byjus.com/maths/division/
    def test_divide(self):
        self.assertEqual(self.calc.divide(48, 6), 8) 
        self.assertEqual(self.calc.divide(6, 2), 3)

    #source from https://betterexplained.com/articles/fun-with-modular-arithmetic/#:~:text=The%20modulo%20operation%20(abbreviated%20“mod,you%20divide%205%20by%203.
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2) 
        self.assertEqual(self.calc.modulo(14, 12), 2)
    

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()