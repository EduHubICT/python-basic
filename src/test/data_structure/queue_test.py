import unittest
from src.main.data_structure.queue import *


class TestQueue(unittest.TestCase):

    def test_all(self):
        q = Queue([1, 4, 2, 9])

        self.assertFalse(q.empty())  # to check that q is initiated

        # test front
        self.assertEqual(q.front(), 1)

        # test pop
        q.pop()
        self.assertEqual(q.size(), 3)

        # test push
        q.push(5)
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.front(), 4)


if __name__ == '__main__':
    unittest.main()
