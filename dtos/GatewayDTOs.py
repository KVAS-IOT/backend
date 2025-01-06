from pydantic import BaseModel


class GatewayGetDTO(BaseModel):
    url: str
    port: int
    username: str
    password: str


class GatewayAddDTO(GatewayGetDTO):
    lab_id: int
