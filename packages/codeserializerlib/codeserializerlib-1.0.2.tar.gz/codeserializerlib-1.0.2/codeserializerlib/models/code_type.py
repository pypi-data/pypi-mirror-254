from enum import Enum

class code_type(Enum):
    """
    This class is an enumeration that represents different types of codes.

    Attributes:
        early_access (int): Represents an early access code.
        store_credit (int): Represents a store credit code.
        discount (int): Represents a discount code.
        free_shipping (int): Represents a free shipping code.
    """
    early_access = 1
    store_credit = 2
    discount = 3
    free_shipping = 4