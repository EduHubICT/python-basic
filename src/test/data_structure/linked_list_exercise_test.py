import unittest
from src.main.data_structure.linked_list_exercise import *


class SinglyLinkedListTest(unittest.TestCase):
    def test_traversing(self):
        l_list = SinglyLinkedList()
        l_list.head = Node(1)
        l_list.head.next = Node(3)
        l_list.head.next.next = Node(2)
        self.assertEqual(l_list.traversing(), [1, 3, 2])

    def test_insertion_at_beginning(self):
        l_list = SinglyLinkedList()
        l_list.head = Node(0)
        l_list.insert_at_beginning(1)
        self.assertEqual(l_list.traversing(), [1, 0])

    def test_insertion_at_middle(self):
        l_list = SinglyLinkedList()
        l_list.head = Node("Me")
        l_list.insert_at_beginning("Father")
        l_list.insert_at_beginning("GrandGrandFather")
        l_list.insert_at_middle(l_list.head, "GrandFather")
        self.assertEqual(
            l_list.traversing(), ["GrandGrandFather", "GrandFather", "Father", "Me"]
        )

    def test_insertion_at_end(self):
        l_list = SinglyLinkedList()
        l_list.head = Node(1)
        l_list.head.next = Node(2)
        l_list.head.next.next = Node(3)
        l_list.insert_at_ending(4)
        self.assertEqual(l_list.traversing(), [1, 2, 3, 4])

    def test_remove_node(self):
        l_list = SinglyLinkedList()
        l_list.head = Node(4)
        l_list.head.next = Node(2)
        l_list.head.next.next = Node(3)
        l_list.head.next.next.next = Node(1)
        l_list.remove_node(3)
        self.assertEqual(l_list.traversing(), [4, 2, 1])


if __name__ == "__main__":
    unittest.main()
