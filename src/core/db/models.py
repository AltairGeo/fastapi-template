from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declared_attr


class BaseModel(AsyncAttrs, DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    id = Column(Integer, primary_key=True)


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], BaseModel):
    @declared_attr
    def user_id(cls):
        return Column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)