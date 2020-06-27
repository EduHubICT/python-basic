from src.main.logger.py_logger import PyLogger


logger = PyLogger.get_configured_logger()


def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number

    logger.info('Average: {}'.format(summation / len(list_of_number)))

    return summation / len(list_of_number)


def list_sort(list_of_number):
    sorted_list = sorted(list_of_number)
    logger.info("Sorted list : {}".format(sorted_list))

    return sorted_list


def find_max(list_of_number):
    max_val = -1000000
    for number in list_of_number:
        if number > max_val:
            max_val = number
    return max_val


def find_min(list_of_number):
    min_val = 1000000
    for number in list_of_number:
        if number < min_val:
            min_val = number
    return min_val


def find_sum(list_of_number) -> int:
    summation = 0
    for number in list_of_number:
        summation = summation + number
    return summation


def sort_list_bubble_asc(list_of_number):
    list_length = len(list_of_number)
    for index in range(0, list_length - 1):
        for ind in range(0, list_length - index - 1):
            if list_of_number[ind] > list_of_number[ind + 1]:
                temp = list_of_number[ind]
                list_of_number[ind] = list_of_number[ind + 1]
                list_of_number[ind + 1] = temp

    return list_of_number


def sort_list_bubble_dsc(list_of_number):
    list_length = len(list_of_number)
    for index in range(0, list_length - 1):
        for ind in range(0, list_length - index - 1):
            if list_of_number[ind] < list_of_number[ind + 1]:
                temp = list_of_number[ind]
                list_of_number[ind] = list_of_number[ind + 1]
                list_of_number[ind + 1] = temp

    return list_of_number


