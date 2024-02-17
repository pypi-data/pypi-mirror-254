import logging
import os
import re
import subprocess as sp
import sys
import time
from typing import Union, Type, List, Literal

from ..esi import ESI
from ..BaseEtherCAT import BaseEtherCAT, ExceptionEtherCAT, EcStates, EcTypes, WatchdogRegs

__all__ = [
    "IgHMaster",
    "EcTypes"
]

logger = logging.getLogger(__file__)
logging.basicConfig(format='[%(levelname)s] %(message)s')

if sys.platform != 'linux':
    exit(1)

# start / stop ethercat kernel module (run as root!)
# IgH EtherCAT master must be installed
ecat_master = "/etc/init.d/ethercat"

# ethercat control command
ETHERCAT_PATH = "/opt/etherlab/bin/ethercat"


if not os.path.isfile(ETHERCAT_PATH):
    logger.warning('EtherCAT Master IgH is not installed.\n'
                   'To install IgH go to "https://github.com/synapticon/Etherlab_EtherCAT_Master/releases".')

SyncManager = {
    "MBoxIn":    0,
    "MBoxOut":   1,
    "BufferIn":  2,
    "BufferOut": 3
}

ECAT_TIMEOUT = 10  # seconds


class IgHMaster(BaseEtherCAT):
    """
    Base Class to communicate with the IgH EtherCAT Master. This class supports
    start and stop of the kernel modules and accesses low level EtherCAT functions.

    Dependencies:
    - IgH EtherCAT Master (with Synapticon patches)
    - Synapticons siitool
    """

    ETHERCAT_PATH: str = ETHERCAT_PATH

    def __init__(self, esi_file: str = None):
        """
        Init Ethercat Module.
        Prints error (No exception on purpose), if IgH is not installed

        """
        super().__init__(False, False)

        if not os.path.isfile(self.ETHERCAT_PATH):
            logger.error('EtherCAT Master IgH is not installed.\n'
                         'To install IgH go to "https://github.com/synapticon/Etherlab_EtherCAT_Master/releases".')

        if esi_file is not None:
            self.esi = ESI(esi_file)

        self.active = False
        self.siiprint = ""
        self._re_int_value = re.compile(r'(0x\w+ )?(-?\d+)')
        self._re_float_value = re.compile(r'(-?\d+.\d+)')

    def start(self) -> None:
        """
        Starts IgH Ethercat Master
        """
        self.active = sp.call(["sudo", ecat_master, "start"], stdout=sp.DEVNULL)

    def stop(self) -> None:
        """
        Stops IgH Ethercat Master
        """
        if sp.call(["sudo", ecat_master, "stop"], stdout=sp.DEVNULL):
            self.active = False

    def restart(self) -> None:
        """
        Restarts IgH Ethercat Master
        """
        self.stop()
        self.start()

    def is_active(self) -> bool:
        """
        Tests, if the communication is active.

        Returns
        -------
        bool
            True, if communication with slave is possible.
        """

        command = f"sudo {self.ETHERCAT_PATH} slaves"
        try:
            res_str = sp.check_output(command, shell=True, stderr=sp.STDOUT)
        except sp.CalledProcessError as e:
            res_str = e.output

        return 'Failed' not in res_str.decode()

    def set_state(self, state: EcStates, timeout: int = 10, slaveid: int = 0) -> bool:
        """
        Set Ethercat state. Possible EcStates are "INIT", "PREOP", "BOOT", "SAFEOP" or "OP".

        Parameters
        ----------
        state : str
            Desired state.
        timeout : int
            Amount of seconds when timeout hits.
        slaveid : int
            Slave ID. First slave = 0.

        Raises
        ------
            ExceptionEtherCAT: If invalid state was requested.
            ExceptionEtherCAT: If not able to set the state.
            ExceptionEtherCAT: If timeout occurred.

        Returns
        -------
        bool
            True, if new state was set.

        """

        command = f"sudo {self.ETHERCAT_PATH} state -p {slaveid} {state.name}"

        t0 = time.time()
        act_state = EcStates.NONE
        while act_state != state:
            if sp.call(command, stdout=sp.DEVNULL, shell=True) != 0:
                raise ExceptionEtherCAT(f'Set State {state.name}')

            act_state = self.get_state(slaveid)

            if timeout == 0:
                return act_state == state

            if time.time() - t0 > timeout:
                raise ExceptionEtherCAT(f'Timeout: Set State {state.name}')

        return act_state == state

    def get_state(self, slaveid: int = 0) -> EcStates:
        """
        Get current state of specific slave.

        Parameters
        ----------
        slaveid : int
            Slave ID

        Returns
        -------
        str
            Current state.

        """
        command = f"sudo {self.ETHERCAT_PATH} slaves -p {slaveid}"
        state_string = sp.check_output(command,
                                       universal_newlines=True,
                                       shell=True)
        res = re.match(r'\d *\d+:\d+ +(.+?) +. (.+$)', state_string)
        if res:
            state = res.group(1)
            if state.lower() == "init+error":
                state = "INIT"
            return EcStates[state]
        return EcStates.NONE

    def slaves(self) -> int:
        """
        Return amount of connected slaves.

        Returns
        -------
        int
        """
        command = f"sudo {self.ETHERCAT_PATH} slaves | wc -l"
        slavecount = sp.check_output(command,
                                     universal_newlines=True,
                                     shell=True)
        return int(slavecount)

    def sii_read(self, slaveid: int = 0) -> str:
        """
        Read SII content from EtherCAT IC. Processed by siitool.

        Parameters
        ----------
        slaveid : int
            Slave ID

        Returns
        -------
        str
            Output from siitool.

        """
        command = f"sudo {self.ETHERCAT_PATH} sii_read -p {slaveid} | siitool -p"
        self.siiprint = sp.check_output(command, universal_newlines=True, shell=True)

        return self.siiprint

    def sii_write(self, filepath: str = "somanet_cia402.sii", slaveid: int = 0) -> bool:
        """
        Writes SII file to EtherCAT IC.

        Parameters
        ----------
        filepath : str
            Path to SII file.
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionEtherCAT: If file does not exist.
            ExceptionEtherCAT: If not able to set the alias.

        Returns
        -------
        bool
            True, if successfully written.

        """
        if not os.path.exists(filepath):
            raise ExceptionEtherCAT(f"File '{filepath}' not found.")

        command = f"sudo {self.ETHERCAT_PATH} alias -f -p {slaveid} 0"

        if sp.call(command, stdout=sp.DEVNULL, shell=True, timeout=20) != 0:
            raise ExceptionEtherCAT("Cannot set alias")

        command = f"sudo {self.ETHERCAT_PATH} sii_write -f -p {slaveid} {filepath}"

        return sp.call(command, stdout=sp.DEVNULL, shell=True, timeout=60) == 0

    def file_write(self, filepath: str, filename: str = None, slaveid: int = 0) -> bool:
        """
        Writes file to EtherCAT slave.

        Parameters
        ----------
        filepath : str
            File path.
        filename : str
            Alternative file name on target slave.
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionEtherCAT: If file not exists.
            ExceptionEtherCAT: If path leads not to a file.

        Returns
        -------
        bool
            True, if successfully written.

        """
        if not os.path.exists(filepath):
            raise ExceptionEtherCAT(f"No valid file path: {filepath}")

        if not os.path.isfile(filepath):
            raise ExceptionEtherCAT(f"Not a valid file: {filepath}")

        command = f"sudo {self.ETHERCAT_PATH} foe_write -p {slaveid} {filepath}"

        if filename is not None:
            command += f' -o {filename}'

        logger.debug(f"[foe_write] Command: {command}")

        return sp.call(command, stdout=sp.DEVNULL, shell=True) == 0

    def file_read(self, cmd: str, output: Union[Type[str], Type[bytes]] = bytes, slaveid: int = 0) -> Union[bool, bytes, str]:

        """
        Reads file from EtherCAT slave.

        Parameters
        ----------
        cmd : str
            Read command or file name.
        output : Union[Type[str], Type[bytes]]
            Output format. Use literal str/bytes objects. If None, returns bool
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionEtherCAT: If reading file failed
            ExceptionEtherCAT: If output type is unknown.

        Returns
        -------
        Union[bool, bytes, str]
            True, if no output is required and file was successfully read.
            Otherwise output in bytes or str
        """
        command = f"sudo {self.ETHERCAT_PATH} foe_read -p {slaveid} {cmd}"
        logger.debug(f"[foe_read] Command: {command}")
        if output is not None:
            try:
                f = sp.check_output(command, shell=True, stderr=sp.STDOUT)
            except sp.CalledProcessError as e:
                raise ExceptionEtherCAT(e.output.decode())

            if output is str:
                return f.decode()
            elif output is bytes:
                return f
            else:
                raise ExceptionEtherCAT(f"Unknown output type {output}")
        else:
            return sp.call(command, stdout=sp.DEVNULL, shell=True) == 0

    def upload(self, index: int, subindex: int, type: EcTypes = None, error: bool = True, slaveid: int = 0) -> Union[int, float, str, bytes]:
        """
        Reads object from object dictionary.
        Converts int or float objects to corresponding types.

        Parameters
        ----------
        index : int
            Dictionary index
        subindex : int
            Dictionary subindex
        type : EcTypes
            Dictionary data type.
        error : bool
            If True, then show error message during upload.
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionEtherCAT: If data type is invalid.

        Returns
        -------
        Union[int, float, str]
            Integer, floating point or string object.

        """
        _type = ""
        if type is not None:
            _type = f"--type {type.name}"
        elif hasattr(self, "esi"):
            esi_type = self.esi[index][subindex].Type
            _type = f"--type {esi_type}"

        command = f"sudo {self.ETHERCAT_PATH} upload -p {slaveid} 0x{index:x} {subindex} {_type}"

        if error:
            _err = sp.STDOUT
        else:
            _err = sp.DEVNULL

        try:
            output = sp.check_output(command, shell=True, stderr=_err)
        except sp.CalledProcessError as e:
            msg = f"{e.output.decode().strip()}: 0x{index:x}:{subindex}"
            raise ExceptionEtherCAT(msg)

        if type == EcTypes.OCTET_STRING:
            return output

        # Try to decode the output. If not possible return the output directly. Then it's no string.
        try:
            output = output.decode().strip().strip("\x00")
        except UnicodeDecodeError:
            return output

        if type == EcTypes.STRING:
            return output

        # Check if output is a integer.
        res = self._re_int_value.match(output)
        if res:
            # return Int value
            return int(res.group(2))

        # Check if output is a float.
        res = self._re_float_value.match(output)
        if res:
            return float(res.group(1))

        # Return string.
        return output.strip()

    def download(self, index: int, subindex: int, value: Union[str, int, float, bytes], type: EcTypes = None, slaveid: int = 0) -> bool:
        """
        Write new value to object dictionary.

        Parameters
        ----------
        index : int
            Dictionary index
        subindex : int
            Dictionary subindex
        value : Union[str, int, float]
            New value.
        type : EcTypes
            Dictionary data type.
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionEtherCAT: If data type is invalid.

        Returns
        -------
        bool
            True, if successfully written.

        """
        _type = ""
        if type is not None:
            _type = f"--type {type.name}"
        elif hasattr(self, "esi"):
            esi_type = self.esi[index][subindex].Type
            _type = f"--type {esi_type}"

        if isinstance(value, bytes):
            value = "0x" + "".join(f"{b:02x}" for b in reversed(value))

        command = f"sudo {self.ETHERCAT_PATH} download -p {slaveid} 0x{index:x} {subindex} {value} {_type}"

        try:
            res = sp.call(command, stdout=sp.DEVNULL, stderr=sp.STDOUT, shell=True) == 0
        except sp.CalledProcessError as e:
            msg = f"{e.output.decode().strip()}: 0x{index:x}:{subindex}"
            raise ExceptionEtherCAT(msg)
        return res

    def reg_write(self, address: int, data: int, type: EcTypes = None, slaveid: int = 0) -> bool:
        """
        Write to register on EtherCAT IC.

        Parameters
        ----------
        address : int
            Start address
        data : Union[int, bytes]
            Data to written to register.
        type : EcTypes
            Data type of "data"
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        bool
            True, otherwise an exception will rise.
        """
        _type = ""
        if type is not None:
            _type = f"--type {type.name}"

        command = f"sudo {self.ETHERCAT_PATH} reg_write -p {slaveid} 0x{address:x} {data} {_type}"

        try:
            res = sp.call(command, stdout=sp.DEVNULL, stderr=sp.STDOUT, shell=True) == 0
        except sp.CalledProcessError as e:
            raise ExceptionEtherCAT(e.output.decode())
        return res

    def reg_read(self, address: int, byte_amount: int, slaveid: int = 0) -> bytes:
        """
        Read register on EtherCAT IC.

        Parameters
        ----------
        address : int
            Start address
        size : int
            Amount of bytes
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        bytes
            Read register content

        """
        command = f"sudo {self.ETHERCAT_PATH} reg_read -p {slaveid} 0x{address:x} {byte_amount}"

        try:
            output = sp.check_output(command, shell=True, stderr=sp.STDOUT)
        except sp.CalledProcessError as e:
            raise ExceptionEtherCAT(e.output.decode())

        return b"".join([int(byte, 16).to_bytes(1, "little") for byte in output.decode().split()])

    def set_watchdog(self, wd_type: Literal["pdi", "processdata"], wd_time_ms: float, slaveid: int = 0):
        """
        Set watchdog timer.

        Parameters
        ----------
        wd_type : Literal["pdi", "processdata"]
            Either "pdi" or "processdata"
        wd_time_ms : float
            Watchdog time in milliseconds
        slaveid : int
            Slave ID / position in the ethercat chain.
        """
        wd_div = int.from_bytes(self.reg_read(int(WatchdogRegs.WD_DIV.value), 2, slaveid),
                                byteorder="little", signed=False)

        wd_div_ns = 40 * (wd_div + 2)
        wd_time_reg = int((wd_time_ms * 1_000_000.0) / wd_div_ns)
        if wd_type == "pdi":
            wd_reg = WatchdogRegs.WD_TIME_PDI
        else:
            wd_reg = WatchdogRegs.WD_TIME_PROCESSDATA
        self.reg_write(int(wd_reg.value), wd_time_reg, EcTypes.UINT16, slaveid)
