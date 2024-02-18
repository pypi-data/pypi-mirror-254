from typing import Optional
from .code_type import code_type


class code:
    """
    This class represents a code with a hash, type, shop name, and value.
    """
    def __init__(self, hash: str, code_type: code_type, shop_name: str, value: Optional[str] = None, min_spend: Optional[str] = None):
        """
        Initialize a new instance of the Code class.

        Args:
            hash (str): The hash of the code.
            code_type (code_type): The type of the code.
            shop_name (str): The name of the shop.
            value (Optional[str]): The value of the code. Defaults to None.
            min_spend (Optional[str]): The minimum spend of the code. Defaults to None.
        """
        self.hash = hash
        self.code_type = code_type
        self.shop_name = shop_name
        self.value = value
        self.min_spend = min_spend

    def to_dict(self) -> dict:
        """
        Convert the Code object to a dictionary.

        Returns:
            data (dict): A dictionary representation of the Code object.
        """
        data = {
            "Hash": self.hash,
            "CodeType": self.code_type.value,
            "ShopName": self.shop_name,
            "Value": self.value,
            "MinSpend": self.min_spend,
        }

        return data

    def __dict__(self):
        return self.to_dict()

