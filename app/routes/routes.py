from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/status", methods=["GET"])
def health_check():
    return jsonify({"Status": "OK"})


@main.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World"})
