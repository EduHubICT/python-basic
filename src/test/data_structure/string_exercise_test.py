import unittest
from src.main.data_structure.string_exercise import *


class TestList(unittest.TestCase):
    def test_char_appearance(self):
        self.assertEqual(
            count_char_appearance("google.com"),
            {"o": 3, ".": 1, "g": 2, "l": 1, "e": 1, "c": 1, "m": 1},
        )
        self.assertEqual(count_char_appearance("Dog"), {"D": 1, "o": 1, "g": 1})
        self.assertEqual(
            count_char_appearance("potato"), {"p": 1, "o": 2, "t": 2, "a": 1}
        )

    def test_add_string(self):
        self.assertEqual(add_string("ab"), "ab")
        self.assertEqual(add_string("abc"), "abcing")
        self.assertEqual(add_string("string"), "stringly")

    def test_string_replace(self):
        self.assertEqual(
            replace_string("The lyrics is not that poor!"), "The lyrics is good!"
        )
        self.assertEqual(replace_string("The lyrics is poor!"), "The lyrics is poor!")

    def test_find_longest_word(self):
        self.assertEqual(
            find_longest_word(["PHP", "Exercises", "Backend"]), "Exercises"
        )
        self.assertEqual(
            find_longest_word(["Dhaka", "khunla", "Chattogram", "barisal"]),
            "Chattogram",
        )

    def test_remove_char(self):
        self.assertEqual(remove_char("Python", 0), "ython")
        self.assertEqual(remove_char("ASPNET", 4), "ASPNT")
        self.assertEqual(remove_char("Laravel", 3), "Larvel")

    def test_count_word(self):
        self.assertEqual(
            count_word("the quick brown fox jumps over the lazy dog."),
            {
                "the": 2,
                "jumps": 1,
                "brown": 1,
                "lazy": 1,
                "fox": 1,
                "over": 1,
                "quick": 1,
                "dog.": 1,
            },
        )
        self.assertEqual(
            count_word("We are the Champion, We are the"),
            {"We": 2, "are": 2, "the": 2, "Champion,": 1},
        )


if __name__ == "__main__":
    unittest.main()
