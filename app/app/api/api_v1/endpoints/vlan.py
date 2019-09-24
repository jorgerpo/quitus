from typing import List, Union
from fastapi import APIRouter, Body, Depends, Security, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from app.models.vlan import VlanIn, VlanOut
from app.models.device import DeviceIn, DeviceOut
from app.config import config
from app.api.utils.security import check_token
from app.crud.vlan import get, get_multi, create, delete

Tags = ["vlan"]

router = APIRouter()


@router.get("/{vlan_id}", tags=Tags, response_model=VlanOut)
def read_vlan(
    vlan_id: int = 1,
    device_type: str = "cisco_ios",
    device_port: int = 22,
    device_host: str = None,
    device_username: str = None,
    device_password: str = None,
    authorized: bool = Depends(check_token),
):
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            port=device_port,
            host=device_host,
            username=device_username,
            password=device_password,
        )
        vlan = get(vlan_id=vlan_id, device=device_in)
        return vlan


@router.get("/", tags=Tags, response_model=List[VlanOut])
def read_vlans(
    device_type: str = "cisco_ios",
    device_port: int = 22,
    device_host: str = None,
    device_username: str = None,
    device_password: str = None,
    authorized: bool = Depends(check_token),
):
    """
    Retrieve vlans
    """
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            port=device_port,
            host=device_host,
            username=device_username,
            password=device_password,
        )
        vlans = get_multi(device=device_in)
        return vlans


@router.post("/", tags=Tags, response_model=VlanOut)
def create_vlan(
    *,
    vlan_in: VlanIn,
    dryrun: bool = config.DRYRUN,
    authorized: bool = Depends(check_token)
):
    """
    Create new vlan
    """
    if authorized:
        vlan = get(name=vlan_in.id, device=vlan_in.device)
        if vlan:
            raise HTTPException(
                status_code=400, detail="The vlan %d already exists." % vlan_in.id
            )
        vlan = create(vlan_in=vlan_in)
        return vlan


@router.delete("/{vlan_id}", tags=Tags, response_model=bool)
def delete_vlan(
    vlan_id: int = 1,
    device_type: str = "cisco_ios",
    device_host: str = None,
    device_port: int = 22,
    device_username: str = None,
    device_password: str = None,
    dryrun: bool = config.DRYRUN,
    authorized: bool = Depends(check_token),
) -> bool:
    """
    delete vlan
    """
    if authorized:
        device_in = DeviceIn(
            device_type=device_type,
            host=device_host,
            port=device_port,
            username=device_username,
            password=device_password,
        )
        vlan = get(vlan_id=vlan_id, device=device_in)
        if not vlan:
            raise HTTPException(status_code=400, detail="The vlan does not exist.")
        return delete(vlan_id=vlan_id, device=device_in)

