import unittest
from src.main.data_structure.set_exercise import *


class SetTest(unittest.TestCase):
    def test_find_union(self):
        set_a = {"a", "b", "c"}
        set_b = {"c", "d"}
        self.assertEqual(find_union(set_a, set_b), set_a.union(set_b))

    def test_find_intersection(self):
        set_a = {"a", "b", "c"}
        set_b = {"c", "d", "e"}
        self.assertEqual(find_intersection(set_a, set_b), set_a.intersection(set_b))

    def test_find_differences(self):
        set_a = {"a", "b", "c"}
        set_b = {"c", "d"}
        self.assertEqual(find_differences(set_a, set_b), set_a.difference(set_b))

    def test_disjoint(self):
        self.assertTrue(find_disjoint({"a", "b"}, {"c", "d"}))
        self.assertFalse(find_disjoint({"a", "b", "c"}, {"c", "d"}))

    def test_subsets(self):
        self.assertTrue(find_subsets({"a", "c", "b"}, {"b", "e", "f", "c", "a"}))
        self.assertFalse(find_subsets({"a", "d", "c"}, {"a", "b", "c", "e"}))

    def test_supersets(self):
        self.assertTrue(find_supersets({"b", "e", "f", "c", "a"}, {"a", "c", "b"}))
        self.assertFalse(find_supersets({"a", "b", "c", "e"}, {"a", "d", "c"}))


if __name__ == '__main__':
    unittest.main()
