from fastapi import APIRouter, Depends, Security

from app.api.utils.security import check_token
from app.config import config
from app.crud.vlan_interface import create, delete
from app.models.device import DeviceIn
from app.models.vlan_interface import VlanInterfaceOut, VlanInterfaceToCreate

Tags = ['interface vlan']

router = APIRouter()

@router.post("/", tags=Tags, response_model=VlanInterfaceOut)
def create_vlan_interface(
    *,
    vlan_interface_in: VlanInterfaceToCreate,
    dryrun: bool = config.DRYRUN,
    authorized : bool = Depends(check_token)
    ):
    """
    Create new Vlan interface
    """
    if authorized:
        vlan_interface = create(vlan_interface_in=vlan_interface_in)
        return vlan_interface

@router.delete("/{vlan_id}", tags=Tags, response_model=bool)
def delete_vlan_interface(
        vlan_id: int = None,
        device_type: str = 'cisco_ios',
        device_host: str = None,
        device_port: int = 22,
        device_username: str = None, 
        device_password: str = None,
        dryrun: bool = config.DRYRUN,
        authorized : bool = Depends(check_token)
    ) -> bool:
    """
    delete Vlan interface
    """
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            host=device_host,
            port=device_port,
            username=device_username,
            password=device_password,
        )
        return delete(vlan_id=vlan_id, device=device_in)
