from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item_by_title(db, title=item.title)
    if db_item:
        raise HTTPException(
            status_code=400, detail="Item with this title already exists"
        )
    return await crud.create_item(db=db, item=item)


@router.get("/", response_model=List[schemas.Item])
async def read_items(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    items = await crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_model=schemas.Item)
async def update_item(
    item_id: int, item: schemas.ItemUpdate, db: AsyncSession = Depends(get_db)
):
    db_item = await crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return await crud.update_item(db=db, item_id=item_id, item=item)


@router.delete("/{item_id}", response_model=schemas.Item)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return await crud.delete_item(db=db, item_id=item_id)