def binary_search(list_of_number, value):
    list_length = len(list_of_number)
    left = 0
    right = list_length - 1

    while left <= right:
        middle = (left+right) // 2
        if value == list_of_number[middle]:
            return "Yes"
        elif value < list_of_number[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return "No"


def binary_search_recursive(list_of_numbers, target, start, end):
    if start > end:
        return 'NO'
    mid = start + (end - start) // 2
    
    if list_of_numbers[mid] == target:
        return 'Yes'
    elif list_of_numbers[mid] > target:
        return binary_search_recursive(list_of_numbers, target, start, mid - 1)
    elif list_of_numbers[mid] < target:
        return binary_search_recursive(list_of_numbers, target, mid + 1, end)
    
    
def binary_search_target_index(list_of_number, value, first_index):

    start = 0
    end = len(list_of_number) - 1
    target_index = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if list_of_number[mid] == value:
            target_index = mid
            # looking for target_value and its first_index or last_index in the
            # sorted list .[0,1,2,2,2,3,4,5] our target value = 2 and we
            # looking for the first indexed 2 or last indexed 2 in the list
            if first_index:
                end = mid - 1 
            else:
                start = mid + 1
        elif list_of_number[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    return target_index
  

def binary_search_count(list_of_number, value):
    
    first_index = binary_search_target_index(list_of_number, value, True)
    
    if first_index != -1:
        last_index = binary_search_target_index(list_of_number, value, False)
        count = last_index - first_index + 1
        
    return count


# CircularRotatedSorted arrary Example : [12,13,14,1,2,3,4] 
# or [2,3,4,12,13,14,1]
def binary_search_circular_sorted(list_of_numbers, value):
    start = 0
    end = len(list_of_numbers) - 1
    
    while start <= end:
        mid = start + (end-start) // 2 
        
        if list_of_numbers[mid] == value:
            return 'Yes'
        
        elif list_of_numbers[mid] <= list_of_numbers[end]:
            if list_of_numbers[mid] < value <= list_of_numbers[end]:
                start = mid + 1
            else:
                end = mid - 1
        
        elif list_of_numbers[start] <= list_of_numbers[mid]:
            if list_of_numbers[start] <= value < list_of_numbers[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1        


def find_square(list_of_numbers):
    list_of_numbers_square = []
    for number in list_of_numbers:
        number = number * number
        list_of_numbers_square.append(number)
    return list_of_numbers_square


def find_prime_number(list_of_numbers):
    is_prime_list = []
    for num in list_of_numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    is_prime_list.append(False)
                    break
            else:
                is_prime_list.append(True)

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            is_prime_list.append(False)

    return is_prime_list

  
def insertion_sort_asc(list_of_number):
    for item in range(1, len(list_of_number)):
        ind = item - 1
        adjacent_item = list_of_number[item]
        while ind >= 0 and list_of_number[ind] > adjacent_item:
            list_of_number[ind + 1] = list_of_number[ind]
            ind = ind - 1
        list_of_number[ind+1] = adjacent_item
    return list_of_number


def insertion_sort_dsc(list_of_number):
    for item in range(1, len(list_of_number)):
        ind = item - 1
        adjacent_item = list_of_number[item]
        while ind >= 0 and list_of_number[ind] < adjacent_item:
            list_of_number[ind + 1] = list_of_number[ind]
            ind = ind - 1
        list_of_number[ind + 1] = adjacent_item
    return list_of_number


# find specified type of item from a list of different type of items

def specified_type_item(list_different_type, data_type):
    count = 0
    for item in list_different_type:
        if type(item) == data_type:
            count += 1
    logger.info('Total count of {} type item : {}'.format(data_type, count))
    return count


def remove_duplicates(list_of_duplicates):
    return list(set(list_of_duplicates))


# Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty tuples. 
def sort_increasing_order(list_of_tuple):
    return sorted(list_of_tuple,key = lambda x : x[1])


#Write a Python program to generate a 3*4*6 3D array whose each element is *
def three_dimensional_array(first,second,third):
    array_3d = [[[1 for item in range(third)] for item in range(second)] for item in range(first)]
    return array_3d


# Shuffle and print a specified list
from random import *
def shuffled_list(list_of_numbers):
    random.seed(0)
    shuffle(list_of_numbers)
    return list_of_numbers


# Write a Python program to convert a list of characters into a string.
def  list_to_string(list_of_characters):
    after_join = ''.join(list_of_characters)
    return after_join


# Find the index of an item in a specified list
def index_of_item(list_of_numbers, number):
    return list_of_numbers.index(number)


# Write a Python program to flatten a shallow list. 
import itertools
def flatten_list(list_2d):
    return list(itertools.chain(*list_2d))


# Select an item randomly from a list
import random
random.seed(0)
def random_choice(list_of_number):
    return random.choice(list_of_number)


#  Check whether two lists are circularly identical
def lists_circularly_identical(list_1, list_2):
    return (' '.join(map(str,list_1)) in ' '.join(map(str,list_2 * 2)))


# Find the second smallest number in a list
def second_smallest(list_of_numbers):
    if len(list_of_numbers)<2:
        return
    elif (len(list_of_numbers) == 2 and list_of_numbers[0] == list_of_numbers[1]):
        return
    else:
        unique_list = list(set(list_of_numbers))
        unique_list.sort()
        return unique_list[1]
    
    
# Find the second largest number in a list
def second_largest(list_of_numbers):
    if len(list_of_numbers)<2:
        return
    elif (len(list_of_numbers) == 2 and list_of_numbers[0] == list_of_numbers[1]):
        return
    else:
        unique_list = list(set(list_of_numbers))
        unique_list.sort()
        return unique_list[-2]
    
    
# Count the number of elements in a list within a specified range
def count_num_within_range(list_of_items, min, max):
    list_of_items.sort()
    for index, item in enumerate(list_of_items):
        if item >= min:
            return len(list_of_items) - index
    return


# Check whether a list contains a sublist
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


# Write a Python program to generate all sublists of a list.
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


# Create a list by concatenating a given list which range goes from 1 to n
def concatenate_list_ranges(list_of_items, _range):
    new_list = ['{}{}'.format(x,y) for y in range(1, _range+1) for x in list_of_items]
    return new_list

random.seed(0)
def get_variable_unique_id(value):
    unique_id = format(id(value), 'x')
    logger.info('variable unique id: {}'.format(unique_id))

