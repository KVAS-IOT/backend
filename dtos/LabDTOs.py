import datetime

from pydantic import BaseModel


class LabGetDTO(BaseModel):
    id: int
    name: str
    number: str
    last_updated_date: datetime.datetime