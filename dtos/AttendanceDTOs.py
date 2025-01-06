import datetime

from pydantic import BaseModel

from models.LabsModel import LectureTimes

class AttendanceGetDTO(BaseModel):
    card_id: str
    attendance_time: datetime.datetime

class LectureAttendancesGetDTO(BaseModel):
    lecture_time: LectureTimes
    attendances: list[AttendanceGetDTO]

class AttendancesByLabAndDateGetDTO(BaseModel):
    lab_id: int
    date: datetime.date
    lectures_attendances: list[LectureAttendancesGetDTO]
    out_of_lectures_attendances: list[AttendanceGetDTO]

