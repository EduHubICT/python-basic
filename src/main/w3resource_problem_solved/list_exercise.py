import itertools
from itertools import combinations
from random import *

from src.main.logger.py_logger import PyLogger

import random
from random import *
import itertools
from itertools import zip_longest, chain, tee, groupby, combinations
from operator import itemgetter
import ast


logger = PyLogger.get_configured_logger()

""" 
w3resources.com problem solved
"""

"""
Write a Python program to get a list, sorted in increasing order
by the last element in each tuple from a given list of non-empty tuples.
"""


def sort_increasing_order(list_of_tuple):
    return sorted(list_of_tuple, key=lambda x: x[1])


"""
Write a Python program to generate a 3*4*6 3D array whose each element is *
"""


def three_dimensional_array(first, second, third):
    array_3d = [
        [[1 for item in range(third)] for item in range(second)]
        for item in range(first)
    ]
    return array_3d


"""
Shuffle and print a specified list
"""


def shuffled_list(list_of_numbers):
    random.seed(0)
    shuffle(list_of_numbers)
    return list_of_numbers


"""
Write a Python program to convert a list of characters into a string.
"""


def list_to_string(list_of_characters):
    after_join = "".join(list_of_characters)
    return after_join


"""
Find the index of an item in a specified list
"""


def index_of_item(list_of_numbers, number):
    return list_of_numbers.index(number)


"""
Write a Python program to flatten a shallow list. 
"""


def flatten_list(list_2d):
    return list(itertools.chain(*list_2d))


"""
Select an item randomly from a list
"""

import random

random.seed(0)


def random_choice(list_of_number):
    return random.choice(list_of_number)


"""
Check whether two lists are circularly identical
"""


def lists_circularly_identical(list_1, list_2):
    return " ".join(map(str, list_1)) in " ".join(map(str, list_2 * 2))


"""
Find the second smallest number in a list
"""


def second_smallest(list_of_numbers):
    if len(list_of_numbers) < 2:
        return
    elif len(list_of_numbers) == 2 and list_of_numbers[0] == list_of_numbers[1]:
        return
    else:
        unique_list = list(set(list_of_numbers))
        unique_list.sort()
        return unique_list[1]


"""
Find the second largest number in a list
"""


def second_largest(list_of_numbers):
    if len(list_of_numbers) < 2:
        return
    elif len(list_of_numbers) == 2 and list_of_numbers[0] == list_of_numbers[1]:
        return
    else:
        unique_list = list(set(list_of_numbers))
        unique_list.sort()
        return unique_list[-2]


"""
Count the number of elements in a list within a specified range
"""


def count_num_within_range(list_of_items, min, max):
    list_of_items.sort()
    for index, item in enumerate(list_of_items):
        if item >= min:
            return len(list_of_items) - index
    return


"""
Check whether a list contains a sublist
"""


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
                if len(sub_list) < 2:
                    return True
                elif (
                    sub_list[1 : len(sub_list)]
                    == list_1[index + 1 : index + len(sub_list)]
                ):
                    return True
                else:
                    return False


"""
Write a Python program to generate all sublists of a list.
"""


def create_all_sublist(list_of_items):
    sub_lists = []
    for item in range(len(list_of_items) + 1):
        temp = [list(sub) for sub in combinations(list_of_items, item)]
        sub_lists.extend(temp)
    return sub_lists


"""

34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.

"""


def prime_eratosthenes(n):
    prime_list = []
    not_prime = []
    for i in range(2, n + 1):
        if i not in not_prime:
            prime_list.append(i)
            for j in range(i * i, n + 1, i):
                not_prime.append(j)
    return prime_list


"""
Create a list by concatenating a given list which range goes from 1 to n
"""


def concatenate_list_ranges(list_of_items, _range):
    new_list = [
        "{}{}".format(x, y) for y in range(1, _range + 1) for x in list_of_items
    ]
    return new_list


"""

36

"""


random.seed(0)


def get_variable_unique_id(value):
    unique_id = format(id(value), "x")
    logger.info("variable unique id: {}".format(unique_id))


"""
Nested Loops in List Comprehension
"""


def list_comprehension(number):
    n = number
    value = [
        (x, y, z)
        for x in range(1, n)
        for y in range(x + 1, n)
        for z in range(y + 1, n)
        if x * y * z % 2 == 1
    ]
    return value


"""

38.Change the position of every n-th value with the (n+1)th in a list

"""


