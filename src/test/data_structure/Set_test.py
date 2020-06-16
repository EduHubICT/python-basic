import unittest

from src.main.data_structure.set import *

class SetTest(unittest.TestCase):
    
    def convert_list_into_set(self):
        self.assertEqual(set_unique_value_from_list([1,1,2,4,3,5,3]),{1,2,3,4,5})
    
    def convert_list_into_set1(self):
        self.assertEqual(set_unique_value_from_list1([1,1,2,4,3,5,3]),{1,2,3,4,5})

if __name__ == '__main__':
    unittest.main()