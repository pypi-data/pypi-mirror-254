import copy
import logging
import os
import struct
import threading
import time
from collections import namedtuple, OrderedDict
from typing import List, Union, Type, Dict, Tuple, Literal

import bitstruct
import pysoem
from elevate import elevate

from ..BaseEtherCAT import BaseEtherCAT, ExceptionEtherCAT, EcStates, EcTypes, float_data_types, string_data_types

logging.basicConfig(format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


class ExceptionTimeout(ExceptionEtherCAT):
    pass


class Node:
    od: List = None
    txpdo_pattern: str = None
    txpdo_dict: Dict = None
    rxpdo_pattern: str = None
    rxpdo_dict: Dict = None


class SOEMMaster(BaseEtherCAT):
    byteorder: Literal["little", "big"] = "little"

    timeout_foe: int = 1e7  # µs
    timeout_rx_pdo: int = 100000  # µs

    loop_time: int = 1_000_000  # nsec -> 1 ms
    # one loop is still too long.
    time_calibration: float = -0.00007  # seconds

    retry_count = 3

    def __init__(self, interface: str, show_log: bool = False, debug_log: bool = False, name: str = "Generic"):
        """
        Init SOEM Master.

        Parameters
        ----------
        interface : str
            Name of interface
        show_log : bool
            Show logging messages.
        debug_log : bool
            Show debug messages
        """
        elevate(graphical=False)
        self._pd_thread_running = threading.Event()
        self._ch_thread_running = threading.Event()
        self._actual_wkc = 0
        self._config_map_done = False
        self._od = {}

        self._name = name

        self.threads_running = False

        self._master = pysoem.Master()
        self._master.in_op = False
        self._master.do_check_state = False
        self._master.open(interface)

        super().__init__(show_log, debug_log)
        logger.propagate = show_log or debug_log
        logger.setLevel(logging.DEBUG if debug_log else logging.INFO)

        if debug_log:
            logger.debug("DEBUG MODE")

        if not self._master.state in EcStates._value2member_map_ or self._master.state == EcStates.NONE.value:
            self._master.state = EcStates.INIT.value
            self._master.write_state()

    def init(self, setup_pdo: bool = True, **kwargs):
        """
        Initialize all slaves.

        Parameters
        ----------
        setup_pdo : bool
            Configure PDOs
        """
        self._master.slaves = []
        self._master.config_init()

        if self.get_slave_count() == 0:
            raise ExceptionEtherCAT("No slaves connected")

        for i in range(self.get_slave_count()):
            self.set_state(EcStates.INIT, slaveid=i, timeout=2)

        self._nodes = []

        for slv in range(self.get_slave_count()):
            self._nodes.append(Node())

        if kwargs:
            # Set callback fx which configures the slave.
            for product_code, cb_function in kwargs.items():
                for slave in self._master.slaves:
                    if slave.name.lower() == product_code.lower():
                        slave.config_func = cb_function

        if setup_pdo or kwargs:
            logger.debug("Set state PREOP")
            for i in range(self.get_slave_count()):
                self.set_state(EcStates.PREOP, slaveid=i, timeout=2)

            # Configures Sync manager, FMMU, etc. and PDO mapping.
            try:
                self._master.config_map()
            except Exception as e:
                logger.warning(str(e))

            logger.debug("Set state SAFEOP")
            for i in range(self.get_slave_count()):
                self.set_state(EcStates.SAFEOP, slaveid=i, timeout=2)

    def rescan(self, setup_pdo: bool = True):
        """
        Rescan network. Actually just an init() call.

        Parameters
        ----------
        setup_pdo : bool
            Configure PDOs
        """
        self.init(setup_pdo)

    def close(self):
        """
        Close connection. Stops also possible PDO communication.
        """
        self.stop_pdo_com()
        self._master.close()

    def _get_slave(self, slaveid: int) -> pysoem.CdefSlave:
        """
        Get slave.

        Parameters
        ----------
        slaveid : int
            Position in EtherCAT chain.

        Returns
        -------
        CdefSlave
            Slave in position <slaveid>

        """
        if slaveid > self.get_slave_count() - 1:
            raise ExceptionEtherCAT(f"ID {slaveid} does not exists. There are {self.get_slave_count()} nodes connected.")
        return self._master.slaves[slaveid]

    def _change_state(self, state: EcStates, timeout: float = 10.0, slaveid: int = 0) -> bool:
        """
        Change the state of a slave

        Parameters
        ----------
        state : EcStates
            Requested Ethercat State
        timeout : float
            Timeout in seconds
        slaveid : int
            Slave ID / position in the ethercat chain.

        Raises
        ------
        ExceptionTimeout: When timeout occurs during state change.

        Returns
        -------
        bool
            True, if state change was successful.

        """

        slave = self._get_slave(slaveid)

        # curr_master_state = EcStates(self._master.state)
        curr_slave_state, error_state = self.get_state(slaveid)
        logger.debug(f"Slave state: {curr_slave_state}, Error: {error_state}")
        t0 = time.time()

        error_acked = False
        while True:
            raw_state = slave.state
            curr_slave_state, error_state = EcStates.get_seperate_state(slave.state)

            if error_state == EcStates.ERROR and not error_acked:
                logger.debug("Reset Error")
                new_state = pysoem.STATE_ACK + state.value
                slave.state = new_state
                error_acked = True
            else:
                new_state = state.value
                slave.state = new_state

            logger.debug(f"Master: {EcStates(self._master.state)}, "
                         f"Slave: {slave.name}, "
                         f"Req: {state} (0x{new_state:x}), "
                         f"Curr: {curr_slave_state} (0x{curr_slave_state.value:x}), "
                         f"Raw: 0x{raw_state:x}, "
                         f"Error: {error_state}, "
                         f"{curr_slave_state == state}")

            slave.write_state()
            slave.state_check(new_state, 50000)

            if curr_slave_state == state and error_state.value == 0:
                break

            if time.time() - t0 > timeout:
                raise ExceptionTimeout(f"Timeout ({timeout}s) during setting state {state} for {slave.name}")

        return curr_slave_state == state

    def get_state(self, slaveid: int = 0) -> Tuple[EcStates, EcStates]:
        """
        Get EtherCAT state of slave <slaveid>.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        Tuple[EcStates, EcStates]
            Returns two EcStates: Regular Ethercat State and the Error "State"

        """
        curr_state = self._get_slave(slaveid).state
        return EcStates.get_seperate_state(curr_state)

    def set_state(self, state: EcStates, timeout: float = 10.0, slaveid: int = 0) -> bool:
        """
        Set state for slave <slaveid>

        Parameters
        ----------
        state : EcStates
            Requested state.
        timeout: float
            Timeout in seconds.
        slaveid : int
            Slave ID / position in the ethercat chain.
        Returns
        -------
        bool
            True, if state was successfully changed.
        """
        requested_state = state
        current_state, error_state = self.get_state(slaveid)
        if current_state == state and not error_state:
            return True
        elif current_state == EcStates.NONE:
            self.rescan()

        al_status = self._get_slave(slaveid)._get_al_status()
        logger.debug(f"AL status: {al_status}")

        if al_status != 0x0:
            self._change_state(EcStates.INIT, timeout, slaveid=slaveid)

        # If req EcStates is BOOT or node is currently in BOOT, go to INIT first.
        if requested_state == EcStates.BOOT or (requested_state != EcStates.BOOT and current_state == EcStates.BOOT):
            logger.debug(f"Change state 1")
            self._change_state(EcStates.INIT, timeout, slaveid=slaveid)

        if requested_state == EcStates.SAFEOP and current_state != EcStates.SAFEOP:
            if current_state == EcStates.INIT:
                self._change_state(EcStates.PREOP, timeout, slaveid=slaveid)
                logger.debug(f"Change state 2")

        if requested_state == EcStates.OP and current_state != EcStates.OP:
            if current_state == EcStates.INIT:
                self._change_state(EcStates.PREOP, timeout, slaveid=slaveid)
                logger.debug(f"Change state 2")
            if current_state == EcStates.PREOP:
                self._change_state(EcStates.SAFEOP, timeout, slaveid=slaveid)
                logger.debug(f"Change state 3")

        logger.debug(f"Change state 4")
        return self._change_state(state, timeout, slaveid=slaveid)

    def get_slave_count(self) -> int:
        """
        Get amounts of slaves

        Returns
        -------
        int
            Amount slaves.
        """
        return len(self._master.slaves)

    def reconfig(self, timeout: float = 0.5, slaveid: int = 0) -> EcStates:
        """
        Reconfigure slave at <slaveid>

        Parameters
        ----------
        timeout : float
            Timeout in seconds
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        EcStates
            Current state of reconfigures slave.

        """
        return EcStates(self._get_slave(slaveid).reconfig(int(timeout * 1000)))

    def slaves(self):
        """
        Print state of all connected slaves.
        """

        for i, slv in enumerate(self._master.slaves):
            state_string = self.get_state(i)
            al_status = slv._get_al_status()
            print(f"{i} - {slv.name}: {state_string}, <0x{al_status:x}> \"{pysoem.al_status_code_to_string(al_status)}\"")

    def reg_read(self, address: int, size: int, slaveid: int = 0) -> bytes:
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
        slave = self._get_slave(slaveid)
        res = slave._fprd(address, size)
        return res

    def reg_write(self, address: int, data: Union[int, bytes], type: EcTypes = None, slaveid: int = 0) -> bool:
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
        slave = self._get_slave(slaveid)
        if isinstance(data, int):
            byte_content = data.to_bytes(type.bytesize, self.byteorder, signed=type.signed)
        elif isinstance(data, bytes):
            byte_content = data
        else:
            raise TypeError("Wrong type for data")

        slave._fpwr(address, byte_content)
        return True

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
        slave = self._get_slave(slaveid)
        slave.set_watchdog(wd_type, wd_time_ms)

    def file_write(self, filepath: str = None, filename: str = None, content: Union[str, bytes] = None, slaveid: int = 0) -> bool:
        """
        Write file to slave.

        Parameters
        ----------
        filepath : str
            Path to file.
        filename : str
            File name.
        slaveid : int
            Slave ID / position in the ethercat chain.

        Raises
        ------
        ExceptionEtherCAT
            If file is not existing.

        Returns
        -------
        bool
            True, if file was successfully written.
        """
        if filepath is None and content is None:
            raise ExceptionEtherCAT(f"Either a file path or file content must be provided. Both are null.")

        if filepath is not None and not os.path.exists(filepath):
            raise ExceptionEtherCAT(f"{filepath} does not exists")

        if filepath is not None:
            if filename is None:
                filename = os.path.basename(filepath)
            logger.debug(f"filepath: {filepath}, filename: {filename}")

            with open(filepath, "rb") as file:
                file_data = file.read()
        else:
            file_data = content

        if len(file_data) < 500:
            logger.debug(f"File name: {filename}, Content: {file_data}")

        try:
            to = int((len(file_data) / 1024) * 1e6 / 10)  # timeout in µs. 1 second / kbyte
            to = to if to > self.timeout_foe else self.timeout_foe
            logger.debug(f"Timeout: {to}, file size: {len(file_data)}")
            result = self._get_slave(slaveid).foe_write(filename, 0, file_data, to)
        except pysoem.MailboxError as e:
            logger.warning(str(e))
            return False

        logger.debug(f"WKC: {result}, expected: {self._master.expected_wkc}")
        return result > 0

    def file_read(self, cmd: str, output: Union[Type[str], Type[bytes]] = bytes, slaveid: int = 0) -> Union[bytes, str]:
        """
        Read file from slave / send filesystem command to slave.

        Parameters
        ----------
        cmd : str
            Filesystem command
        output : Union[Type[str], Type[bytes]]
            Output format. Either as str or as bytes.
        slaveid : int
            Slave ID / position in the ethercat chain.

        Raises
        ------
        ExceptionEtherCAT
            If "output" type is unknown.

        Returns
        -------
        Union[bytes, str]
            File content.
        """
        max_file_size = 10_000
        file_output = self._get_slave(slaveid).foe_read(cmd, 0, max_file_size, self.timeout_foe)

        if output is str:
            try:
                return file_output.decode()
            except UnicodeDecodeError:
                return file_output
        elif output is bytes:
            return file_output

        raise ExceptionEtherCAT(f"Unknown output type {output}")

    def sdos(self, slaveid: int = 0):
        """
        Print the object dictionary of the slave.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.
        """

        self._od[slaveid] = self._get_slave(slaveid).od
        for o in self._od[slaveid]:
            _subindex = 0
            print(f"SDO 0x{o.index:x}, \"{o.name}\"")

            if o.entries:
                for e in o.entries:
                    data_type = EcTypes(e.data_type).name if EcTypes.has_value(e.data_type) else 'N/A'
                    try:
                        value = str(self.upload(o.index, _subindex, slaveid=slaveid))
                    except:
                        value = None

                    try:
                        name = e.name
                    except:
                        name = "N/A"

                    print(f"  0x{o.index:x}:"
                          f"{_subindex:02x}, "
                          f"{data_type}, "
                          f"\"{name}\": "
                          f"{value}")
                    _subindex += 1
            else:
                data_type = EcTypes(o.data_type).name if EcTypes.has_value(o.data_type) else 'N/A'
                print(f"  0x{o.index:x}:{_subindex:02}, {data_type}, \"{o.name}\"")

    def sii_write(self, filepath: str, slaveid: int = 0) -> int:
        """
        Write SII to EEPROM.

        Parameters
        ----------
        filepath : str
            Path to SII file.
        slaveid : int
            Slave ID

        Raises
        ------
          ExceptionEtherCAT: If any exceptions raises.

        Returns
        -------
        int
            Bytes written
        """
        _slave = self._get_slave(slaveid)

        bytes_written = 0
        try:
            with open(filepath, "rb") as f:
                sii_cont = f.read()

            # Write always one word (2 bytes)
            for i in range(0, int(len(sii_cont) / 2)):
                to_write = sii_cont[i * 2:i * 2 + 2]
                logger.debug(f'{i:04x}:')
                logger.debug(f'|'.join('{_byte:02x}' for _byte in to_write))
                logger.debug(f'{i * 2:04x}:')
                _slave.eeprom_write(i, to_write)
                bytes_written += len(to_write)
        except Exception as e:
            raise ExceptionEtherCAT(e) from e

        return bytes_written

    def sii_read(self, slaveid: int = 0, read_size: int = 0x300, print_content: bool = False) -> bytes:
        """
        Read SII content from EEPROM.

        Parameters
        ----------
        slaveid : int
            Slave ID
        read_size : int
            Amount of bytes
        print_content : bool
            If true, print the SII content.

        Returns
        -------
        bytes
            EEPROM content

        """
        _slave = self._get_slave(slaveid)

        ba = bytes()

        for i in range(0, read_size, 2):
            eepr = _slave.eeprom_read(i)

            if print_content:
                print('{:04x}:'.format(i), end=' ')
                print('|'.join('{:02x}'.format(x) for x in eepr))

            ba += eepr
        return ba

    def _update_od(self, slaveid: int = 0):
        """
        Update the local copy of the object dictionary.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.
        """
        if self._nodes[slaveid].od is None:
            try:
                self._nodes[slaveid].od = self._get_slave(slaveid).od
            except pysoem.SdoInfoError as e:
                logger.debug(f"Slave {slaveid}: {e}")

    def _get_od_entry(self, index: int, slaveid: int):
        return list(filter(lambda e: e.index == index, self._nodes[slaveid].od))[0]

    def _get_datatype(self, index: int, subindex: int, slaveid: int) -> Tuple[str, int, bool, str]:
        """
        Get datatype for object dictionary entry.
        Parameters
        ----------
        index : int
            Index of entry
        subindex : int
            Sub-index of entry
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        Tuple[str, int, bool, str]
            Data type
        """

        self._update_od(slaveid)

        entry = self._get_od_entry(index, slaveid)

        logger.debug(f"Entry - Index: 0x{entry.index:x}, Name: {entry.name}, Datatype: {entry.data_type}")

        if subindex > 0:
            logger.debug(f"Subindex: {subindex}, Amount: {len(entry.entries)}")
            assert subindex < len(entry.entries), f"Subindex out of range: {subindex} > {len(entry.entries)}"
            _data_type = entry.entries[subindex].data_type
        else:
            _data_type = entry.data_type

        return _data_type

    def upload(self, index: int, subindex: int, type: EcTypes = None, error: bool = True, slaveid: int = 0) -> Union[int, float, str]:
        """
        Reads object from object dictionary.
        Converts int or float objects to corresponding types.

        Parameters
        ----------
        index : int
            Dictionary index
        subindex : int
            Dictionary subindex
        error : bool
            If True, then show error message during upload.
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionIgH: If data type is invalid.

        Returns
        -------
        Union[int, float, str]
            Integer, floating point or string object.

        """

        # Try n times to upload value if error occurs
        exception = None
        for _ in range(self.retry_count):
            try:
                output = self._get_slave(slaveid).sdo_read(index, subindex)
                break
            except Exception as e:
                exception = e
        else:
            raise exception

        logger.debug(f"Upload: 0x{index:x}:{subindex}, Raw Output: {output}")

        try:
            data_type = self._get_datatype(index, subindex, slaveid)

            if data_type in [0x8, 0x11]:
                return struct.unpack("f", output)[0]
            elif data_type in [0x9]:
                return output.decode().rstrip('\x00').strip()
            else:
                try:
                    signed = EcTypes(data_type).signed
                except:
                    logger.warning(f"Could not find data type {data_type}. Use unsigned as default.")
                    signed = False
                return int.from_bytes(output, byteorder=self.byteorder, signed=signed)
        except (KeyError, TypeError):
            return int.from_bytes(output, byteorder=self.byteorder, signed=False)

    def download(self, index: int, subindex: int, value: Union[str, int, float, bytes], type: EcTypes = None, slaveid: int = 0) -> None:
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
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionIgH: If data type is invalid.
        """

        if type:
            data_type = type
        else:
            data_type = self._get_datatype(index, subindex, slaveid)

        if isinstance(data_type, EcTypes):
            byte_size = data_type.bytesize
            signed = data_type.signed
        elif EcTypes.has_value(data_type):
            byte_size = EcTypes(data_type).bytesize
            signed = EcTypes(data_type).signed
        else:
            _entry = self._get_od_entry(index, slaveid)
            entry = _entry.entries[subindex]

            byte_size = int(entry.bit_length / 8) + 1
            logger.debug(f"name: {entry.name}, byte size: {byte_size}, bit length: {entry.bit_length}")
            signed = False

        if data_type in float_data_types:
            value = struct.pack("f", value)
        elif data_type in string_data_types:
            value = value.encode()
        elif not isinstance(value, bytes):
            logger.debug(f"Signed: {signed}, byte size: {byte_size}")
            value = int.to_bytes(value, byteorder=self.byteorder, signed=signed, length=byte_size)

        logger.debug(f"Download: 0x{index:x}:{subindex}: {value}")
        # Try n times to download value if error occurs
        exception = None
        for _ in range(self.retry_count):
            try:
                self._get_slave(slaveid).sdo_write(index, subindex, value)
                break
            except Exception as e:
                exception = e
        else:
            raise exception

    def _processdata_thread(self):
        """
        Thread for PDO communication
        """

        logger.debug(f"{self._name}:_processdata_thread started!")
        while self._pd_thread_running.is_set():
            t0 = time.time_ns()
            self._master.send_processdata()
            self._actual_wkc = self._master.receive_processdata(self.timeout_rx_pdo)

            if not self._actual_wkc == self._master.expected_wkc:
                logger.debug(f'{self._name}: incorrect wkc: act: {self._actual_wkc}, exp: {self._master.expected_wkc}')

            t_delta = time.time_ns() - t0
            wait_time = ((self.loop_time - t_delta) / 1e9)  # + self.time_calibration
            if wait_time > 0:
                time.sleep(wait_time)

            # logger.debug(f"wait time: {wait_time} s, delta: {t_delta / 1e9} s")
        logger.debug(f"{self._name}: _processdata_thread stopped!")

    def start_pdo_com(self, skip_setup_pdo: bool = False):
        """
        Start PDO and check thread.
        Sets state to PREOP and OP.

        Parameters
        ----------
        skip_setup_pdo : bool
            If true, don't setup PDOs.
        """
        for i in range(self.get_slave_count()):
            self.set_state(EcStates.PREOP, slaveid=i)

        if not skip_setup_pdo:
            for i in range(self.get_slave_count()):
                self.setup_pdos(i)

        for i in range(self.get_slave_count()):
            self.set_state(EcStates.OP, slaveid=i)

        if not self.threads_running:
            self._pd_thread_running.set()
            self._ch_thread_running.set()
            self.check_thread = threading.Thread(target=self._check_thread)
            self.check_thread.start()
            self.proc_thread = threading.Thread(target=self._processdata_thread)
            self.proc_thread.start()
            self.threads_running = True

        self._master.in_op = True

    def stop_pdo_com(self):
        """
        Stop PDO and check thread.
        """
        if not hasattr(self, "proc_thread"):
            return
        self._pd_thread_running.clear()
        self._ch_thread_running.clear()
        self.proc_thread.join()
        self.check_thread.join()
        self.threads_running = False
        self._master.in_op = False
        logger.debug("Threads stopped")

    def exchange_pdo(self, slaveid: int = 0, **kwargs) -> Dict[str, Union[int, str, float]]:
        """
        Exchange PDOs with the communication thread.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.
        kwargs :
            Optional arguments. Every argument name corresponds to a PDO name and a new value for it.

        Returns
        -------
        Dict[str, Union[int, str, float]]
            Dict with received PDOs.
        """

        _node = self._nodes[slaveid]

        # Get PDOs from slave
        txpdo_raw = self._get_slave(slaveid).input

        txpdo_tuple = namedtuple("txpdo_tuple", _node.txpdo_dict.keys())

        txpdo = txpdo_tuple._make(bitstruct.unpack(_node.txpdo_pattern, txpdo_raw))

        logger.debug(f"Tx PDO Raw: {txpdo_raw}")
        logger.debug(f"Tx PDO: {txpdo}")

        # Send PDOs to slave
        for name, value in kwargs.items():
            name = name.lower().replace(" ", "_")
            if name is not None and value is not None:
                if name in _node.rxpdo_dict.keys():
                    _node.rxpdo_dict[name] = value
                else:
                    raise ExceptionEtherCAT(f"PDO {name} not in RxPDO list: {_node.rxpdo_dict.keys()}")

        rxpdo_raw = bitstruct.pack(_node.rxpdo_pattern, *_node.rxpdo_dict.values())

        # logger.debug(f"Rx PDO Raw: {rxpdo_raw}")

        slave = self._get_slave(slaveid)
        slave.output = rxpdo_raw

        logger.debug(f"Rx PDO: {_node.rxpdo_dict}")

        return txpdo._asdict()

    @staticmethod
    def _check_slave(slave: pysoem.CdefSlave, pos: int):
        """
        Function to check state of slave.
        Called by _check_thread().

        Parameters
        ----------
        slave : pysoem.CdefSlave
            Slave to check
        pos : int
            Postion in ethercat chain.
        """
        if slave.state == (pysoem.SAFEOP_STATE + pysoem.STATE_ERROR):
            logger.error(f'Slave {pos}:{slave.name} is in SAFE_OP + ERROR, attempting ack.')
            slave.state = pysoem.SAFEOP_STATE + pysoem.STATE_ACK
            slave.write_state()
            slave.state_check(slave.state, 50000)
        elif slave.state == pysoem.SAFEOP_STATE:
            logger.warning(f'Slave {pos}:{slave.name} is in SAFE_OP, try change to OPERATIONAL.')
            slave.state = pysoem.OP_STATE
            slave.write_state()
            slave.state_check(slave.state, 50000)
        elif slave.state > pysoem.NONE_STATE:
            logger.info(f'Slave {pos}:{slave.name} state is not NONE')
            if slave.reconfig():
                slave.is_lost = False
                logger.info(f'Slave {pos}:{slave.name} reconfigured')
        elif not slave.is_lost:
            logger.error(f'Check if slave {pos}:{slave.name} is lost')
            slave.state_check(pysoem.OP_STATE)
            if slave.state == pysoem.NONE_STATE:
                slave.is_lost = True
                logger.error(f'Slave {pos}:{slave.name} lost')
        if slave.is_lost:
            logger.error(f'Slave {pos}:{slave.name} is lost')
            if slave.state == pysoem.NONE_STATE:
                if slave.recover():
                    slave.is_lost = False
                    logger.info(f'Slave {pos}:{slave.name} recovered')
            else:
                slave.is_lost = False
                logger.info(f'Slave {pos}:{slave.name} found')

    def _check_thread(self):
        """
        Thread to check state of connected slaves.
        """
        logger.debug(f'Check thread started. {self._master.in_op}')
        while self._ch_thread_running.is_set():
            if self._master.in_op and ((self._actual_wkc != self._master.expected_wkc) or self._master.do_check_state):
                logger.debug('Start check')
                self._master.do_check_state = False
                self._master.read_state()

                for i, slave in enumerate(self._master.slaves):
                    if slave.state != pysoem.OP_STATE:
                        self._master.do_check_state = True
                        SOEMMaster._check_slave(slave, i)

                if not self._master.do_check_state:
                    logger.debug('OK : all slaves resumed OPERATIONAL.')

            time.sleep(0.01)

    def _pdo_get_sdo_indexes(self, slaveid: int = 0) -> Dict[str, List[int]]:
        """
        Get the object entry indexes/subindexes from the mapping objects 0x1A00+ and 0x1600+.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        Dict[str, List[int]]
            Dictionary with the PDO mapping information.
        """
        PDO_MAP_IDX_TX_START = 0x1A00
        PDO_MAP_IDX_TX_END = 0x1BFF
        PDO_MAP_IDX_RX_START = 0x1600
        PDO_MAP_IDX_RX_END = 0x17FF
        SM_ASSIGN_IDX_TX = 0x1c13
        SM_ASSIGN_IDX_RX = 0x1c12

        self._update_od(slaveid)
        #                 min     max
        tpdo = ("txpdo", PDO_MAP_IDX_TX_START, PDO_MAP_IDX_TX_END)
        rpdo = ("rxpdo", PDO_MAP_IDX_RX_START, PDO_MAP_IDX_RX_END)

        # Try get PDO config from slave
        # Incoming, RX
        try:
            cnt_subindex = self.upload(SM_ASSIGN_IDX_RX, 0, slaveid=slaveid)
            if cnt_subindex != 0:
                mapping_index = self.upload(SM_ASSIGN_IDX_RX, 1, slaveid=slaveid)
                rpdo = ("rxpdo", mapping_index, mapping_index + cnt_subindex)
        except Exception as e:
            logger.debug(str(e))

        try:
            # Outgoing, TX
            cnt_subindex = self.upload(SM_ASSIGN_IDX_TX, 0, slaveid=slaveid)
            if cnt_subindex != 0:
                mapping_index = self.upload(SM_ASSIGN_IDX_TX, 1, slaveid=slaveid)
                tpdo = ("txpdo", mapping_index, mapping_index + cnt_subindex)
        except Exception as e:
            logger.debug(str(e))

        pdo_mapping = {}

        for _pdo_index_list in [tpdo, rpdo]:
            pdo_mapping[_pdo_index_list[0]] = []
            for index in range(_pdo_index_list[1], _pdo_index_list[2]):
                if getattr(self._nodes[slaveid], "od") is None:
                    continue

                entry = list(filter(lambda e: e.index == index, self._nodes[slaveid].od))

                if not entry:
                    continue

                sub_entries_count = int(self.upload(index, 0, slaveid=slaveid))

                for sub_entry in range(1, sub_entries_count + 1):
                    pdo_mappping_value = self.upload(index, sub_entry, slaveid=slaveid)
                    pdo_mapping[_pdo_index_list[0]].append(
                        (
                            (int(pdo_mappping_value) >> 16) & 0xffff,  # Index
                            (int(pdo_mappping_value) >> 8) & 0xff,  # Subindex
                        )
                    )

        return pdo_mapping

    def _pdo_get_sdo_entries(self, pdo_mapping: Dict[str, List[int]], slaveid: int = 0) -> Dict[str, List[pysoem.CdefCoeObjectEntry]]:
        """
        Get the SDO entries, that are mapped to PDOs and save them.

        Parameters
        ----------
        pdo_mapping : Dict[str, List[int]]
        slaveid : int
            Slave ID / position in the ethercat chain.

        Returns
        -------
        Dict[str, List[pysoem.CdefCoeObjectEntry]]
            PDO entries.

        """

        pdo_entries = {}

        for key, pdo_list in pdo_mapping.items():
            pdo_entries[key] = []

            for idx, subindex in pdo_list:
                entry = list(filter(lambda e: e.index == idx, self._nodes[slaveid].od))

                if entry:
                    if subindex != 0:
                        e = entry[0].entries[subindex]
                    else:
                        e = entry[0]
                    pdo_entries[key].append(e)

        return pdo_entries

    def setup_pdos(self, slaveid: int = 0, pdo_config: Dict = None):
        """
        Setup automatic PDO encoding/decoding.

        Parameters
        ----------
        slaveid : int
            Slave ID / position in the ethercat chain.
        pdo_config : Dict
            Optional manually created PDO config, when it's not stored in object dictionary.
        """
        logger.debug(f">>> Setup PDO for slave {slaveid}")
        if pdo_config is None:
            pdo_mapping = self._pdo_get_sdo_indexes(slaveid)

            if not pdo_mapping:
                return

            logger.debug(f"PDO mapping: {pdo_mapping}")
            pdo_config = self._pdo_get_sdo_entries(pdo_mapping, slaveid)

            if not pdo_config:
                raise ExceptionEtherCAT("Could not setup PDOs")

        _duplicate_names = []
        logger.debug(f"PDO entries: {pdo_config}")

        for key, l in pdo_config.items():
            byte_pattern = ">"
            pdo_names = OrderedDict()

            for e in l:
                if hasattr(e, "data_type") and hasattr(e, "name"):
                    logger.debug(f"Data Type: {e.name}, Size: {e.bit_length}")
                    # Workaround if datatype is 0
                    try:
                        ec_type = EcTypes(e.data_type)
                        bitstruct_symbol = ec_type.bitstruct_symbol
                    except:
                        # Get fallback datatype
                        byte_size = int(e.bit_length / 8)
                        signed = False
                        ec_type = EcTypes.get_datatype(byte_size, signed)
                        bitstruct_symbol = ec_type[4]

                    byte_pattern += bitstruct_symbol
                    _name = e.name
                    if isinstance(_name, bytes):
                        _name = _name.decode()
                    _name = _name.replace(" ", "_").lower()
                else:
                    byte_pattern += e["pattern"]
                    _name = e["name"].replace(" ", "_").lower()

                # if pdo name is already in dict, append index
                logger.debug(f"PDO name: {_name}")

                if _name in pdo_names:
                    # save duplicate name
                    if not _name in _duplicate_names:
                        _duplicate_names.append(_name)
                    # Replace existing key with key+index
                    _name_with_index = _name
                    idx = 1

                    while _name_with_index in pdo_names:
                        _name_with_index = f"{_name}_{idx}"
                        idx += 1
                    _name = _name_with_index

                if _name != "padding":
                    pdo_names[_name] = 0

            if len(byte_pattern) > 1:
                byte_pattern += "<"
            else:
                byte_pattern = ""

            # Replace now the first duplicate and add index 0 to it
            for duplicate in _duplicate_names:
                pdo_names = OrderedDict([(f"{duplicate}_0", v) if k == duplicate else (k, v) for k, v in pdo_names.items()])

            setattr(self._nodes[slaveid], key + "_pattern", byte_pattern)
            logger.debug(f"{key}_pattern: {byte_pattern}")
            setattr(self._nodes[slaveid], key + "_dict", copy.deepcopy(pdo_names))
            logger.debug(f"{key}_dict: {pdo_names}")
