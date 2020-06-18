<<<<<<< HEAD
from src.main.logger.py_logger import PyLogger


logger = PyLogger.get_configured_logger()

# set contain only unique value. No duplicate is possible. 
# set is immutable but mutable as whole

def create_unique_value(list_of_number):
    unique_values = set(list_of_number)

    logger.info('Unique value representation: {}'.format(unique_values))

    return unique_values


def accessing_value_in_set(set_of_number, value):
    for number in set_of_number:
        if number == value:
            logger.info('{} is in the set'.format(value))
            
            return 'yes'
        
def add_remove_in_set(set_of_number, add_value, remove_value):
    if add_value is not None:
        set_of_number.add(add_value)
        logger.info('New set after adding a value: {}'.format(set_of_number))
        
        return 'Add'
    
    elif remove_value is not None:
        set_of_number.discard(remove_value)
        logger.info('New set after removing a value: {}'.format(set_of_number))
        
        return 'Remove'
    
    
def union_intersection_in_set(set_of_number_1, set_of_number_2, u_i):
    if u_i == 'Union':
        new_set_union = set_of_number_1 | set_of_number_2
        logger.info('New Set after union: {}'.format(new_set_union))
        
        return 'Union'
    
    elif u_i == 'Intersection':
        new_set_intersection = set_of_number_1 & set_of_number_2
        logger.info('New Set after intersection: {}'.format(new_set_intersection))
        
        return 'Intersection'
    
    else:
        logger.info('No operation is passed')
        return None
    
    
def difference_compare_in_set(set_of_number_1, set_of_number_2, u_i):
    if u_i == 'Difference':
        new_set = set_of_number_1 - set_of_number_2
        logger.info('New Set after Difference: {}'.format(new_set))
        
        return 'Difference'
    
    elif u_i == 'Compare':
        if (set_of_number_1 <= set_of_number_2):
            logger.info('Subset')
            
            return 'Subset'
        else:
            logger.info('Superset')
            
            return 'Superset'
    
    else:
        logger.info('No operation is passed')
        return None
    
            
        
=======
"""
{} - this is an empty dict, but
{0, 1} - this is a set; 0, 1 are elements
set() - to define an empty set
"""


# return new set containing common and uncommon items between set_a and set_b
def find_union(set_a, set_b) -> set:
    new_set = set_a
    for item in set_b:
        new_set.add(item)

    return new_set


# return a new set containing common items between set_a & set_b
def find_intersection(set_a, set_b) -> set:
    new_set = set()
    for item in set_a:
        if item in set_b:
            new_set.add(item)

    return new_set


# return True of self.set is disjoint with set_b
def find_disjoint(set_a, set_b) -> bool:
    for item in set_a:
        if item in set_b:
            return False

    return True


# return a new set containing only items of set_a that are not in set_b
def find_differences(set_a, set_b) -> set:
    new_set = set()
    for item in set_a:
        if item not in set_b:
            new_set.add(item)

    return new_set


# return True if set_a is subset of set_b
def find_subsets(set_a, set_b) -> bool:
    for item in set_a:
        if item not in set_b:
            return False

    return True


# return True if set_a is superset of set_b
def find_supersets(set_a, set_b) -> bool:
    for item in set_b:
        if item not in set_a:
            return False

    return True
>>>>>>> ce0055878cd154249e92bfc24019a31b879491d6
