from fastapi import APIRouter
from app.utils.vpn_manager import start_vpn, stop_vpn

router = APIRouter()

@router.post("/start")
def start_vpn_route():
    start_vpn()
    return {"message": "VPN started"}

@router.post("/stop")
def stop_vpn_route():
    stop_vpn()
    return {"message": "VPN stopped"}
