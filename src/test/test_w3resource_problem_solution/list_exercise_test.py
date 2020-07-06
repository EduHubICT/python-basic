import unittest

from src.main.w3resource_problem_solved.list_exercise import *


class TestList(unittest.TestCase):
    def test_sort_increasing_order(self):
        self.assertEqual(
            sort_increasing_order([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]),
            [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)],
        )

    def test_three_dimensional_array(self):
        self.assertEqual(
            three_dimensional_array(3, 4, 6),
            [
                [
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                ],
                [
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                ],
                [
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                ],
            ],
        )

    def test_shuffled_list(self):
        self.assertEqual(shuffled_list([1, 2, 3, 4, 5, 6]), [5, 3, 2, 1, 6, 4])

    def test_list_to_string(self):
        self.assertEqual(list_to_string(["p", "y", "t"]), "pyt")

    def test_index_of_item(self):
        self.assertEqual(index_of_item([1, 2, 3, 4, 5, 6], 3), 2)

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_random_choice(self):
        self.assertEqual(random_choice([1, 2, 3, 4, 5]), 4)

    def test_lists_circularly_identical(self):
        self.assertEqual(
            lists_circularly_identical([1, 1, 0, 0, 1], [1, 1, 1, 0, 0]), True
        )

    def test_second_smallest(self):
        self.assertEqual(second_smallest([5, -1, 0, 10, -29]), -1)

    def test_second_largest(self):
        self.assertEqual(second_largest([5, -1, 0, 10, -29]), 5)

    def test_count_num_within_range(self):
        self.assertEqual(
            count_num_within_range([10, 20, 30, 40, 40, 40, 70, 80, 99], 40, 100), 6
        )

    def test_check_sublist(self):
        self.assertEqual(check_sublist([2, 4, 3, 5, 7], [4, 3]), True)
        self.assertEqual(check_sublist([2, 4, 3, 5, 7], [3, 7]), False)
        self.assertEqual(check_sublist([2, 4, 3, 5, 7], [3]), True)

    def test_create_all_sublist(self):
        self.assertEqual(create_all_sublist([10, 20]), [[], [10], [20], [10, 20]])
        self.assertEqual(
            create_all_sublist(["X", "Y", "Z"]),
            [
                [],
                ["X"],
                ["Y"],
                ["Z"],
                ["X", "Y"],
                ["X", "Z"],
                ["Y", "Z"],
                ["X", "Y", "Z"],
            ],
        )

    def test_prime_eratosthenes(self):
        self.assertEqual(prime_eratosthenes(10), [2, 3, 5, 7])

    def test_concatenate_list_ranges(self):
        self.assertEqual(
            concatenate_list_ranges(["p", "q"], 2), ["p1", "q1", "p2", "q2"]
        )

    def test_get_variable_unique_id(self):
        self.assertEqual(get_variable_unique_id(100), None)

    def test_list_comprehension(self):
        self.assertEqual(
            list_comprehension(10),
            [
                (1, 3, 5),
                (1, 3, 7),
                (1, 3, 9),
                (1, 5, 7),
                (1, 5, 9),
                (1, 7, 9),
                (3, 5, 7),
                (3, 5, 9),
                (3, 7, 9),
                (5, 7, 9),
            ],
        )

    def test_change_position(self):
        self.assertEqual(change_position([0, 1, 2, 3, 4, 5]), [1, 0, 3, 2, 5, 4])

    def test_arrange_character_wise(self):
        self.assertEqual(
            arrange_character_wise(
                [
                    "be",
                    "have",
                    "do",
                    "say",
                    "get",
                    "make",
                    "go",
                    "know",
                    "take",
                    "see",
                    "come",
                    "think",
                    "look",
                    "want",
                    "give",
                    "use",
                    "find",
                    "tell",
                    "ask",
                    "work",
                    "seem",
                    "feel",
                    "leave",
                    "call",
                ]
            ),
            None,
        )

    def test_sorted_unique_array(self):
        self.assertEqual(
            sorted_unique_array(
                [
                    (1, 2),
                    (3, 4),
                    (1, 2),
                    (5, 6),
                    (7, 8),
                    (1, 2),
                    (3, 4),
                    (3, 4),
                    (7, 8),
                    (9, 10),
                ]
            ),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

    def test_insert_element_before(self):
        self.assertEqual(
            insert_element_before(["Red", "Green", "Black"]),
            ["k", "Red", "k", "Green", "k", "Black"],
        )

    def test_nested_lists(self):
        self.assertEqual(nested_lists([["Red"], ["Green"], ["Black"]]), None)

    def test_sort_nested_dictionary(self):
        self.assertEqual(
            sort_nested_dictionary(
                [
                    {"key": {"subkey": 1}},
                    {"key": {"subkey": 10}},
                    {"key": {"subkey": 5}},
                ]
            ),
            [{"key": {"subkey": 10}}, {"key": {"subkey": 5}}, {"key": {"subkey": 1}}],
        )

    def test_split_list_nth_element(self):
        self.assertEqual(
            split_list_nth_element(
                ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
                3,
            ),
            [
                ["a", "d", "g", "j", "m"],
                ["b", "e", "h", "k", "n"],
                ["c", "f", "i", "l"],
            ],
        )

    def test_concatenate_elements(self):
        self.assertEqual(concatenate_elements(["red", "green", "orange"]), None)

    def test_remove_specific_key(self):
        self.assertEqual(
            remove_specific_key(
                [
                    {"key1": "value1", "key2": "value2"},
                    {"key1": "value3", "key2": "value4"},
                ]
            ),
            [{"key2": "value2"}, {"key2": "value4"}],
        )

    def test_string_to_list(self):
        self.assertEqual(
            string_to_list("['Red', 'Green', 'White']"), ["Red", "Green", "White"]
        )

    def test_replace_last_item(self):
        self.assertEqual(
            replace_last_item([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]),
            [1, 3, 5, 7, 9, 2, 4, 6, 8],
        )

    def test_tuple_with_smallest_second_value(self):
        self.assertEqual(
            tuple_with_smallest_second_value([(4, 1), (1, 2), (6, 0)]), (6, 0)
        )

    def test_access_by_index(self):
        self.assertEqual(
            access_by_index({"physics": 80, "math": 90, "chemistry": 86}), None
        )

    def test_find_list_highest_sum(self):
        self.assertEqual(
            find_list_highest_sum([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]),
            [10, 11, 12],
        )

    def test_all_greater_num(self):
        self.assertEqual(all_greater_num([220, 330, 500]), True)

    def test_extend_list(self):
        self.assertEqual(
            extend_list([10, 20, 30], [40, 50, 60]), [40, 50, 60, 10, 20, 30]
        )

    def test_list_of_lists_remove_duplicate(self):
        self.assertEqual(
            list_of_lists_remove_duplicate(
                [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
            ),
            [[10, 20], [30, 56, 25], [33], [40]],
        )

    def test_compress(self):
        self.assertEqual(
            compress([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]),
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4],
        )

    def test_pack_consecutive_duplicates(self):
        self.assertEqual(
            pack_consecutive_duplicates(
                [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
            ),
            [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]],
        )

    def test_encode_list(self):
        self.assertEqual(
            encode_list([1, 1, 2, 3, 4, 4.3, 5, 1]),
            [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]],
        )

    def test_decode(self):
        self.assertEqual(decode([[2, 1], 2, 3, [2, 4], 5, 1]), [1, 1, 2, 3, 4, 4, 5, 1])

    def test_remove_kth_element(self):
        self.assertEqual(
            remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3), [1, 1, 3, 4, 4, 5, 1]
        )

    def test_insert_spec_position(self):
        self.assertEqual(
            insert_spec_position(12, [1, 1, 2, 3, 4, 4, 5, 1], 3),
            [1, 1, 12, 2, 3, 4, 4, 5, 1],
        )

    def test_random_select_nums(self):
        self.assertEqual(random_select_nums([1, 1, 2, 3, 4, 4, 5, 1], 3), None)


if __name__ == "__main__":
    unittest.main()
