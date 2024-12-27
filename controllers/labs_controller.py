from fastapi import APIRouter

from dtos.LabDTOs import LabGetDTO
from services.LabService import LabService

labs_router = APIRouter()

@labs_router.get("/")
async def get_labs() -> list[LabGetDTO]:
    return await LabService.get_all_labs()

@labs_router.get("/{lab_id}/lectures")
async def get_lab(lab_id: int):
    return {
        "lectures": [
            "7:30-9:00",
            "9:10-10:40",
            "10:50-12:20",
            "12:30-14:00",
            "14:10-15:40",
            "15:50-17:20",
        ],
        "error_code": 100,
        "error_message": None
    }