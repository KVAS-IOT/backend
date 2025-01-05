import datetime

from fastapi import APIRouter

from dtos.AttendanceDTOs import AttendancesByLabAndDateGetDTO
from services.AttendanceService import AttendanceService

attendances_router = APIRouter()

@attendances_router.get("/")
async def get_attendances(lab_id: int, date: datetime.date) -> AttendancesByLabAndDateGetDTO:
    return await AttendanceService.get_attendances_by_lab_and_date(lab_id, date)