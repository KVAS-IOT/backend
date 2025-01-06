from loguru import logger

from database.DatabaseConfig import async_session_factory, DBBaseModel, async_engine

from models.AttendanceScannersModel import AttendanceScannersModel
from models.AttendancesModel import AttendancesModel
from models.GatewaysModel import GatewaysModel
from models.LabsModel import LabsModel


async def create_db_tables():
    async with async_engine.begin() as engine:
        await engine.run_sync(DBBaseModel.metadata.drop_all)
        await engine.run_sync(DBBaseModel.metadata.create_all)
        logger.info("Tables were created")