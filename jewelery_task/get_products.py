import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_products():
    """Fetch product data from MockAPI using URL from environment variables."""
    url = os.getenv("MOCKAPI_URL")
    if not url:
        return "Error: MOCKAPI_URL not found in environment variables."

    try:
        response = requests.get(f"{url}", timeout=15)  # f-string kullanıyoruz
        response.raise_for_status()  # HTTP hatalarını yakalar

        products = response.json()
        # id varsa kaldır
        for product in products:
            product.pop("id", None)

        return products

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"