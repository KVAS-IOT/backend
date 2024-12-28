from models.AttendancesModel import AttendancesModel
from repositories.AttendanceRepository import AttendanceRepository
from services.DatetimeService import DatetimeService


class AttendanceService:
    @staticmethod
    async def save_attendances(attendances: dict, lab_id: int):
        attendances_to_save = []
        for attendance in attendances:
            for date in attendance["attendance_times"]:
                attendance_to_save = AttendancesModel(card_id=attendance["card_id"], date=DatetimeService.convert_date_string_to_datetime(date), lab_id=lab_id)
                attendances_to_save.append(attendance_to_save)

        await AttendanceRepository.save_attendances(attendances_to_save)