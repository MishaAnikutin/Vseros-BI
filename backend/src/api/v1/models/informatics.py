from enum import Enum
from dataclasses import dataclass


class ParticipantStatus(Enum, str):
    winner = 'победитель'
    pre_winner = 'призер'
    participant = 'участник'


@dataclass
class GetPassingPoints:
    year: int
    

@dataclass
class GetInformaticsReg:
    year: int
    is_passed: bool
    limit: int = 10


@dataclass
class GetInformaticsFinal:
    year: int
    participant: ParticipantStatus
    limit: int = 10
