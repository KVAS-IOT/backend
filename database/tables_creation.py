from database.database_config import async_session_factory, BaseModel, async_engine

from models.AttendanceScannersModel import AttendanceScannersModel
from models.AttendancesModel import AttendancesModel
from models.LabsModel import LabsModel


async def create_db_tables():
    async with async_engine.begin() as engine:
        await engine.run_sync(BaseModel.metadata.drop_all)
        await engine.run_sync(BaseModel.metadata.create_all)