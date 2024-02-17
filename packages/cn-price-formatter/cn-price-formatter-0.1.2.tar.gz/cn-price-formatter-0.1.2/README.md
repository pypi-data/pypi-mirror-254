# PriceFormatter Package

This package provides a PriceFormatter class for handling and formatting hotel pricing data.

## Installation

You can install the package using pip:

```bash
pip install cn-price-formatter


from my_package.price_formatter import PriceFormatter

# Example usage
formatter = PriceFormatter()
formatter.hotel_planner(json_data)
total_price_before_tax = formatter.get_total_price_before_tax()

