from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.config import settings
from .models import BaseModel, User
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase 

# -------------------------------------------------------------------------------
#  CREATION ENGINE AND SESSION

try:
    engine = create_async_engine(
        settings.db_url,
        pool_size=20,
        max_overflow=0,
        pool_recycle=300,
        pool_pre_ping=True
    )
except Exception as e:
    print(e)
    try:
        engine = create_async_engine(settings.db_url)
    except Exception as e:
        print(e)


async_session_maker = async_sessionmaker(engine, expire_on_commit=False)  # Create session maker
async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)

# ----------------------------------------------------------------------------------