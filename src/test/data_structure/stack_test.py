import unittest

from src.main.data_structure.stack import *


class TestStack(unittest.TestCase):

    def test_top(self):
        stack = Stack([1, 5, 4, 8, 10])
        self.assertEqual(stack.top(), 10)

    def test_pop(self):
        stack = Stack([1, 3, 2, 9])
        stack.pop()
        self.assertEqual(stack.size(), 3)

    def test_push(self):
        stack = Stack()
        stack.push(9)
        stack.push(5)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.top(), 5)

    def test_size(self):
        stack = Stack([1, 0, 2, 2, 4, 4])
        self.assertEqual(stack.size(), 6)

    def test_empty(self):
        stack = Stack([5])
        self.assertEqual(stack.empty(), False)
        stack.pop()
        self.assertEqual(stack.empty(), True)

    def test_display(self):
        stack = Stack([1, 9, 2])
        self.assertEqual(stack.display(), [1, 9, 2])


if __name__ == '__main__':
    unittest.main()
