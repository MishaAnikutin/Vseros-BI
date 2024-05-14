from enum import Enum
from sqlalchemy import (
    Column,
    VARCHAR,
    SMALLINT,
    BOOLEAN,
    CheckConstraint
)

from .basemodel import BaseModel


class ParticipantStatus(Enum, str):
    winner = 'победитель'
    pre_winner = 'призер'
    participant = 'участник'


class InformaticsRegPassingPointsDB(BaseModel):
    """Проходные баллы на всерос"""
    
    __tablename__ = 'informatics_passing_points'
    
    ID = Column('ID', SMALLINT, primary_key=True)  # Добавлен primary key столбец
    year = Column('year', SMALLINT, nullable=False)
    user_class = Column('user_class', SMALLINT)
    passing_point = Column('passing_point', SMALLINT)


class InformaticsFinalDB(BaseModel):
    """Модель SQLAlchemy таблицы всероса по информатике"""
    
    __tablename__ = 'informatics_final'

    year = Column('year', SMALLINT, nullable=False)
    user_hash = Column('user_hash', VARCHAR(32), unique=True, nullable=False, primary_key=True)
    region = Column('region', VARCHAR(64), unique=False, nullable=False)
    user_class = Column('user_class', SMALLINT)
    
    A1 = Column('A1', SMALLINT)
    B1 = Column('B1', SMALLINT)
    C1 = Column('C1', SMALLINT)
    D1 = Column('D1', SMALLINT)
    A2 = Column('A2', SMALLINT)
    B2 = Column('B2', SMALLINT)
    C2 = Column('C2', SMALLINT)
    D2 = Column('D2', SMALLINT)
    
    total_sum = Column('total_sum', SMALLINT)
    status = Column(ParticipantStatus)
    
    # Проверка, что статус участника только один из 3:
    __table_args__ = (CheckConstraint(status.in_(['победитель', 'призер', 'участник']), name='check_status'),)
    
    def __str__(self) -> str:
        return f'<Final:{self.user_hash} {self.region} class: {self.user_class}>'


class InformaticsRegDB(BaseModel):
    """Модель SQLAlchemy таблицы региона по информатике"""

    __tablename__ = 'informatics_reg'

    year = Column('year', SMALLINT, nullable=False)
    user_hash = Column('user_hash', VARCHAR(32), unique=True, nullable=False, primary_key=True)
    region = Column('region', VARCHAR(64), unique=False, nullable=False)
    user_class = Column('user_class', SMALLINT)
    
    A1 = Column('A1', SMALLINT)
    B1 = Column('B1', SMALLINT)
    C1 = Column('C1', SMALLINT)
    D1 = Column('D1', SMALLINT)
    A2 = Column('A2', SMALLINT)
    B2 = Column('B2', SMALLINT)
    C2 = Column('C2', SMALLINT)
    D2 = Column('D2', SMALLINT)
    
    total_sum = Column('total_sum', SMALLINT)
    passed_to_final = Column('passed_to_final', BOOLEAN)
    
    def __str__(self) -> str:
        return f'<Reg:{self.user_hash} {self.region} class: {self.user_class}>'
