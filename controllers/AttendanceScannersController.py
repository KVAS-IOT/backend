from fastapi import APIRouter, status

from dtos.AttendanceScannerDTOs import AttendanceScannerDTO
from dtos.GatewayDTOs import GatewayGetDTO
from services.AttendanceScannerService import AttendanceScannerService

attendance_scanners_router = APIRouter()


@attendance_scanners_router.get("/{scanner_id}/lab")
async def get_scanner_gateway(scanner_id: str) -> GatewayGetDTO:
    return await AttendanceScannerService.get_scanner_gateway(scanner_id)


@attendance_scanners_router.get("/")
async def get_all_attendance_scanners() -> list[AttendanceScannerDTO]:
    return await AttendanceScannerService.get_all_attendance_scanners()


@attendance_scanners_router.post("", status_code=status.HTTP_201_CREATED)
async def create_attendance_scanner(device: AttendanceScannerDTO) -> None:
    await AttendanceScannerService.create_new_attendance_scanner(device)


@attendance_scanners_router.put("/{scanner_id}/lab", status_code=status.HTTP_202_ACCEPTED)
async def update_scanner_lab(scanner_id: str, lab_id: int) -> None:
    await AttendanceScannerService.update_attendance_scanner_lab(scanner_id, lab_id)
