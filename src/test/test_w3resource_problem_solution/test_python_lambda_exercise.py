import unittest
from src.main.w3resource_problem_solved.python_lambda_exercise import *


class PythonLambdaTestCase(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(simple_addition(100), 115)  # 100 will be added with given 15
        self.assertEqual(simple_multiplication(5, 6), 30)

    def test_solution_2(self):
        res = anonymous_multiplication(3)
        self.assertEqual(res(15), 45)  # this means 3 *15
        res = anonymous_multiplication(4)
        self.assertEqual(res(15), 60)  # this means 4 *15

    def test_solution_3(self):
        my_output = sort_tuples_list(
            [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
        )
        expected_output = [
            ("Social sciences", 82),
            ("English", 88),
            ("Science", 90),
            ("Maths", 97),
        ]
        self.assertEqual(my_output, expected_output)

    def test_solution_4(self):
        my_output = sort_dict_list(
            [
                {"Name": "Rafi", "Age": 17},
                {"Name": "Tania", "Age": 9},
                {"Name": "Himu", "Age": 12},
                {"Name": "Simi", "Age": 7},
            ],
            "Age",
        )
        expected_output = [
            {"Name": "Simi", "Age": 7},
            {"Name": "Tania", "Age": 9},
            {"Name": "Himu", "Age": 12},
            {"Name": "Rafi", "Age": 17},
        ]
        self.assertEqual(my_output, expected_output)

    def test_solution_5(self):
        self.assertEqual(
            get_odd_numbers_only([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9]
        )
        self.assertEqual(
            get_even_numbers_only([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10]
        )

    def test_solution_6(self):
        self.assertEqual(square_list_item([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        self.assertEqual(cube_list_item([1, 2, 3, 4, 5]), [1, 8, 27, 64, 125])

    def test_solution_7(self):
        self.assertTrue(find_word_with_character("Python", "P"))
        self.assertFalse(find_word_with_character("Java", "K"))

    def test_solution_10(self):
        my_output = get_fibonacci_series(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(my_output, expected)

    def test_solution_11(self):
        my_output = find_intersection([1, 2, 3], [2, 3, 4])
        expected = [2, 3]
        self.assertEqual(my_output, expected)

    def test_solution_17(self):
        my_output = find_divisible_numbers(
            [13, 26, 19, 247, 108, 38, 51, 52, 57, 34, 39], 13, 19
        )
        expected = [13, 26, 19, 247, 38, 52, 57, 39]
        self.assertEqual(my_output, expected)

    def test_solution_18(self):
        output = find_palindromes(["mom", "madam", "father", "dad"])
        expected = ["mom", "madam", "dad"]
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
