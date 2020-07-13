"""
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""

"""
1. Write a Python program to calculate the sum of a list of numbers.
"""


def sum_of_list(list_of_numbers):
    if not list_of_numbers:
        return 0
    else:
        return list_of_numbers[0] + sum_of_list(list_of_numbers[1:])


"""
2. Write a Python program to converting an Integer to a string in any base
(base upto 36)
"""


def convert_decimal_to_any_base(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if number < base:
        return digits[number]
    else:
        return convert_decimal_to_any_base(number // base, base) + digits[number % base]


"""
3. Write a Python program of recursion list sum.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""


def sum_of_2d_list(list_of_elements):
    total = 0
    for data in list_of_elements:
        if type([]) == type(data):
            total += sum_of_2d_list(data)
        else:
            total += data
    return total


"""
4. Write a Python program to get the factorial of a non-negative integer. 
"""


def get_factorial(n):
    if n == 0:
        return 1
    else:
        return n * get_factorial(n - 1)


"""
5. Write a Python program to solve the Fibonacci sequence using recursion.
"""


def get_fibonacci_number(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)


"""
6. Write a Python program to get the sum of a non-negative integer.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9
"""


def get_sum_of_digits(number):
    if number < 10:
        return number
    else:
        return get_sum_of_digits(number // 10) + number % 10


"""
7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""


def get_sum_of_series(n):
    if n <= 0:
        return n
    else:
        return n + get_sum_of_series(n - 2)


"""
8. Write a Python program to calculate the harmonic sum of n-1. 
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example : harmonic series
"""


def get_harmonic_sum(n):
    if n <= 1:
        return n
    else:
        return 1.0 / n + get_harmonic_sum(n - 1)


"""
10. Write a Python program to calculate the value of 'a' to the power 'b'.
Test Data :
power(3,4) -> 81
"""


def get_power(base, mul):
    if mul == 0:
        return 1
    else:
        return base * get_power(base, mul - 1)


"""
11. Write a Python program to find the greatest common divisor (gcd) of two integers.
"""


def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)
