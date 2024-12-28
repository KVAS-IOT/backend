from fastapi import APIRouter

from dtos.AttendanceScannerDTOs import AttendanceScannerAddDTO
from dtos.GatewayDTOs import GatewayGetDTO
from services.AttendanceScannerService import AttendanceScannerService

devices_router = APIRouter()

@devices_router.get("/{scanner_id}/lab")
async def get_device_gateway(scanner_id: str) -> GatewayGetDTO:
    return await AttendanceScannerService.get_scanner_gateway(scanner_id)


@devices_router.post("")
async def create_device(device: AttendanceScannerAddDTO) -> None:
    # TODO: Implement
    pass

@devices_router.put("/{scanner_id}/lab")
async def update_device_lab(scanner_id: str, lab_id: int) -> None:
    # TODO: Implement
    pass
