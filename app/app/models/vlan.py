from typing import Optional
from pydantic import BaseModel, conint
from app.models.device import DeviceIn, DeviceOut


# Shared properties
class VlanBase(BaseModel):
    id: conint(ge=1, le=4094)
    name: Optional[str] = None


# Additional properties Entry
class VlanIn(VlanBase):
    device: DeviceIn
    pass


# Additional properties Output
class VlanOut(VlanBase):
    device: Optional[DeviceOut] = None
    pass
