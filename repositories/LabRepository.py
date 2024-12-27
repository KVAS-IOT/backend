from sqlalchemy import select

from database.database_config import async_session_factory
from models.LabsModel import LabsModel

class LabRepository:
    @staticmethod
    async def get_all_labs() -> list[LabsModel]:
        async with async_session_factory() as session:
            async with session.begin():
                query = (
                    select(LabsModel)
                )

                res = await session.execute(query)
                lab_models = res.scalars().all()
                return lab_models