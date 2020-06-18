import unittest

from src.main.data_structure.set_exercise import *
#from src.main.data_structure.list_exercise import *

class TestSet(unittest.TestCase):
    def test_unique_value(self):
        self.assertEqual(create_unique_value([ 1, 1, 2, 4, 3, 5, 3]), { 1, 2, 3, 4, 5})
        #self.assertEqual(find_average([1, 2, 3, 4, 5, 6, 7, -1]), 3.375)
        # self.assertEqual(find_average([1, 2, 3]), 2)

if __name__ == '__main__':
    unittest.main()