from loguru import logger

from database.DatabaseConfig import DBBaseModel, async_engine


async def create_db_tables():
    async with async_engine.begin() as engine:
        await engine.run_sync(DBBaseModel.metadata.drop_all)
        await engine.run_sync(DBBaseModel.metadata.create_all)
        logger.info("Tables were created")
