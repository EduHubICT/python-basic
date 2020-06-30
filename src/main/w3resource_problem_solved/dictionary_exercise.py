from typing import Dict, Any

from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()

from collections import Counter
import operator
import itertools


class Dict:

    # to initiate dictionary
    def __init__(self, init_dict):
        if init_dict is None:
            init_dict = {}
        self.dict = init_dict
    
    
    '''
    sort value in descending order
    '''
    
    
    def sort_dict_descending_order(self):
        descending_order = dict(sorted(self.dict.items(), key = operator.itemgetter(1)))
        return descending_order
    
    
    '''
    Write a Python script to concatenate following dictionaries to create a new one.
    '''
    
    
    def concatenate_dicts(self, dict2):
        new_dict = {}
        for d in (self.dict, dict2):
            new_dict.update(d)
        return new_dict
    
    
    '''
    Generate and print a dictionary that contains a number in the form (x, x*x)
    '''
    
    
    def create_dict_within_range(self, _range):
        _dict = dict()
        for x in range(1, _range + 1):
            _dict [x] = x * x
        return _dict


    '''
    Write a Python program to map two lists into a dictionary.
    '''
    
    
    def two_lists_into_dictionary(self, keys,values):
        _dict = dict(zip(keys, values))
        return _dict
    
    
    '''
    Remove duplicates from Dictionary
    '''
    
    
    def remove_duplicates(self):
        result = dict()
        for key, value in self.dict.items():
            if value not in result.values():
                result[key] = value
        return result
        
    
    '''
    dictionary empty or not
    '''
    
    
    def empty_or_not(self):
        if not bool(self.dict):
            return True
        return False
    
    
    '''
    Write a Python program to combine two dictionary adding values for common keys.
    '''
    
    
    def common_keys_sum(self, dict1):
        new_dict = Counter(self.dict) + Counter(dict1)
        return new_dict
    
    
    '''
    list unique values of dict
    '''
    
    
    def unique_values(self):
        new_list = set([values for _, values in self.dict.items()])
        return new_list
    
    '''Create and display all combinations of letters, selecting each letter from a different key in a dictionary
    (*) for unpacking, it is not for function but just 
    unpack the list or tuple data to other variables dynamically.
    '''
    
    
    def combination_of_values(self):
        list_combo = []
        for combo in itertools.product(*[self.dict[k] for k in sorted(self.dict.keys())]):
            list_combo.append(''.join(combo))
        return list_combo
    
    
    '''Combine values in python list of dictionaries
    https://www.guru99.com/python-counter-collections-example.html#:~:text=in%20the%20container.-,Counter%20is%20a%20sub%2Dclass%20available%20inside%20the%20dictionary%20class,and%20the%20count%20as%20values.'''
    
    
    def combine_values_counter(self, list_of_dict):
        result = Counter()
        for dict1 in list_of_dict:
            result[dict1['item']] += dict1['amount']
        return result
    
    
    '''Create a dictionary from a string
    we can also solve it using Counter concept
    '''
    
    
    def string_to_dictionary(self, str1):
        new_dict = {}
        for letter in str1:
            new_dict[letter] = new_dict.get(letter,0) + 1
        return new_dict
    
    
    '''we get list of list, which is one argument for zip. But to combine we need
       two or more list/tuple etc. Using '*' we unpack list of list to lists.
    Then again unpack to display without unwanted comma,() etc    
    '''
    
    
    def create_table(self):
        my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
        for row in zip(*[[key] + (value) for key, value in sorted(my_dict.items())]):
            print(*row)

    