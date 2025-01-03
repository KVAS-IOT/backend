from fastapi import APIRouter, status

from dtos.GatewayDTOs import GatewayGetDTO
from dtos.LabDTOs import LabGetDTO, LabAddDTO
from models.LabsModel import LectureTimes
from services.GatewayService import GatewayService
from services.LabService import LabService

labs_router = APIRouter()

@labs_router.get("/")
async def get_labs() -> list[LabGetDTO]:
    return await LabService.get_all_labs()

@labs_router.get("/{lab_id}/lectures")
async def get_lab(lab_id: int) -> list[LectureTimes]:
    return await LabService.get_lab_lecture_times_by_lab_id(lab_id)

@labs_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_lab(lab: LabAddDTO) -> None:
    await LabService.create_lab(lab)

@labs_router.put("/{lab_id}/lectures", status_code=status.HTTP_202_ACCEPTED)
async def update_lab_lectures(lab_id: int, lecture_times: list[LectureTimes]) -> None:
    await LabService.update_lab_lectures(lab_id, lecture_times)

@labs_router.get("/{lab_id}/gateway")
async def get_lab_gateway(lab_id: int) -> GatewayGetDTO:
    return await GatewayService.get_gateway_by_lab_id(lab_id)