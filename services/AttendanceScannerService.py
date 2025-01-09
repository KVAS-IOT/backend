from dtos.AttendanceScannerDTOs import AttendanceScannerAddDTO
from dtos.GatewayDTOs import GatewayGetDTO
from models.AttendanceScannersModel import AttendanceScannersModel
from repositories.AttendanceScannersRepository import AttendanceScannersRepository
from services.GatewayService import GatewayService


class AttendanceScannerService:
    @staticmethod
    async def get_scanner_gateway(scanner_id: str) -> GatewayGetDTO:
        scanner_lab_id = await AttendanceScannersRepository.get_lab_id_by_scanner_id(scanner_id)

        gateway_model = await GatewayService.get_gateway_by_lab_id(scanner_lab_id)

        return GatewayGetDTO(url=gateway_model.url, port=gateway_model.port, username=gateway_model.username,
                             password=gateway_model.password)

    @staticmethod
    async def create_new_attendance_scanner(attendance_scanner_add_dto: AttendanceScannerAddDTO) -> None:
        scanner_from_db = await AttendanceScannersRepository.get_scanner_by_id(attendance_scanner_add_dto.id)
        if scanner_from_db:
            await AttendanceScannersRepository.update_scanner_lab(attendance_scanner_add_dto.id, attendance_scanner_add_dto.lab_id)
        else:
            await AttendanceScannersRepository.create_new_attendance_scanner(
                AttendanceScannersModel(**attendance_scanner_add_dto.model_dump()))

    @staticmethod
    async def update_attendance_scanner_lab(scanner_id: str, lab_id: int) -> None:
        await AttendanceScannersRepository.update_scanner_lab(scanner_id, lab_id)
