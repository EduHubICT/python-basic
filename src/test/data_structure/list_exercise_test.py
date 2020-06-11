import unittest

from src.main.data_structure.list_exercise import find_average


class TestList(unittest.TestCase):

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3]), 2)
        self.assertEqual(find_average([1, 2 , 3, 4, 5, 6, 7, -1]), 3.375)