import datetime

from sqlalchemy import select, cast, Date

from database.DatabaseConfig import async_session_factory
from models.AttendancesModel import AttendancesModel


class AttendanceRepository:
    @staticmethod
    async def save_attendances(attendances: list[AttendancesModel]):
        async with async_session_factory() as session:
            session.add_all(attendances)
            await session.commit()

    @staticmethod
    async def get_attendances_by_lab_and_date(lab_id: int, date: datetime.date) -> list[AttendancesModel]:
        async with async_session_factory() as session:
            query = (
                select(AttendancesModel)
                .filter(
                    AttendancesModel.lab_id == lab_id,
                    cast(AttendancesModel.date, Date) == date
                )
            )

            res = await session.execute(query)

            return res.scalars().all()
