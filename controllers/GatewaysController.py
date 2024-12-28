from fastapi import APIRouter

from dtos.GatewayDTOs import GatewayAddDTO

gateways_router = APIRouter()


@gateways_router.post("/")
async def create_gateway(gateway: GatewayAddDTO) -> None:
    # TODO: Implement
    pass