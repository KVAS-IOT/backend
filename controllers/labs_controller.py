from fastapi import APIRouter

from dtos.LabDTOs import LabGetDTO
from services.LabService import LabService

labs_router = APIRouter()

@labs_router.get("/")
async def get_labs() -> list[LabGetDTO]:
    return await LabService.get_all_labs()

@labs_router.get("/{lab_id}/lectures")
async def get_lab(lab_id: int) -> list[str]:
    return await LabService.get_lab_lecture_times_by_lab_id(lab_id)
