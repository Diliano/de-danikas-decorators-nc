import logging

logger = logging.getLogger(__name__)

def debug(func):
    def wrapper(*args, **kwargs):
        logger.debug(f"Function: '{func.__name__}'")
        logger.debug(f"Args: {list(args)}")
        logger.debug(f"Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"Return value: {result}")
        return result
    return wrapper