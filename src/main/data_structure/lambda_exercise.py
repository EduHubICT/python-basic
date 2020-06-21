from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()

# lambda is a anonymous function. Which can take any number of
# argument, but only one expression is possible.


# closure is used.
def find_square_of_value():
    square_value = lambda x : x * x
    logger.info('Square of the given value: {}'.format(square_value))

    return square_value
    

# map take all elemnets in list and pass it to function. And return values for all element. whether it is bool/other_type
def multiply_by_two(list_of_number):
    multiply = list(map(lambda x : x * 2, list_of_number))
    logger.info('Multiply given number by two: {}'.format(multiply))
    
    return multiply


# filter takes all elements in a list and pass it to function. And return values only for true ones.
def find_even_numbers(list_of_number):
    even_numbers = list(filter(lambda x: (x % 2 == 0), list_of_number))
    logger.info('Even Numbers: {}'.format(even_numbers))
    
    return even_numbers


#closure is used
def add_two_value(y):
    second_value_add = lambda x : x + y
    logger.info('Two value is add: {}'.format(second_value_add))

    return second_value_add


high_order_function = lambda x, function : x + function(x)


even_or_odd =  lambda x : (x % 2 and 'odd' or 'even')


def sort_id_number(ids):
    sort_number = sorted(ids, key=lambda x: int(x[2:]))
    logger.info('Sorted id number : {}'.format(sort_number))
    
    return sort_number
