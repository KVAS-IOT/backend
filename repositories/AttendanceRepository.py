from database.database_config import async_session_factory
from models.AttendancesModel import AttendancesModel


class AttendanceRepository:
    @staticmethod
    async def save_attendances(attendances: list[AttendancesModel]):
        async with async_session_factory() as session:
            session.add_all(attendances)
            await session.commit()