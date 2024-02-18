import inspect
import sys
from functools import wraps

from .LoggerLocal import Logger


class MetaLogger(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        """This method is called before the class is created. It is used to create the class namespace."""
        return super().__prepare__(name, bases, **kwargs)

    def __new__(cls, name, bases, dct, **kwargs):
        logger = Logger.create_logger(**kwargs)
        dct['logger'] = logger
        for key, value in dct.items():
            if callable(value) and not key.endswith("__"):  # Exclude magic methods
                dct[key] = cls.wrap_function(value, logger)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def wrap_function(func, logger):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Obtain the module name of the wrapped function
            function_module = getattr(func, '__module__', None) or func.__globals__.get('__name__', 'unknown_module')
            function_name = f"{function_module}.{func.__name__}"

            signature = inspect.signature(func)
            arg_names = [param.name for param in signature.parameters.values()]
            if len(args) + len(kwargs) == len(arg_names) + 1:  # staticmethod called with class instance
                args = args[1:]

            kwargs_updated = {**dict(zip(arg_names, args)), **kwargs}
            logger.start(function_name, object=kwargs_updated)
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as exception:
                # Use traceback to capture frame information
                # Use sys.exc_info() to get exception information
                exc_type, exc_value, exc_traceback = sys.exc_info()
                # Extract the frame information from the traceback
                frame = exc_traceback.tb_next.tb_frame
                # Get the local variables
                locals_before_exception = frame.f_locals

                logger.error(function_name,
                             object={"exception": exception, "locals_before_exception": locals_before_exception})
                raise exception
            finally:
                logger.end(function_name, object={"result": result})
            return result

        return wrapper
