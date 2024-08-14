import pytest


@pytest.mark.asyncio
async def test_read_users(async_client):
    """Test the /users endpoint"""
    response = await async_client.get("/users")
    assert response.status_code == 200
    assert isinstance(
        response.json(), list
    )  # Предполагаем, что /users возвращает список


@pytest.mark.asyncio
async def test_create_user(async_client):
    """Test creating a user"""
    new_user = {"username": "testuser", "email": "testuser@example.com"}
    response = await async_client.post("/users", json=new_user)
    assert response.status_code == 201
    assert response.json()["username"] == new_user["username"]
    assert response.json()["email"] == new_user["email"]


@pytest.mark.asyncio
async def test_read_user(async_client):
    """Test reading a single user by ID"""
    user_id = 1  # Предполагаем, что такой пользователь существует в базе данных
    response = await async_client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert "username" in response.json()
    assert "email" in response.json()


@pytest.mark.asyncio
async def test_update_user(async_client):
    """Test updating a user"""
    user_id = 1  # Предполагаем, что такой пользователь существует в базе данных
    updated_data = {"username": "updateduser", "email": "updateduser@example.com"}
    response = await async_client.put(f"/users/{user_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["username"] == updated_data["username"]
    assert response.json()["email"] == updated_data["email"]


@pytest.mark.asyncio
async def test_delete_user(async_client):
    """Test deleting a user"""
    user_id = 1  # Предполагаем, что такой пользователь существует в базе данных
    response = await async_client.delete(f"/users/{user_id}")
    assert response.status_code == 204
