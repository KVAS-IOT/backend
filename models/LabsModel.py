import enum

from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import DBBaseModel

class LectureTimes(enum.Enum):
    T_7_30_9_00 = "7:30-9:00"
    T_9_10_10_40 = "9:10-10:40"
    T_10_50_12_20 = "10:50-12:20"
    T_13_30_15_00 = "13:30-15:00"
    T_15_10_16_40 = "15:10-16:40"


class LabsModel(DBBaseModel):
    __tablename__ = "labs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    number: Mapped[str]
    gateway_url: Mapped[str]
    last_updated_date: Mapped[str]

    lecture_times: Mapped[list[LectureTimes]] = mapped_column(ARRAY(Enum(LectureTimes)), nullable=True)
