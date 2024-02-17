#!/usr/bin/python3

"""
    SOMANET UART Firmware Uploader v1.0
    author: Henrik Strötgen
"""

VERSION = "1.0.0"

import sys
import os
import serial
import time
import logging
import platform
from typing import Union, List, Tuple, Dict, Any, Type

from ymodem.YModem import YModem

from ..BaseFileSystem import BaseFileSystem, SomanetFileSystem

# logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='[%(levelname)s]: %(message)s')
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


class ExceptionUART(Exception):
    pass


class ExceptionNoBinary(ExceptionUART):
    pass


class UARTFWUploader(BaseFileSystem, SomanetFileSystem):

    def __init__(self, serial_device: str, baudrate: int = 115200):
        """
        UART Firmware Uploader.

        Parameters
        ----------
        serial_device : str
            path to serial device (e.g. ttyUSB0 or /dev/ttyUSB0)
        baudrate : int
            Baud rate of serial device. Bootloader has 115200. So don't change it!
        """

        if not serial_device.startswith('/dev/') and platform.system() == "Linux":
            self.__port = os.path.join('/dev/', serial_device)
        else:
            self.__port = serial_device

        if not os.path.exists(self.__port) and platform.system() == "Linux":
            raise ExceptionUART(f"Device \"{self.__port}\" does not exists")

        self.__baudrate = baudrate

        self.modem = YModem(self.getc, self.putc)

        try:
            self.uart = serial.Serial(self.__port, self.__baudrate)
        except serial.serialutil.SerialException as e:
            print(e)
            sys.exit(1)

    @staticmethod
    def _print(res: bytes):
        """

        Parameters
        ----------
        res :

        Returns
        -------

        """
        """
        Print a received message in a console style format.
        :param res: Incoming message
        :type res: binary
        """
        if not res:
            return
        try:
            res = res.decode(errors='backslashreplace')

            if len(res) > 0:
                for l in res.splitlines():
                    if l:
                        l = "".join([r for r in l if r.isprintable()])
                        logger.info(f'>>> {l}')
            else:
                logger.info('-')
        except UnicodeDecodeError:
            logger.error(f'Error: {res}')

    def getc(self, size: int) -> Union[bytes, None]:
        """
        Callback function for YMODEM.
        Receive <size> of bytes from bootloader.

        Parameters
        ----------
        size : int
            Amount of bytes to read

        Returns
        -------
        Union[bytes, None]
            Response
        """
        return self.uart.read(size) or None

    def putc(self, data: bytes) -> int:
        """
        Callback function for YMODEM.
        Send bytes to bootloader.

        Parameters
        ----------
        data : bytes
            Byte strings

        Returns
        -------
        int
            Amount of send bytes

        """
        return self.uart.write(data)

    def close(self):
        """
        Close connection
        """
        self.uart.close()

    def _clean_msg(self, msg: bytes) -> str:
        """
        Convert bytestring into string and remove or replace all unnecessary chars.

        Parameters
        ----------
        msg : bytes
            Response message from bootloader

        Returns
        -------
        str
            Cleaned response message as string

        """
        msg = msg.decode()
        for pattern in [("\r\n", "\n"), (">", ""), ("\x08", ""), ("\r", "\n")]:
            msg = msg.replace(*pattern)
        return msg.strip()

    def _send_cmd(self, cmd: str, timeout: int = 2) -> bytes:
        """
        Send a single command to bootloader. NOT YMODEM related.

        Parameters
        ----------
        cmd : str
             Command (like getlist, boot, flash)
        timeout : int
            Timeout in seconds

        Returns
        -------
        bytes
            Response message
        """
        self.uart.timeout = timeout
        self.uart.reset_input_buffer()
        _cmd = cmd

        for c in _cmd:
            _c = c.encode()
            self.uart.write(_c)
            time.sleep(0.002)
        self.uart.write(b'\r\n')

        # wait for reply
        t0 = time.time()
        while self.uart.in_waiting == 0:
            if (time.time() - t0) > timeout:
                raise ExceptionUART("Timeout! Not received any reply! Perhaps drive is not in BOOT mode. Call with -o")

        _input = b''
        while self.uart.in_waiting:
            _input_bytes = self.uart.in_waiting
            _input += self.uart.read(_input_bytes)
            time.sleep(0.05)
        self.uart.reset_input_buffer()
        return _input

    def _file_write(self, cmd: str, file_path: str) -> bytes:
        """
        Sends a file to bootloader.

        Parameters
        ----------
        cmd : str
            Command for bootloader. Either "flash" (write app/firmware) or "write" (write generic file).
        file_path : str
            Path to binary or file.

        Returns
        -------
        bytes
            Response message

        """
        # Calculate timeout based on file size.
        file_size = os.path.getsize(file_path)
        # Speed: roughly 8000 bytes/seconds
        timeout = (file_size / 8000) + 1

        if timeout < 5:
            timeout = 5

        res = self._send_cmd('\n')
        if not res:
            raise ExceptionUART("No response received for '\\n'")

        res = self._send_cmd(cmd)
        if not res:
            raise ExceptionUART(f"No response received for '{cmd}'")

        self._print(res)
        logger.info("")

        self.uart.timeout = timeout
        self.modem.send_file(file_path)
        time.sleep(0.01)

        res = self.uart.read(self.uart.in_waiting)
        return res

    def _file_read(self, cmd: str, file_name: str) -> bytes:
        """
        Read file from flash storage.

        Parameters
        ----------
        cmd : str
            shall always be "read". There are at the moment not more commands.
        file_name : str
            File name

        Returns
        -------
        bytes
            File content

        """

        # Get file size and also check if file is existing on node
        file_size = self.ls()[file_name]
        if not file_size:
            raise ExceptionUART('File not in file system')

        # Calculate timeout. 8000 bytes per second is roughly the speed.
        timeout = (file_size / 8000) + 1
        if timeout < 5:
            timeout = 5

        self._send_cmd('\n')
        cmd += ' ' + file_name
        res = self._send_cmd(cmd)
        self._print(res)

        print()
        self.uart.timeout = timeout
        self.uart.reset_input_buffer()
        self.uart.reset_output_buffer()

        _file_name, file_content, amountb = self.modem.recv_file()
        time.sleep(0.01)

        if self.uart.in_waiting > 0:
            res = self.uart.read(self.uart.in_waiting)

        return file_content

    def send_cmd(self, cmd: str) -> str:
        """
        Send command to bootloader. Retry on received "Unknown command"

        Parameters
        ----------
        cmd : str
            To send command

        Returns
        -------
        str
            Received response. Filtered and decoded byte string
        """

        retry = 5
        while True:
            res = self._send_cmd(cmd)
            if b'Unknown command' not in res or retry == 0:
                break
            retry -= 1

        return self._clean_msg(res)

    def boot(self) -> str:
        """

        Returns
        -------

        """
        return self.send_cmd('boot')

    def hold(self) -> str:
        """

        Returns
        -------

        """
        return self.send_cmd("hold")

    def check(self) -> str:
        """

        Returns
        -------

        """
        return self.send_cmd("check")

    def file_write(self, filepath: str, filename: str = None, slaveid: int = 0) -> bool:
        """
        Send a file to the servo drive.

        Parameters
        ----------
        filepath : str
            Path to file
        filename : str
            NOT USED (JUST FOR API COMPATIBILITY)
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------
        bool
            True if successfully written.

        """
        logger.info(f"Write: '{filepath}'")
        res = self._file_write('write', filepath)
        self.modem.reset()
        if not res:
            raise ExceptionUART(f'Could not write file {filepath}')
        return True

    def file_read(self, filename: str, output: Union[Type[str], Type[bytes]] = bytes, slaveid: int = 0) -> Union[bool, bytes, str]:
        """
        Read file from servo drive.
        Returns file content.

        Parameters
        ----------
        filename : str
            File name
        output : Union[Type[str], Type[bytes]]
            NOT USED (JUST FOR API COMPATIBILITY)
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------
        Union[bool, bytes, str]
            File content as str. Rest types for API COMPATIBILITY

        """

        logger.info(f"Read: '{filename}'")
        file_content = self._file_read('read', filename)
        self.modem.reset()
        if not file_content:
            raise ExceptionUART(f'Could not read file {filename}')

        return file_content

    def rm(self, filename: str, slaveid: int = None):
        """

        Parameters
        ----------
        filename :
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------

        """
        logger.info(f"Remove: '{filename}'")
        if not self.send_cmd(f'rm {filename}'):
                raise ExceptionUART(f'Could not delete file {filename}')

    def ls(self, slaveid: int = None) -> Dict[str, Any]:
        """

        Parameters
        ----------
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------

        """
        _list = self.send_cmd("ls")
        res = self._parse_file_list(_list)

        return res

    def get_bootloader_version(self, slaveid: int = 0) -> str:
        """
        Returns the bootloader version. Sets automatically the BOOT state.

        Parameters
        ----------
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------
        str
            Bootloader version as string.
        """

        return self.send_cmd("version")

    def get_bootloader_help(self, slaveid: int = 0) -> str:
        """
        Returns the bootloader help text. Sets automatically the BOOT state.

        Parameters
        ----------
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------
        str
            Bootloader help text.
        """

        return self.send_cmd("help")

    def flash_fw(self, binary_path: str, slaveid: int = 0) -> str:
        """
        Flash firmware.
        Firmware can be a binary (*.bin) or a SOMANET package (*.zip)

        Parameters
        ----------
        binary_path : str
            Path to binary/somanet package
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------
        str
            Response message
        """


        binary_path = self._get_fw_file(binary_path)
        res = self._file_write('flash', binary_path)
        return self._clean_msg(res)

    def remove_fw(self, slaveid: int = 0) -> str:
        """
        Remove firmware

        Parameters
        ----------
        slaveid : int
            NOT USED (JUST FOR API COMPATIBILITY)

        Returns
        -------
        str
            Response message (static msg, because

        """
        # Create pseudo binary, which contains only a string and flash this file.

        with self._empty_app() as empty_app:
            # Return value is always empty, because flashing the empty app is from the bootloaders point of view not successful.
            self._file_write('flash', empty_app)

        return "Successfully removed"


