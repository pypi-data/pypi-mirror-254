import logging
import os
import platform
import struct
import time
from dataclasses import dataclass
from typing import List, Tuple, Union, Dict, Any

import serial
import serial.tools.list_ports

__all__ = [
    "ExceptionPSU",
    "ExceptionTimeout",
    "PsuEA",
]

ERR_STRINGS = {
    0x0:  'NO ERROR',

    # Communication Error
    0x3:  'CHECKSUM WRONG',
    0x4:  'STARTDELIMITER WRONG',
    0x5:  'WRONG OUTPUT',
    0x7:  'OBJECT UNDEFINED',

    # User Error
    0x8:  'OBJECT LENGTH INCORRECT',
    0x9:  'NO RW ACCESS',
    0xf:  'DEVICE IN LOCK STATE',
    0x30: 'UPPER LIMIT OF OBJECT EXCEEDED',
    0x31: 'LOWER LIMIT OF OBJECT EXCEEDED'
}


@dataclass()
class ObjectEntry:
    index: int
    length: int
    datatype: str


@dataclass()
class Objects:
    DEV_TYPE: ObjectEntry = ObjectEntry(0x0, 16, 's')
    SERIAL: ObjectEntry = ObjectEntry(0x1, 16, 's')
    NOM_U: ObjectEntry = ObjectEntry(0x2, 4, '>f')
    NOM_I: ObjectEntry = ObjectEntry(0x3, 4, '>f')
    NOM_P: ObjectEntry = ObjectEntry(0x4, 4, '>f')
    DEV_ARTICLE_NO: ObjectEntry = ObjectEntry(0x6, 16, 's')
    MANUFACTURER: ObjectEntry = ObjectEntry(0x8, 16, 's')
    SW_VERSION: ObjectEntry = ObjectEntry(0x9, 16, 's')
    DEV_CLASS: ObjectEntry = ObjectEntry(0x13, 2, '>BB')
    OVP_THRESHOLD: ObjectEntry = ObjectEntry(0x26, 2, '>H')
    OCP_THRESHOLD: ObjectEntry = ObjectEntry(0x27, 2, '>H')
    SET_U: ObjectEntry = ObjectEntry(0x32, 2, '>H')
    SET_I: ObjectEntry = ObjectEntry(0x33, 2, '>H')
    CONTROL: ObjectEntry = ObjectEntry(0x36, 2, '>BB')
    STATUS_ACTUAL: ObjectEntry = ObjectEntry(0x47, 6, '>BBHH')
    STATUS_TARGET: ObjectEntry = ObjectEntry(0x48, 6, '>BBHH')


# Telegram Headers #
SEND_MSG = 0xC0
RECEIVE_MSG = 0x40

DIRECTION_MSG = 0x10  # From PC to device
CAST_TYPE = 0x20  # for sending/querying it must be set to 1, in answers it will be 0

# Telegram Header
SEND_HEADER = SEND_MSG + CAST_TYPE + DIRECTION_MSG
RECEIVE_HEADER = RECEIVE_MSG + CAST_TYPE + DIRECTION_MSG

CONTROL_HEADER = [SEND_HEADER + 1, 0x0, Objects.CONTROL.index]
#            Header  Output Obj  Mask   Command
REMOTE_MSG = CONTROL_HEADER + [0x10, 0x10]
OUTPUT_MSG = CONTROL_HEADER + [0x01, 0x01]

TRACKING_ON = CONTROL_HEADER + [0xF0, 0xF0]
TRACKING_OFF = CONTROL_HEADER + [0xF0, 0xE0]

ACKNOWLEDGE_ALARM = CONTROL_HEADER + [0x0A, 0x0A]

# Indexes #
IDX_DN = 1  # For Triple: Device output number, else always 0
IDX_OBJ = 2
IDX_DATA = 3
IDX_DATA_MASK = IDX_DATA
IDX_DATA_VALUE = IDX_DATA_MASK + 1


