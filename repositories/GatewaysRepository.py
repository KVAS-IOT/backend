from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

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

    @staticmethod
    async def update_lab_gateway(gateway: GatewaysModel) -> None:
        async with async_session_factory() as session:
            existing_lab_gateway = await GatewaysRepository.get_gateway_by_lab_id(gateway.lab_id)

            if existing_lab_gateway:
                await session.delete(existing_lab_gateway)
                await session.flush()

            try:
                session.add(gateway)
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e