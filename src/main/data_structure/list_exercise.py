
def find_average(list_of_number):
    summation = 0
    for number in list_of_number:
        summation = summation + number

    return summation / len(list_of_number)


def even_finder(list_of_number):
    even_list = []
    for number in list_of_number :
        if number % 2 ==0 :
            even_list.append(number)
                    
    return even_list

numbers = even_finder([10,4,3,5,7,9,12,16])

print(numbers)