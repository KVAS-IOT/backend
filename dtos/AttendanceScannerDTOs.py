from pydantic import BaseModel


class AttendanceScannerDTO(BaseModel):
    id: str
    lab_id: int
