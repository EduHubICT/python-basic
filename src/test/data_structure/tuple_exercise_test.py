import unittest
from src.main.data_structure.tuple_exercise import *


class TestTuple(unittest.TestCase):
    def test_tuple_indexing(self):
        tup = Tuple((1, 2, 3))
        self.assertEqual(tup.tuple_indexing(1, 3), (2, 3))

    def test_tuple_updating(self):
        tup = Tuple((1, 2, 3))

        self.assertEqual(tup.tuple_updating((4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_remove_tuple_element(self):
        tup = Tuple((1, 2, 3, 4, 5, 6, 7))
        self.assertEqual(tup.remove_tuple_element(3), (1, 2, 3, 5, 6, 7))

    def test_tuple_size(self):
        tup = Tuple(('There', 'is', 'six', 'season', 'in', 'Bangladesh'))
        self.assertEqual(tup.tuple_size(), 6)

    def test_check_tuple_element(self):
        tup = Tuple(('Summer', 'Rainy', 'Autumn', 'Late Autumn', 'Winter', 'Spring'))
        self.assertEqual(tup.check_tuple_element('Harvest'), False)
        self.assertEqual(tup.check_tuple_element('Rainy'), True)

    def test_tuple_repetition(self):
        tup = Tuple(('a', 'b', 'c'))
        self.assertEqual(tup.tuple_element_repetition(2), ('a', 'b', 'c', 'a', 'b', 'c'))


if __name__ == '__main__':
    unittest.main()
