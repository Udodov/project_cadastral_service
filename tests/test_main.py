import pytest


@pytest.mark.asyncio
async def test_ping(async_client):
    """Test the /ping endpoint"""
    response = await async_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_create_query(async_client):
    """Test creating a query"""
    new_query = {"field1": "value1", "field2": "value2"}
    response = await async_client.post("/query", json=new_query)
    assert response.status_code == 201
    assert response.json()["field1"] == new_query["field1"]
    assert response.json()["field2"] == new_query["field2"]


@pytest.mark.asyncio
async def test_get_result(async_client):
    """Test getting a result"""
    query_id = 1  # Предполагаем, что такой запрос существует в базе данных
    response = await async_client.get(f"/result/{query_id}")
    assert response.status_code == 200
    assert "result" in response.json()
