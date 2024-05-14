from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .interface import DatabaseInterface
from ..models.informatics import (InformaticsRegDB, InformaticsFinalDB, InformaticsRegPassingPointsDB)
from ...api.v1.models.informatics import (GetPassingPoints, GetInformaticsReg, GetInformaticsFinal)

from ...config.postgres_config import DATABASE_URL

"""Actions to PostgreSQL"""


class DatabaseActions(DatabaseInterface):
    class MetaData():
        DATABASE_ENGINE: str = "postgresql"
        DATABASE_URL: str = DATABASE_URL
    
    @classmethod
    async def get_informatics_reg(
            self,
            data: GetInformaticsReg,
            async_session: AsyncSession
        ) -> InformaticsRegDB:
        """Получение таблицы регионального этапа по информатике

        Args:
            data (InformaticsRegModel): модель получения данных
            async_session (AsyncSession): асинхронная сессия в БД

        Returns:
            InformaticsRegDB: таблица
        """
        async with async_session.begin():
            
            stmt = select(InformaticsRegDB).where(InformaticsRegDB.year == data.year)
            response = await async_session.execute(stmt)

        result: InformaticsRegDB = response.fetchone()
        return result 

    @classmethod
    async def get_informatics_final(
            self,
            data: GetInformaticsFinal,
            async_session: AsyncSession
        ) -> InformaticsFinalDB:
        """Получение таблицы заключительного этапа по информатике

        Args:
            data (InformaticsFinalModel): модель получения данных
            async_session (AsyncSession): асинхронная сессия в БД

        Returns:
            InformaticsFinalDB: таблица
        """
        
        async with async_session.begin():
            
            stmt = select(InformaticsRegDB).where(InformaticsRegDB.year == data.year)
            response = await async_session.execute(stmt)

        result: InformaticsRegDB = response.fetchone()

        return result 
    
    @classmethod
    async def get_informatics_passing_points(
            self,
            data: GetPassingPoints,
            async_session: AsyncSession
        ) -> InformaticsRegPassingPointsDB:
        """Получение данных о проходных баллах

        Args:
            data (PassingModel): модель получения данных
            async_session (AsyncSession): асинхронная сессия в БД

        Returns:
            InformaticsRegPassingPointsDB: таблица
        """
        
        async with async_session.begin():
            stmt = select(InformaticsRegPassingPointsDB).where(InformaticsRegPassingPointsDB.year == data.year)
            response = await async_session.execute(stmt)

        result: InformaticsRegDB = response.fetchone()

        return result 