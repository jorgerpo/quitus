from typing import Optional

from pydantic import BaseModel

# import ipaddress
# from pydantic.types import IPvAnyAddress


# Shared properties
class DeviceBase(BaseModel):
    device_type: str = 'cisco_ios'
    host: str = None
    port: Optional[int] = 22


# Additional properties Entry
class DeviceIn(DeviceBase):
    username: str = None
    password: str = None


# Additional properties Entry
class DeviceOut(DeviceBase):
    pass
