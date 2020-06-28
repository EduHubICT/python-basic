import unittest

from src.main.data_structure.list_exercise import *


class TestList(unittest.TestCase):

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3]), 2)
        self.assertEqual(find_average([1, 2, 3, 4, 5, 6, 7, -1]), 3.375)

    def test_sort_list(self):
        self.assertEqual(sort_list([3, 5, 1, 9]), [1, 3, 5, 9])

    def test_find_max(self):
        self.assertEqual(find_max([0, 3, 2, 4, 5, 6, 100]), 100)

    def test_find_min(self):
        self.assertEqual(find_min([2, 4, 3, 5, -1, -1000]), -1000)

    def test_find_sum(self):
        self.assertEqual(find_sum([1, 2, 3, 4]), 10)

    def test_sort_list_bubble(self):
        self.assertEqual(sort_list_bubble_asc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_list_bubble_dsc(self):
        self.assertEqual(sort_list_bubble_dsc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 100), "Yes")
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 1000), "No")
        self.assertEqual(binary_search([1, 5, 15, 35, 100, 305, 390], 390), "Yes")
        self.assertEqual(binary_search([1, 5], 100), "No")

    def test_recursive_binary_search(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 3, 0, 7), 'Yes')

    def test_binary_search_index(self):
        self.assertEqual(binary_search_target_index([1, 5, 15, 100, 100, 305, 390], 100, True), 3)

    def test_binary_search_similar_target_count(self):
        self.assertEqual(binary_search_count([1, 5, 15, 100, 100, 305, 390], 100), 2)

    def test_binary_search_circular_sorted(self):
        self.assertEqual(binary_search_circular_sorted([12, 13, 14, 1, 2, 3, 4], 14), 'Yes')

    def test_find_square(self):
        self.assertEqual(find_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        self.assertEqual(find_square([20, 12, 11]), [400, 144, 121])

    def test_find_prime(self):
        self.assertEqual(find_prime_number([11, 12, 33, 84, 95, 101]), [True, False, False, False, False, True])

    def test_insertion_sort_asc(self):
        self.assertEqual(insertion_sort_asc([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort_asc([5, 10, 3, 22, 23, 24, 25]), [3, 5, 10, 22, 23, 24, 25])
        self.assertEqual(insertion_sort_asc([10, 9, 8, 7, 5, 1, 2, 4, 3, 6]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_insertion_sort_dsc(self):
        self.assertEqual(insertion_sort_dsc([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(insertion_sort_dsc([5, 10, 3, 22, 23, 24, 25]), [25, 24, 23, 22, 10, 5, 3])
        self.assertEqual(insertion_sort_dsc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        
    def test_specified_type_item(self):
        self.assertEqual(specified_type_item([1,2,'abc',2.2], int), 2)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])
 
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

    def test_find(self):
        primary = [10, 4, 6, 3, 5]
        self.assertEqual(Stack.find(primary), [5, 6, 10])
        

if __name__ == '__main__':
    unittest.main()
