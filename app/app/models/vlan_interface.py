from typing import Optional
from pydantic import BaseModel, conint
from app.models.device import DeviceIn, DeviceOut


# Shared properties
class VlanInterfaceBase(BaseModel):
    vlan_id: conint(ge=1, le=4094) = None
    ip_address: Optional[str] = None
    ip_mask: Optional[str] = None
    status: Optional[str] = None


# Additional properties Entry
class VlanInterfaceIn(VlanInterfaceBase):
    device: DeviceIn
    pass


# Additional properties Output
class VlanInterfaceOut(VlanInterfaceBase):
    device: Optional[DeviceOut] = None
    pass


class VlanInterfaceToCreate(VlanInterfaceIn):
    pass
