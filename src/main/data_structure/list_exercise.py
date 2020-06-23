from src.main.logger.py_logger import PyLogger


logger = PyLogger.get_configured_logger()


def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number

    logger.info('Average: {}'.format(summation / len(list_of_number)))

    return summation / len(list_of_number)


def list_sort(list_of_number):
    sorted_list = sorted(list_of_number)
    logger.info("Sorted list : {}".format(sorted_list))

    return sorted_list


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
        middle = (left+right) // 2
        if value == list_of_number[middle]:
            return "Yes"
        elif value < list_of_number[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return "No"


def binary_search_recursive(list_of_numbers, target, start, end):
    if start > end:
        return 'NO'
    mid = start + (end - start) // 2
    
    if list_of_numbers[mid] == target:
        return 'Yes'
    elif list_of_numbers[mid] > target:
        return binary_search_recursive(list_of_numbers, target, start, mid - 1)
    elif list_of_numbers[mid] < target:
        return binary_search_recursive(list_of_numbers, target, mid + 1, end)
    
    
def binary_search_target_index(list_of_number, value, first_index):

    start = 0
    end = len(list_of_number) - 1
    target_index = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if list_of_number[mid] == value:
            target_index = mid
            # looking for target_value and its first_index or last_index in the
            # sorted list .[0,1,2,2,2,3,4,5] our target value = 2 and we
            # looking for the first indexed 2 or last indexed 2 in the list
            if first_index:
                end = mid - 1 
            else:
                start = mid + 1
        elif list_of_number[mid] > value:
            end = mid - 1
        else:
            start = mid + 1
    return target_index
  

def binary_search_count(list_of_number, value):
    
    first_index = binary_search_target_index(list_of_number, value, True)
    
    if first_index != -1:
        last_index = binary_search_target_index(list_of_number, value, False)
        count = last_index - first_index + 1
        
    return count


# CircularRotatedSorted arrary Example : [12,13,14,1,2,3,4] 
# or [2,3,4,12,13,14,1]
def binary_search_circular_sorted(list_of_numbers, value):
    start = 0
    end = len(list_of_numbers) - 1
    
    while start <= end:
        mid = start + (end-start) // 2 
        
        if list_of_numbers[mid] == value:
            return 'Yes'
        
        elif list_of_numbers[mid] <= list_of_numbers[end]:
            if list_of_numbers[mid] < value <= list_of_numbers[end]:
                start = mid + 1
            else:
                end = mid - 1
        
        elif list_of_numbers[start] <= list_of_numbers[mid]:
            if list_of_numbers[start] <= value < list_of_numbers[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1        


def find_square(list_of_numbers):
    list_of_numbers_square = []
    for number in list_of_numbers:
        number = number * number
        list_of_numbers_square.append(number)
    return list_of_numbers_square


def find_prime_number(list_of_numbers):
    is_prime_list = []
    for num in list_of_numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    is_prime_list.append(False)
                    break
            else:
                is_prime_list.append(True)

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            is_prime_list.append(False)

    return is_prime_list

  
def insertion_sort_asc(list_of_number):
    for item in range(1, len(list_of_number)):
        ind = item - 1
        adjacent_item = list_of_number[item]
        while ind >= 0 and list_of_number[ind] > adjacent_item:
            list_of_number[ind + 1] = list_of_number[ind]
            ind = ind - 1
        list_of_number[ind+1] = adjacent_item
    return list_of_number


def insertion_sort_dsc(list_of_number):
    for item in range(1, len(list_of_number)):
        ind = item - 1
        adjacent_item = list_of_number[item]
        while ind >= 0 and list_of_number[ind] < adjacent_item:
            list_of_number[ind + 1] = list_of_number[ind]
            ind = ind - 1
        list_of_number[ind + 1] = adjacent_item
    return list_of_number
