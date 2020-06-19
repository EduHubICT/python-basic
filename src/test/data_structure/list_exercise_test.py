import unittest

from src.main.data_structure.list_exercise import *


class TestList(unittest.TestCase):
    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3]), 2)
        self.assertEqual(find_average([1, 2, 3, 4, 5, 6, 7, -1]), 3.375)

    def test_sort_list(self):
        self.assertEqual(list_sort([3, 5, 1, 9]), [1, 3, 5, 9])

    def test_find_max(self):
        self.assertEqual(find_max([0, 3, 2, 4, 5, 6, 100]), 100)

    def test_find_min(self):
        self.assertEqual(find_min([2, 4, 3, 5, -1, -1000]), -1000)

    def test_find_sum(self):
        self.assertEqual(find_sum([1, 2, 3, 4]), 10)

    def test_sort_list_bubble(self):
        self.assertEqual(sort_list_bubble_asc([10, 9, 8, 7, 5, 1, 2, 4,3, 6]), [1, 2, 3, 4, 5, 6,7, 8, 9, 10])

    def test_sort_list_bubble_dsc(self):
        self.assertEqual(sort_list_bubble_dsc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_slicing_list(self):
        self.assertEqual(list_slicing([1, 2, 3, 4, 5, 6]), [4, 5, 6])

    def test_replace(self):
        self.assertEqual(list_element_replacement([1, 3, 3]), [1, 2, 3])

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 100), "Yes")
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 1000), "No")
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 390), "Yes")
        self.assertEqual(binary_search([1, 5], 100), "No")

    def test_recursive_binary_search(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 3, 0, 7), 'Yes')

    def test_binary_search_index(self):
        self.assertEqual(binary_search_target_index([1, 5, 15, 100, 100, 305, 390], 100, True), 3)

    def test_binary_search_similar_target_count(self):
        self.assertEqual(binary_search_count([1, 5, 15, 100, 100, 305, 390], 100), 2)

    def test_binary_search_circular_sorted(self):
        self.assertEqual(binary_search_circular_sorted([12, 13, 14, 1, 2, 3, 4], 14), 'Yes')

    def test_find_square(self):
        self.assertEqual(find_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        self.assertEqual(find_square([20, 12, 11]), [400, 144, 121])

    def test_find_prime(self):
        self.assertEqual(find_prime_number([11, 12, 33, 84, 95, 101]), [True, False, False, False, False, True])

    def test_insertion_sort_asc(self):
        self.assertEqual(insertion_sort_asc([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort_asc([5, 10, 3, 22, 23, 24, 25]), [3, 5, 10, 22, 23, 24, 25])
        self.assertEqual(insertion_sort_asc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_insertion_sort_dsc(self):
        self.assertEqual(insertion_sort_dsc([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(insertion_sort_dsc([5, 10, 3, 22, 23, 24, 25]), [25, 24, 23, 22, 10, 5, 3])
        self.assertEqual(insertion_sort_dsc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
