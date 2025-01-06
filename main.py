from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controllers.GatewaysController import gateways_router
from database.DatabaseConfig import check_database_connection
from controllers.LabsController import labs_router
from controllers.AttendancesController import attendances_router
from controllers.AttendanceScannersController import attendance_scanners_router
from database.fake_data.FakeDataScripts import insert_fake_data_to_db
from database.TablesCreation import create_db_tables
from services.MQTTReaderService import MQTTReaderService


@asynccontextmanager
async def lifespan(_: FastAPI):
    await check_database_connection()
    await create_db_tables()
    await insert_fake_data_to_db()
    MQTTReaderService()
    yield
    MQTTReaderService().stop()
    print("Application shutdown")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # List of allowed origins
    allow_credentials=True,         # Whether to allow credentials (e.g., cookies)
    allow_methods=["*"],            # List of allowed HTTP methods
    allow_headers=["*"],            # List of allowed headers
)

app.include_router(labs_router, prefix="/labs", tags=["labs"])
app.include_router(attendances_router, prefix="/attendances", tags=["attendances"])
app.include_router(attendance_scanners_router, prefix="/devices", tags=["devices"])
app.include_router(gateways_router, prefix="/gateways", tags=["gateways"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
