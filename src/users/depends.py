from src.users.models import User, AccessToken
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase 
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from src.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import settings




async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=User)

async def get_access_token_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


def get_database_stategy(
        access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db)
    ) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, settings.token_lifetime)