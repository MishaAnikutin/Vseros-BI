from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


from src.schemas.informaticsDTO import InformaticsDTO
from src.controllers.informatics import InformaticsController
from src.database.session import get_session
informatics_router = APIRouter()

@informatics_router.get("/final/{year}", response_model=InformaticsDTO)
def get_final(
        year: int,
        session: AsyncSession = Depends(get_session)
    ) -> Optional[InformaticsDTO]:
    
    data: InformaticsDTO = InformaticsController.get_final_data(session, year)
    
    if data is None:
        raise HTTPException(status_code=404, detail="Данные не найдены")
    
    return data

@informatics_router.get("/region/{year}", response_model=InformaticsDTO)
def get_region(
        year: int,
        session: AsyncSession = Depends(get_session)
    ) -> Optional[InformaticsDTO]:
    
    data: InformaticsDTO = InformaticsController.get_reg_data(session, year)
    
    if data is None:
        raise HTTPException(status_code=404, detail="Данные не найдены")
    
    return data
