from pydantic import BaseModel


class GatewayGetDTO(BaseModel):
    url: str
    port: int
    username: str
    password: str