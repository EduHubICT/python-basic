import unittest
from src.main.data_structure.set_exercise import *


class SetTest(unittest.TestCase):
    def test_unique_value(self):
        self.assertEqual(
            create_unique_value_set([1, 1, 2, 4, 3, 5, 3]), {1, 2, 3, 4, 5}
        )

    def test_access_value_in_set(self):
        self.assertEqual(access_value_in_set({1, 3, 5, 6, 8, 9}, 3), "yes")

    def test_add_remove_in_set(self):
        self.assertEqual(add_remove_in_set({1, 3, 5, 6, 8, 9}, 2, None), "Add")
        self.assertEqual(add_remove_in_set({1, 3, 5, 6, 8, 9}, None, 9), "Remove")

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

    def test_find_maximum_value(self):
        self.assertEqual(find_maximum_value({11, 33, 25, 62, 18, 90}), 90)
        self.assertEqual(find_maximum_value({15, 39, 125, 32, 74, 83}), 125)

    def test_find_minimum_value(self):
        self.assertEqual(find_minimum_value({121, 133, 65, 32, 98, 190}), 32)
        self.assertEqual(find_minimum_value({150, 19, 225, 22, 94, 43}), 19)


if __name__ == "__main__":
    unittest.main()
