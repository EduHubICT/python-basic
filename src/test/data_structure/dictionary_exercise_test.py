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
        _string = str("dict_keys(['Key1', 'Key2'])")

        self.assertEqual(str(_dict.keys()), _string)

    def test_items(self):
        _dict = Dict({'a': 'apple', 'b': 'banana'})
        string = "dict_items([('a', 'apple'), ('b', 'banana')])"
        self.assertEqual(str(_dict.items()), string)


if __name__ == '__main__':
    unittest.main()
