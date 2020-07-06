from math import *
from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


# A function to calculate the factorial of a number
def find_factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# A function that accepts a string and calculate the number of upper case letters and lower case letters.
def determine_letters_case(sentence):
    upper_case_count = 0
    lower_case_count = 0
    for letter in sentence:
        if letter.isupper():
            upper_case_count += 1
        elif letter.islower():
            lower_case_count += 1
    logger.info(
        "Original String : {} , UpperCase : {} , LowerCase {}".format(
            sentence, upper_case_count, lower_case_count
        )
    )
    return upper_case_count, lower_case_count


# A function to determine whether a number is prime or not
def is_prime(number):
    # any number less than 2 is not prime
    if number < 2:
        return False
    # check if the num is divisible by any number up to the square root of num
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# A function to determine whether a string is palindrome or not
def is_palindrome(string):
    rev = "".join(reversed(string))
    if string == rev:
        return True
    return False
