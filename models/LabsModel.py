from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import BaseModel


class LabsModel(BaseModel):
    __tablename__ = "labs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    number: Mapped[str]
    gateway_url: Mapped[str]
    last_updated_date: Mapped[str]