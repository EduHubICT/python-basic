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
    
    def test_count_values_true(self):
        _dict = Dict({})
        self.assertEqual(_dict.count_values_true([{'id': 1, 'success': True, 'name': 'Lary'},\
                                                  {'id': 2, 'success': False, 'name': 'Rabi'},\
                                                  {'id': 3, 'success': True, 'name': 'Alex'}]),\
                         2)
        
    def test_remove_space(self):
        _dict = Dict({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})
        self.assertEqual(_dict.remove_space(), {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']})
        
    def test_top_three(self):
        _dict = Dict({'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24})
        self.assertEqual(_dict.top_three(), None)
        
    def test_dictionary_indexing(self):
        _dict = Dict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
        self.assertEqual(_dict.dictionary_indexing(), None)
        
    def test_check_key_existing(self):
        _dict = Dict({'name': 'Alex', 'class': 'V', 'roll_id': '2'})
        self.assertEqual(_dict.check_key_existing({'class', 'name'}), True)
        
    def test_number_values_in_dictionary(self):
        _dict = Dict({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']})
        self.assertEqual(_dict.number_values_in_dictionary(), 5)
        
    def test_replace_with_average(self):
        _dict = Dict({})
        
        self.assertEqual(_dict.replace_with_average([{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]), \
                         [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, \
                          {'subject': 'math', 'id': 2, 'V+VI': 73.5}, \
                          {'subject': 'math', 'id': 3, 'V+VI': 80.5}] )

    
    def test_dictionary_in_jason(self):
        _dict = Dict({})
        list_of_dict =  [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
        self.assertEqual(_dict.dictionary_in_jason(), None)
        
        
if __name__ == '__main__':
    unittest.main()
