
def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number

    return summation / len(list_of_number)
