from enum import Enum

class CodeType(Enum):
    """
    This class is an enumeration that represents different types of codes.

    Attributes:
        EarlyAccess (int): Represents an early access code.
        StoreCredit (int): Represents a store credit code.
        Discount (int): Represents a discount code.
        FreeShipping (int): Represents a free shipping code.
    """
    EarlyAccess = 1
    StoreCredit = 2
    Discount = 3
    FreeShipping = 4