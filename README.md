# Project Cadastral Service

## Описание

Проект "Cadastral Service" — это веб-приложение, предназначенное для управления кадастровыми данными.<br>
Приложение построено на основе FastAPI и использует PostgreSQL в качестве базы данных.<br> Оно также включает в себя дополнительный внешний сервер.

## Структура проекта

project_cadastral_service/<br>
│<br>
├── app/<br>
│   ├── __init__.py<br>
│   ├── main.py<br>
│   ├── admin.py<br>
│   ├── models.py<br>
│   ├── schemas.py<br>
│   ├── database.py<br>
│   ├── crud.py<br>
│   ├── auth.py<br>
│   └── routers/<br>
│       ├── __init__.py<br>
│       ├── users.py<br>
│       └── items.py<br>
│<br>
├── tests/<br>
│   ├── __init__.py<br>
│   ├── conftest.py<br>
│   ├── test_main.py<br>
│   ├── test_users.py<br>
│   ├── test_models.py<br>
│   └── test_items.py<br>
│<br>
├── alembic/<br>
│   ├── versions/<br>
│   └── env.py<br>
│<br>
├── external_service/<br>
│   ├── __init__.py<br>
│   └── main.py<br>
│<br>
├── Dockerfile<br>
├── Dockerfile.external_service<br>
├── docker-compose.yml<br>
├── requirements.txt<br>
├── alembic.ini<br>
├── .dockerignore<br>
├── .gitignore<br>
└── README.md<br>

## Установка и запуск

### Предварительные требования

- Docker
- Docker Compose

### Шаги для запуска

1. Клонируйте репозиторий:

    
sh
    git clone https://github.com/Udodov/project_cadastral_service.git 
    cd project_cadastral_service   
    
2. Создайте файл .env в корневой директории проекта и добавьте необходимые переменные окружения:

    
env
    DATABASE_URL=postgresql+asyncpg://user:password@db/dbname   
    
 
3. Запустите контейнеры Docker:
 
    
sh
    docker-compose up --build
    
 
4. Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000), а внешний сервис — по адресу [http://localhost:8001](http://localhost:8001).

## Миграции базы данных

Для управления миграциями используется Alembic. Чтобы создать новую миграцию, выполните:

sh
alembic revision --autogenerate -m "описание миграции"
Чтобы применить миграции, выполните:

sh
alembic upgrade head
## Тестирование

Для запуска тестов используйте pytest. Убедитесь, что вы находитесь в корневой директории проекта и выполните:

sh
pytest
## Структура директорий

- app/: Основное приложение FastAPI.
  - main.py: Точка входа приложения.
  - admin.py: Административные функции.
  - models.py: Модели базы данных.
  - schemas.py: Схемы Pydantic.
  - database.py: Настройка базы данных.
  - crud.py: Операции CRUD.
  - auth.py: Аутентификация и авторизация.
  - routers/: Маршруты приложения.
    - users.py: Маршруты для пользователей.
    - items.py: Маршруты для предметов.

- tests/: Тесты приложения.
  - conftest.py: Конфигурация тестов.
  - test_main.py: Тесты для основного приложения.
  - test_users.py: Тесты для пользователей.
  - test_models.py: Тесты для моделей.
  - test_items.py: Тесты для предметов.

- alembic/: Миграции базы данных.
  - versions/: Версии миграций.
  - env.py: Конфигурация Alembic.

- external_service/: Внешний сервис.
  - main.py: Точка входа внешнего сервиса.

## Лицензия

Отсутствует. Проект рассматривается как "Тестовое задание для Backend разработчика (junior)", с описанием выполнения можно ознакомиться по ссылке:<br>
[https://imaginary-cinema-82a.notion.site/project_cadastral_service-6099b04b24e844f894c83a11cbca2a9c?pvs=4](https://imaginary-cinema-82a.notion.site/project_cadastral_service-6099b04b24e844f894c83a11cbca2a9c?pvs=4)
