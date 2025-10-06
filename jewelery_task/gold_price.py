import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()


def make_gprice_request():
    """Something to make pylint warning disappear."""
    api_key = os.getenv("GOLD_API_KEY")  # API key to dont expose it.
    if not api_key:
        return "Error: GOLD_API_KEY not found in environment variables."

    symbol = "XAU"  # Gold
    curr = "USD"
    date = ""  # gives the current price.

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"

    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data.get("price_gram_24k", 1.0))
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
