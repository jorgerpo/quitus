from fastapi import APIRouter
  
from app.api.api_v1.endpoints import vlan, interface, vlan_interface

api_router = APIRouter()
api_router.include_router(vlan.router, prefix="/vlan")
api_router.include_router(interface.router, prefix="/interface")
api_router.include_router(vlan_interface.router, prefix="/interface-vlan")
