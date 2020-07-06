"""
- It consists of key-value pair.
  The whole pair is called an item of the dictionary.

- Each key is separated from its value by a colon (:),
  the items are separated by commas,
  and the whole thing is enclosed in curly braces.
"""

from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


class Dict:

    # to initiate dictionary
    def __init__(self, init_dict):
        if init_dict is None:
            init_dict = {}
        self.dict = init_dict

    # to add single item
    def add_element(self, key, value):
        self.dict[key] = value
        # self.dict.update({key : value})
        return self.dict

    # to get single item value
    def get_element_by_key(self, key):
        logger.warning("You can get key error, use exception")
        return self.dict[key]

    # to remove single item
    def delete_element_by_key(self, key):
        logger.warning("You can get key error, use exception")
        del self.dict[key]
        return self.dict

    # python built in method

    # to remove entire dictionary
    def clear(self):
        return self.dict.clear()

    # to return dict keys
    def keys(self):
        return self.dict.keys()

    # to return dict values
    def values(self):
        return self.dict.values()

    def mapping_list_into_dictionary(self, key_list, value_list):
        self.dict = dict(zip(key_list, value_list))
        logger.info(self.dict)
        return self.dict

    # find the max value in a dictionary
    def find_max_value(self):
        max_key = max(self.dict, key=self.dict.get)
        max_value = self.dict[max_key]
        logger.info(max_value)
        return max_value

    # find the max value in a dictionary
    def find_min_value(self):
        min_key = min(self.dict, key=self.dict.get)
        min_value = self.dict[min_key]
        logger.info(min_value)
        return min_value

    # sort dictionary by key
    def sort_dict_by_key(self):
        _dict_items = self.dict.items()
        sorted_items = dict(sorted(_dict_items))
        return sorted_items

    def tutorial_marks_average(self):
        tutorial = [
            {"id": 101, "subject": "C", "First": 23, "Second": 22},
            {"id": 102, "subject": "Python", "First": 23, "Second": 24},
            {"id": 103, "subject": "Java", "First": 25, "Second": 16},
        ]
        for marks in tutorial:
            n1 = marks.pop("First")
            n2 = marks.pop("Second")
            marks["First + Second"] = (n1 + n2) / 2
        return tutorial
