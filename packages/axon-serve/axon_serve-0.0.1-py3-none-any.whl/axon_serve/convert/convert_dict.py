from typing import Any
from google.protobuf.struct_pb2 import Struct


def dict_to_struct(dict: dict[str, Any]) -> Struct:
    struct = Struct()
    struct.update(dict)

    return struct


def struct_to_dict(struct: Struct) -> dict[str, Any]:
    dict_out: dict[str, Any] = {}

    for key, value in struct.items():
        if isinstance(value, Struct):
            dict_out[key] = struct_to_dict(value)
        else:
            dict_out[key] = value

    return dict_out
