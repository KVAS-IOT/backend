import datetime

from sqlalchemy import select

from database.database_config import async_session_factory
from models.LabsModel import LabsModel, LectureTimes


class LabRepository:
    @staticmethod
    async def get_all_labs() -> list[LabsModel]:
        async with async_session_factory() as session:
            query = (
                select(LabsModel)
            )

            res = await session.execute(query)
            lab_models = res.scalars().all()
            return lab_models

    @staticmethod
    async def get_lab_lecture_times_by_lab_id(lab_id: int) -> list[LectureTimes]:
        async with async_session_factory() as session:
            query = (
                select(LabsModel.lecture_times)
                .filter(LabsModel.id == lab_id)
            )

            res = await session.execute(query)
            return res.scalars().first()

    @staticmethod
    async def update_lab_last_update_time(lab_id: int, new_last_updated_date: datetime.datetime):
        async with async_session_factory() as session:
            query = (
                select(LabsModel)
                .filter(LabsModel.id == lab_id)
            )

            res = await session.execute(query)
            lab_model = res.scalars().first()
            lab_model.last_updated_date = new_last_updated_date
            await session.commit()

    @staticmethod
    async def create_lab(lab: LabsModel):
        async with async_session_factory() as session:
            session.add(lab)
            await session.commit()

    @staticmethod
    async def update_lab_lectures(lab_id: int, lecture_times: list[LectureTimes]):
        async with async_session_factory() as session:
            query = (
                select(LabsModel)
                .filter(LabsModel.id == lab_id)
            )

            res = await session.execute(query)
            lab_model = res.scalars().first()
            lab_model.lecture_times = lecture_times
            await session.commit()