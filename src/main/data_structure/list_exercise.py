
def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number
    print('Average: ',summation / len(list_of_number))

    return summation / len(list_of_number)

def sort_list(list_1):
    
    sorted_lst = sorted(list_1)
    print("Sorted list :", sorted_lst)
    
    return sorted_lst
    


