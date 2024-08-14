# Импорт нужных библиотек и компонентов
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db, SQLALCHEMY_DATABASE_URL

# URL для тестовой базы данных
TEST_SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://user:password@localhost/test_dbname"
)

# Создание асинхронного движка для тестовой базы данных
test_engine = create_async_engine(TEST_SQLALCHEMY_DATABASE_URL, echo=True)
TestSessionLocal = sessionmaker(
    bind=test_engine, class_=AsyncSession, expire_on_commit=False
)


@pytest.fixture(scope="session")
async def setup_test_db():
    async with test_engine.begin() as conn:
        # Создаем все таблицы в тестовой базе данных
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        # Удаляем все таблицы после завершения тестов
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def db_session(setup_test_db):
    async with TestSessionLocal() as session:
        yield session
        await session.rollback()  # Откатываем изменения после каждого теста


@pytest.fixture()
def override_get_db(db_session):
    async def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture(autouse=True)
def apply_override_get_db(override_get_db, monkeypatch):
    monkeypatch.setattr("app.database.get_db", override_get_db)
