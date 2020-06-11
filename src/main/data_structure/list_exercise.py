
def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number

    return summation / len(list_of_number)


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


def sort_list_bubble_ass(list_of_number):
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
