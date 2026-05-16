import pytest
from app import create_app
from app.services import estoque_service


@pytest.fixture
def client():
    app = create_app()

    estoque_service.products.clear()
    estoque_service.current_id = 1

    return app.test_client()


def test_product_flow(client):
    # 1. Criar produto
    response = client.post(
        "/products",
        json={
            "name": "Notebook",
            "quantity": 10
        }
    )

    assert response.status_code == 201

    product = response.get_json()
    product_id = product["id"]

    # 2. Buscar produto
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200

    # 3. Atualizar produto
    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Notebook Gamer",
            "quantity": 5
        }
    )

    assert response.status_code == 200

    updated_product = response.get_json()

    assert updated_product["name"] == "Notebook Gamer"
    assert updated_product["quantity"] == 5

    # 4. Deletar produto
    response = client.delete(f"/products/{product_id}")

    assert response.status_code == 204

    # 5. Garantir que foi removido
    response = client.get(f"/products/{product_id}")

    assert response.status_code == 404


def test_list_products(client):
    client.post(
        "/products",
        json={
            "name": "Mouse",
            "quantity": 20
        }
    )

    client.post(
        "/products",
        json={
            "name": "Teclado",
            "quantity": 15
        }
    )

    response = client.get("/products")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2


def test_create_3_new_products_and_list(client):
    client.post(
        "/products",
        json={
            "name": "Monitor",
            "quantity": 8
        }
    )

    client.post(
        "/products",
        json={
            "name": "Headset",
            "quantity": 12
        }
    )

    client.post(
        "/products",
        json={
            "name": "Webcam",
            "quantity": 6
        }
    )

    response = client.get("/products")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 3


def test_should_return_400_when_product_already_exists(client):
    client.post(
        "/products",
        json={
            "name": "Notebook",
            "quantity": 10
        }
    )

    response = client.post(
        "/products",
        json={
            "name": "Notebook",
            "quantity": 5
        }
    )

    assert response.status_code == 400


def test_should_update_product_quantity(client):
    response = client.post(
        "/products",
        json={
            "name": "Impressora",
            "quantity": 3
        }
    )

    product = response.get_json()
    product_id = product["id"]

    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Impressora",
            "quantity": 7
        }
    )

    assert response.status_code == 200

    updated_product = response.get_json()

    assert updated_product["quantity"] == 7