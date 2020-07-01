from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()

"""
Set contain only unique value. No duplicate is possible. 
set is immutable but mutable as whole.
{} - this is an empty dict, but
{0, 1} - this is a set; 0, 1 are elements
set() - to define an empty set
"""


# convert list into set, which contain unique value only
def create_unique_value_set(list_of_number):
    unique_values = set(list_of_number)

    logger.info('Unique value representation: {}'.format(unique_values))

    return unique_values


# return yes if expected value contains in the set
def access_value_in_set(set_of_number, value):
    for number in set_of_number:
        if number == value:
            logger.info('{} is in the set'.format(value))

            return 'yes'


# add a value in the set or remove a value
def add_remove_in_set(set_of_number, add_value, remove_value):
    if add_value is not None:
        set_of_number.add(add_value)
        logger.info('New set after adding a value: {}'.format(set_of_number))

        return 'Add'

    elif remove_value is not None:
        set_of_number.discard(remove_value)
        logger.info('New set after removing a value: {}'.format(set_of_number))

        return 'Remove'


# return new set containing common and uncommon items between set_a and set_b
def find_union(set_a, set_b) -> set:
    new_set = set_a
    for item in set_b:
        new_set.add(item)

    return new_set


# return a new set containing common items between set_a & set_b
def find_intersection(set_a, set_b) -> set:
    new_set = set()
    for item in set_a:
        if item in set_b:
            new_set.add(item)

    return new_set


# return True if set_a is disjoint with set_b
def find_disjoint(set_a, set_b) -> bool:
    for item in set_a:
        if item in set_b:
            return False

    return True


# return a new set containing only items of set_a that are not in set_b
def find_differences(set_a, set_b) -> set:
    new_set = set()
    for item in set_a:
        if item not in set_b:
            new_set.add(item)

    return new_set


# return True if set_a is subset of set_b
def find_subsets(set_a, set_b) -> bool:
    for item in set_a:
        if item not in set_b:
            return False

    return True


# return True if set_a is superset of set_b
def find_supersets(set_a, set_b) -> bool:
    for item in set_b:
        if item not in set_a:
            return False

    return True


# Find Maximum value in a set
def find_maximum_value(set_a) -> int:
    return max(set_a)


# Find Minimum value in a set
def find_minimum_value(set_a) -> int:
    return min(set_a)
