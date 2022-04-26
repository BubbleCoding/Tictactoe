#TODO make a class or enum out of field

from enum import IntEnum, unique

@unique
class Field(IntEnum):
    O = 0
    X = 1
