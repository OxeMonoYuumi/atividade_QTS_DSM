import pytest
from app import create_app
from app.services import estoque_service


@pytest.fixture
def client():
    app = create_app()

    estoque_service.products.clear()
    estoque_service.current_id = 1

    return app.test_client()


def test_should_create_product(client):
    response = client.post("/products", json={"name": "Notebook", "quantity": 10})

    data = response.get_json()

    assert response.status_code == 201
    assert data["id"] == 1
    assert data["name"] == "Notebook"
    assert data["quantity"] == 10


def test_should_get_product_by_id(client):
    create_response = client.post("/products", json={"name": "Mouse", "quantity": 20})

    product = create_response.get_json()

    response = client.get(f"/products/{product['id']}")

    data = response.get_json()

    assert response.status_code == 200
    assert data["name"] == "Mouse"
    assert data["quantity"] == 20


def test_should_update_product(client):
    create_response = client.post("/products", json={"name": "Teclado", "quantity": 15})

    product = create_response.get_json()

    response = client.put(
        f"/products/{product['id']}", json={"name": "Teclado Mecânico", "quantity": 8}
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data["name"] == "Teclado Mecânico"
    assert data["quantity"] == 8


def test_should_delete_product(client):
    create_response = client.post("/products", json={"name": "Monitor", "quantity": 5})

    product = create_response.get_json()

    delete_response = client.delete(f"/products/{product['id']}")

    assert delete_response.status_code == 204

    get_response = client.get(f"/products/{product['id']}")

    assert get_response.status_code == 404


def test_should_return_400_when_product_already_exists(client):
    client.post("/products", json={"name": "Headset", "quantity": 7})

    response = client.post("/products", json={"name": "Headset", "quantity": 3})

    assert response.status_code == 400
