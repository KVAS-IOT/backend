from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import DBBaseModel


class GatewaysModel(DBBaseModel):
    __tablename__ = "gateways"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]
    port: Mapped[int]
    username: Mapped[str]
    password: Mapped[str]

    lab_id: Mapped[int] = mapped_column(ForeignKey("labs.id", ondelete="CASCADE"), unique=True)