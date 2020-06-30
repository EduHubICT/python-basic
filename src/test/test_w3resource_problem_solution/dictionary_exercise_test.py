import unittest
from src.main.w3resource_problem_solved.dictionary_exercise import *


class DictTest(unittest.TestCase):
        
    def test_sort_dict_descending_order(self):
        _dict = Dict({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
        self.assertEqual(_dict.sort_dict_descending_order(), {3: 4, 4: 3, 1: 2, 2: 1, 0: 0})
        
    def test_concatenate_dicts(self):
        _dict = Dict ({1:10, 2:20})
        self.assertEqual(_dict.concatenate_dicts({3:30, 4:40}), {1: 10, 2: 20, 3: 30, 4: 40})

    def test_create_dict_within_range(self):
        _dict = Dict({})
        self.assertEqual(_dict.create_dict_within_range(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
        
    def test_two_lists_into_dictionary(self):
        _dict = Dict({})
        self.assertEqual(_dict.two_lists_into_dictionary(['red', 'green', 'blue'],[1, 2, 3]), {'green': 2, 'blue': 3, 'red': 1})
        
    def test_remove_duplicates(self):
        _dict = Dict({'id1': 1, 'id2' : 1, 'id3' : 2})
        self.assertEqual(_dict.remove_duplicates(), {'id1': 1, 'id3' : 2})
        
    def test_empty_or_not(self):
        _dict = Dict({})
        self.assertEqual(_dict.empty_or_not(), True)
        _dict1 = Dict({1: 2})
        self.assertEqual(_dict1.empty_or_not(), False)
        
    def test_common_keys_sum(self):
        _dict = Dict({'a': 100, 'b': 200, 'c':300})
        self.assertEqual(_dict.common_keys_sum({'a': 300, 'b': 200, 'd':400}), \
                         Counter({'b': 400, 'd': 400, 'a': 400, 'c': 300}))
        
    def test_unique_values(self):
        _dict = Dict({'x': 10, 'y': 10, 'z': 30})
        self.assertEqual(_dict.unique_values(), {10, 30})
        
    def test_combination_of_values(self):
        _dict = Dict({'1':['a','b'], '2':['c','d'], '3' : ['e','f']})
        self.assertEqual(_dict.combination_of_values(), \
                         ['ace', 'acf', 'ade', 'adf', 'bce', 'bcf', 'bde', 'bdf'])
       
    def test_combine_values_counter(self):
        _dict = Dict({})
        self.assertEqual(_dict.combine_values_counter([{'item': 'item1', 'amount': 400},\
                                                       {'item': 'item2', 'amount': 300},\
                                                       {'item': 'item1', 'amount': 750}]),\
                         Counter({'item1': 1150, 'item2': 300}))
        
    def test_string_to_dictionary(self):
        _dict = Dict({})
        self.assertEqual(_dict.string_to_dictionary('w3resource'), \
                         {'o': 1, '3': 1, 's': 1, 'r': 2, 'w': 1, 'u': 1, 'e': 2, 'c': 1})
     
    def test_create_table(self):
        _dict = Dict({})
        self.assertEqual(_dict.create_table(), None)
        
        
if __name__ == '__main__':
    unittest.main()
