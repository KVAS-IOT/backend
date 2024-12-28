from dtos.GatewayDTOs import GatewayGetDTO
from repositories.AttendanceScannersRepository import AttendanceScannersRepository
from repositories.GatewaysRepository import GatewaysRepository


class AttendanceScannerService:
    @staticmethod
    async def get_scanner_gateway(scanner_id: str) -> GatewayGetDTO:
        scanner_lab_id = await AttendanceScannersRepository.get_lab_id_by_scanner_id(scanner_id)

        gateway_model = await GatewaysRepository.get_gateway_by_lab_id(scanner_lab_id)

        return GatewayGetDTO(url=gateway_model.url, port=gateway_model.port, username=gateway_model.username, password=gateway_model.password)