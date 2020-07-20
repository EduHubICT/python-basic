import unittest
from src.main.w3resource_problem_solved.recursion_exercise import *


class TestRecursion(unittest.TestCase):
    def test_sum_of_list(self):
        self.assertEqual(sum_of_list([1, 2, 4]), 7)

    def test_base_conversion(self):
        self.assertEqual(convert_decimal_to_any_base(948199477, 36), "FOJ7ED")

    def test_2d_sum(self):
        self.assertEqual(sum_of_2d_list([1, [1, 2], [1, 2, 3]]), 10)

    def test_factorial(self):
        self.assertEqual(get_factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(get_fibonacci_number(7), 13)

    def test_digit_sum(self):
        self.assertEqual(get_sum_of_digits(123456), 21)

    # series: n + (n-2) + (n-4) + ...
    def test_series_sum(self):
        self.assertEqual(get_sum_of_series(10), 30)

    def test_harmonic_sum(self):
        self.assertEqual(get_harmonic_sum(4), 2.083333333333333)

    def test_power(self):
        self.assertEqual(get_power(3, 2), 9)
        self.assertEqual(get_power(100, 0), 1)

    def test_gcd(self):
        self.assertEqual(get_gcd(6, 10), 2)

    def test_isPal(self):
        self.assertEqual(isPal(12321), True)
        self.assertEqual(isPal(12), False)

    def test_printAllKLengthRec(self):
        list_1 = ["a", "b"]
        self.assertEqual(printAllKLengthRec(["a"], "", 1, 3), None)
        self.assertEqual(
            printAll(list_1, 3),
            ["aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"],
        )

    def test_str_to_num(self):
        self.assertEqual(str_to_num(0, "123"), 123)


if __name__ == "__main__":
    unittest.main()