def _check_result(res: bytes):
    UARTFWUploader._print(res)
    if not res:
        logger.error("...FAILED!")


def print_file_list(file_list: Dict[str, Any]):
    max_len = max([len(f) for f in file_list.keys()])
    for name, size in file_list.items():
        print(f'{name:{max_len}}  {size:>4} b')


if __name__ == '__main__':
    import argparse

    if platform.system() == "Linux":
        default_serial = 'ttl232r-3v3-0'
        help_string = "On Linux the serial device looks like /dev/ttyUSB0."
    elif platform.system() == "Windows":
        help_string = "On Windows the serial device looks like COM1."
        default_serial = "COM1"

    parser = argparse.ArgumentParser(description=f"SOMANET Firmware Upgrader for UART bootloader - v{VERSION}")
    parser.add_argument('-d', '--device', dest='device', help="The name of the serial adapter. " + help_string, type=str, default=default_serial)
    parser.add_argument('-o', '--hold', dest='hold', help='Prevent booting the firmware and stay in bootloader mode.', action='store_true')
    parser.add_argument('-w', '--write', nargs='+', dest='write', metavar='FILE', help='Write <FILE> to device. Can be several files separated by space.', type=str)
    parser.add_argument('-r', '--read', nargs='+', dest='read', metavar='FILE', help='Read <FILE> on device. Can be several files separated by space.', type=str)
    parser.add_argument('-a', '--app', dest='app', metavar='APP', help='Flash firmware <APP> to device. Can also be a SOMANET firmware package (package_SOMANET_xxx.zip).',
                        type=str)
    parser.add_argument('-b', '--boot', dest='boot', help='Boot into firmware.', action='store_true')
    parser.add_argument('-l', '--list', dest='getlist', help='Get list of files.', action='store_true')
    parser.add_argument('-i', '--info', dest='info', help='Get flash storage info.', action='store_true')
    parser.add_argument('-c', '--check', dest='check', help='Check the flash storage.', action='store_true')
    parser.add_argument('-v', '--version', dest='version', help='Get bootloader version.', action='store_true')
    parser.add_argument('-bh', '--bootloader-help', dest='help', help='Show bootloader help.', action='store_true')
    parser.add_argument('-rm', '--remove', nargs='+', dest='remove', metavar='FILE', help='Remove <FILE> from device. Can be several files separated by space.', type=str)
    parser.add_argument('-rma', '--remove-app', dest='remove_bin', help='Remove firmware from device.', action='store_true')

    args = parser.parse_args()
    dev = args.device
    uart_fw = UARTFWUploader(dev)

    # Just always send hold
    uart_fw.send_cmd("hold")

    for arg, value in vars(args).items():
        if value is None or not value or arg == "device":
            continue

        if arg == "app":
            logger.info('Flash FW...')
            res = uart_fw.flash_fw(args.app)
            _check_result(res)
        elif arg == "write":
            uart_fw.write_file(args.write)
            logger.info(f'Done')
        elif arg == "read":
            uart_fw.read_file(args.read)
            logger.info(f'Done')
        elif arg == "boot":
            logger.info('Boot device...')
            res = uart_fw.boot()
            _check_result(res)
        elif arg in ("hold", "check", "info", "version", "help"):
            logger.info(f"{arg}...")
            res = uart_fw.send_cmd(arg)
            _check_result(res)
        elif arg == "getlist":
            logger.info(f"Get file list ...")
            file_list = uart_fw.ls()
            print_file_list(file_list)

        elif arg == "remove":
            logger.info(f'Remove "{args.remove}" from device...')
            uart_fw.rm(args.remove)
        elif arg == "remove_bin":
            logger.info("Remove app from device...")
            uart_fw.remove_fw()
        else:
            parser.print_help()

    uart_fw.close()
