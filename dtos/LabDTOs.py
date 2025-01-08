import datetime
from typing import Optional

from pydantic import BaseModel


class LabAddDTO(BaseModel):
    name: str
    number: str


class LabGetDTO(LabAddDTO):
    id: int
    last_updated_date: Optional[datetime.datetime]
