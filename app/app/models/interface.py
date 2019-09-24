from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from app.models.device import DeviceIn,DeviceOut

# Shared properties
class InterfaceBase(BaseModel):
    port: str = None
    name: Optional[str] = None
    status: Optional[str] = None

# Additional properties Entry
class InterfaceIn(InterfaceBase):
    device: DeviceIn
    pass

# Additional properties Output
class InterfaceOut(InterfaceBase):
    vlan: str = None
    duplex: str = None
    speed: str = None
    type: str = None
    device: Optional[DeviceOut] = None
    pass

class InterfaceToCreate(InterfaceIn):
    # vlan: Optional[str] = None
    duplex: Optional[str] = None
    speed: Optional[str] = None