from database.database_config import async_session_factory
from models.LabsModel import LabsModel


async def insert_labs_fake_data():
    fake_labs = [
        LabsModel(name="Abydoss", number="A536", gateway_url="abydos-gw.fei.tuke.sk", last_updated_date="2024-12-26 00:00:00"),
        LabsModel(name="Dune", number="B529", gateway_url="dune-gw.fei.tuke.sk", last_updated_date="2024-12-26 00:00:00"),
        LabsModel(name="Endor", number="B526", gateway_url="endor-gw.fei.tuke.sk", last_updated_date="2024-12-26 00:00:00"),
        LabsModel(name="Meridian", number="B519", gateway_url="meridian-gw.fei.tuke.sk", last_updated_date="2024-12-26 00:00:00"),
        LabsModel(name="Vulcan", number="A514", gateway_url="vulcan-gw.fei.tuke.sk", last_updated_date="2024-12-26 00:00:00"),
    ]

    async with async_session_factory() as session:
        session.add_all(fake_labs)
        await session.commit()

async def insert_fake_data_to_db():
    await insert_labs_fake_data()