from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()

''' 
w3resources.com problem solved
'''

'''
Write a Python program to get a list, sorted in increasing order
by the last element in each tuple from a given list of non-empty tuples.
'''


def sort_increasing_order(list_of_tuple):
    return sorted(list_of_tuple,key = lambda x : x[1])


'''
Write a Python program to generate a 3*4*6 3D array whose each element is *
'''


def three_dimensional_array(first,second,third):
    array_3d = [[[1 for item in range(third)] for item in range(second)] for item in range(first)]
    return array_3d


'''
Shuffle and print a specified list
'''


from random import *
def shuffled_list(list_of_numbers):
    random.seed(0)
    shuffle(list_of_numbers)
    return list_of_numbers


'''
Write a Python program to convert a list of characters into a string.
'''


def  list_to_string(list_of_characters):
    after_join = ''.join(list_of_characters)
    return after_join


'''
Find the index of an item in a specified list
'''


def index_of_item(list_of_numbers, number):
    return list_of_numbers.index(number)


'''
Write a Python program to flatten a shallow list. 
'''

import itertools
def flatten_list(list_2d):
    return list(itertools.chain(*list_2d))


'''
Select an item randomly from a list
'''


import random
random.seed(0)
def random_choice(list_of_number):
    return random.choice(list_of_number)


'''
Check whether two lists are circularly identical
'''


def lists_circularly_identical(list_1, list_2):
    return (' '.join(map(str,list_1)) in ' '.join(map(str,list_2 * 2)))


'''
Find the second smallest number in a list
'''


def second_smallest(list_of_numbers):
    if len(list_of_numbers)<2:
        return
    elif (len(list_of_numbers) == 2 and list_of_numbers[0] == list_of_numbers[1]):
        return
    else:
        unique_list = list(set(list_of_numbers))
        unique_list.sort()
        return unique_list[1]
    
    
'''
Find the second largest number in a list
'''


def second_largest(list_of_numbers):
    if len(list_of_numbers)<2:
        return
    elif (len(list_of_numbers) == 2 and list_of_numbers[0] == list_of_numbers[1]):
        return
    else:
        unique_list = list(set(list_of_numbers))
        unique_list.sort()
        return unique_list[-2]
    
    
'''
Count the number of elements in a list within a specified range
'''


def count_num_within_range(list_of_items, min, max):
    list_of_items.sort()
    for index, item in enumerate(list_of_items):
        if item >= min:
            return len(list_of_items) - index
    return


'''
Check whether a list contains a sublist
'''


def check_sublist(list_1, sub_list):
    if sub_list == []:
        return True
    elif sub_list == list_1:
        return True
    elif len(sub_list) > len(list_1):
        return False
    else:
        for index, item in enumerate(list_1):
            if item == sub_list[0]:
                if len(sub_list) <2:
                    return True
                elif (sub_list[1: len(sub_list)] == list_1[index+1 : index+len(sub_list)]):
                      return True
                else:
                      return False


'''
Write a Python program to generate all sublists of a list.
'''


from itertools import combinations
def create_all_sublist(list_of_items):
    sub_lists = []
    for item in range (len(list_of_items) + 1):
        temp = [list(sub) for sub in combinations(list_of_items, item)]
        sub_lists.extend(temp)
    return sub_lists


# 
def prime_eratosthenes(n):
    prime_list = []
    not_prime = []
    for i in range(2, n + 1):
        if i not in not_prime:
            prime_list.append(i)
            for j in range(i * i, n + 1, i):
                not_prime.append(j)
    return prime_list


'''
Create a list by concatenating a given list which range goes from 1 to n
'''


def concatenate_list_ranges(list_of_items, _range):
    new_list = ['{}{}'.format(x,y) for y in range(1, _range+1) for x in list_of_items]
    return new_list


random.seed(0)
def get_variable_unique_id(value):
    unique_id = format(id(value), 'x')
    logger.info('variable unique id: {}'.format(unique_id))
    
    
'''
Nested Loops in List Comprehension
'''


def list_comprehension(number):
    n = number
    value = [(x, y, z) for x in range(1, n) for y in range(x + 1, n) for z in range(y + 1, n) if x * y * z % 2 == 1]
    return value
