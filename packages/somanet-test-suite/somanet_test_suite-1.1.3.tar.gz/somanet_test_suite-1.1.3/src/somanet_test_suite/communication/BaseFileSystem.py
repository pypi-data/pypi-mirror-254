from abc import ABC
import glob
import os
import re
import tempfile
import zipfile
from typing import Union, List, Dict, Type, Callable


class ExceptionFileSystem(Exception):
    pass


class BaseFileSystem(ABC):


    def file_read(self, cmd: str, output: Union[Type[str], Type[bytes]] = bytes, slaveid: int = 0) -> Union[bool, bytes, str]:
        ...

    def file_write(self, filepath: str, filename: str = None, slaveid: int = 0) -> bool:
        ...

    def get_bootloader_version(self, slaveid: int = 0) -> str:
        ...

    def get_bootloader_help(self, slaveid: int = 0) -> str:
        ...

    def ls(self, slaveid: int = 0) -> List[Dict[str, Union[str, int]]]:
        ...

    def rm(self, filename: str, slaveid: int = 0) -> str:
        ...

    def get_filesystem_info(self, slaveid: int = 0) -> Dict[str, int]:
        ...

    def flash_fw(self, filepath: str, slaveid: int = 0) -> bool:
        ...

    def remove_fw(self, slaveid: int = 0) -> bool:
        ...


class SomanetFileSystem:

    def _parse_file_list(self, file_list: str) -> Dict[str, Union[str, int]]:
        """
        Returns the bootloader version. Sets automatically the BOOT state.

        Parameters
        ----------
        slaveid : int
            Slave ID

        Returns
        -------
        List[Dict[str, Union[str, int]]]
            List with dictionary with items name:str and size:int in bytes.
        """
        res = dict()
        try:
            file_list = re.findall(r'(.+), size: (.+)', file_list)
        except TypeError:
            raise ExceptionFileSystem("Could not parse file list.")

        for name, size in file_list:
            res[name] = int(size)

        return res

    def _parse_filesystem_info(self, fs_info: str) -> Dict[str, int]:
        """
        Returns total, used and free memory on filesystem in bytes.

        Parameters
        ----------
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionIgH: If not possible, to parse filesystem info message.

        Returns
        -------
        Dict[str, int]
            Dict with total and used amount of bytes.
        """
        res = re.findall(r'(\d+)', fs_info)
        if not res:
            raise ExceptionFileSystem("Could not parse filesystem info message")

        return {"total": int(res[0]), "used": int(res[1]), "free": int(res[0]) - int(res[1])}

    def _get_fw_file(self, filepath: str) -> str:
        """
        Flash firmware to EtherCAT Slave. Set's automatically state BOOT.

        Parameters
        ----------
        filepath : str
            Path to firmware file. Can be the binary file with pattern "app.*.bin" or a SOMANET package
            (Will only flash the firmware binary).
        slaveid : int
            Slave ID

        Raises
        ------
            ExceptionFileSystem: If firmware file does not exist
            ExceptionFileSystem: If firmware is not a valid SOMANET firmware.

        Returns
        -------
        str
            Path to binary

        """
        if not os.path.exists(filepath):
            raise ExceptionFileSystem(f'File does not exists')

        file_name = os.path.basename(filepath)

        if re.match(r"^package.+\.zip$", file_name, re.M):
            # Unzip package to a temporary directory.
            dtemp = tempfile.mkdtemp(None, 'somanet-')
            with zipfile.ZipFile(filepath) as zf:
                zf.extractall(dtemp)
            filepath = glob.glob(os.path.join(dtemp, 'app*.bin'))[0]
            if not filepath:
                raise ExceptionFileSystem('No valid firmware found in package')

        elif not re.match(r'^app.+\.bin$', file_name, re.M):
            raise ExceptionFileSystem(f'{file_name}" is not a valid SOMANET firmware')

        return filepath

    def _empty_app(self) -> 'CreateAppEmpty':
        """
        Returns a context manager, which creates and deletes an empty pseudo app.

        Returns
        -------
        CreateAppEmpty
            Context manager
        """

        class CreateAppEmpty:
            bin_empty = 'app_empty.bin'

            def __enter__(self):
                if not os.path.isfile(self.bin_empty):
                    with open(self.bin_empty, 'w') as f:
                        f.write("void\n")

                return self.bin_empty

            def __exit__(self, exc_type, exc_val, exc_tb):
                os.remove(self.bin_empty)

        return CreateAppEmpty()
