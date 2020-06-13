import unittest

from src.main.data_structure.stack import *


class TestStack(unittest.TestCase):

    def test_all(self):
        stack = Stack([1, 5, 2, 10])  # stack object created

        # test top
        self.assertEqual(stack.top(), 10)

        # test pop
        stack.pop()
        self.assertEqual(stack.size(), 3)

        # test push
        stack.push(9)
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.top(), 9)


if __name__ == '__main__':
    unittest.main()
