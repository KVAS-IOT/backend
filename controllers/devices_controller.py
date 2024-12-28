from fastapi import APIRouter

from dtos.GatewayDTOs import GatewayGetDTO
from services.AttendanceScannerService import AttendanceScannerService

devices_router = APIRouter()

@devices_router.get("/{device_id}/lab")
async def get_device_gateway(scanner_id: str) -> GatewayGetDTO:
    return await AttendanceScannerService.get_scanner_gateway(scanner_id)
