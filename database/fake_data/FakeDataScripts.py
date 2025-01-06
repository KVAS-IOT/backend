import json

from database.DatabaseConfig import async_session_factory
from models.AttendanceScannersModel import AttendanceScannersModel
from models.AttendancesModel import AttendancesModel
from models.GatewaysModel import GatewaysModel
from models.LabsModel import LabsModel, LectureTimes
from services.DatetimeService import DatetimeService


async def insert_labs_fake_data():
    fake_labs = []

    with open("database/fake_data/FakeLabs.json", "r", encoding="utf-8") as file:
        labs = json.load(file)

    for lab in labs:
        fake_labs.append(LabsModel(name=lab["name"], number=lab["number"], last_updated_date=DatetimeService.convert_date_string_to_datetime(lab["last_updated_date"]), lecture_times=lab["lecture_times"]))

    async with async_session_factory() as session:
        session.add_all(fake_labs)
        await session.commit()

async def insert_attendance_scanners_fake_data():
    with open("database/fake_data/FakeAttendanceScanners.json", "r", encoding="utf-8") as file:
        attendance_scanners = json.load(file)

    fake_attendance_scanners = [AttendanceScannersModel(**scanner) for scanner in attendance_scanners]

    async with async_session_factory() as session:
        session.add_all(fake_attendance_scanners)
        await session.commit()

async def insert_attendances_fake_data():
    fake_attendances = []

    with open("database/fake_data/FakeAttendances.json", "r", encoding="utf-8") as file:
        attendance_records = json.load(file)

    for record in attendance_records:
        fake_attendances.append(AttendancesModel(card_id=record["card_id"], date=DatetimeService.convert_date_string_to_datetime(record["date"]), lab_id=record["lab_id"]))

    async with async_session_factory() as session:
        session.add_all(fake_attendances)
        await session.commit()

async def insert_gateway_fake_data():
    with open("database/fake_data/FakeGateways.json", "r", encoding="utf-8") as file:
        gateways = json.load(file)

    fake_gateways = [GatewaysModel(**gateway) for gateway in gateways]

    async with async_session_factory() as session:
        session.add_all(fake_gateways)
        await session.commit()

async def insert_fake_data_to_db():
    await insert_labs_fake_data()
    await insert_attendance_scanners_fake_data()
    await insert_attendances_fake_data()
    await insert_gateway_fake_data()