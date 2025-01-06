from fastapi import APIRouter, status

from dtos.GatewayDTOs import GatewayAddDTO
from services.GatewayService import GatewayService

gateways_router = APIRouter()


@gateways_router.post("/", status_code=status.HTTP_201_CREATED)
async def update_lab_gateway(gateway: GatewayAddDTO) -> None:
    await GatewayService.update_lab_gateway(gateway)
