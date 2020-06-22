import unittest

from src.main.data_structure.lambda_exercise import *


class TestLambda(unittest.TestCase):
    
    def test_find_square_of_value(self):
        closure = find_square_of_value()
        self.assertEqual(closure(2), 4)
        
    def test_find_even_numbers_in_list(self):
        self.assertEqual(multiply_by_two([1, 2, 3]), [2, 4, 6])
        
    def test_find_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        
    def test_add_two_value(self):
        closure = add_two_value(2)
        self.assertEqual(closure(4), 6)


if __name__ == '__main__':
    unittest.main()
