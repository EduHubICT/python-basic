import unittest

from src.main.data_structure.list_exercise import find_average
from src.main.data_structure.list_exercise import sort_list

class TestList(unittest.TestCase):

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3]), 2)
        self.assertEqual(find_average([1, 2 , 3, 4, 5, 6, 7, -1]), 3.375)
        
class SortTest(unittest.TestCase):
    
    def test_sort_list(self):
        self.assertEqual(sort_list([3,5,1,9]),[1,3,5,9])

if __name__ == '__main__':
    unittest.main()