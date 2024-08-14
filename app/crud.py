from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas

# Пользователи


async def get_user(db: AsyncSession, user_id: int):
    """Get a user by ID"""
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    return result.scalars().first()


async def create_user(db: AsyncSession, user: schemas.UserCreate):
    """Create a new user"""
    db_user = models.User(
        username=user.username, email=user.email, hashed_password=user.password
    )  # В реальном приложении хэшируйте пароль
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    """Get a list of users"""
    result = await db.execute(select(models.User).offset(skip).limit(limit))
    return result.scalars().all()


async def update_user(db: AsyncSession, user_id: int, user_update: schemas.UserUpdate):
    """Update an existing user"""
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    return None


async def delete_user(db: AsyncSession, user_id: int):
    """Delete a user by ID"""
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        await db.delete(db_user)
        await db.commit()
        return True
    return False


# Элементы


async def get_item(db: AsyncSession, item_id: int):
    """Get an item by ID"""
    result = await db.execute(select(models.Item).filter(models.Item.id == item_id))
    return result.scalars().first()


async def create_item(db: AsyncSession, item: schemas.ItemCreate):
    """Create a new item"""
    db_item = models.Item(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def get_items(db: AsyncSession, skip: int = 0, limit: int = 10):
    """Get a list of items"""
    result = await db.execute(select(models.Item).offset(skip).limit(limit))
    return result.scalars().all()


async def update_item(db: AsyncSession, item_id: int, item_update: schemas.ItemUpdate):
    """Update an existing item"""
    result = await db.execute(select(models.Item).filter(models.Item.id == item_id))
    db_item = result.scalars().first()
    if db_item:
        for key, value in item_update.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
        return db_item
    return None


async def delete_item(db: AsyncSession, item_id: int):
    """Delete an item by ID"""
    result = await db.execute(select(models.Item).filter(models.Item.id == item_id))
    db_item = result.scalars().first()
    if db_item:
        await db.delete(db_item)
        await db.commit()
        return True
    return False


async def get_item_by_title(db: AsyncSession, title: str):
    """Get an item by title"""
    result = await db.execute(select(models.Item).filter(models.Item.title == title))
    return result.scalars().first()
