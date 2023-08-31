import unittest

from src.examples.a_example.devprocess import add_numbers, get_remainder, operator_precedence_1, operator_precedence_2, square_value
from src.examples.a_example.devprocess import echo_numbers
from src.examples.a_example.devprocess import floating_point_division
from src.examples.a_example.devprocess import test_integer_division
from src.examples.a_example.devprocess import test_square_value


class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))
    
    def test_add_numbers_425(self):
        self.assertEqual(4.5, add_numbers(2.25, 2.25))

    def test_add_numbers_100(self):
        self.assertEqual(100, add_numbers(100,0))

    def test_echo_number_5(self):
        self.assertEqual(5, echo_numbers(5))

    def test_floating_point_division_1(self):
        self.assertEqual(2.5, floating_point_division(5, 2))

    def test_floating_point_division_2(self):
        self.assertEqual(2.5, floating_point_division(20, 8))

    def test_integer_division_1(self):
        self.assertEqual(2, test_integer_division(5, 2))
    
    def test_integer_division_2(self):
        self.assertEqual(2, test_integer_division(20, 8))
    
    def test_operator_precedence_1(self):
        self.assertEqual(14, operator_precedence_1(12, 6, 3))

    def test_operator_precedence_2(self):
        self.assertEqual(6, operator_precedence_2(12, 6, 3))
    
    def test_square_value_1(self):
        self.assertEqual(4, square_value(2))
        self.assertEqual(16, square_value(4))
    
    def test_get_remainder(self):
        self.assertEqual(0, get_remainder(2, 2))
        self.assertEqual(1, get_remainder(5, 2))
    
