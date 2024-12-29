from sqlalchemy import select

from database.database_config import async_session_factory
from models.AttendanceScannersModel import AttendanceScannersModel


class AttendanceScannersRepository:
    @staticmethod
    async def get_lab_id_by_scanner_id(scanner_id: str) -> int:
        async with async_session_factory() as session:
            query = (
                select(AttendanceScannersModel.lab_id)
                .filter(AttendanceScannersModel.id == scanner_id)
            )

            res = await session.execute(query)
            return res.scalars().first()

    @staticmethod
    async def create_new_attendance_scanner(attendance_scanner: AttendanceScannersModel) -> None:
        async with async_session_factory() as session:
            session.add(attendance_scanner)
            await session.commit()