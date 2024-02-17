from abc import ABC
from typing import Union, Dict
from enum import Enum

# This is here to prevent circular imports
class EcStates(Enum):
    NONE = 0x0
    INIT = 0x1
    PREOP = 0x2
    BOOT = 0x3
    SAFEOP = 0x4
    OP = 0x8
    ERROR = 0x10
    #ACK = 0x10

    def __eq__(self, other):
        return self.value == other.value

    @classmethod
    def is_error_state(cls, state):
        return bool(state.value & cls.ERROR)

    @classmethod
    def get_seperate_state(cls, state):
        return cls(state % cls.ERROR.value), cls(state & cls.ERROR.value)



class BaseCANOpen(ABC):

    def start_pdo_com(self, *args, **kwargs):
        ...

    def stop_pdo_com(self, *args, **kwargs):
        ...

    def exchange_pdo(self, slaveid: int = 0, **kwargs) -> Dict[str, Union[int, str, float]]:
        ...

    def upload(self, index: int, subindex: int, slaveid: int = 0) -> Union[str, float, int, bool]:
        ...

    def download(self, index: int, subindex: int, value: Union[str, int, float, bool], slaveid: int = 0):
        ...

    def set_state(self, state: EcStates, timeout: int = 10, slaveid: int = 0):
        ...

    def get_state(self, slaveid: int = 0) -> EcStates:
        ...


