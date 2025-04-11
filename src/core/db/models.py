from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer


class BaseModel(AsyncAttrs, DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    id = Column(Integer, primary_key=True)