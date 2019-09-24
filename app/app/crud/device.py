
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.db.device import Device
from app.models.device import DeviceInCreate, DeviceInUpdate
import datetime

def get(db_session, *, device_id: int) -> Optional[Device]:
    return db_session.query(Device).filter(Device.id == device_id).first()

def get_by_name(db_session, *, name: str) -> Optional[Device]:
    return db_session.query(Device).filter(Device.name == name).first()

def get_multi(db_session, *, skip=0, limit=100) -> List[Optional[Device]]:
    return db_session.query(Device).offset(skip).limit(limit).all()

def create(db_session, *, device_in: DeviceInCreate) -> Device:
    device = Device(
        name=device_in.name,
        fqdn=device_in.fqdn,
        serial=device_in.serial,
        management_ip=device_in.management_ip,
    )
    db_session.add(device)
    db_session.commit()
    db_session.refresh(device)
    return device

def update(db_session, *, device: Device, device_in: DeviceInUpdate) -> Device:
    device_data = jsonable_encoder(device)
    for field in device_data:
        if field in device_in.fields:
            value_in = getattr(device_in, field)
            if value_in is not None:
                setattr(device, field, value_in)
    device.updated_at = str(datetime.datetime.now())
    db_session.add(device)
    db_session.commit()
    db_session.refresh(device)
    return device

def delete(db_session, *, device_id: int) -> bool:
    device = get(db_session, device_id=device_id)
    if Device:
        db_session.delete(device)
        db_session.commit()
        return True
    return False




