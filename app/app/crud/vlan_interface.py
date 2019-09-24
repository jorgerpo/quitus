
import datetime
from typing import List, Optional
from fastapi.encoders import jsonable_encoder

from app.models.device import DeviceIn
from app.models.vlan_interface import VlanInterfaceIn, VlanInterfaceOut, VlanInterfaceToCreate
from app.lib.genconf import genconf
from app.lib.logging import logger
from app.lib.net import net

def get(*, device: DeviceIn = None, vlan_id: int) -> Optional[VlanInterfaceOut]:
    vlan_interface = VlanInterfaceIn(
        vlan_id=vlan_id,
        device=device
    )
    return vlan_interface

def create(*, vlan_interface_in: VlanInterfaceToCreate) -> VlanInterfaceOut:
    _, result_out = net.deploy(
        device=vlan_interface_in.device,
        configuration=genconf.generate(template_name="vlan_interface_add", infos=vlan_interface_in, outputType="LIST")
        )
    logger.info(result_out)
    logger.info(vlan_interface_in)
    vlan_interface_out = []
    logger.info(vlan_interface_out)
    return vlan_interface_out

def delete(*, device: DeviceIn = None, vlan_id: int) -> bool:
    vlan_interface = get(device=device, vlan_id=vlan_id)
    # if vlan_interface:
    result, _ = net.deploy(
        device=device,
        configuration=genconf.generate(template_name="vlan_interface_delete", infos=vlan_interface, outputType="LIST")
        )
    if result:
        return True
    return False
