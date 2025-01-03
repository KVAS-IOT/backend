from dtos.GatewayDTOs import GatewayAddDTO, GatewayGetDTO
from models.GatewaysModel import GatewaysModel
from repositories.GatewaysRepository import GatewaysRepository


class GatewayService:
    @staticmethod
    async def create_new_gateway(gateway: GatewayAddDTO) -> None:
        new_gateway_model = GatewaysModel(**gateway.model_dump())
        await GatewaysRepository.create_new_gateway(new_gateway_model)

    @staticmethod
    async def get_gateway_by_lab_id(lab_id: int) -> GatewayGetDTO:
        gateway_model = await GatewaysRepository.get_gateway_by_lab_id(lab_id)
        return GatewayGetDTO(url=gateway_model.url, port=gateway_model.port, username=gateway_model.username, password=gateway_model.password)