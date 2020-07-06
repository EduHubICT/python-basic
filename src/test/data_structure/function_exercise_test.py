import unittest
from src.main.data_structure.function_exercise import *


class MyTestCase(unittest.TestCase):
    def test_find_factorial(self):
        self.assertEqual(find_factorial(4), 24)

    def test_determine_letters_case(self):
        self.assertEqual(determine_letters_case("Stay Home, Stay Safe"), (4, 12))

    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(33), False)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(23), True)
        self.assertEqual(is_prime(89), True)
        self.assertEqual(is_prime(97), True)
        self.assertEqual(is_prime(111), False)

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("exe"), True)
        self.assertEqual(is_palindrome("asrta"), False)
        self.assertEqual(is_palindrome("daddad"), True)
        self.assertEqual(is_palindrome("xecrghuotr"), False)
        self.assertEqual(is_palindrome("1234321"), True)


if __name__ == "__main__":
    unittest.main()
