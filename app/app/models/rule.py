from enum import Enum

from pydantic import BaseModel, conint, constr, UUID4
from ipaddress import IPv4Address


class ProtocolName(str, Enum):
    tcp = "tcp"
    udp = "udp"
    icmp = "icmp"


class ActionName(str, Enum):
    allow = "allow"
    deny = "deny"


# Shared properties
class RuleBase(BaseModel):
    src_ip: constr(
        regex="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    ) = None
    dst_ip: constr(
        regex="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    ) = None
    protocol: ProtocolName = ProtocolName.tcp
    port: conint(ge=1, le=65535) = 80
    action: ActionName = ActionName.allow

    class Config:
        orm_mode = True

    def __iter__(self):
        for x in range(self.n):
            yield x


# Additional properties Entry
class RuleIn(RuleBase):
    pass


# Additional properties Entry
class RuleOut(RuleBase):
    id: UUID4 = None
    src_zone: str = None
    dst_zone: str = None


class Rule(RuleOut):
    pass
