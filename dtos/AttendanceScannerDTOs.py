from pydantic import BaseModel


class AttendanceScannerAddDTO(BaseModel):
    id: str
    lab_id: int
