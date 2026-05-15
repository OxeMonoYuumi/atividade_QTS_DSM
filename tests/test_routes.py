import pytest
from app import create_app

# def test_health_check():
#     app = create_app()
#     client = app.test_client()

#     response = client.get("/status")

#     assert response.status_code == 200
#     assert response.get_json() == {"Status": "OK"}

# def test_hello():
#     app = create_app()
#     client = app.test_client()

#     response = client.get("/hello")

#     assert response.status_code == 200
#     assert response.get_json() == {"message":"Hello World"}


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_create_user_success(client):
    response = client.post("/users", json={"name": "Pedro"})

    assert response.status_code == 201
    assert response.get_json()["name"] == "Pedro"


def test_create_user_without_name(client):
    response = client.post("/users", json={})

    assert response.status_code == 400
    assert "name is required" in str(response.data)


def test_get_users(client):
    client.post("/users", json={"name": "Teste"})

    response = client.get("/users/1")

    assert response.status_code == 200


def test_user_not_found(client):
    response = client.get("/users/999")

    assert response.status_code == 404
    assert "User not found" in str(response.data)


def test_delete_user(client):
    client.post("/users", json={"name": "Delete"})

    response = client.delete("/users/1")

    assert response.status_code == 204


def test_update_user(client):
    # 1 - Criar usuário
    response = client.post("/users", json={"name": "Pedro"})
    assert response.status_code == 201

    user_id = response.get_json()["id"]

    # 2 - Atualizar usuário
    response = client.put(f"/users/{user_id}", json={"name": "Novo Nome"})

    assert response.status_code == 200
    assert response.get_json()["name"] == "Novo Nome"
