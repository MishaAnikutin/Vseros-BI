from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.informaticsDTO import InformaticsDTO
from src.database.actions import DatabaseActions


class InformaticsController:
    @classmethod
    async def get_reg_data():
        ...
    
    @classmethod
    async def get_final_data(session: AsyncSession, year: InformaticsDTO):
        ...