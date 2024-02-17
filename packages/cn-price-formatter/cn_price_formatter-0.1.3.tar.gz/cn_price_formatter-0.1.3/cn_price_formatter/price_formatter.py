import json
from collections import defaultdict

class PriceFormatter:
    """
    PriceFormatter class for handling and formatting hotel pricing data.
    """

    def __init__(self):
        """
        Initializes PriceFormatter with default values for various pricing attributes.
        """
        self.total_price_before_tax = 0
        self.total_price_after_tax = 0
        self.avg_price_before_tax = 0
        self.avg_price_after_tax = 0
        self.total_tax = 0
        self.total_tax_rate = 0
        self.rooms_available = 0
        self.room_count = 0
        self.pay_now = 0
        self.cn_fee = 6

    def hotel_planner(self, json_data):
        """
        Parses and sets class variables based on hotel planner JSON data.

        Args:
            json_data (str): JSON data containing hotel pricing information.
        """
        # Validate if json_data is a string
        if not isinstance(json_data, str):
            raise ValueError("Invalid input: json_data must be a string.")

        try:
            data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")

        # Validate the structure of the JSON data
        if not isinstance(data, list) or not data:
            raise ValueError("Invalid JSON structure: Expecting a non-empty list.")

         # Validate the presence of required keys in the JSON data
        required_keys = ['totalBeforeTax', 'totalAfterTax', 'averageBeforeTax', 'averageAfterTax',
                        'totalTaxRate', 'roomsAvailable', 'roomCount', 'payNow']

        for key in required_keys:
            if key not in data[0]:
                raise ValueError(f"Missing key '{key}' in the JSON data.")

        

         # Validate numeric values
        numeric_keys = ['totalBeforeTax', 'totalAfterTax', 'averageBeforeTax', 'averageAfterTax',
                        'totalTaxRate', 'roomsAvailable', 'roomCount', 'payNow']

        for key in numeric_keys:
            if not isinstance(data[0][key], (int, float)):
                raise ValueError(f"Invalid value for '{key}': Expecting a numeric value.")

        self.cn_fee = 6
        self.total_price_before_tax = data[0]['totalBeforeTax']
        self.total_price_after_tax = data[0]['totalAfterTax']
        self.avg_price_before_tax = data[0]['averageBeforeTax']
        self.avg_price_after_tax = data[0]['averageAfterTax']
        self.total_tax = float(self.total_price_after_tax) - float(self.total_price_before_tax)
        self.total_tax_rate = data[0]['totalTaxRate']

        self.rooms_available = data[0]['roomsAvailable']

        self.room_count = data[0]['roomCount']
        self.pay_now = data[0]['payNow']

    def hp_get_room_date_wise(self, json_data):
        """
        Parses and organizes room data by effectiveDate from hotel planner JSON data.

        Args:
            json_data (str): JSON data containing hotel room pricing information.
        """
        data = json.loads(json_data)

        # Organize data by effectiveDate
        effective_dates_data = defaultdict(lambda: {"totalBeforeTax": [], "totalAfterTax": []})

        for rate in data[0]["rates"]:
            effective_date = rate["effectiveDate"]
            effective_dates_data[effective_date]["totalBeforeTax"].append(rate["totalBeforeTax"])
            effective_dates_data[effective_date]["totalAfterTax"].append(rate["totalAfterTax"])

    def get_total_price_before_tax(self) -> float:
        """
        Returns the total price before tax.

        Returns:
            float: Total price before tax.
        """
        # Validate that total_price_before_tax is a numeric value
        if not isinstance(self.total_price_before_tax, (int, float)):
            raise ValueError("Invalid value for total_price_before_tax: Expecting a numeric value.")
        return self.total_price_before_tax

    def get_total_price_after_tax(self) -> float:
        """
        Returns the total price after tax.

        Returns:
            float: Total price after tax.
        """
        # Validate that total_price_after_tax is a numeric value
        if not isinstance(self.total_price_after_tax, (int, float)):
            raise ValueError("Invalid value for total_price_after_tax: Expecting a numeric value.")
        return self.total_price_after_tax

    def get_avg_price_before_tax(self) -> float:
        """
        Returns the average price before tax.

        Returns:
            float: Average price before tax.
        """
        # Validate that avg_price_before_tax is a numeric value
        if not isinstance(self.avg_price_before_tax, (int, float)):
            raise ValueError("Invalid value for avg_price_before_tax: Expecting a numeric value.")
        return self.avg_price_before_tax

    def get_avg_price_after_tax(self) -> float:
        """
        Returns the average price after tax.

        Returns:
            float: Average price after tax.
        """
        # Validate that avg_price_after_tax is a numeric value
        if not isinstance(self.avg_price_after_tax, (int, float)):
            raise ValueError("Invalid value for avg_price_after_tax: Expecting a numeric value.")
        return self.avg_price_after_tax

    def get_total_tax(self) -> float:
        """
        Returns the total tax amount.

        Returns:
            float: Total tax amount.
        """
        # Validate that total_tax is a numeric value
        if not isinstance(self.total_tax, (int, float)):
            raise ValueError("Invalid value for total_tax: Expecting a numeric value.")
        return self.total_tax

    def get_total_cn_fee(self) -> float:
        """
        Returns the total CN fee based on the total price after tax and CN fee percentage.

        Returns:
            float: Total CN fee.
        """
        # Validate that total_price_after_tax and cn_fee are numeric values
        if not isinstance(self.total_price_after_tax, (int, float)):
            raise ValueError("Invalid value for total_price_after_tax: Expecting a numeric value.")
        if not isinstance(self.cn_fee, (int, float)):
            raise ValueError("Invalid value for cn_fee: Expecting a numeric value.")

        return (self.total_price_after_tax / 100) * self.cn_fee

