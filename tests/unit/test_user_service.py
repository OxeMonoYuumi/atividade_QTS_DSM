def test_should_not_allow_duplicate_users():
    from app.services import user_service

    user_service.users.clear()
    user_service.current_id = 1

    user_service.create_user({"name": "Pedro"})

    user = user_service.create_user({"name": "Pedro"})

    assert user is None
