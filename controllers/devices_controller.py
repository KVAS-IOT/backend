from fastapi import APIRouter

devices_router = APIRouter()

@devices_router.get("/{device_id}/lab")
async def get_device_gateway(device_id: int):
    return {
        "gateway": "meridian-gw.fei.tuke.sk:1883",
        "error_code": 100,
        "error_message": None
    }
