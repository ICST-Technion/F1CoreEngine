from enum import Enum


# return values for your functions
class ReturnValue(Enum):
    OK = 0
    NOT_EXISTS = 1
    ALREADY_EXISTS = 2
    ERROR = 3
    BAD_PARAMS = 4
