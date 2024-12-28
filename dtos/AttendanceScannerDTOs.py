from pydantic import BaseModel


class AttendanceScannerAddDTO(BaseModel):
    device_id: str
    lab_id: int