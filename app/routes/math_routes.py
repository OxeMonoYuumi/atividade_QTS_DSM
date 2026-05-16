from flask import Blueprint, request, jsonify

math_bp = Blueprint("math", __name__, url_prefix="/math")


@math_bp.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    if "a" not in data or "b" not in data:
        return jsonify({"error": "a and b are required"}), 400

    result = data["a"] + data["b"]

    return jsonify({"operation": "sum", "result": result}), 200


@math_bp.route("/subtract", methods=["POST"])
def subtract_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    if "a" not in data or "b" not in data:
        return jsonify({"error": "a and b are required"}), 400

    result = data["a"] - data["b"]

    return jsonify({"operation": "subtract", "result": result}), 200


@math_bp.route("/multiply", methods=["POST"])
def multiply_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    if "a" not in data or "b" not in data:
        return jsonify({"error": "a and b are required"}), 400

    result = data["a"] * data["b"]

    return jsonify({"operation": "multiply", "result": result}), 200


@math_bp.route("/divide", methods=["POST"])
def divide_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    if "a" not in data or "b" not in data:
        return jsonify({"error": "a and b are required"}), 400

    if data["b"] == 0:
        return jsonify({"error": "division by zero"}), 400

    result = data["a"] / data["b"]

    return jsonify({"operation": "divide", "result": result}), 200


@math_bp.route("/power", methods=["POST"])
def power_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    if "a" not in data or "b" not in data:
        return jsonify({"error": "a and b are required"}), 400

    result = data["a"] ** data["b"]

    return jsonify({"operation": "power", "result": result}), 200
