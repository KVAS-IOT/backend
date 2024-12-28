from database.database_config import async_session_factory
from models.AttendanceScannersModel import AttendanceScannersModel
from models.AttendancesModel import AttendancesModel
from models.GatewaysModel import GatewaysModel
from models.LabsModel import LabsModel, LectureTimes
from services.DatetimeService import DatetimeService


async def insert_labs_fake_data():
    fake_labs = [
        LabsModel(name="Abydoss", number="A536", last_updated_date=DatetimeService.convert_date_string_to_datetime("2024-12-26 00:00:00"), lecture_times=[LectureTimes.T_7_30_9_00, LectureTimes.T_9_10_10_40, LectureTimes.T_10_50_12_20, LectureTimes.T_13_30_15_00, LectureTimes.T_15_10_16_40]),
        LabsModel(name="Dune", number="B529", last_updated_date=DatetimeService.convert_date_string_to_datetime("2024-12-26 00:00:00"), lecture_times=[LectureTimes.T_7_30_9_00, LectureTimes.T_9_10_10_40, LectureTimes.T_10_50_12_20, LectureTimes.T_13_30_15_00, LectureTimes.T_15_10_16_40]),
        LabsModel(name="Endor", number="B526", last_updated_date=DatetimeService.convert_date_string_to_datetime("2024-12-26 00:00:00"), lecture_times=[LectureTimes.T_7_30_9_00, LectureTimes.T_9_10_10_40, LectureTimes.T_10_50_12_20, LectureTimes.T_13_30_15_00, LectureTimes.T_15_10_16_40]),
        LabsModel(name="Meridian", number="B519", last_updated_date=DatetimeService.convert_date_string_to_datetime("2024-12-26 00:00:00"), lecture_times=[LectureTimes.T_7_30_9_00, LectureTimes.T_9_10_10_40, LectureTimes.T_10_50_12_20, LectureTimes.T_13_30_15_00, LectureTimes.T_15_10_16_40]),
        LabsModel(name="Vulcan", number="A514", last_updated_date=DatetimeService.convert_date_string_to_datetime("2024-12-26 00:00:00"), lecture_times=[LectureTimes.T_7_30_9_00, LectureTimes.T_9_10_10_40, LectureTimes.T_10_50_12_20, LectureTimes.T_13_30_15_00, LectureTimes.T_15_10_16_40]),
    ]

    async with async_session_factory() as session:
        session.add_all(fake_labs)
        await session.commit()

async def insert_attendance_scanners_fake_data():
    fake_attendance_scanners = [
        AttendanceScannersModel(id="4c729f87-34f7-4c50-841c-54ee60f2383d", lab_id=1),
        AttendanceScannersModel(id="84b08fa2-a8d8-4b97-b33d-43b2abf7d57d", lab_id=2),
        AttendanceScannersModel(id="35a75f61-bc1d-4afd-92ae-68857ee9a6a4", lab_id=3),
        AttendanceScannersModel(id="f795f515-a5ba-43e9-80c6-03d360e888c5", lab_id=4),
        AttendanceScannersModel(id="ea9c104e-7c2e-4cd6-bc7d-5ca4475e6cb1", lab_id=5),
    ]

    async with async_session_factory() as session:
        session.add_all(fake_attendance_scanners)
        await session.commit()

async def insert_attendances_fake_data():
    fake_attendances = [
        # LAB 1
        AttendancesModel(card_id="36145173625782788", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:25:02"), lab_id=1),
        AttendancesModel(card_id="52389740174017432", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:26:02"), lab_id=1),
        AttendancesModel(card_id="48293017564829173", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:27:02"), lab_id=1),
        AttendancesModel(card_id="38592017463829175", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:28:02"), lab_id=1),
        AttendancesModel(card_id="72938461502748391", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:29:02"), lab_id=1),
        AttendancesModel(card_id="59381720475638291", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:30:02"), lab_id=1),
        # LAB 2
        AttendancesModel(card_id="36145173625782788", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:25:02"), lab_id=2),
        AttendancesModel(card_id="52389740174017432", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:26:02"), lab_id=2),
        AttendancesModel(card_id="48293017564829173", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:27:02"), lab_id=2),
        AttendancesModel(card_id="38592017463829175", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:28:02"), lab_id=2),
        AttendancesModel(card_id="72938461502748391", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:29:02"), lab_id=2),
        AttendancesModel(card_id="59381720475638291", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:30:02"), lab_id=2),
        # LAB 3
        AttendancesModel(card_id="36145173625782788", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:25:02"), lab_id=3),
        AttendancesModel(card_id="52389740174017432", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:26:02"), lab_id=3),
        AttendancesModel(card_id="48293017564829173", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:27:02"), lab_id=3),
        AttendancesModel(card_id="38592017463829175", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:28:02"), lab_id=3),
        AttendancesModel(card_id="72938461502748391", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:29:02"), lab_id=3),
        AttendancesModel(card_id="59381720475638291", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:30:02"), lab_id=3),
        # LAB 4
        AttendancesModel(card_id="36145173625782788", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:25:02"), lab_id=4),
        AttendancesModel(card_id="52389740174017432", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:26:02"), lab_id=4),
        AttendancesModel(card_id="48293017564829173", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:27:02"), lab_id=4),
        AttendancesModel(card_id="38592017463829175", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:28:02"), lab_id=4),
        AttendancesModel(card_id="72938461502748391", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:29:02"), lab_id=4),
        AttendancesModel(card_id="59381720475638291", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:30:02"), lab_id=4),
        # LAB 5
        AttendancesModel(card_id="36145173625782788", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:25:02"), lab_id=5),
        AttendancesModel(card_id="52389740174017432", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:26:02"), lab_id=5),
        AttendancesModel(card_id="48293017564829173", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:27:02"), lab_id=5),
        AttendancesModel(card_id="38592017463829175", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:28:02"), lab_id=5),
        AttendancesModel(card_id="72938461502748391", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:29:02"), lab_id=5),
        AttendancesModel(card_id="59381720475638291", date=DatetimeService.convert_date_string_to_datetime("2024-12-24 7:30:02"), lab_id=5),
    ]

    async with async_session_factory() as session:
        session.add_all(fake_attendances)
        await session.commit()

async def insert_gateway_fake_data():
    fake_gateways = [
        GatewaysModel(url="abydos-gw.fei.tuke.sk", port= 1883, username="maker", password="this.is.mqtt", lab_id=1),
        GatewaysModel(url="dune-gw.fei.tuke.sk", port= 1883, username="maker", password="this.is.mqtt", lab_id=2),
        GatewaysModel(url="endor-gw.fei.tuke.sk", port= 1883, username="maker", password="this.is.mqtt", lab_id=3),
        GatewaysModel(url="meridian-gw.fei.tuke.sk", port= 1883, username="maker", password="this.is.mqtt", lab_id=4),
        GatewaysModel(url="vulcan-gw.fei.tuke.sk", port= 1883, username="maker", password="this.is.mqtt", lab_id=5),
    ]

    async with async_session_factory() as session:
        session.add_all(fake_gateways)
        await session.commit()

async def insert_fake_data_to_db():
    await insert_labs_fake_data()
    await insert_attendance_scanners_fake_data()
    await insert_attendances_fake_data()
    await insert_gateway_fake_data()