@dataclass()
class PSUQuantities:
    # Nominal values
    nom_voltage: float = 0.0
    nom_current: float = 0.0
    nom_power: float = 0.0
    # Actual PSU voltage
    act_voltage: float = 0.0
    # Maximum possible current supported by this PSU and the set voltage
    max_current: float = 0.0


class ExceptionPSU(Exception):
    pass


class ExceptionTimeout(Exception):
    pass


class PsuEA:
    OUTPUT_1 = 0x0
    OUTPUT_2 = 0x1

    CV = 0x0
    CC = 0x2

    OUTPUT_ON = 0x01
    OUTPUT_OFF = 0x00
    REMOTE_ON = 0x10
    REMOTE_OFF = 0x00

    SCALING_FACTOR = 25600.0
    DECIMAL_PLACES = 3

    VENDOR_ID = 0x232e
    DEVICE_CLASS_SINGLE = 0x10
    DEVICE_CLASS_TRIPLE = 0x18

    def __init__(self, comport: str = None, sn: str = None, designator: str = None,
                 baudrate: int = 115200, log: bool = False, debug: bool = False):
        """
        Driver to control PSUs from Elektro Automatik's PS series.

        Parameters
        ----------
        comport : str
            Comport name
        sn : str
            Serial number of the PSU
        designator : str
            Name of the PSU
        baudrate : int
            Baud rate. Don't change.
        log : bool
            If true show logs.
        debug : bool
            If true show debug logs.
        """
        ch_console = logging.StreamHandler()
        if debug:
            logger_level = logging.DEBUG
        else:
            logger_level = logging.INFO
        log_handler = [ch_console]
        logging.basicConfig(format='[%(levelname)s] %(asctime)s.%(msecs)03d - L%(lineno)d > %(message)s',
                            datefmt="%H:%M:%S", level=logger_level, handlers=log_handler)
        self.logger = logging.getLogger(__name__)
        self.logger.propagate = log or debug
        self.logger.info("LOG MODE")
        self.logger.debug("DEBUG MODE")

        self._port = None
        self._baud = baudrate

        self.psu = None

        self.desc = {'name':                 '-',
                     'serial':               '-',
                     'manufacturer':         '-',
                     'software version':     '-',
                     'device article no':    '-',
                     'controllable_outputs': 1
                     }

        _d_state = {'output':           self.OUTPUT_1,
                    'remote on':        False,
                    'output on':        False,
                    'controller state': 'CV',
                    'tracking active':  False,
                    'OVP active':       False,
                    'OCP active':       False,
                    'OPP active':       False,
                    'OTP active':       False,
                    'act voltage':      0.0,
                    'act current':      0.0
                    }

        self.__output_state: List[Dict] = [_d_state, _d_state.copy()]
        self.__output_state[self.OUTPUT_2]['output'] = self.OUTPUT_2

        self.__quantities = PSUQuantities()

        self.__find_devices(comport, sn, designator)

        if self._port:
            self.get_status()

    def __del__(self):
        self.close()

    def __find_devices(self, comport: str, sn: str, designator: str):
        """
        Find device and connect to them or list a help string.
        If no value is provided and only one PSU is connected, it will connect to this one.

        Parameters
        ----------
        comport : str
            Path to port
        sn : str
            Serial number
        designator : str
            PSU name

        Raises
        ------
        ExceptionPSU: If no PSU could be found.
        ExceptionPSU: If multiple PSUs where found, but arguments are None.
        """

        filter_value = None

        # Get Device list
        dev_list = list(filter(lambda p: p.vid == self.VENDOR_ID, serial.tools.list_ports.comports()))

        if comport:
            if not os.path.exists(comport):
                raise ExceptionPSU(f"Port {comport} does not exists")
            filter_value = comport
            if os.path.islink(comport):
                # resolve symlink and return absolute path to target
                filter_value = os.path.realpath(comport)

            filtered_dev_list = list(filter(lambda p: filter_value in p.device, dev_list))
        elif sn:
            filter_value = str(sn)
            filtered_dev_list = list(filter(lambda p: filter_value == p.serial_number, dev_list))
        elif designator:
            filter_value = designator
            filtered_dev_list = list(filter(lambda p: designator == p.description, dev_list))
        elif not comport and not sn and not designator and len(dev_list) == 1:
            filtered_dev_list = dev_list
        else:
            # Create help output
            help_str = [' Found these PSUs:']
            for idx, _dev in enumerate(dev_list):
                outputs = 1 if _dev.pid == self.DEVICE_CLASS_SINGLE else 3
                plural = "s" if outputs > 1 else ""
                help_ = f'{idx + 1}) {_dev.description}, SN: {_dev.serial_number}, Output{plural}: {outputs}, Port: {_dev.device}'
                help_str.append(help_)
            help_str = '\n'.join(help_str)

            raise ExceptionPSU(f'No PSU specified.{help_str}')

        if len(filtered_dev_list) > 1:
            raise ExceptionPSU(f"Found more than one PSU for {filter_value}")

        if not filtered_dev_list:
            additional_info = ""
            if filter_value:
                additional_info = f" for {filter_value}"

            raise ExceptionPSU('ERROR: No PSU found' + additional_info)

        dev = filtered_dev_list[0]
        self._port = dev.device
        self.connect()

    @staticmethod
    def __pack_list(_list: List[int]) -> bytes:
        """
        Pack list of bytes to bytestring

        Parameters
        ----------
        _list : List[int]
            Telegram for PSU.

        Returns
        -------
        bytes
            Telegram as bytes
        """
        return struct.pack(f'{len(_list)}B', *_list)

    @staticmethod
    def __int_to_bytes(num: int, num_bytes: int) -> List[int]:
        """
        Convert a number into bytes

        Parameters
        ----------
        num : int
            Number to convert
        num_bytes : int
            Amount of bytes.

        Returns
        -------
        List[int]
            List of bytes.

        """

        _list = [8 * i for i in reversed(range(num_bytes))]
        return [(num >> i & 0xff) for i in _list]

    def __calc_checksum(self, cmd_list: List[int]) -> List[int]:
        """
        Calculate the checksum.
        It's just the sum of all bytes in the message. 16 bit long.

        Parameters
        ----------
        cmd_list : List[int]
            Telegram,
        Returns
        -------
        List[int]
            Checksum
        """
        checksum = 0
        for byte in cmd_list:
            checksum += byte
        return self.__int_to_bytes(checksum, 2)

    @staticmethod
    def __get_message(response: bytes) -> bytes:
        """
        Get actual message from response.

        Parameters
        ----------
        response : bytes
            Message without frame.

        Returns
        -------
        bytes
            Message
        """
        return response[3:-2]

    def __tx_rx(self, cmd: List[int], expect_length: int) -> bytes:
        """
        Send a telegram and receive response.

        Parameters
        ----------
        cmd : List[int]
            Telegram
        expect_length : int
            Expected length of response.
        Returns
        -------
        bytes
            Response message.
        """
        timeout = 2

        if not self.psu:
            raise ExceptionPSU('No PSU connected')

        self.psu.reset_input_buffer()
        checksum = self.__calc_checksum(cmd)
        output = self.__pack_list(cmd + checksum)
        self.psu.write(output)
        time.sleep(0.005)

        _amount_bytes = 0
        response = b""
        t0 = time.time()

        while self.psu.in_waiting == 0:
            if time.time() - t0 > timeout:
                raise ExceptionTimeout(f'Didn\'t receive any bytes in time.')

        while self.psu.in_waiting:
            _recv_bytes = self.psu.in_waiting
            _amount_bytes += _recv_bytes
            response += self.psu.read(_recv_bytes)

        # Look at last data byte. Shall be a zero byte if it's a string. Some strings are too short
        if response[-3] != 0 and _amount_bytes < expect_length:
            raise ExceptionPSU(f"No proper response: {response}")

        res = self.__get_message(response)
        time.sleep(0.04)
        return res

    def _check_outputs(self, output_num: int):
        """
        Check, if requested output number is in range of actual available outputs.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Raises
        -------
        ExceptionPSU : If device has only one output and output_num is > 0.
        ExceptionPSU : If tracking is active.
        """

        existing_outputs = self.desc['controllable_outputs']
        if output_num > 0 and output_num >= existing_outputs:
            raise ExceptionPSU(f'Error: PSU has only {existing_outputs} output{"s" if existing_outputs > 1 else ""}.')

        if self.__output_state[output_num]["tracking active"] and output_num > 0:
            raise ExceptionPSU('Error: Tracking is active. Second output is not controllable!')

    def __set_value(self, value: Union[int, float], max_value: Union[int, float], obj: ObjectEntry, output: int):
        """
        Set value on device

        Parameters
        ----------
        value : Union[int, float]
            voltage or current value
        max_value : Union[int, float]
            Max value (nominal value)
        obj : ObjectEntry
            Object entry
        output : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Raises
        ------
        ExceptionPSU : if max_value is Zero
        ExceptionPSU : If an error occurs.
        """

        self._check_outputs(output)

        if not self.__output_state[output]['remote on']:
            self.remote_on(output)

        if max_value == 0.0:
            raise ExceptionPSU('Error: "Max Value" in "set_value()" is zero.')

        value_percent = int((value * self.SCALING_FACTOR) / max_value)
        value_bytes = self.__int_to_bytes(value_percent, obj.length)
        packet = [SEND_HEADER + obj.length - 1, output, obj.index] + value_bytes
        res = self.__tx_rx(packet, 1)
        self._check_for_error(res)

    def __get_value(self, obj: ObjectEntry, output: int) -> Union[bytes, Tuple[Any]]:
        """
        Get integer value from device.

        Parameters
        ----------
        obj : ObjectEntry
            Object entry
        output : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        Union[bytes, Tuple[Any]]
            Response from device.
        """

        self._check_outputs(output)

        if not self.__output_state[output]['remote on']:
            self.remote_on(output)

        packet = [RECEIVE_HEADER + obj.length - 1, output, obj.index]
        res = self.__tx_rx(packet, obj.length)

        if obj.datatype == 's':
            return res
        return struct.unpack(obj.datatype, res)

    def __get_float(self, obj: ObjectEntry, output: int) -> Tuple[Any]:
        """
        Get Float value from device

        Parameters
        ----------
        obj : ObjectEntry
            Object entry
        output : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        Tuple[Any]
            Response from device.
        """

        self._check_outputs(output)

        packet = [RECEIVE_HEADER, output, obj.index]
        res = self.__tx_rx(packet, obj.length)
        return struct.unpack('>f', res)

    def __get_string(self, obj: ObjectEntry) -> str:
        """
        Get string value from device
        Parameters
        ----------
        obj : ObjectEntry
            Object entry

        Returns
        -------
        str
            Response string
        """
        msg = self.__get_value(obj, 0)
        # Check if last byte is a null byte
        if msg[-1] == 0:
            # Remove it
            msg = msg[:-1]
        return msg.decode('ascii')

    def _check_for_error(self, response: bytes):
        """
        Check if device responses with an error.
        Parameters
        ----------
        response : bytes
            Response from device

        Raises
        ------
        ExceptionPSU : If error is not Zero.
        """
        error = struct.unpack('B', response)[0]
        if error != 0x0:
            raise ExceptionPSU(ERR_STRINGS[error])

    def _calculate_value(self, value: Union[int, float], nom_value: Union[int, float]) -> float:
        """
        Calculate the voltage or current coming from device.

        Parameters
        ----------
        value : Union[int, float]
            value from device
        nom_value : Union[int, float]
            Nominal value.

        Returns
        -------
        float
            Actual readable voltage / current
        """

        return round((value * nom_value) / self.SCALING_FACTOR, self.DECIMAL_PLACES)

    def __send_msg(self, msg: List[int], state_name: str = None):
        """
        Send message to PSU and throw error if a problem occurs.

        Parameters
        ----------
        msg : List[int]
            Telegram message for PSU
        state_name : str
            State names in dict to set the new value there.

        Raises
        ------
            ExceptionPSU: If error is not null
            ExceptionPSU: If sending message failed 5 times
        """
        counter = 5

        output_num = msg[IDX_DN]
        value = msg[IDX_DATA_VALUE]

        while True:
            res = self.__tx_rx(msg, 1)
            if len(res) == 1:
                self._check_for_error(res)

                if state_name:
                    self.__output_state[output_num][state_name] = bool(value)
                break

            if counter == 0:
                raise ExceptionPSU(f'ERROR: Did not received ACK for {state_name.upper()}: {value}')

            counter -= 1

    def _send_remote(self, value: int, output_num: int, init: bool):
        """
        Send remote message (on/off)

        Parameters
        ----------
        value : int
            1 or 0 (on or off)
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        init : bool
        Init device first (only for remote_on())
        Returns
        -------

        """

        self.logger.debug("send_remote({})".format(output_num))

        self._check_outputs(output_num)

        REMOTE_MSG[IDX_DN] = output_num
        REMOTE_MSG[IDX_DATA_VALUE] = value

        self.__send_msg(REMOTE_MSG, 'remote on')

        if init:
            self._init_device(output_num)

    def _send_output(self, value: int, output_num: int):
        """
        Turn on or off power output on device.

        Parameters
        ----------
        value : int
            1 or 0 (On or Off)
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        """

        self._check_outputs(output_num)

        OUTPUT_MSG[IDX_DN] = output_num
        OUTPUT_MSG[IDX_DATA_VALUE] = value

        self.__send_msg(OUTPUT_MSG, 'output on')

    def _init_device(self, output_num: int = 0):
        """
        Initialize device.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------

        """
        self.get_nominal_values(output_num, True)
        self.set_ovp(self.__quantities.nom_voltage, output_num)
        self.set_ocp(self.__quantities.nom_current, output_num)

    def connect(self, comport: str = None) -> Dict[str, Union[str, int]]:
        """
        Connect with PSU

        Parameters
        ----------
        comport : str
            Path to comport.

        Returns
        -------
        Dict[str, Union[str, int]]
            Device description
        """

        port = ''
        if platform.system() == 'Windows':
            port = comport or self._port.device
        elif platform.system() == 'Linux':
            port = comport or self._port
        self.psu = serial.Serial(port, self._baud, timeout=5)
        return self.get_device_description(True)

    def close(self):
        """
        Closes the serial connection.
        """
        if hasattr(self, "psu") and self.psu is not None:
            for output in range(self.desc['controllable_outputs']):
                if output > self.OUTPUT_1 and self.__output_state[output]['tracking active']:
                    continue
                self.remote_off(output)

            self.psu.close()
        self.psu = None
        self._port = None

    def get_status(self, update: bool = True) -> List[Dict]:
        """
        Get status from device. See programming Guide for further information page 11.

        Parameters
        ----------
        update : bool
            Pull information from device.

        Returns
        -------
        List[Dict]
            Status information
        """

        if update:
            outputs = self.desc['controllable_outputs']
            self.logger.debug("get_status(), Controllable outputs: %d", outputs)
            output_state = []
            status = []
            for output_num in range(outputs):
                output_state.append({})
                # if tracking active and this is the second output, skip getting value and use status from first output.
                if output_num == self.OUTPUT_2 and output_state[0]['tracking active']:
                    self.logger.debug("Tracking is active")
                else:
                    status = self.__get_value(Objects.STATUS_ACTUAL, output_num)

                remote_on = status[0]
                status_byte = status[1]
                output_state[output_num]['remote on'] = remote_on == 1
                output_state[output_num]['output on'] = (status_byte & 0x1) == 1
                output_state[output_num]['controller state'] = 'CV' if (status_byte >> 1) & 0x3 == self.CV else 'CC'
                output_state[output_num]['tracking active'] = ((status_byte >> 3) & 0x1) == 1
                output_state[output_num]['OVP active'] = ((status_byte >> 4) & 0x1) == 1
                output_state[output_num]['OCP active'] = ((status_byte >> 5) & 0x1) == 1
                output_state[output_num]['OPP active'] = ((status_byte >> 6) & 0x1) == 1
                output_state[output_num]['OTP active'] = ((status_byte >> 7) & 0x1) == 1
                output_state[output_num]['act voltage'] = self._calculate_value(status[2], self.__quantities.nom_voltage)
                output_state[output_num]['act current'] = self._calculate_value(status[3], self.__quantities.nom_current)
            self.__output_state = output_state
        return self.__output_state

    def get_device_description(self, update: bool = False) -> Dict[str, Union[str, int]]:
        """
        Get device description

        Parameters
        ----------
        update : bool
            Pull information from device.

        Returns
        -------
        Dict[str, Union[str, int]]
            Description dictionary
        """

        self.logger.debug("get_device_description()")
        if self.desc['name'] == '-' or update:
            self.logger.debug("get_device_description(): Update")
            self.desc['name'] = self.__get_string(Objects.DEV_TYPE)
            self.desc['serial'] = self.__get_string(Objects.SERIAL)
            self.desc['manufacturer'] = self.__get_string(Objects.MANUFACTURER)
            self.desc['software version'] = self.__get_string(Objects.SW_VERSION)
            self.desc['device article no'] = self.__get_string(Objects.DEV_ARTICLE_NO)
            self.desc['controllable_outputs'] = 1 if self.__get_value(Objects.DEV_CLASS, 0)[1] == self.DEVICE_CLASS_SINGLE else 2
        return self.desc.copy()

    def remote_on(self, output_num: int = 0, init: bool = True):
        """
        Activates remote mode on device

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        init : bool
            if True, initialize the output.
        """

        self._send_remote(self.REMOTE_ON, output_num, init)

    def remote_off(self, output_num: int = 0):
        """
        Deactivates remote mode on device

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        """

        if not self.__output_state[output_num]["remote on"]:
            self.logger.debug("Remote already off")
            return
        self._send_remote(self.REMOTE_OFF, output_num, False)

    def get_nominal_voltage(self, output_num: int = 0, update: bool = False) -> float:
        """
        Get nominal voltage from device.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B) int

        update : bool
            Update nom. values. If true, get it from PSU. Otherwise, use cached value.

        Returns
        -------
        float
            Nominal voltage in V
        """

        if not self.__quantities.nom_voltage or update:
            self.__quantities.nom_voltage = self.__get_float(Objects.NOM_U, output_num)[0]
            self.logger.debug("Get from PSU nom voltage: %f", self.__quantities.nom_voltage)
        return self.__quantities.nom_voltage

    def get_nominal_current(self, output_num: int = 0, update: bool = False) -> float:
        """
        Get nominal current from device.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B) int

        update : bool
            Update nom. values. If true, get it from PSU. Otherwise, use cached value.

        Returns
        -------
        float
            Nominal current in A
        """
        if not self.__quantities.nom_current or update:
            self.__quantities.nom_current = self.__get_float(Objects.NOM_I, output_num)[0]
            self.logger.debug("Get from PSU nom current: %f", self.__quantities.nom_current)
        return self.__quantities.nom_current

    def get_nominal_power(self, output_num: int = 0, update: bool = False) -> float:
        """
        Get nominal power from device.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B) int

        update : bool
            Update nom. values. If true, get it from PSU. Otherwise, use cached value.

        Returns
        -------
        float
            Nominal power in W
        """
        if not self.__quantities.nom_power or update:
            self.__quantities.nom_power = self.__get_float(Objects.NOM_P, output_num)[0]
            self.logger.debug("Get from PSU nom power: %f", self.__quantities.nom_power)
        return self.__quantities.nom_power

    def get_nominal_values(self, output_num: int = 0, update: bool = False) -> (float, float, float):
        """
        Get nominal voltage, current and power from device.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B) int

        update : bool
            Update nom. values. If true, get it from PSU. Otherwise, use cached value.

        Returns
        -------
        (float, float, float)
            Voltage, Current, Power
        """
        self.get_nominal_voltage(output_num, update)
        self.get_nominal_current(output_num, update)
        self.get_nominal_power(output_num, update)
        self.logger.debug("Nom Values: U: %f, I: %f, P: %f",
                          self.__quantities.nom_voltage, self.__quantities.nom_current, self.__quantities.nom_power)
        return self.__quantities.nom_voltage, self.__quantities.nom_current, self.__quantities.nom_power

    def set_voltage(self, voltage: Union[int, float], output_num: int = 0) -> float:
        """
        Set output voltage on <output_num>.
        If requested voltage exceeds nominal voltage, it will set it to the nominal value.
        If requested voltage and the current exceeds nominal power, it will respect the current value
        and calculates the maximum possible voltage: set_voltage = nominal_power / actual_current.

        Important: If you want to have maximum voltage, set voltage before current.

        Parameters
        ----------
        voltage : Union[int, float]
            Requested voltage in Volt
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            Actual set voltage in V
        """
        if not isinstance(voltage, (int, float)):
            raise ExceptionPSU("Voltage is not a number")

        # Calculate actual possible maximum current depending on maximum output power
        set_voltage = voltage
        if set_voltage > self.__quantities.nom_voltage:
            set_voltage = self.__quantities.nom_voltage
        try:
            if set_voltage > self.__quantities.nom_power / self.__quantities.max_current:
                set_voltage = self.__quantities.nom_power / self.__quantities.max_current
                self.logger.info(f'Set voltage to {set_voltage:.2f} V '
                                 f'due to maximum power of {self.__quantities.nom_power:.2f} W')
        except ZeroDivisionError:
            pass

        self.__quantities.act_voltage = float(set_voltage)
        self.__set_value(set_voltage, self.__quantities.nom_voltage, Objects.SET_U, output_num)
        return self.__quantities.act_voltage

    def set_current(self, current: Union[int, float], output_num: int = 0) -> float:
        """
        Set output current on <output_num>.
        If requested current exceeds nominal current, it will set it to the nominal value.
        If requested current and the current voltage exceeds nominal power, it will respect the voltage value
        and calculates the maximum possible current: set_current = nominal_power / actual_voltage

        Important: If you want to have maximum current, set current before voltage.

        Parameters
        ----------
        current : Union[int, float]
            Requested current value in A
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            Actual set current in A
        """
        if not isinstance(current, (int, float)):
            raise ExceptionPSU("Current is not a number")

        # Calculate actual possible maximum current depending on maximum output power
        set_current = current
        if set_current > self.__quantities.nom_current:
            set_current = self.__quantities.nom_current
        try:
            if set_current > self.__quantities.nom_power / self.__quantities.act_voltage:
                set_current = self.__quantities.nom_power / self.__quantities.act_voltage
                self.logger.info(f'Set current to {set_current:.2f} A '
                                 f'due to maximum power of {self.__quantities.nom_power:.2f} W '
                                 f'and current voltage of {self.__quantities.act_voltage:.2f} V')
        except ZeroDivisionError:
            pass

        self.__quantities.max_current = float(set_current)
        self.__set_value(set_current, self.__quantities.nom_current, Objects.SET_I, output_num)
        return self.__quantities.max_current

    def get_voltage(self, output_num: int = 0) -> float:
        """
        Get current output voltage from <output_num>

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            Voltage in Volt
        """
        self._check_outputs(output_num)

        if self.__quantities.nom_voltage <= 0.0:
            self.get_nominal_voltage(output_num)

        status = self.get_status()
        if status:
            return status[output_num]['act voltage']
        self.logger.debug("Warning: Status is empty")
        return 0.0

    def get_current(self, output_num: int = 0) -> float:
        """
        Get current of <output_num>

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            Current in Ampere
        """
        self._check_outputs(output_num)

        if self.__quantities.nom_current <= 0.0:
            self.get_nominal_current(output_num)

        status = self.get_status()
        if status:
            return status[output_num]['act current']
        self.logger.debug("Warning: Status is empty")
        return 0.0

    def get_power(self, output_num: int = 0) -> float:
        """
        Get power of <output_num>

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            Power in Watt
        """
        self._check_outputs(output_num)

        status = self.get_status()
        return round(status[output_num]['act voltage'] * status[output_num]['act current'], self.DECIMAL_PLACES)

    def output_on(self, output_num: int = 0, all_outputs: bool = False):
        """
        Turn on power output on device

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        all_outputs : bool
            If true, turn all outputs off (for multi-port devices)
        """
        if all_outputs:
            for i in range(self.desc['controllable_outputs']):
                self._send_output(self.OUTPUT_ON, i)
        else:
            self._send_output(self.OUTPUT_ON, output_num)

    def output_off(self, output_num: int = 0, all_outputs: bool = False):
        """
        Turn off power output on device

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        all_outputs : bool
            If true, turn all outputs off (for multi-port devices)
        """
        if all_outputs:
            for i in range(self.desc['controllable_outputs']):
                self._send_output(self.OUTPUT_OFF, i)
        else:
            self._send_output(self.OUTPUT_OFF, output_num)

    def set_ovp(self, voltage: float, output_num: int = 0):
        """
        Set Over-voltage Protection

        Parameters
        ----------
        voltage : float
            Voltage value
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        """
        self.__set_value(voltage, self.__quantities.nom_voltage, Objects.OVP_THRESHOLD, output_num)

    def set_ocp(self, current: float, output_num: int = 0):
        """
        Set Over-current Protection

        Parameters
        ----------
        current : float
            Current value
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        """
        self.__set_value(current, self.__quantities.nom_current, Objects.OCP_THRESHOLD, output_num)

    def get_ovp(self, output_num: int = 0) -> float:
        """
        Get Over-voltage Protection value

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            OVP value
        """
        val = self.__get_value(Objects.OVP_THRESHOLD, output_num)
        return self._calculate_value(val[0], self.__nom_voltage)

    def get_ocp(self, output_num: int = 0) -> float:
        """
        Get Over-current Protection value

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)

        Returns
        -------
        float
            OCP value

        """
        val = self.__get_value(Objects.OCP_THRESHOLD, output_num)
        return self._calculate_value(val[0], self.__nom_current)

    def reset_error(self, output_num: int = 0):
        """
        Reset error (OVP, OCP, OPP, OTP).
        Resetting error turns off all outputs.

        Parameters
        ----------
        output_num : int
            Output number for multi output devices (e.g. PS 2342-10B)
        """

        ACKNOWLEDGE_ALARM[IDX_DN] = output_num
        self.__send_msg(ACKNOWLEDGE_ALARM)

    def tracking_on(self):
        """
        Turn tracking on. If tracking is on, output 2 control is disable and output 1 controls also output 2

        Raises
        ------
            ExceptionPSU: If user tries to turn on tracking on single output PSU.
        """
        if self.desc["controllable_outputs"] == 1:
            raise ExceptionPSU("Tracking is only available on Triple Output PSUs")

        self.__send_msg(TRACKING_ON)
        # Set status manual, because we have to do it for both outputs
        for idx in range(self.desc["controllable_outputs"]):
            self.__output_state[idx]["tracking active"] = True

    def tracking_off(self):
        """
        Turn tracking off.
        """
        self.__send_msg(TRACKING_OFF)
        # Set status manual, because we have to do it for both outputs
        for idx in range(self.desc["controllable_outputs"]):
            self.__output_state[idx]["tracking active"] = False
