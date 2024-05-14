from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config.postgres_config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
async_session = sessionmaker(engine, autoflush=False, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator:
    """Dependency for getting async session"""
    
    async with async_session() as session:
        yield session
