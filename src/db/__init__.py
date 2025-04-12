from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.config import settings


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
    try:
        engine = create_async_engine(settings.db_url)
    except Exception as e:
        print(str(e))


async_session_maker = async_sessionmaker(engine, expire_on_commit=False)  # Create session maker
async def get_async_session():
    async with async_session_maker() as session:
        yield session

# ----------------------------------------------------------------------------------