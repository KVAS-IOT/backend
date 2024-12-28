from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import DBBaseModel


class GatewaysModel(DBBaseModel):
    __tablename__ = "gateways"

    id: Mapped[int] = mapped_column(primary_key=True)
    gateway_url: Mapped[str]
    gateway_port: Mapped[int]
    gateway_username: Mapped[str]
    gateway_password: Mapped[str]

    gateway_lab: Mapped[int] = mapped_column(ForeignKey("labs.id", ondelete="CASCADE"), unique=True)