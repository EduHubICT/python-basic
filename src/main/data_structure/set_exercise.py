from src.main.logger.py_logger import PyLogger


logger = PyLogger.get_configured_logger()


def create_unique_value(list_of_number):
    unique_values = set(list_of_number)

    logger.info('Unique value representation: {}'.format(unique_values))

    return unique_values