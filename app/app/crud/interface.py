
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from app.models.interface import InterfaceIn,InterfaceOut,InterfaceToCreate
import datetime
from app.lib.parse import parse_interface,parse_interfaces
from app.lib.logging import logger
from app.lib.genconf import genconf, GENConfErrorException
from app.lib.net import net, NETConfigErrorException, NETConnectionErrorException, NETLockErrorException
from app.models.device import DeviceIn,DeviceOut

def get(*, device: DeviceIn = None, interface_port: str) -> Optional[InterfaceOut]:
    
    interface = InterfaceIn(
        port=interface_port,
        device=device
    )
    if interface:
        result,interface_result=net.get(
                device=device,
                command=genconf.generate(template_name="interface_get_multi",infos=interface,outputType="STR")
                )
        if result:
                for item in interface_result:
                        if item['port'] == interface_port:
                                item['device'] = device
                                logger.info(item)
                                return item
                

def get_multi(device: DeviceIn = None) -> List[Optional[InterfaceOut]]:
    result,interface_result=net.get(
            device=device,
            command=genconf.generate(template_name="interface_get_multi",infos={},outputType="STR")
            )
    if result:
            for item in interface_result:
                    item['device'] = device
            return interface_result
        

def create(*, interface_in: InterfaceToCreate) -> InterfaceOut:
    result,result_out=net.deploy(
            device=interface_in.device,
            configuration=genconf.generate(template_name="interface_add",infos=interface_in,outputType="LIST")
            )
    logger.info(result_out)
    logger.info(interface_in)
    interface_out = get(device=interface_in.device,interface_port=interface_in.port)
    logger.info(interface_out)
    return interface_out

def delete(*, device: DeviceIn = None, interface_port: str) -> bool:
    interface = get(device=device,interface_port=interface_port)
    if interface:
        result,result_output=net.deploy(
                device=device,
                configuration=genconf.generate(template_name="interface_delete",infos=interface,outputType="LIST")
                )
        if result:
            return True
    return False




