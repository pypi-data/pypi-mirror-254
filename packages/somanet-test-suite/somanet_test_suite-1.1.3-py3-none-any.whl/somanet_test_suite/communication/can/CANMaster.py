# CiA402 CAN Master for PEAK Adapter

import logging
import time
import subprocess as sp
from enum import Enum
from typing import Union, Dict, Type, List, Callable

import canopen
from canopen.profiles.p402 import BaseNode402

from ..BaseCANOpen import BaseCANOpen

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)

class ExceptionCAN(Exception):
    pass


class States(Enum):
    BOOT = 'BOOT' # Custom state
    INIT = 'INITIALISING'
    PREOP = 'PRE-OPERATIONAL'
    OP = 'OPERATIONAL'
    STOPPED = 'STOPPED'
    SLEEP = 'SLEEP'
    STANDBY = 'STANDBY'
    RESET = 'RESET'
    RESET_COMMUNICATION = 'RESET COMMUNICATION'


class CANMaster(BaseCANOpen):

    def __init__(self, eds_file: str, channel: str = "can0", bitrate: int = 1000000, same_node_version: bool = False):
        """

        Parameters
        ----------
        eds_file :
        channel :
        bitrate :
        """

        self.eds = eds_file
        self.channel = channel
        self._config_peak_can(channel, bitrate)
        self._network = canopen.Network()
        self._network.connect(channel=channel, bustype="socketcan", bitrate=bitrate)

        if same_node_version:
            self.scan()



    def _config_peak_can(self, channel_name: str, bitrate: int):
        """

        Parameters
        ----------
        channel_name :
        bitrate :

        Returns
        -------

        """
        output = sp.check_output(f"sudo ip link show {channel_name}", shell=True).decode()
        if "qlen 1000" in output and "DOWN" in output:
            print("set interface up")
            self._set_interface_state(channel_name, "up")
            logger.debug("can is already configured.")
            return
        sp.call(["sudo", "modprobe", "peak_usb"])
        sp.call(["sudo", "modprobe", "peak_pci"])
        sp.call(["sudo", "ip", "link", "set", channel_name, "up", "type", "can", "bitrate", str(bitrate)])
        sp.call(["sudo", "ip", "link", "set", channel_name, "txqueuelen", "1000"])

    def _set_interface_state(self, channel_name: str, state: str):
        """

        Parameters
        ----------
        channel_name :
        state :

        Returns
        -------

        """
        sp.call(["sudo", "ip", "link", "set", channel_name, state])

    def _get_slave_id(self, slaveid: int = 0):
        """

        Parameters
        ----------
        slaveid :

        Returns
        -------

        """

        return slaveid + 1

    def scan(self):
        """

        Returns
        -------

        """
        self._network.scanner.search()
        time.sleep(0.05)
        _nodes = self._network.scanner.nodes
        logger.info(f"Found {len(_nodes)}")
        self._network.nodes.clear()
        for node_id in _nodes:
            self.add_node(node_id-1)

    def add_node(self, slaveid: int = 0, eds_file: str = None):
        """

        Parameters
        ----------
        slaveid :
        eds_file :

        Returns
        -------

        """
        if eds_file:
            _eds = eds_file
        else:
            _eds = self.eds
        node = BaseNode402(self._get_slave_id(slaveid), _eds)
        self._network.add_node(node)
        return node

    def upload(self, index: int, subindex: int, slaveid: int = 0) -> Union[str, float, int, bool]:
        """

        Parameters
        ----------
        index :
        subindex :
        slaveid :

        Returns
        -------

        """
        slaveid = self._get_slave_id(slaveid)
        _node = self._network.nodes[slaveid]
        var = _node.sdo[index]
        if isinstance(var, (canopen.sdo.base.Array, canopen.sdo.base.Record)):
            if subindex > var[0].raw:
                raise ExceptionCAN(f"Subindex {subindex} does not exists in object 0x{index:04x}")
            return var[subindex].raw
        else:
            return var.raw

    def download(self, index: int, subindex: int, value: Union[str, int, float, bool], slaveid: int = 0):
        """

        Parameters
        ----------
        index :
        subindex :
        value :
        slaveid :

        Returns
        -------

        """
        slaveid = self._get_slave_id(slaveid)
        _node = self._network.nodes[slaveid]
        var = _node.sdo[index]
        if isinstance(var, (canopen.sdo.base.Array, canopen.sdo.base.Record)):
            if subindex > var[0].raw:
                raise ExceptionCAN(f"Subindex {subindex} does not exists in object 0x{index:04x}")
            var[subindex].raw = value
        else:
            var.raw = value

    def _setup_pdo(self, pdo_type: str, pdo_index: int, objects: List[str], trans_type: int, even_timer: int = None, slaveid: int = 0):
        """

        Parameters
        ----------
        pdo_type :
        pdo_index :
        objects :
        trans_type :
        even_timer :
        slaveid :

        Returns
        -------

        """
        if pdo_index <= 0:
            raise ExceptionCAN("PDO index starts at 1")
        slaveid = self._get_slave_id(slaveid)
        _node = self._network.nodes[slaveid]
        _pdo_obj = getattr(_node, pdo_type)[pdo_index]
        _pdo_obj.read()
        _pdo_obj.clear()
        if not objects:
            return

        for name in objects:
            _pdo_obj.add_variable(name)
        _pdo_obj.trans_type = trans_type
        if even_timer:
            _pdo_obj.event_timer = even_timer
        _pdo_obj.enabled = True
        _pdo_obj.save()

    def setup_tpdo(self, pdo_index: int, objects: List[str] = None, trans_type: int = None, even_timer: int = None):
        """

        Parameters
        ----------
        pdo_index :
        objects :
        trans_type :
        even_timer :

        Returns
        -------

        """
        self._setup_pdo("tpdo", pdo_index, objects, trans_type, even_timer)

    def setup_rpdo(self, pdo_index: int, objects: List[str] = None, trans_type: int = None, even_timer: int = None):
        """

        Parameters
        ----------
        pdo_index :
        objects :
        trans_type :
        even_timer :

        Returns
        -------

        """
        self._setup_pdo("rpdo", pdo_index, objects, trans_type, even_timer)

    def start_pdo_com(self, pdo_id: int, time: int, slaveid: int = 0):
        """

        Parameters
        ----------
        pdo_id :
        time :
        slaveid :

        Returns
        -------

        """
        slaveid = self._get_slave_id(slaveid)
        _node = self._network.nodes[slaveid]
        _node.rpdo[pdo_id].start(time)

    def stop_pdo_com(self, pdo_id: int, slaveid: int = 0):
        """

        Parameters
        ----------
        pdo_id :
        slaveid :

        Returns
        -------

        """
        slaveid = self._get_slave_id(slaveid)
        _node = self._network.nodes[slaveid]
        _node.rpdo[pdo_id].stop()

    def set_state(self, state: States, slaveid: int = None):
        """

        Parameters
        ----------
        state :
        slaveid :

        Returns
        -------

        """
        if slaveid is None:
            self._network.nmt.state = state.value
        else:
            slaveid = self._get_slave_id(slaveid)
            self._network.nodes[slaveid].nmt.state = state.value

    def get_state(self, slaveid: int = None) -> States:
        """

        Parameters
        ----------
        slaveid :

        Returns
        -------

        """
        if slaveid is None:
            return States[self._network.nmt.state]
        else:
            slaveid = self._get_slave_id(slaveid)
            return States[self._network.nodes[slaveid].nmt.state]


    def exchange_pdo(self, slaveid: int = 0, **kwargs) -> Dict[str, Union[int, str, float]]:
        """

        Parameters
        ----------
        slaveid :
        kwargs :

        Returns
        -------

        """
        slaveid = self._get_slave_id(slaveid)
        if kwargs:
            _rpdo = self._network.nodes[slaveid].rpdo
            for name, value in kwargs.items():
                _rpdo[name.replace("_", " ")].raw = value

        _tpdo = self._network.nodes[slaveid].tpdo
        ret_dict = {}
        for entry in _tpdo.values():
            for pdo in entry:
                ret_dict[pdo.name] = pdo.raw
        return ret_dict

    # def file_write(self, filepath: str, cmd: str = None, slaveid: int = 0) -> bool:
    #     """
    #
    #     Parameters
    #     ----------
    #     filepath :
    #     cmd :
    #     slaveid :
    #
    #     Returns
    #     -------
    #
    #     """
    #     # try:
    #     #     self.file_handler.__write_file(cmd, filepath)
    #     # except Exception as e:
    #     #     logger.error(str(e))
    #     #     return False
    #     #
    #     # return True
    #     pass
    #
    # def file_read(self, cmd: str, output: Union[Type[str], Type[bytes]] = bytes, slaveid: int = 0) -> Union[bool, bytes, str]:
    #     """
    #
    #     Parameters
    #     ----------
    #     cmd :
    #     output :
    #     slaveid :
    #
    #     Returns
    #     -------
    #
    #     """
    #     # cmd, file = cmd.split("=")
    #     # if cmd == "fs-getlist":
    #     #     return self.file_handler.get_list()
    #     # elif cmd == "fs-remove":
    #     #     return self.file_handler.remove([file])
    #     # else:
    #     #     return self.file_handler.read_file([cmd])
    #     pass


    def disconnect(self):
        """

        Returns
        -------

        """
        self._network.disconnect()
        self._set_interface_state(self.channel, "down")
