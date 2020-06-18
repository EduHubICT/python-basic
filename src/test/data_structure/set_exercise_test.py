import unittest

from src.main.data_structure.set_exercise import *


class TestSet(unittest.TestCase):
    def test_unique_value(self):
        self.assertEqual(create_unique_value([ 1, 1, 2, 4, 3, 5, 3]), { 1, 2, 3, 4, 5})

    def test_accessing_value_in_set(self):
        self.assertEqual(accessing_value_in_set({1, 3, 5, 6, 8, 9}, 3), 'yes')
       
    def test_add_remove_in_set(self):
        self.assertEqual(add_remove_in_set({1, 3, 5, 6, 8, 9}, 2, None), 'Add')
        self.assertEqual(add_remove_in_set({1, 3, 5, 6, 8, 9}, None, 9), 'Remove')
        
    def test_union_intersection_in_set(self):
        self.assertEqual(union_intersection_in_set({1, 3, 5}, {2, 4, 6}, 'Union'), 'Union')
        self.assertEqual(union_intersection_in_set({1, 3, 5}, {2, 3, 6}, 'Intersection'), 'Intersection')
        
    def test_difference_compare_in_set(self):
        self.assertEqual(difference_compare_in_set({1, 3, 5}, {2, 4, 6}, 'Difference'), 'Difference')
        self.assertEqual(difference_compare_in_set({1, 3, 5}, {1, 3, 5, 7, 9}, 'Compare'), 'Subset')
        self.assertEqual(difference_compare_in_set({1, 3, 5, 7, 9, 11,13}, {1, 3, 5, 7, 9}, 'Compare'), 'Superset')


if __name__ == '__main__':
    unittest.main()