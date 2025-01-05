import datetime

from fastapi import APIRouter

from dtos.AttendanceDTOs import AttendancesByLabAndDateGetDTO

attendances_router = APIRouter()

@attendances_router.get("/")
async def get_attendances(lab_id: int, date: datetime.date) -> AttendancesByLabAndDateGetDTO:
    print(date)
    return {
        "attendances": [
            {
                "card_id": "36145173625782788",
                "time": "24-12-2024 7:25:02"
            },
            {
                "card_id": "52389740174017432",
                "time": "24-12-2024 7:26:02"
            },
            {
                "card_id": "48293017564829173",
                "time": "24-12-2024 7:27:02"
            },
            {
                "card_id": "38592017463829175",
                "time": "24-12-2024 7:28:02"
            },
            {
                "card_id": "72938461502748391",
                "time": "24-12-2024 7:29:02"
            },
            {
                "card_id": "59381720475638291",
                "time": "24-12-2024 7:30:02"
            },
        ],
        "error_code": 100,
        "error_message": None
    }