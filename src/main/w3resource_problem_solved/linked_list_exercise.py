"""
w3Resource link: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list.php
"""
from src.main.logger.py_logger import *
# called the singly linked list we already implemented in data_structure
from src.main.data_structure.linked_list_exercise import *

'''
1. Write a Python program to create a singly linked list, append some items and iterate through the list.
'''


def get_solution_1():
    sl_list = SinglyLinkedList()
    sl_list.insert_at_beginning(5)
    sl_list.insert_at_beginning(4)
    sl_list.insert_at_beginning(6)
    sl_list.insert_at_beginning(10)
    sl_list.insert_at_beginning(7)
    sl_list.traversing()


'''
2. Write a python program to get the size of a singly linked list
'''


def get_size(sl_list):
    logger.info(len(sl_list))
    return len(sl_list)
