from sqlalchemy import select

from database.DatabaseConfig import async_session_factory
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
    async def get_scanner_by_id(scanner_id: str) -> AttendanceScannersModel:
        async with async_session_factory() as session:
            query = (
                select(AttendanceScannersModel)
                .filter(AttendanceScannersModel.id == scanner_id)
            )

            res = await session.execute(query)
            return res.scalars().first

    @staticmethod
    async def create_new_attendance_scanner(attendance_scanner: AttendanceScannersModel) -> None:
        async with async_session_factory() as session:
            session.add(attendance_scanner)
            await session.commit()

    @staticmethod
    async def update_scanner_lab(scanner_id: str, lab_id: int) -> None:
        async with async_session_factory() as session:
            query = (
                select(AttendanceScannersModel)
                .filter(AttendanceScannersModel.id == scanner_id)
            )

            res = await session.execute(query)
            scanner = res.scalars().first()
            scanner.lab_id = lab_id
            await session.commit()
