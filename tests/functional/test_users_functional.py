import pytest
from app import create_app
from app.services import user_service


@pytest.fixture
def client():
    app = create_app()
    user_service.users.clear()
    user_service.current_id = 1

    return app.test_client()


def test_user_flow(client):
    # 1. Criar usuário
    response = client.post("/users", json={"name": "Pedro"})
    assert response.status_code == 201

    user = response.get_json()
    user_id = user["id"]

    # 2. Buscar usuário
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

    # 3. Atualizar usuário
    response = client.put(f"/users/{user_id}", json={"name": "Novo Nome"})
    assert response.status_code == 200
    assert response.get_json()["name"] == "Novo Nome"

    # 4. Deletar usuário
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    # 5. Garantir que foi removido
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404


def test_list_users(client):
    client.post("/users", json={"name": "User1"})
    client.post("/users", json={"name": "User2"})

    response = client.get("/users")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2


def test_create_3_new_users_and_list(client):
    client.post("/users", json={"name": "Rodrigo"})
    client.post("/users", json={"name": "Maylon"})
    client.post("/users", json={"name": "Rafael"})

    response = client.get("/users")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 3


def test_should_return_400_when_user_already_exists(client):
    client.post("/users", json={"name": "Pedro"})

    response = client.post("/users", json={"name": "Pedro"})

    assert response.status_code == 400
