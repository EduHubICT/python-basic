import unittest


from src.main.data_structure.list_exercise import *


class TestList(unittest.TestCase):

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3]), 2)
        self.assertEqual(find_average([1, 2 , 3, 4, 5, 6, 7, -1]), 3.375)
    
    def test_sort_list(self):
        self.assertEqual(sort_list([3,5,1,9]),[1,3,5,9])

    def test_find_max(self):
        self.assertEqual(find_max([0, 3, 2, 4, 5, 6, 100]), 100)

    def test_find_min(self):
        self.assertEqual(find_min([2, 4, 3, 5, -1, -1000]), -1000)

    def test_find_sum(self):
        self.assertEqual(find_sum([1, 2, 3, 4]), 10)

    def test_sort_list_bubble(self):
        self.assertEqual(sort_list_bubble_asc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_list_bubble_dsc(self):
        self.assertEqual(sort_list_bubble_dsc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

        
if __name__ == '__main__':
    unittest.main()