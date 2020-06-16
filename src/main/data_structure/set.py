from src.main.logger.py_logger import PyLogger


logger = PyLogger.get_configured_logger()

def set_unique_value_from_list(list_of_number):
    unique_number = list_of_number
    
    logger.info(unique_number)
    
    return unique_number


def set_unique_value_from_list1(list_of_number):
    unique_number = set(list_of_number)
    
    logger.info(unique_number)
    
    return unique_number