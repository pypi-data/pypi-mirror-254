from collections import OrderedDict
from typing import Union

import xmltodict

from .BaseEtherCAT import EcTypes

# ec_types = {
#     "BOOL":             "bool",
#     "SINT":             "int8",
#     "INT":              "int16",
#     "DINT":             "int32",
#     "LINT":             "int64",
#     "USINT":            "uint8",
#     "UINT":             "uint16",
#     "UDINT":            "uint32",
#     "ULINT":            "uint64",
#     "REAL":             "float",
#     "DOUBLE":           "double",
#     "STRING(2)":        "string",
#     "STRING(8)":        "string",
#     "STRING(50)":       "string",
#     "OCTET_STRING(8)":  "octet_string",
#     "OCTET_STRING(25)": "octet_string",
# }
#
# class Types(Enum):
#     BOOL = 1
#     INT8 = 2
#     INT16 = 3
#     INT32 = 4
#     INT64 = 5
#     UINT8 = 6
#     UINT16 = 7
#     UINT32 = 8
#     UINT64 = 9
#     FLOAT = 10
#     DOUBLE = 11
#     STRING = 12
#     OCTET_STRING = 13
#     UNICODE_STRING = 14
#     SM8 = 15
#     SM16 = 16
#     SM32 = 17
#     SM64 = 18
#
#     types_ = {  # name, bytesize, signed, bitstruct symbol
#         ect.ECT_BOOLEAN:        ("bool", 1, True, 'b8'),
#         ect.ECT_INTEGER8:       ("int8", 1, True, 's8'),
#         ect.ECT_INTEGER16:      ("int16", 2, True, 's16'),
#         ect.ECT_INTEGER32:      ("int32", 4, True, 's32'),
#         ect.ECT_INTEGER64:      ("int64", 8, True, 's64'),
#         ect.ECT_UNSIGNED8:      ("uint8", 1, False, 'u8'),
#         ect.ECT_UNSIGNED16:     ("uint16", 2, False, 'u16'),
#         ect.ECT_UNSIGNED32:     ("uint32", 4, False, 'u32'),
#         ect.ECT_UNSIGNED64:     ("uint64", 8, False, 'u64'),
#         ect.ECT_REAL32:         ("float", 4, True, 'f32'),
#         ect.ECT_REAL64:         ("double", 8, True, 'f64'),
#         ect.ECT_VISIBLE_STRING: ("string", None, None, 't'),
#         ect.ECT_OCTET_STRING:   ("octet_string", None, None, 't'),
#         ect.ECT_BIT1:           ("bit1", 0.1, False, "u1"),
#         ect.ECT_BIT2:           ("bit2", None, None, None),
#         ect.ECT_BIT3:           ("bit3", None, None, None),
#         ect.ECT_BIT4:           ("bit4", None, None, None),
#         ect.ECT_BIT5:           ("bit5", None, None, None),
#         ect.ECT_BIT6:           ("bit6", None, None, None),
#         ect.ECT_BIT7:           ("bit7", None, None, None),
#         ect.ECT_BIT8:           ("bit8", None, None, None),
#     }

def convert_str(value: str) -> Union[float, int, str]:
    if v := EcTypes(value):
        return v.esi_name
    elif "." in value:
        try:
            value = float(value)
        except:
            pass
    else:
        try:
            value = int(value)
        except:
            pass
    return value


class SubEntry:

    def __init__(self, od: OrderedDict):
        for name, value in od.items():
            if isinstance(value, str):
                setattr(self, name, convert_str(value))
            else:
                setattr(self, name, value)


class ObjectIndex:

    def __init__(self, od: OrderedDict):
        for name, value in od.items():
            if name == "SubItem" and isinstance(value, list):
                self.subitems = [ObjectIndex(o) for o in value]
            else:
                if isinstance(value, str):
                    setattr(self, name, convert_str(value))
                elif isinstance(value, OrderedDict):
                    setattr(self, name, SubEntry(value))
                else:
                    setattr(self, name, value)

    def __getitem__(self, subindex):
        return self.subitems[subindex]

    def __iter__(self):
        return iter(self.subitems)

    def __len__(self):
        return len(self.subitems)

    def __contains__(self, subindex):
        return subindex in self.subitems

    def __str__(self):
        return str(self.subitems)


class ESI:

    def __init__(self, esi_file: str):
        f = open(esi_file, "r")
        xml_cont = f.read()
        f.close()

        od_dict = xmltodict.parse(xml_cont)
        # objects = od_dict["EtherCATInfo"]["Descriptions"]["Devices"]["Device"]["Profile"]["Dictionary"]["Objects"]["Object"]
        objects = od_dict["EtherCATInfo"]["Descriptions"]["Devices"]["Device"]["Profile"]["Dictionary"]["DataTypes"]["DataType"]
        self.object_dict = {}

        for o in objects:
            if not o.get("Name"):
                continue

            idx = o.pop("Name")
            idx = idx.replace("DT", "0x")
            try:
                idx = int(idx, 16)
            except:
                continue
            self.object_dict[idx] = ObjectIndex(o)

    def __getitem__(self, idx):
        return self.object_dict[idx]

    def __iter__(self):
        return iter(self.object_dict)

    def __len__(self):
        return len(self.object_dict)

    def __contains__(self, idx):
        return idx in self.object_dict

    def __str__(self):
        return str(self.object_dict)
