import json
import logging
import time
from typing import Union, List

from .dataformat import *

logger = logging.getLogger(__file__)
logging.basicConfig(format='[%(levelname)s] %(message)s')


class BuildHardwareDescription:
    file_name = '.hardware_description'

    def __init__(self):
        self.device: DeviceInfo
        self.assembly: AssemblyInfo
        self.json_content: str

    def __generate_component(self, component: List[str]) -> ComponentInfo:
        """
        Create a new Component Info object and add information to it.

        Parameters
        ----------
        component : List[str]
            Tuple/list with component information.

        Returns
        -------
        ComponentInfo
            New ComponentInfo object
        """

        comp = ComponentInfo()
        comp.set_name(component[0])
        comp.set_version(component[1])
        comp.set_serial_number(component[2])
        return comp

    def __set_info(self, type: Union[DeviceInfo, AssemblyInfo], name: str, id: Union[int, str], version: Union[int, str], sn: str, components: List[List[str]]):
        """
        Set new Device or assembly info.

        Parameters
        ----------
        type : Union[DeviceInfo, AssemblyInfo]
            New Device or Assembly object
        name : str
            Assembly name
        id : str
            ID
        version : str
            Version
        sn : str
            serial number
        components : List[List[str]]
            List of components
        """
        type.set_name(name)
        type.set_id(id)
        type.set_version(version)
        type.set_serial_number(sn)
        if components:
            for c in components:
                type.add_component(self.__generate_component(c))

    def set_device(self, name: str,
                   id: Union[int, str],
                   version: Union[int, str],
                   sn: str,
                   components: List[List[str]],
                   mac: Union[int, str] = None,
                   key_id: str = None) -> bool:
        """
        Set Device info.

        Parameters
        ----------
        name : str
            Assembly name
        id : str
            ID
        version : str
            Version
        sn : str
            serial number
        components : List[List[str]]
            List of components
        mac : Union[int, str]
            MAC Address
        key_id: str
            Key ID for encryption key

        Returns
        -------
        bool
            True if successfully created.

        """
        try:
            self.device = DeviceInfo()
            if mac:
                self.device.set_mac_address(mac)
            if key_id:
                self.device.set_key_id(key_id)

            self.__set_info(self.device, name, id, version, sn, components)
        except ExceptionHardwareDescription as e:
            logger.error(e)
            return False
        return True

    def set_assembly(self, name: str, id: Union[int, str], version: Union[int, str], sn: str, components: List[List[str]] = None) -> bool:
        """
        Set assembly info.

        Parameters
        ----------
        name : str
            Assembly name
        id : str
            ID
        version : str
            Version
        sn : str
            serial number
        components : List[List[str]]
            List of components

        Returns
        -------
        bool
            True, if successfully created.

        """
        try:
            self.assembly = AssemblyInfo()
            self.__set_info(self.assembly, name, id, version, sn, components)
        except ExceptionHardwareDescription as e:
            logger.error(e)
            return False
        return True

    def generate(self, postfix: str = None, write_file: bool = True) -> Union[str, None]:
        """
        Generate new file.

        Parameters
        ----------
        postfix : str
            Optional postfix, concat to file name (e.g. timestamp)
        write_file : bool
            If true, create a JSON file with name .hardware_description_<postfix>.

        Returns
        -------
        Union[str, None]
            JSON file content, if write_file is False, otherwise None.

        """
        # Create a new stack
        hw = HardwareDescription()
        hw.set_device(self.device)
        if hasattr(self, "assembly"):
            hw.set_assembly(self.assembly)

        # Log the results of the stack_info file.
        lines = str(hw).split('\n')

        for line in lines:
            logger.info(line)

        logger.info(hw)
        self.json_content = json.dumps(hw, ensure_ascii=False, default=lambda o: o.__dict__)
        logger.info(self.json_content)

        if not write_file:
            return self.json_content

        if postfix:
            self.file_name += '_' + postfix
        # Write to a file
        with open(self.file_name, 'w') as hardware_description_file:
            hardware_description_file.write(self.json_content)

        return None
