"""Calculates the prices."""


def calculate_price(product, gold_price):
    """
    Calculate the product price based on the formula:
    Price = (popularityScore + 1) * weight * goldPrice
    """
    try:
        popularity = float(product.get("popularityScore", 0))
    except (ValueError, TypeError):
        popularity = 0.0
    try:
        weight = float(product.get("weight", 0))
    except (ValueError, TypeError):
        weight = 0.0
    try:
        gold_price = float(gold_price)
    except (ValueError, TypeError):
        gold_price = 1.0

    price = (popularity + 1) * weight * gold_price
    return round(price, 2)  # USD with 2 decimals


def convert_popularity_to_5star(popularity):
    """Convert 0-100 popularity score to 0-5 scale with 1 decimal."""
    try:
        popularity = float(popularity)
    except (ValueError, TypeError):
        popularity = 0.0

    return round(popularity * 5, 1)
