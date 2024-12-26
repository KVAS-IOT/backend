import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import BaseModel


class AttendancesModel(BaseModel):
    __tablename__ = "attendances"

    id: Mapped[int] = mapped_column(primary_key=True)
    card_id: Mapped[str]
    date: Mapped[datetime.datetime]
    lab_id: Mapped[int] = mapped_column(ForeignKey("labs.id", ondelete="CASCADE"))
