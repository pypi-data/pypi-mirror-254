from enum import Enum

class label(Enum):
    """
    This class is an enumeration that represents different types of labels.

    Attributes:
        credit_amount (str): Represents a label for credit amount.
        credit_code (str): Represents a label for credit code.
        early_access_code (str): Represents a label for early access code.
        free_item (str): Represents a label for free item.
        free_item_code (str): Represents a label for free item code.
        free_shipping_code (str): Represents a label for free shipping code.
        minimum_order_value (str): Represents a label for minimum order value.
        percentage (str): Represents a label for percentage.
        percentage_code (str): Represents a label for percentage code.
        code_count (str): Represents a label for code count.
    """
    credit_amount = "credit_amount"
    credit_code = "credit_code"
    early_access_code = "early_access_code"
    free_item = "free_item"
    free_item_code = "free_item_code"
    free_shipping_code = "free_shipping_code"
    minimum_order_value = "minimum_order_value"
    percentage = "percentage"
    percentage_code = "percentage_code"
    code_count = "code_count"

__all__ = ['label']