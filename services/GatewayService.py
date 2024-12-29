from dtos.GatewayDTOs import GatewayAddDTO
from models.GatewaysModel import GatewaysModel
from repositories.GatewaysRepository import GatewaysRepository


class GatewayService:
    @staticmethod
    async def create_new_gateway(gateway: GatewayAddDTO) -> None:
        new_gateway_model = GatewaysModel(**gateway.model_dump())
        await GatewaysRepository.create_new_gateway(new_gateway_model)