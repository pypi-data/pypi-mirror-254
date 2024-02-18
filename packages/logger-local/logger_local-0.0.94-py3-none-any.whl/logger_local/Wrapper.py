from functools import wraps

from .Logger import Logger


# TODO: do we use it anywhere?
def log_function_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger_local = Logger.create_logger(**kwargs)
        object1 = {
            'args': str(args),
            'kwargs': str(kwargs),
        }
        logger_local.start(object=object1)
        result = func(*args, **kwargs)  # Execute the function
        object2 = {
            'result': result,
        }
        logger_local.end(object=object2)
        return result

    return wrapper
