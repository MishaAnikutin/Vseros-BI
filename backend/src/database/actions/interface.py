from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.informatics import (InformaticsRegDB, InformaticsFinalDB, InformaticsRegPassingPointsDB)
from ...api.v1.models.informatics import (GetInformaticsFinal, GetInformaticsReg, GetPassingPoints)


class DatabaseInterface(ABC):
    @classmethod
    @abstractmethod
    async def get_informatics_final(self, data: GetInformaticsFinal, async_session: AsyncSession) -> InformaticsFinalDB:
        ... 
    
    
    @classmethod
    @abstractmethod
    async def get_informatics_reg(self, data: GetInformaticsReg, async_session: AsyncSession) -> InformaticsRegDB:
        ... 
        
    @classmethod
    @abstractmethod
    async def get_informatics_passing_points(self, data: GetPassingPoints, async_session: AsyncSession) -> InformaticsRegPassingPointsDB:
        ...
