from typing import List, Union
from fastapi import APIRouter, Body, Depends, Security, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from app.models.interface import InterfaceIn,InterfaceOut,InterfaceToCreate
from app.models.device import DeviceIn,DeviceOut
from app.config import config
from app.api.utils.security import check_token
from app.crud.interface import get,get_multi,create,delete

Tags = ['interface']

router = APIRouter()


@router.get("/{interface_port}", tags=Tags,response_model=InterfaceOut)
def read_interface(
    interface_port: str = None,
    device_type: str = 'cisco_ios',
    device_host: str = None,
    device_port: int = 22,
    device_username: str = None, 
    device_password: str = None,
    authorized : bool = Depends(check_token)):
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            host=device_host,
            port=device_port,
            username=device_username,
            password=device_password,
        )
        interface = get(interface_port=interface_port, device=device_in)
        return interface

@router.get("/", tags=Tags, response_model=List[InterfaceOut])
def read_interfaces(
    device_type: str = 'cisco_ios',
    device_host: str = None,
    device_port: int = 22,
    device_username: str = None, 
    device_password: str = None,
    authorized : bool = Depends(check_token)
    ):
    """
    Retrieve interfaces
    """
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            host=device_host,
            port=device_port,
            username=device_username,
            password=device_password,
        )
        interfaces = get_multi(device=device_in)
        return interfaces

@router.post("/", tags=Tags, response_model=InterfaceOut)
def create_interface(
    *,
    interface_in: InterfaceToCreate,
    dryrun: bool = config.DRYRUN,
    authorized : bool = Depends(check_token)
    ):
    """
    Create new interface
    """
    if authorized:
        interface = create(interface_in=interface_in)
        return interface

@router.delete("/{interface_port}", tags=Tags, response_model=bool)
def delete_interface(
        interface_port: str = None,
        device_type: str = 'cisco_ios',
        device_host: str = None,
        device_port: int = 22,
        device_username: str = None, 
        device_password: str = None,
        dryrun: bool = config.DRYRUN,
        authorized : bool = Depends(check_token)
    ) -> bool:
    """
    delete interface
    """
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            host=device_host,
            port=device_port,
            username=device_username,
            password=device_password,
        )
        return delete(interface_port=interface_port,device=device_in)

