import datetime

from pydantic import BaseModel


class LabAddDTO(BaseModel):
    name: str
    number: str


class LabGetDTO(LabAddDTO):
    id: int
    last_updated_date: datetime.datetime
