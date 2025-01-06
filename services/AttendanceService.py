import datetime
from typing import Optional

from dtos.AttendanceDTOs import AttendancesByLabAndDateGetDTO, AttendanceGetDTO, LectureAttendancesGetDTO
from models.AttendancesModel import AttendancesModel
from models.LabsModel import LectureTimes
from repositories.AttendanceRepository import AttendanceRepository
from repositories.LabRepository import LabRepository
from services.DatetimeService import DatetimeService


class AttendanceService:
    @staticmethod
    async def save_attendances(attendances: dict, lab_id: int):
        attendances_to_save = []
        for attendance in attendances:
            for date in attendance["attendance_times"]:
                attendance_to_save = AttendancesModel(card_id=attendance["card_id"],
                                                      date=DatetimeService.convert_date_string_to_datetime(date),
                                                      lab_id=lab_id)
                attendances_to_save.append(attendance_to_save)

        await AttendanceRepository.save_attendances(attendances_to_save)

    @staticmethod
    def get_attendance_lecture_time(attendance_time: datetime.datetime, lab_lectures: list[LectureTimes]) -> Optional[
        LectureTimes]:
        for lecture in lab_lectures:
            if lecture.get_attendance_start_time() <= attendance_time.time() <= lecture.get_end_time():
                return lecture
        return None

    @staticmethod
    async def get_attendances_by_lab_and_date(lab_id: int, date: datetime.date) -> AttendancesByLabAndDateGetDTO:
        attendances = await AttendanceRepository.get_attendances_by_lab_and_date(lab_id, date)
        attendance_get_dtos = [AttendanceGetDTO(card_id=attendance.card_id, attendance_time=attendance.date) for
                               attendance in attendances]

        lab_lectures = await LabRepository.get_lab_lecture_times_by_lab_id(lab_id)
        sorted_lab_lectures = sorted(lab_lectures, key=lambda x: x.get_attendance_start_time())

        lecture_attendances_dict: dict[LectureTimes, list[AttendanceGetDTO]] = {}
        out_of_lecture_attendances: list[AttendanceGetDTO] = []

        for attendance in attendance_get_dtos:
            lecture_time = AttendanceService.get_attendance_lecture_time(attendance.attendance_time,
                                                                         sorted_lab_lectures)
            if lecture_time:
                if lecture_time not in lecture_attendances_dict:
                    lecture_attendances_dict[lecture_time] = []
                lecture_attendances_dict[lecture_time].append(attendance)
            else:
                out_of_lecture_attendances.append(attendance)

        lecture_attendances = []

        for lecture, attendances in lecture_attendances_dict.items():
            lecture_attendances.append(LectureAttendancesGetDTO(lecture_time=lecture, attendances=attendances))

        return AttendancesByLabAndDateGetDTO(lab_id=lab_id, date=date, lectures_attendances=lecture_attendances,
                                             out_of_lectures_attendances=out_of_lecture_attendances)
