
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.vlan import VlanIn,VlanOut
import datetime
from app.lib.parse import parse_vlan,parse_vlans
from app.lib.logging import logger
from app.lib.genconf import genconf, GENConfErrorException
from app.lib.net import net, NETConfigErrorException, NETConnectionErrorException, NETLockErrorException
from app.models.device import DeviceIn,DeviceOut

def get(*, device: DeviceIn = None, vlan_id: int) -> Optional[VlanOut]:
    
    vlan = VlanIn(
        id=vlan_id,
        device=device
    )
    if vlan:
        result,result_output=net.get(
                device=device,
                command=genconf.generate(template_name="vlan_get_one",infos=vlan,outputType="STR")
                )
        if result:
                vlan = VlanOut(**result_output)
                vlan.device = device
                return vlan

def get_multi(device: DeviceIn = None) -> List[Optional[VlanOut]]:
    result,result_output=net.get(
            device=device,
            command=genconf.generate(template_name="vlan_get_multi",infos={},outputType="STR")
            )
    if result:
            return result_output
        # vlanInfos = parse_vlans(device_in=device,output=result_output)
        # return vlanInfos

def create(*, device: DeviceIn = None, vlan_in: VlanIn) -> VlanOut:
    vlan = VlanIn(
        id=vlan_in.id,
        name=vlan_in.name,
        device=device,
    )
    result,result_output=net.deploy(
            device=device,
            configuration=genconf.generate(template_name="vlan_add",infos=vlan,outputType="LIST")
            )
    if result:
        return vlan

def delete(*, device: DeviceIn = None, vlan_id: int) -> bool:
    vlan = get(device=device,vlan_id=vlan_id)
    if vlan:
        result,result_output=net.deploy(
                device=device,
                configuration=genconf.generate(template_name="vlan_delete",infos=vlan,outputType="LIST")
                )
        if result:
            return True
    return False
