import asyncio
import random
from typing import List

from app.crud import (
    create_query,
    create_result,
    get_history,
    get_history_by_cadastral_number,
)
from app.database import get_db
from app.schemas import QuerySchema, ResultSchema, HistorySchema
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import httpx

from app.admin import create_admin_app
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Логика, выполняемая при старте приложения
    admin_app = await create_admin_app()
    app.mount("/admin", admin_app)

    yield

    # Логика, выполняемая при завершении приложения (если необходимо)
    # Например, закрытие подключений или освобождение ресурсов
    print("Приложение завершается. Освобождение ресурсов...")
    # Здесь можно добавить код для закрытия подключений к БД или другим ресурсам
    pass


app = FastAPI(
    title="Кадастровый сервис",
    description="API для работы с кадастровыми запросами",
    lifespan=lifespan,  # Указываем обработчик событий жизненного цикла
)


@app.post("/query", response_model=QuerySchema)
async def create_query_endpoint(query: QuerySchema, db: AsyncSession = Depends(get_db)):
    """Создание нового запроса"""
    db_query = await create_query(db, query)
    return db_query


@app.get("/result/{query_id}", response_model=ResultSchema)
async def get_result(query_id: int, db: AsyncSession = Depends(get_db)):
    """Получение результата запроса"""
    # Эмуляция внешнего сервера
    await asyncio.sleep(random.randint(1, 60))
    result = random.choice([True, False])
    db_result = await create_result(db, query_id, result)
    return db_result


@app.get("/ping")
async def ping():
    """Проверка работы сервера"""
    return {"status": "ok"}


@app.get("/history", response_model=List[HistorySchema])
async def get_history_endpoint(db: AsyncSession = Depends(get_db)):
    """Получение истории всех запросов"""
    history = await get_history(db)
    return history


@app.get("/history/{cadastral_number}", response_model=List[HistorySchema])
async def get_history_by_cadastral_number_endpoint(
    cadastral_number: str, db: AsyncSession = Depends(get_db)
):
    """Получение истории запросов по кадастровому номеру"""
    history = await get_history_by_cadastral_number(db, cadastral_number)
    return history


@app.get("/send-request")
async def send_request():
    """Отправка запроса ко второму сервису"""
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/emulate")
        return {"message": response.json()}
