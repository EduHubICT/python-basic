from src.main.logger.py_logger import PyLogger


logger = PyLogger.get_configured_logger()


def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number

    logger.info('Average: {}'.format(summation / len(list_of_number)))

    return summation / len(list_of_number)


def sort_list(list_of_number):
    
    sorted_list = sorted(list_of_number)
    logger.info("Sorted list : {}".format(sorted_list))
    
    return sorted_list


def slicing(list1):
    lst_len = len(list1)
    lst = []
    i = 0
    for index in range(lst_len):
        if index > 2:
            lst.append(list1[index])
            i += 1
    return lst


def rep(list1):
    for index in range(len(list1)):
        if index == 1:
            list1[index] = 2
    return list1


def find_max(list_of_number):
    max_val = -1000000
    for number in list_of_number:
        if number > max_val:
            max_val = number
    return max_val


def find_min(list_of_number):
    min_val = 1000000
    for number in list_of_number:
        if number < min_val:
            min_val = number
    return min_val


def find_sum(list_of_number) -> int:
    summation = 0
    for number in list_of_number:
        summation = summation + number
    return summation


def sort_list_bubble_asc(list_of_number):
    list_length = len(list_of_number)
    for index in range(0, list_length - 1):
        for ind in range(0, list_length - index - 1):
            if list_of_number[ind] > list_of_number[ind + 1]:
                temp = list_of_number[ind]
                list_of_number[ind] = list_of_number[ind + 1]
                list_of_number[ind + 1] = temp

    return list_of_number


def sort_list_bubble_dsc(list_of_number):
    list_length = len(list_of_number)
    for index in range(0, list_length - 1):
        for ind in range(0, list_length - index - 1):
            if list_of_number[ind] < list_of_number[ind + 1]:
                temp = list_of_number[ind]
                list_of_number[ind] = list_of_number[ind + 1]
                list_of_number[ind + 1] = temp

    return list_of_number


def binary_search(list_of_number, value):
    list_length = len(list_of_number)
    left = 0
    right = list_length - 1

    while left <= right:
        middle = (left+right)//2
        if value == list_of_number[middle]:
            return "Yes"
        elif value < list_of_number[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return "No"


def find_square(list_of_numbers):
    list_of_numbers_square = []
    for number in list_of_numbers:
        number = number*number
        list_of_numbers_square.append(number)
    return list_of_numbers_square

