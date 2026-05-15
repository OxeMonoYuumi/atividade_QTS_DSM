import pytest
from app.services.user_service import users


@pytest.fixture(autouse=True)
def clear_users():
    users.clear()
