import unittest

from src.main.w3resource_problem_solved.tuple_exercise import *


class TestTuple(unittest.TestCase):
    def test_repeated_item(self):
        self.assertEqual(repeated_item((2, 4, 5, 6, 2, 3, 4, 4, 7), 4), None)

    def test_element_existance(self):
        self.assertEqual(
            element_existance(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), "r"),
            True,
        )

    def test_tuple_to_dictionary(self):
        self.assertEqual(tuple_to_dictionary(((2, "w"), (3, "r"))), {"r": 3, "w": 2})

    def test_individual_lists(self):
        self.assertEqual(
            individual_lists([(1, 2), (3, 4), (8, 9)]), [(1, 3, 8), (2, 4, 9)]
        )

    def test_reverse_tuple(self):
        self.assertEqual(reverse_tuple((5, 10, 15, 20)), (20, 15, 10, 5))

    def test_convert_list_to_tuple(self):
        self.assertEqual(
            convert_list_to_tuple(
                [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
            ),
            {"y": [1, 2], "z": [1], "x": [1, 2, 3]},
        )

    def test_remove_empty_tuple(self):
        self.assertEqual(
            remove_empty_tuple([(), (), ("",), ("a", "b"), ("a", "b", "c"), ("d")]),
            [("",), ("a", "b"), ("a", "b", "c"), "d"],
        )

    def test_sort_tuple(self):
        self.assertEqual(
            sort_tuple([("item1", "12.20"), ("item2", "15.10"), ("item3", "24.5")]),
            [("item3", "24.5"), ("item2", "15.10"), ("item1", "12.20")],
        )

    def test_count_untill_tuple(self):
        self.assertEqual(count_untill_tuple([10, 20, 30, (10, 20), 40]), 3)


if __name__ == "__main__":
    unittest.main()
