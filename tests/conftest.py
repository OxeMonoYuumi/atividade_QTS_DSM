import pytest
import app.services.user_service as user_service

@pytest.fixture(autouse=True)
def clear_users():
    user_service.users.clear()
    user_service.current_id = 1