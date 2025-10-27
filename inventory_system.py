"""
Inventory Management System

Provides functions to manage an inventory of items, including adding,
removing, checking quantities, and saving/loading data from a JSON file.
"""

import json
from datetime import datetime


def add_item(stock, item="default", qty=0, logs=None):
    """Add or update an item in the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        raise ValueError("Invalid types: item must be str, qty must be int")

    stock[item] = stock.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return stock, logs


def remove_item(stock, item, qty):
    """Remove a quantity of an item from the inventory."""
    if item not in stock:
        print(f"Warning: Tried to remove non-existent item '{item}'")
        return stock
    if not isinstance(qty, int):
        print(f"Invalid qty type for {item}, must be int")
        return stock

    stock[item] -= qty
    if stock[item] <= 0:
        del stock[item]
    return stock


def get_qty(stock, item):
    """Return the quantity of an item in the inventory."""
    return stock.get(item, 0)


def check_low_items(stock, threshold=5):
    """Return a list of items with quantity below the threshold."""
    return [item for item, qty in stock.items() if qty < threshold]


def save_data(stock, file_name="inventory.json"):
    """Save the inventory data to a JSON file."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(stock, file, indent=4)
    except OSError as error:
        print(f"Error saving inventory: {error}")


def load_data(file_name="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def print_data(stock):
    """Print all items and their quantities."""
    print("Items Report:")
    for item, qty in stock.items():
        print(f"{item} -> {qty}")


def main():
    """Main function demonstrating inventory operations."""
    logs = []
    stock = {}

    try:
        stock, logs = add_item(stock, "apple", 10, logs)
        stock, logs = add_item(stock, "banana", -2, logs)
        stock, logs = add_item(stock, 123, "ten", logs)
    except ValueError as err:
        print(f"Input error: {err}")

    stock = remove_item(stock, "apple", 3)
    stock = remove_item(stock, "orange", 1)

    print("Apple stock:", get_qty(stock, "apple"))
    print("Low items:", check_low_items(stock))

    save_data(stock)
    stock = load_data()
    print_data(stock)

    print("Eval removed for safety.")


if __name__ == "__main__":
    main()
