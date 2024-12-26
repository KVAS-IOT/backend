from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import BaseModel


class AttendanceScannersModel(BaseModel):
    __tablename__ = "attendance_scanners"

    id: Mapped[str] = mapped_column(primary_key=True)
    lab_id: Mapped[int] = mapped_column(ForeignKey("labs.id", ondelete="CASCADE"))
