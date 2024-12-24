from fastapi import FastAPI

from controllers.labs_controller import labs_router
from controllers.attendances_controller import attendances_router
from controllers.devices_controller import devices_router

app = FastAPI()

app.include_router(labs_router, prefix="/labs")
app.include_router(attendances_router, prefix="/attendances")
app.include_router(devices_router, prefix="/devices")


@app.get("/")
async def root():
    return {"message": "Hello World"}
