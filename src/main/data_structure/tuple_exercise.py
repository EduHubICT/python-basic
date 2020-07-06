"""
A tuple is a sequence of immutable Python objects.
(Immutable means values of tuple can't be changed or updated)
Tuples are sequences, just like lists.
The differences between tuples and lists are,
the tuples cannot be changed unlike lists and tuples use parentheses,
whereas lists use square brackets.
(https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm)
"""
from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


class Tuple:
    def __init__(self, tup):
        self.tuple = tup

    # method overloading to return a single object or a range of object
    def tuple_indexing(self, left, right):
        if right is not None:
            return self.tuple[
                left:right
            ]  # this will return object from left(including) to right(excluding)
        else:
            return self.tuple[left]  # this will return a single object

    # this concatenate two tuple into tuple
    def tuple_updating(self, new_tuple):
        return self.tuple + new_tuple

    # to remove a single element from tuple
    # Actually, tuple doesn't support removing element by index
    def remove_tuple_element(self, index):
        tuple_length = self.tuple_size()
        tuple1 = self.tuple[0:index]
        tuple2 = self.tuple[index + 1 : tuple_length]

        return tuple1 + tuple2

    # to return tuple size
    def tuple_size(self):
        return len(self.tuple)

    # this will return True or False
    def check_tuple_element(self, target_value):
        return target_value in self.tuple

    # repetition of tuple x times
    def tuple_element_repetition(self, times):
        return self.tuple * times

    # tuple into string
    def tuple_to_string(self):
        _str = "".join(self.tuple)
        logger.info(_str)
        return _str

    # sort a tuple by its float element.
    def sort_tuple_by_float_element(self):
        return tuple(sorted(self.tuple, key=lambda x: float(x[1]), reverse=True))

    # Count and average Best three tutorial marks
    def calculate_average_tutorial_marks(self):
        marks = [
            ("course1", "12"),
            ("course2", "18"),
            ("course3", "15"),
            ("course4", "20"),
            ("course5", "25"),
        ]
        total = 0
        temp = 100
        average = 0
        for x in marks:
            key = int(x[1])
            if key < temp:
                temp = key
            total = total + key
            average = total / len(marks)
        return average
