import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Item, Query
from app.database import get_db
from sqlalchemy.future import select


@pytest.mark.asyncio
async def test_create_user(setup_test_db):
    async with get_db() as session:
        async with session.begin():
            user = User(
                username="testuser",
                email="testuser@example.com",
                hashed_password="hashedpassword",
            )
            session.add(user)
        await session.commit()

        result = await session.execute(select(User).filter_by(username="testuser"))
        user_from_db = result.scalars().first()

        assert user_from_db is not None
        assert user_from_db.username == "testuser"
        assert user_from_db.email == "testuser@example.com"


@pytest.mark.asyncio
async def test_create_item(setup_test_db):
    async with get_db() as session:
        async with session.begin():
            user = User(
                username="itemowner",
                email="itemowner@example.com",
                hashed_password="hashedpassword",
            )
            session.add(user)
            await session.flush()  # Ensure user is added and we have an ID for the foreign key

            item = Item(title="Test Item", description="A test item", owner_id=user.id)
            session.add(item)
        await session.commit()

        result = await session.execute(select(Item).filter_by(title="Test Item"))
        item_from_db = result.scalars().first()

        assert item_from_db is not None
        assert item_from_db.title == "Test Item"
        assert item_from_db.description == "A test item"
        assert item_from_db.owner_id == user.id


@pytest.mark.asyncio
async def test_create_query(setup_test_db):
    async with get_db() as session:
        async with session.begin():
            query = Query(content="SELECT * FROM users", result=None)
            session.add(query)
        await session.commit()

        result = await session.execute(
            select(Query).filter_by(content="SELECT * FROM users")
        )
        query_from_db = result.scalars().first()

        assert query_from_db is not None
        assert query_from_db.content == "SELECT * FROM users"
        assert query_from_db.result is None
