import unittest
from src.main.data_structure.dictionary_exercise import *


class DictTest(unittest.TestCase):

    def test_add_element(self):
        _dict = Dict({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(_dict.add_element('d', 4), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_get_element_by_key(self):
        _dict = Dict({('a', 'b'): 12})
        self.assertEqual(_dict.get_element_by_key(('a', 'b')), 12)

    def test_delete_element_by_key(self):
        _dict = Dict({'a': 0, 'b': 1})
        self.assertEqual(_dict.delete_element_by_key('a'), {'b': 1})

    def test_clear(self):
        _dict = Dict({'a': 'b', 'b': 'c', 'c': 'a'})
        self.assertEqual(Dict({1: 'Google', 2: 'Facebook', 3: 'Twitter'}).clear(), _dict.clear())

    def test_keys(self):
        _dict = Dict({'Key1': 1, 'Key2': 2})
        self.assertEqual(list(_dict.keys()), list(['Key1', 'Key2']))

    def test_values(self):
        _dict = Dict({'Key1': 1, 'Key2': 2})
        self.assertEqual(list(_dict.values()), list([1, 2]))

    def test_mapping_list_into_dictionary(self):
        _dict = Dict({})
        key_list = ['red', 'green', 'blue']
        value_list = ['#FF0000', '#008000', '#0000FF']
        self.assertEqual(_dict.mapping_list_into_dictionary(key_list, value_list), {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'})

    def test_find_max_value(self):
        _dict = Dict({"a": 1, "b": 22, "c": 3})
        self.assertEqual(_dict.find_max_value(), 22)

    def test_find_min_value(self):
        _dict = Dict({"a": 1, "b": 22, "c": 30, "d": 2})
        self.assertEqual(_dict.find_min_value(), 1)

    def test_sort_dict_by_key(self):
        _dict = Dict({"b": 2, "f": 30, "d": 34, "c": 3, "a": 1})
        self.assertEqual(_dict.sort_dict_by_key(), {"a": 1, "b": 2, "c": 3, "d": 34, "f": 30})

    def test_tutorial_marks_average(self):
        _dict = Dict({})
        self.assertEqual(_dict.tutorial_marks_average(), [
            {'id': 101, 'subject': 'C', 'First + Second': 22.5}, {'id': 102, 'subject': 'Python', 'First + Second': 23.5}, {'id': 103, 'subject': 'Java', 'First + Second': 20.5}])
        
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
        
if __name__ == '__main__':
    unittest.main()
