from typing import List, Tuple, Any
from pydantic import BaseModel


class InformaticsDTO(BaseModel):
    data: List[Tuple[Any]]
