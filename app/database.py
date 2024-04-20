from typing import AsyncGenerator

from fastapi import Depends

from sqlalchemy import Column, BigInteger, Integer, String, Text
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from app.models.models_articles import Publics
from app.models.models_stats import Subs

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


engine = create_async_engine(DB_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_subs(session: AsyncSession = Depends(get_async_session)):
    async with session.begin():
        subs = await async_session.execute(Subs.__table__.select())
        return subs.mappings().fetchall()

async def get_user_publics(session: AsyncSession = Depends(get_async_session)):
    async with session.begin():
        publics = await session.execute(Publics.__table__.select())
        return publics.mappings().fetchall()