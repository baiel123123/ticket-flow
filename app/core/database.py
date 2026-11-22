from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .config import settings

DATABASE_URL = settings.db_url

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commint=False)


async def get_async_session(async_session_maker):
    async with async_session_maker as session:
        yield session