def change_position(list_of_items):
    return list(
        chain.from_iterable(zip_longest(list_of_items[1::2], list_of_items[::2]))
    )


"""

40. Split a list based on first character of word
 
"""


def arrange_character_wise(list_of_words):
    for letter, words in groupby(sorted(list_of_words), key=itemgetter(0)):
        logger.info("Key: {}".format(letter))
        for word in words:
            logger.info(word)


"""

45.  Convert a pair of values into a sorted unique array

"""


def sorted_unique_array(list_of_set):
    return sorted(set().union(*list_of_set))


"""

47.Insert an element before each element of a list

"""


def insert_element_before(list_of_ele):
    return [item for ele in list_of_ele for item in ("k", ele)]


"""

48. Print a nested lists using the print() function

"""


def nested_lists(list_of_list):
    logger.info("\n".join([str(nested_list) for nested_list in list_of_list]))


"""

50.  Sort a list of nested dictionaries

"""


def sort_nested_dictionary(list_nested_dictionary):
    list_nested_dictionary.sort(key=lambda e: e["key"]["subkey"], reverse=True)
    return list_nested_dictionary


"""

51. Split a list every Nth element

"""


def split_list_nth_element(list_of_items, n):
    return [list_of_items[i::n] for i in range(n)]


"""

54. Write a Python program to concatenate elements of a list.

"""


def concatenate_elements(list_of_string):
    logger.info("-".join(list_of_string))
    logger.info("".join(list_of_string))
    # print(''.join(list_of_string))


"""

55. Write a Python program to remove key values pairs from a list of dictionaries. 

"""


def remove_specific_key(list_of_dictionaries):
    return [{k: v for k, v in d.items() if k != "key1"} for d in list_of_dictionaries]


"""

56.Write a Python program to convert a string to a list. 

"""


def string_to_list(string):
    output_list = ast.literal_eval(string)
    return output_list


"""

58. Write a Python program to replace the last element in a list with another list. 

"""


def replace_last_item(num_1, num_2):
    # um_1[-1] = num_2 ,then output will be like [1, 3, 5, 7, 9, [2, 4, 6, 8]]
    num_1[-1:] = num_2
    return num_1


"""

60.Python program to find a tuple, the smallest second index value from a list of tuples.

"""


def tuple_with_smallest_second_value(list_of_tuple):
    return min(list_of_tuple, key=lambda a: a[1])


"""

65.Access dictionary key’s element by index

"""


def access_by_index(dictionary):
    logger.info(list(dictionary)[0])  # First key
    logger.info(list(dictionary)[1])  # Second key
    logger.info(list(dictionary))  # fAll element


"""

66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.

"""


def find_list_highest_sum(list_of_list):
    return max(list_of_list, key=sum)


"""

67.Find all the values in a list are greater than a specified number

"""


def all_greater_num(list_of_num):
    return all(num >= 200 for num in list_of_num)


"""

68.Extend a list without append

"""


def extend_list(list_1, list_2):
    list_1[:0] = list_2
    return list_1


"""

69. Write a Python program to remove duplicates from a list of lists.

"""


def list_of_lists_remove_duplicate(list_of_lists):
    list_of_lists.sort()
    return list(item for item, _ in itertools.groupby(list_of_lists))


"""

73. Remove consecutive duplicates of a given list

"""


def compress(l_nums):
    return [key for key, group in itertools.groupby(l_nums)]


"""

74. Pack consecutive duplicates of a given list elements into sublists

"""


def pack_consecutive_duplicates(list_of_num):
    return [list(group) for key, group in itertools.groupby(list_of_num)]


"""

75.Create a list reflecting the run-length encoding from a list

"""


def encode_list(s_list):
    return [[len(list(group)), key] for key, group in groupby(s_list)]


"""

77. Decode a run-length encoded given list

"""


def decode(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]

    return [x for g in alist for x, R in aux(g) for i in R]


"""

79. Remove the K'th element from a given list, print the new list

"""


def remove_kth_element(n_list, L):
    return n_list[: L - 1] + n_list[L:]


"""

80.Write a Python program to insert an element at a specified position into a given list.

"""


def insert_spec_position(x, n_list, pos):
    return n_list[: pos - 1] + [x] + n_list[pos - 1 :]


"""

81.Extract a given number of randomly selected elements from a given list

"""


def random_select_nums(n_list, n):
    new_list = random.sample(n_list, n)
    logger.info(new_list)
