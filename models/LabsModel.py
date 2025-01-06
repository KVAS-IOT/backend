import enum
from datetime import datetime, timedelta

from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from database.DatabaseConfig import DBBaseModel
from services.DatetimeService import DatetimeService


class LectureTimes(enum.Enum):
    T_7_30_9_00 = "7:30-9:00"
    T_9_10_10_40 = "9:10-10:40"
    T_10_50_12_20 = "10:50-12:20"
    T_13_30_15_00 = "13:30-15:00"
    T_15_10_16_40 = "15:10-16:40"

    def get_start_time(self) -> datetime.time:
        return DatetimeService.convert_time_string_to_time_object(self.value.split("-")[0])

    def get_end_time(self) -> datetime.time:
        return DatetimeService.convert_time_string_to_time_object(self.value.split("-")[1])

    def get_attendance_start_time(self) -> datetime.time:
        lecture_start_datetime = datetime.combine(datetime.today(), self.get_start_time())
        attendance_start_datetime = lecture_start_datetime - timedelta(minutes=10)
        return attendance_start_datetime.time()


class LabsModel(DBBaseModel):
    __tablename__ = "labs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    number: Mapped[str]
    last_updated_date: Mapped[datetime] = mapped_column(nullable=True)

    lecture_times: Mapped[list[LectureTimes]] = mapped_column(ARRAY(Enum(LectureTimes)), nullable=True)
