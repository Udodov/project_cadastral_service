from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models, schemas
from typing import List
from sqlalchemy.future import select
import httpx

router = APIRouter(tags=["service"])


@router.post("/query")
async def receive_query(query: str, db: AsyncSession = Depends(get_db)):
    """Receive a query and store it in the database"""
    new_query = models.Query(content=query)
    db.add(new_query)
    await db.commit()
    await db.refresh(new_query)

    # Здесь вы обычно обрабатываете запрос и отправляете его во внешнюю службу
    # Для демонстрации мы просто вернем идентификатор запроса
    return {"query_id": new_query.id}


@router.post("/result")
async def send_result(result: str, query_id: int, db: AsyncSession = Depends(get_db)):
    """Receive a result for a specific query"""
    query = await db.get(models.Query, query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")

    query.result = result
    await db.commit()
    return {"status": "Result received and stored"}


@router.get("/history", response_model=List[schemas.QueryHistory])
async def get_history(db: AsyncSession = Depends(get_db)):
    """Get the history of queries"""
    result = await db.execute(select(models.Query))
    queries = result.scalars().all()
    return queries
