import pytest
from flask import Flask

from app.routes.math_routes import math_bp


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(math_bp)

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_sum_success(client):
    response = client.post("/math/sum", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert response.get_json() == {"operation": "sum", "result": 15}


def test_sum_missing_fields(client):
    response = client.post("/math/sum", json={"a": 10})

    assert response.status_code == 400
    assert response.get_json() == {"error": "a and b are required"}


def test_subtract_success(client):
    response = client.post("/math/subtract", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert response.get_json() == {"operation": "subtract", "result": 5}


def test_subtract_missing_fields(client):
    response = client.post("/math/subtract", json={"a": 10})

    assert response.status_code == 400
    assert response.get_json() == {"error": "a and b are required"}


def test_multiply_success(client):
    response = client.post("/math/multiply", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert response.get_json() == {"operation": "multiply", "result": 50}


def test_multiply_missing_fields(client):
    response = client.post("/math/multiply", json={"a": 10})

    assert response.status_code == 400
    assert response.get_json() == {"error": "a and b are required"}


def test_divide_success(client):
    response = client.post("/math/divide", json={"a": 10, "b": 2})

    assert response.status_code == 200
    assert response.get_json() == {"operation": "divide", "result": 5.0}


def test_divide_by_zero(client):
    response = client.post("/math/divide", json={"a": 10, "b": 0})

    assert response.status_code == 400
    assert response.get_json() == {"error": "division by zero"}


def test_power_success(client):
    response = client.post("/math/power", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.get_json() == {"operation": "power", "result": 8}


def test_power_missing_fields(client):
    response = client.post("/math/power", json={"a": 2})

    assert response.status_code == 400
    assert response.get_json() == {"error": "a and b are required"}
