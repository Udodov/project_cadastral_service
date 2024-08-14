from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Field, Model
from fastapi_admin.widgets import inputs, displays
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Query, Result


class QueryAdmin(Model):
    label = "Query"
    model = Query
    fields = [
        Field(
            name="id",
            label="ID",
            input_=inputs.DisplayOnly(),
            display=displays.DisplayOnly(),
        ),
        Field(name="cadastral_number", label="Cadastral Number"),
        Field(name="latitude", label="Latitude"),
        Field(name="longitude", label="Longitude"),
        Field(
            name="created_at",
            label="Created At",
            display=displays.DateTimeDisplay(format_="%Y-%m-%d %H:%M:%S"),
        ),
    ]


class ResultAdmin(Model):
    label = "Result"
    model = Result
    fields = [
        Field(
            name="id",
            label="ID",
            input_=inputs.DisplayOnly(),
            display=displays.DisplayOnly(),
        ),
        Field(name="query_id", label="Query ID"),
        Field(name="success", label="Success"),
        Field(
            name="created_at",
            label="Created At",
            display=displays.DateTimeDisplay(format_="%Y-%m-%d %H:%M:%S"),
        ),
    ]


async def create_admin_app() -> FastAPI:
    admin_app.init(
        admin_secret="your-secret",
        providers=[
            UsernamePasswordProvider(
                admin_model=None  # Здесь вы можете определить свою собственную модель администрирования
            )
        ],
        resources=[
            QueryAdmin,
            ResultAdmin,
        ],
    )
    return admin_app
