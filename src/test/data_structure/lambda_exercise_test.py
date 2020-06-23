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

    
    def test_high_order_function(self):
        self.assertEqual(high_order_function(2, lambda x : x * x), 6)
        
    def test_odd_or_even(self):
        self.assertEqual(even_or_odd(2), 'even')
        
    def test_sort_id_number(self):
        self.assertEqual(sort_id_number(['id1', 'id2', 'id30', 'id3', 'id22', 'id100']),\
                         ['id1', 'id2', 'id3', 'id22', 'id30', 'id100'])

if __name__ == '__main__':
    unittest.main()
