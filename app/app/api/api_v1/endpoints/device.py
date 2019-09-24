from typing import List
  
from fastapi import APIRouter, Body, Depends, Security, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.api.utils.db import get_db
from app.models.db.device import Device as DBDevice
from app.models.device import Device, DeviceInDB, DeviceInCreate, DeviceInUpdate
from app.api.utils.security import check_token
from app.crud.device import get,get_multi,get_by_name,create,delete,update
from pprint import pprint

Tags = ['device']

router = APIRouter()

@router.get("/{device_id}",tags=Tags,response_model=Device)
def read_device(device_id: int, db: Session = Depends(get_db),authorized : bool = Depends(check_token)):
    if authorized:
        device = get(db, device_id=device_id)
        return device

@router.get("/", tags=Tags, response_model=List[Device])
def read_devices(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    authorized : bool = Depends(check_token)
):
    """
    Retrieve devices
    """
    if authorized:
        devices = get_multi(db, skip=skip, limit=limit)
        return devices

@router.post("/", tags=Tags, response_model=Device)
def create_device(
    *,
    db: Session = Depends(get_db),
    device_in: DeviceInCreate,
    authorized : bool = Depends(check_token)
):
    """
    Create new device
    """
    if authorized:
        device = get_by_name(db, name=device_in.name)
        if device:
            raise HTTPException(
                status_code=400,
                detail="The device already exists.",
            )
        device = create(db, device_in=device_in)
        return device

@router.put("/{device_id}", tags=Tags, response_model=Device)
def update_device(
    *,
    db: Session = Depends(get_db),
    device_id: int,
    device_in: DeviceInUpdate,
    authorized : bool = Depends(check_token)
):
    """
    Update a device
    """
    if authorized:
        device = get(db, device_id=device_id)

        if not device:
            raise HTTPException(
                status_code=404,
                detail="Device does not exist",
            )
        device = update(db, device=device, device_in=device_in)
        return device

@router.delete("/{device_id}", tags=Tags, response_model=bool)
def delete_device(device_id: int, db: Session = Depends(get_db),authorized : bool = Depends(check_token)):
    """
    delete device
    """
    if authorized:
        device = get(db, device_id=device_id)
        if not device:
            raise HTTPException(
                status_code=400,
                detail="The device does not exist.",
            )
        if delete(db, device_id=device_id):
            return True
        return False

