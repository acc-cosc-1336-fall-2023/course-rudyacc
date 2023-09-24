import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio (self):
        self.assertEqual(0.25, get_options_ratio (5,20))
        self.assertEqual(0.50, get_options_ratio (10,20))

    def test_get_faculty_rating (self):
        self.assertEqual(get_faculty_rating (0.91), "Excellent")
        self.assertEqual(get_faculty_rating (0.85), "Very Good")
        self.assertEqual(get_faculty_rating (0.71), "Good")
        self.assertEqual(get_faculty_rating (0.66), "Needs Improvement")
        self.assertEqual(get_faculty_rating (0.45), "Unacceptable")
        self.assertEqual(get_faculty_rating (-1), "Invalid Rating")
        