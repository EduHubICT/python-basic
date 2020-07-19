import unittest
from src.main.w3resource_problem_solved.string_exercise import *


class StringTestCase(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(get_length("sample"), 6)

    def test_solution_2(self):
        self.assertEqual(
            get_characters_frequency("samples"),
            {"s": 2, "a": 1, "m": 1, "p": 1, "l": 1, "e": 1},
        )

    def test_solution_3(self):
        sample1 = "w3resource"
        expected1 = "w3ce"
        sample2 = "w3"
        expected2 = "w3w3"
        sample3 = "w"
        expected3 = ""
        self.assertEqual(solved_problem_3(sample1), expected1)
        self.assertEqual(solved_problem_3(sample2), expected2)
        self.assertEqual(solved_problem_3(sample3), expected3)

    def test_solution_4(self):
        sample = "restart"
        expected = "resta$$"
        self.assertEqual(solved_problem_4(sample), expected)

    def test_solution_5(self):
        sample1, sample2 = "abc", "xyz"
        expected1, expected2 = "xyc", "abz"
        self.assertEqual(swap_characters(sample1, sample2), (expected1, expected2))

    def test_solution_6(self):
        sample = "abc"
        expected = "abcing"
        self.assertEqual(solved_problem_6(sample), expected)
        self.assertEqual(solved_problem_6(expected), "abcingly")

    def test_solution_7(self):
        sample = "The Big0one is not that high"
        expect = "The Big0one is good"
        self.assertEqual(solved_problem_7(sample, "not", "high", "good"), expect)

    def test_solution_12(self):
        self.assertEqual(
            get_word_frequency("stay home stay safe"), {"stay": 2, "home": 1, "safe": 1}
        )

    def test_solution_24(self):
        self.assertTrue(check_starts_with("Python", "Py"))
        self.assertFalse(check_starts_with("Python", "Ja"))

    def test_solution_25(self):
        sample = "ABCD"
        expect = "DEFG"
        self.assertEqual(caesar_cipher_encrypt(sample), expect)

    def test_solution_38(self):
        sample = "The quick brown fox jumps over the lazy dog."
        self.assertEqual(count_substring_occurrences(sample, "dog"), 1)

    def test_solution_39(self):
        self.assertEqual(reverse("IoT"), "ToI")

    def test_solution_40(self):
        self.assertEqual(
            reverse_words("This is not a paragraph."), "paragraph. a not is This"
        )


if __name__ == "__main__":
    unittest.main()
