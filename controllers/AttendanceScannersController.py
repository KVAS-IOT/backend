from fastapi import APIRouter

from dtos.AttendanceScannerDTOs import AttendanceScannerAddDTO
from dtos.GatewayDTOs import GatewayGetDTO
from services.AttendanceScannerService import AttendanceScannerService

attendance_scanners_router = APIRouter()

@attendance_scanners_router.get("/{scanner_id}/lab")
async def get_scanner_gateway(scanner_id: str) -> GatewayGetDTO:
    return await AttendanceScannerService.get_scanner_gateway(scanner_id)


@attendance_scanners_router.post("")
async def create_attendance_scanner(device: AttendanceScannerAddDTO) -> None:
    # TODO: Implement
    pass

@attendance_scanners_router.put("/{scanner_id}/lab")
async def update_scanner_lab(scanner_id: str, lab_id: int) -> None:
    # TODO: Implement
    pass
