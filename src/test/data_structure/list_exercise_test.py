import unittest

from src.main.data_structure.list_exercise import find_average



class TestList(unittest.TestCase):

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3]), 2)
        self.assertEqual(find_average([1, 2 , 3, 4, 5, 6, 7, -1]), 3.375)
    

    

from src.main.data_structure.list_exercise import even_finder

class Test_List(unittest.TestCase):


    def test_even_finder(self):
        self.assertEqual(even_finder([5,3,2,6,0,1,10,56]),[2,6,0,10,56])
        self.assertEqual(even_finder([3,4,7,9,10]),[4,10])