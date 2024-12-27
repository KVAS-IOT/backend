from pydantic import BaseModel


class LabGetDTO(BaseModel):
    id: int
    name: str
    number: str