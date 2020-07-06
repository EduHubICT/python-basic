from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()

"""

w3resources.com tuple problem solve

"""


"""

9. Repeated items of a tuple

"""


def repeated_item(tuple_1, item):
    logger.info(tuple_1.count(item))


"""

10. Check whether an element exists within a tuple

"""


def element_existance(tuple_1, element):
    return element in tuple_1


"""

16.Convert a tuple to a dictionary

"""


def tuple_to_dictionary(tuple_1):
    return dict((y, x) for x, y in tuple_1)


"""

17.Unzip a list of tuples into individual lists

"""


def individual_lists(list_of_tuple):
    return list(zip(*list_of_tuple))


"""

18.Reverse a tuple

"""


def reverse_tuple(tuple_1):
    new_tuple = reversed(tuple_1)
    return tuple(new_tuple)


"""

19.Converting a list of tuples into a dictionary

"""


def convert_list_to_tuple(list_of_tuple):
    dict_1 = {}
    for a, b in list_of_tuple:
        dict_1.setdefault(a, []).append(b)

    return dict_1


"""

22. Remove an empty tuple(s) from a list of tuples

"""


def remove_empty_tuple(list_of_tuple):
    new_list = [t for t in list_of_tuple if t]
    return new_list


"""

23.Sort a tuple by its float element

"""


def sort_tuple(list_of_tuple):
    return sorted(list_of_tuple, key=lambda x: x[1], reverse=True)


"""

24.  Count the elements in a list until an element is a tuple

"""


def count_untill_tuple(list_of_tuple):
    count = 0
    for n in list_of_tuple:
        if isinstance(n, tuple):
            break
        count += 1
    return count


"""

black and pre-commit check

"""


def tuple_range(list_of_tuple):
    logger.info(list_of_tuple[:1])
