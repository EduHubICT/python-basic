"""
Resource link: https://www.w3resource.com/python-exercises/lambda/index.php
Tried to solve most problem that i like to solve
unit test file added in test section
"""

""" 
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
    also create a lambda function that multiplies argument x with argument y and print the result.
"""


def simple_addition(x):
    add = lambda a: a + 15
    return add(x)


def simple_multiplication(a, b):
    mul = lambda x, y: x * y
    return mul(a, b)


""" 
2. Write a Python program to create a function that takes one argument, 
    and that argument will be multiplied with an unknown given number 
"""


def anonymous_multiplication(n):
    return lambda x: x * n


"""
3. Write a Python program to sort a list of tuples using Lambda.
"""


def sort_tuples_list(list_of_tuples):
    list_of_tuples.sort(key=lambda x: x[1])
    return list_of_tuples


"""
4. Write a Python program to sort a list of dictionaries using Lambda.
"""


def sort_dict_list(list_of_dict, key):
    list_of_dict.sort(key=lambda x: x[key])
    return list_of_dict


"""
5. Write a Python program to filter a list of integers using Lambda.
"""


def get_odd_numbers_only(list_of_numbers):
    return list(filter(lambda x: x % 2 != 0, list_of_numbers))


def get_even_numbers_only(list_of_numbers):
    return list(filter(lambda x: x % 2 == 0, list_of_numbers))


"""
6. Write a Python program to square and cube every number in a given list of integers using Lambda.
"""


def square_list_item(list_of_numbers):
    return list(map(lambda x: x * x, list_of_numbers))


def cube_list_item(list_of_numbers):
    return list(map(lambda x: x * x * x, list_of_numbers))


"""
7. Write a Python program to find if a given string starts with a given character using Lambda.
"""


def find_word_with_character(word, char):
    match = lambda x: True if x.startswith(char) else False
    return match(word)


"""
10. Write a Python program to create Fibonacci series upto n using Lambda.
"""


def get_fibonacci_series(n):
    fib_series = [0, 1]  # pre define
    any(map(lambda _: fib_series.append(fib_series[-2] + fib_series[-1]), range(2, n)))
    return fib_series


"""
11. Write a Python program to find intersection of two given arrays using Lambda.
"""


def find_intersection(list1, list2):
    return list(filter(lambda x: x in list1, list2))


"""
17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
"""


def find_divisible_numbers(list_of_numbers, divisor1, divisor2):
    return list(filter(lambda x: (x % divisor1 == 0 or x % divisor2 == 0), list_of_numbers))


"""
18. Write a Python program to find palindromes in a given list of strings using Lambda.
"""


def find_palindromes(list_of_words):
    return list(filter(lambda x: (x == x[::-1]), list_of_words))
