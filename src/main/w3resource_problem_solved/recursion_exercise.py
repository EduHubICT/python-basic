from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()

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


""" geeksforgeeks problem"""

"""
12.  A recursive Pyhton3 program to check 
 whether a given number is palindrome or not 
 """


"""A function that reurns true  
only if num contains one digit """


def oneDigit(num):

    # comparison operation is faster
    # than division operation. So
    # using following instead of
    # "return num / 10 == 0;"
    return (num >= 0) and (num < 10)


""" A recursive function to find out whether num is palindrome or not. 
Initially, dupNum contains address of a copy of num. """


def isPalUtil(num, dupNum):

    # Base case (needed for recursion
    # termination): This statement
    # mainly compares the first digit
    # with the last digit
    if oneDigit(num):
        return num == (dupNum) % 10

    # This is the key line in this
    # method. Note that all recursive
    # calls have a separate copy of
    # num, but they all share same
    # copy of *dupNum. We divide num
    # while moving up the recursion tree
    if isPalUtil(int(num / 10), dupNum) == False:
        return -1

    # The following statements are
    # executed when we move up the
    # recursion call tree
    dupNum = int(dupNum / 10)

    # At this point, if num%10
    # contains i'th digit from
    # beiginning, then (*dupNum)%10
    # contains i'th digit from end
    return num % 10 == (dupNum) % 10


""" The main function that uses recursive function isPalUtil() to find out whether num is palindrome or not """


def isPal(num):
    # If num is negative,
    # make it positive
    if num < 0:
        num = -num

    # Create a separate copy of
    # num, so that modifications
    # made to address dupNum
    # don't change the input number.
    dupNum = num
    # *dupNum = num

    if isPalUtil(num, dupNum) == 0:
        return True
    else:
        return False


""" 13. Python 3 program to print all possible strings of length k """

# to print all possible
# strings of length k
list_of_k_length = []


def printAllKLengthRec(set, prefix, n, k):
    # Base case: k is 0,
    # print prefix
    # global list_1
    if k == 0:
        logger.info(prefix)
        list_of_k_length.append(prefix)
        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):

        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1)


def printAll(set, k):
    global list_of_k_length
    list_of_k_length.clear()
    printAllKLengthRec(set, "", len(set), k)
    return list_of_k_length


"""
14. Recursive Implementation of atoi()
The atoi() function takes a string (which represents an integer) as an argument and returns its value.
"""


def str_to_num(sum_1, str_1):
    if len(str_1) == 1:
        return sum_1 * 10 + int(str_1)

    return str_to_num(sum_1 * 10 + int(str_1[0:1]), str_1[1:])
