from sqlalchemy import select

from database.database_config import async_session_factory
from models.GatewaysModel import GatewaysModel


class GatewaysRepository:
    @staticmethod
    async def get_gateway_by_lab_id(lab_id: int) -> GatewaysModel:
        async with async_session_factory() as session:
            query = (
                select(GatewaysModel)
                .filter(GatewaysModel.lab_id == lab_id)
            )

            res = await session.execute(query)
            return res.scalars().first()