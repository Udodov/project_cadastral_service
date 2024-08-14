import pytest


@pytest.mark.asyncio
async def test_read_items(async_client):
    """Test the /items endpoint"""
    response = await async_client.get("/items")
    assert response.status_code == 200
    assert isinstance(
        response.json(), list
    )  # Предполагаем, что /items возвращает список


@pytest.mark.asyncio
async def test_create_item(async_client):
    """Test creating an item"""
    new_item = {"name": "testitem", "description": "A test item"}
    response = await async_client.post("/items", json=new_item)
    assert response.status_code == 201
    assert response.json()["name"] == new_item["name"]
    assert response.json()["description"] == new_item["description"]


@pytest.mark.asyncio
async def test_read_item(async_client):
    """Test reading a single item by ID"""
    item_id = 1  # Предполагаем, что такой элемент существует в базе данных
    response = await async_client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "description" in response.json()


@pytest.mark.asyncio
async def test_update_item(async_client):
    """Test updating an item"""
    item_id = 1  # Предполагаем, что такой элемент существует в базе данных
    updated_data = {"name": "updateditem", "description": "An updated test item"}
    response = await async_client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]
    assert response.json()["description"] == updated_data["description"]


@pytest.mark.asyncio
async def test_delete_item(async_client):
    """Test deleting an item"""
    item_id = 1  # Предполагаем, что такой элемент существует в базе данных
    response = await async_client.delete(f"/items/{item_id}")
    assert response.status_code == 204
