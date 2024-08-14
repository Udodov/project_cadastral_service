from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    """Base user schema"""

    username: str
    email: EmailStr


class UserCreate(UserBase):
    """User creation schema"""

    password: str


class UserUpdate(UserBase):
    """User update schema"""

    password: Optional[str] = None


class User(UserBase):
    """User response schema"""

    id: int
    is_active: bool

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    """Base item schema"""

    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """Item creation schema"""

    pass


class ItemUpdate(BaseModel):
    """Item update schema"""

    title: Optional[str] = None
    description: Optional[str] = None


class Item(ItemBase):
    """Item response schema"""

    id: int
    owner_id: int

    class Config:
        orm_mode = True


class QueryHistory(BaseModel):
    """Query history schema"""

    id: int
    content: str
    result: Optional[str]
    timestamp: datetime

    class Config:
        orm_mode = True


# Убедимся, что объекты datetime соответствуют часовому поясу
def ensure_aware(dt: datetime) -> datetime:
    if dt.tzinfo is None:  # Проверяем, есть ли информация о часовом поясе
        return dt.replace(tzinfo=timezone.utc)  # Если нет, добавляем временную зону UTC
    return dt  # Если есть, возвращаем объект без изменений
