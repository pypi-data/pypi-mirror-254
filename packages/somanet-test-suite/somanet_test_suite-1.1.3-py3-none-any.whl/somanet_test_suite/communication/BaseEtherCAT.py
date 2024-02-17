import logging
import time
from typing import Union, List, Dict, Literal
from pysoem import ec_datatype as ect
from enum import Enum

from .BaseCANOpen import BaseCANOpen, EcStates

from .BaseFileSystem import BaseFileSystem, SomanetFileSystem

logger = logging.getLogger(__file__)
logging.basicConfig(format='[%(levelname)s] %(message)s')

_types_ = {  # name, ESI name, bytesize, signed, bitstruct symbol
    ect.ECT_BOOLEAN:        ("bool", "BOOL", 1, True, 'b8'),
    ect.ECT_INTEGER8:       ("int8", "SINT", 1, True, 's8'),
    ect.ECT_INTEGER16:      ("int16", "INT", 2, True, 's16'),
    ect.ECT_INTEGER32:      ("int32", "DINT", 4, True, 's32'),
    ect.ECT_INTEGER64:      ("int64", "LINT", 8, True, 's64'),
    ect.ECT_UNSIGNED8:      ("uint8", "USINT", 1, False, 'u8'),
    ect.ECT_UNSIGNED16:     ("uint16", "UINT", 2, False, 'u16'),
    ect.ECT_UNSIGNED32:     ("uint32", "UDINT", 4, False, 'u32'),
    ect.ECT_UNSIGNED64:     ("uint64", "ULINT", 8, False, 'u64'),
    ect.ECT_REAL32:         ("float", "REAL", 4, True, 'f32'),
    ect.ECT_REAL64:         ("double", "DOUBLE", 8, True, 'f64'),
    ect.ECT_VISIBLE_STRING: ("string", "STRING", None, None, 't'),
    ect.ECT_OCTET_STRING:   ("octet_string", "OCTET_STRING", None, None, 't'),
    ect.ECT_UNICODE_STRING: ("unicode_string", "UNICODE_STRING", None, None, 't'),
    ect.ECT_BIT1:           ("bit1", "", 1, False, "u1"),
    ect.ECT_BIT2:           ("bit2", "", 1, False, None),
    ect.ECT_BIT3:           ("bit3", "", 1, False, None),
    ect.ECT_BIT4:           ("bit4", "", 1, False, None),
    ect.ECT_BIT5:           ("bit5", "", 1, False, None),
    ect.ECT_BIT6:           ("bit6", "", 1, False, None),
    ect.ECT_BIT7:           ("bit7", "", 1, False, None),
    ect.ECT_BIT8:           ("bit8", "", 1, False, None),
    0x21:                   ("pdo_mapping", "", None, False, None),
}

float_data_types = (ect.ECT_REAL32, ect.ECT_REAL64)
string_data_types = (ect.ECT_VISIBLE_STRING, ect.ECT_UNICODE_STRING)


class EcTypes(Enum):
    BOOL = ect.ECT_BOOLEAN
    INT8 = ect.ECT_INTEGER8
    INT16 = ect.ECT_INTEGER16
    INT32 = ect.ECT_INTEGER32
    INT64 = ect.ECT_INTEGER64
    UINT8 = ect.ECT_UNSIGNED8
    UINT16 = ect.ECT_UNSIGNED16
    UINT32 = ect.ECT_UNSIGNED32
    UINT64 = ect.ECT_UNSIGNED64
    FLOAT = ect.ECT_REAL32
    DOUBLE = ect.ECT_REAL64
    STRING = ect.ECT_VISIBLE_STRING
    OCTET_STRING = ect.ECT_OCTET_STRING
    UNICODE_STRING = ect.ECT_UNICODE_STRING
    BIT1 = ect.ECT_BIT1
    BIT2 = ect.ECT_BIT2
    BIT3 = ect.ECT_BIT3
    BIT4 = ect.ECT_BIT4
    BIT5 = ect.ECT_BIT5
    BIT6 = ect.ECT_BIT6
    BIT7 = ect.ECT_BIT7
    BIT8 = ect.ECT_BIT8
    PDO_MAPPING = 0x21

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __eq__(self, other):
        return self.value == other.value

    @property
    def name(self):
        return _types_[self.value][0]

    @property
    def esi_name(self):
        return _types_[self.value][1]

    @property
    def bytesize(self):
        return _types_[self.value][2]

    @property
    def signed(self):
        return _types_[self.value][3]

    @property
    def bitstruct_symbol(self):
        return _types_[self.value][4]

    @classmethod
    def get_datatype(cls, bytelength: int, signed: bool):
        for t in _types_.values():
            if t[2] == bytelength and t[3] == signed:
                return t

class WatchdogRegs(Enum):
    WD_DIV = 0x400
    WD_TIME_PDI = 0x410
    WD_TIME_PROCESSDATA = 0x420


class ExceptionEtherCAT(Exception):
    pass


