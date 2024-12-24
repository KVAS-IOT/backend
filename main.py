from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controllers.labs_controller import labs_router
from controllers.attendances_controller import attendances_router
from controllers.devices_controller import devices_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # List of allowed origins
    allow_credentials=True,         # Whether to allow credentials (e.g., cookies)
    allow_methods=["*"],            # List of allowed HTTP methods
    allow_headers=["*"],            # List of allowed headers
)

app.include_router(labs_router, prefix="/labs")
app.include_router(attendances_router, prefix="/attendances")
app.include_router(devices_router, prefix="/devices")


@app.get("/")
async def root():
    return {"message": "Hello World"}
