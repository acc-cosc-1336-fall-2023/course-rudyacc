import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
        
    def test_is_key_in_dictionary(self):
        phonebook = {'Chris': '555-1111', 'Katie' : '555-2222', 'Joanne': '555-3333'}
        
        self.assertEqual(is_key_in_dictionary)
        self.assertEqual(is_key_in_dictionary)

