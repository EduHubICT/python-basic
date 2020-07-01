"""
Linked List:    i) Singly linked list
               ii) Doubly linked list
              iii) i & ii both can be circular
"""

from src.main.logger.py_logger import PyLogger
logger = PyLogger.get_configured_logger()


class Node:
    def __init__(self, data=None):
        self.data = data  # to store value
        self.next = None  # pointer to define next node
        self.prev = None  # pointer to define previous node


"""
Singly list can only move into forward direction
"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traversing(self):
        current = self.head
        traversing_path = list([])
        while current:
            traversing_path.append(current.data)
            current = current.next

        logger.info("{}".format(traversing_path))
        return traversing_path

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_ending(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.insert_at_beginning(new_data)
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    @staticmethod
    def insert_at_middle(given_node, new_data):
        if given_node is None:
            raise Exception("Node must be needed.")
        new_node = Node(new_data)
        new_node.next = given_node.next
        given_node.next = new_node

    def remove_node(self, node_key):
        current_node = self.head
        previous_node = None

        if current_node is not None and current_node.data == node_key:
            self.head = current_node.next
            current_node = None

        while current_node is not None:
            if current_node.data == node_key:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next


'''
Doubly linked list can move both direction
'''


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
        else:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None

    def traversing(self):
        current = self.head
        get_iterations = []
        while current:
            get_iterations.append(current.data)
            logger.info("{}".format(current.data))
            current = current.next
        return get_iterations

