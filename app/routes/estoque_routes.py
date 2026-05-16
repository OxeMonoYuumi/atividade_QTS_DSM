from flask import Blueprint, request, jsonify
from app.services.estoque_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)

product_bp = Blueprint("products", __name__, url_prefix="/products")


@product_bp.route("", methods=["GET"])
def list_products():
    return jsonify(get_all_products()), 200


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = get_product_by_id(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200


@product_bp.route("", methods=["POST"])
def create():
    data = request.get_json()

    if not data or "name" not in data or "quantity" not in data:
        return jsonify({"error": "name and quantity are required"}), 400

    product = create_product(data)

    if product is None:
        return jsonify({"error": "Product already exists"}), 400

    return jsonify(product), 201


@product_bp.route("/<int:product_id>", methods=["PUT"])
def update(product_id):
    data = request.get_json()

    if not data or "name" not in data or "quantity" not in data:
        return jsonify({"error": "name and quantity are required"}), 400

    product = update_product(product_id, data)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200


@product_bp.route("/<int:product_id>", methods=["DELETE"])
def delete(product_id):
    product = get_product_by_id(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    delete_product(product_id)

    return "", 204