class BaseEtherCAT(BaseFileSystem, BaseCANOpen, SomanetFileSystem):

    def __init__(self, show_log: bool, debug_log: bool):
        logger.propagate = show_log or debug_log
        logger.setLevel(logging.DEBUG if debug_log else logging.INFO)
        logger.debug("BaseEtherCAT DEBUG MODE")

    def reg_read(self, address: int, size: int, slaveid: int = 0) -> List[str]:
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

    def get_filesystem_info(self, slaveid: int = 0) -> Dict[str, int]:
        """
        Returns total, used and free memory on filesystem in bytes.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Raises
        ------
            ExceptionIgH: If not possible, to parse filesystem info message.

        Returns
        -------
        Dict[str, int]
            Dict with total and used amount of bytes.
        """
        info = self.file_read(cmd=f"fs-info", slaveid=slaveid, output=str).strip()
        return self._parse_filesystem_info(info)

    def get_filesystem_help(self, slaveid: int = 0) -> str:
        """
        Get filesystem help.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        str
            Help string.
        """
        help = self.file_read(cmd=f"fs-help", slaveid=slaveid, output=str).strip()
        return help

    def get_bootloader_version(self, slaveid: int = 0) -> str:
        """
        Returns the bootloader version. Sets automatically the BOOT state.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        str
            Bootloader version as string.
        """

        self.set_state(EcStates.BOOT, slaveid=slaveid)
        return self.file_read(cmd="bversion", slaveid=slaveid, output=str).strip()

    def get_bootloader_help(self, slaveid: int = 0) -> str:
        """
        Returns the bootloader help text. Sets automatically the BOOT state.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        str
            Bootloader help text.
        """

        self.set_state(EcStates.BOOT, slaveid=slaveid)
        return self.file_read(cmd="help", slaveid=slaveid, output=str).strip()

    def ls(self, slaveid: int = 0) -> Dict[str, Union[str, int]]:
        """
        List file system content on slave.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        Dict[str, Union[str, int]]
            Dictionary with filenames and file size.

        """
        res = self.file_read(cmd="fs-getlist", slaveid=slaveid, output=str).strip()
        return self._parse_file_list(res)

    def rm(self, filename: str, slaveid: int = 0) -> str:
        """
        Delete file from slave.

        Parameters
        ----------
        filename : str
            File name
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        str
        """

        return self.file_read(cmd=f"fs-remove={filename}", slaveid=slaveid, output=str).strip()

    def filesystem_unlock(self, password: str, slaveid: int = 0) -> str:
        """
        Unlocks the file protection. Necessary when deleting hidden files (.filename).

        Parameters
        ----------
        password: str
            Password to unlock the protection.
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        str
            Response message.
        """

        return self.file_read(cmd=f"fs-stackunlock={password}", slaveid=slaveid, output=str).strip()

    def flash_fw(self, filepath: str, slaveid: int = 0) -> bool:
        """
        Flash firmware to slave.
        Can be a binary file or a SOMANET firmware package.

        Attention: In case of a firmware package just the binary will be flashed.

        Parameters
        ----------
        filepath : str
            Path to firmware binary or package
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        bool
            True, if firmware was successfully written.

        """

        filepath = self._get_fw_file(filepath)

        logger.debug("Set BOOT state...")
        self.set_state(EcStates.BOOT, slaveid=slaveid)
        logger.debug(f"State is {self.get_state(slaveid=slaveid)}")

        time.sleep(0.1)
        logger.debug(f"Flash firmware... {filepath}")

        return self.file_write(slaveid=slaveid, filepath=filepath)

    def remove_fw(self, slaveid: int = 0) -> bool:
        """
        Remove FW from slave.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        bool
            True, if successfully deleted

        """
        with self._empty_app() as app:
            return self.flash_fw(slaveid=slaveid, filepath=app)

    def write_hardware_description(self, filepath: str, fs_unlock_password: str, slaveid: int = 0) -> bool:
        """
        Flash JSON file to servo drive.
        Includes verification of written content.

        Parameters
        ----------
        fs_unlock_password : str
            Password to unlock filesystem protection.

        Returns
        -------
        bool
            True, if successfully written.

        """
        file_name = ".hardware_description"

        with open(filepath, "r") as f:
            file_content = f.read()

        try:
            if not self.set_state(EcStates.BOOT, timeout=5, slaveid=slaveid):
                raise ExceptionEtherCAT('Set slave to state BOOT failed')

            time.sleep(0.1)

            if not self.filesystem_unlock(fs_unlock_password):
                raise ExceptionEtherCAT('Unlock stack failed')

            time.sleep(0.1)

            if not self.file_write(filepath=filepath, filename=file_name):
                raise ExceptionEtherCAT('Writing file failed')

            time.sleep(0.1)

            read_json = self.file_read(file_name, output=str)
            if read_json != file_content:
                logger.debug(read_json)
                logger.debug(file_content)
                raise ExceptionEtherCAT('Files doesn\'t match')

        except ExceptionEtherCAT as e:
            logger.error(e)
            logger.error("The file was not successfully flashed to the stack.")
            return False
        return True
