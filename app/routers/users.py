# app/routers/users.py:

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    """Create a new user"""
    return await crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Get a user by ID"""
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[schemas.User])
async def read_users(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    """Get a list of users"""
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users


@router.put("/{user_id}", response_model=schemas.User)
async def update_user(
    user_id: int, user: schemas.UserUpdate, db: AsyncSession = Depends(get_db)
):
    """Update a user by ID"""
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.update_user(db=db, db_user=db_user, user=user)


@router.delete("/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a user by ID"""
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.delete_user(db=db, user_id=user_id)
