"""
w3Resource link: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-linked-list.php
"""
# called the singly linked list we already implemented in data_structure
from src.main.data_structure.linked_list_exercise import *

"""
1. Write a Python program to create a singly linked list, append some items and iterate through the list.
"""


def get_solution_1():
    sl_list = SinglyLinkedList()
    sl_list.insert_at_beginning(5)
    sl_list.insert_at_beginning(4)
    sl_list.insert_at_beginning(6)
    sl_list.insert_at_beginning(10)
    sl_list.insert_at_beginning(7)
    logger.info(sl_list.traversing())
