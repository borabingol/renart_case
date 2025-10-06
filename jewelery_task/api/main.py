import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from gold_price import make_gprice_request
from get_products import get_products
from price_utils import calculate_price, convert_popularity_to_5star

app = Flask(__name__, static_folder="../static")  # static folder root'a göre
CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/products", methods=["GET"])
def products_endpoint():
    try:
        gold_price = make_gprice_request()
        products = get_products()

        min_price = request.args.get("min_price", type=float)
        max_price = request.args.get("max_price", type=float)
        min_pop = request.args.get("min_popularity", type=float)
        max_pop = request.args.get("max_popularity", type=float)

        result = []
        for p in products:
            price = calculate_price(p, gold_price)
            popularity_5star = convert_popularity_to_5star(p.get("popularityScore", 0))
            product_info = {
                "name": p.get("name"),
                "images": p.get("images", []),
                "weight": p.get("weight"),
                "popularityScore": popularity_5star,
                "price": price
            }
            result.append(product_info)

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serverless için export et
handler = app
