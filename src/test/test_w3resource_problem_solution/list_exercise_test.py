import unittest

from src.main.w3resource_problem_solved.list_exercise import *


class TestList(unittest.TestCase):
 
    def test_sort_increasing_order(self):
        self.assertEqual(sort_increasing_order([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]),\
                         [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])

    def test_three_dimensional_array(self):
        self.assertEqual(three_dimensional_array(3,4,6), [[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],\
                                                           [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],\
                                                          [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],\
                                                           [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]],\
                                                          [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],\
                                                           [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]] )

    def test_shuffled_list(self):
        self.assertEqual(shuffled_list([1, 2, 3, 4, 5, 6]), [5, 3, 2, 1, 6, 4])

    def test_list_to_string(self):
        self.assertEqual(list_to_string(['p', 'y', 't']), 'pyt')

    def test_index_of_item(self):
        self.assertEqual(index_of_item([1, 2, 3, 4, 5, 6], 3), 2)

    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_random_choice(self):
        self.assertEqual(random_choice([1, 2, 3, 4, 5]), 4)

    def test_lists_circularly_identical(self):
        self.assertEqual(lists_circularly_identical([1, 1, 0, 0, 1], [1, 1, 1, 0, 0]), True)

    def test_second_smallest(self):
        self.assertEqual(second_smallest([5, -1, 0, 10, -29]), -1)

    def test_second_largest(self):
        self.assertEqual(second_largest([5, -1, 0, 10, -29]), 5)

    def test_count_num_within_range(self):
        self.assertEqual(count_num_within_range([10, 20, 30, 40, 40, 40, 70, 80, 99] , 40, 100), 6)
        
    def test_check_sublist(self):
        self.assertEqual(check_sublist([2, 4, 3, 5, 7], [4, 3]), True)
        self.assertEqual(check_sublist([2, 4, 3, 5, 7], [3, 7]), False)
        self.assertEqual(check_sublist([2, 4, 3, 5, 7], [3]), True)
        
    def test_create_all_sublist(self):
        self.assertEqual(create_all_sublist([10, 20]), [[], [10], [20], [10,20]])
        self.assertEqual(create_all_sublist(['X', 'Y', 'Z']), [[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']])
        
    def test_prime_eratosthenes(self):
        self.assertEqual(prime_eratosthenes(10), [2, 3, 5, 7])
        
    def test_concatenate_list_ranges(self):
        self.assertEqual(concatenate_list_ranges(['p', 'q'], 2), ['p1', 'q1', 'p2', 'q2'])
        
    def test_get_variable_unique_id(self):
        self.assertEqual(get_variable_unique_id(100), None)
                         
    def test_list_comprehension(self):
        self.assertEqual(list_comprehension(10), [(1, 3, 5), (1, 3, 7), (1, 3, 9), (1, 5, 7), (1, 5, 9), (1, 7, 9), (3, 5, 7), (3, 5, 9), (3, 7, 9), (5, 7, 9)])
        

if __name__ == '__main__':
    unittest.main()
