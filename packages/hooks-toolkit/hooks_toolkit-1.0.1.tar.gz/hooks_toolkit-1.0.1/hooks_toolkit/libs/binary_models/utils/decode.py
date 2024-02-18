#!/usr/bin/env python
# coding: utf-8

from typing import Any

from xrpl.utils import hex_to_str
from xrpl.core.addresscodec import encode_classic_address

from ..utils import length_to_hex
from .types import (
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    UInt224,
    VarString,
    XFL,
    Currency,
    XRPAddress,
)

from hooks_toolkit.utils import flip_hex, to_string


def decode_field(
    field_value: Any, field_type: str, max_string_length: int = None
) -> str:
    if field_type == "uint8":
        return hex_to_uint8(field_value)
    elif field_type == "uint32":
        return hex_to_uint32(field_value)
    elif field_type == "uint64":
        return hex_to_uint64(field_value)
    elif field_type == "uint224":
        return hex_to_uint224(field_value)
    elif field_type == "hash256":
        return field_value
    elif field_type == "publicKey":
        return field_value
    elif field_type == "varString":
        if max_string_length is None:
            raise ValueError("maxStringLength is required for type varString")
        return hex_to_var_string(field_value, max_string_length)
    elif field_type == "xfl":
        return hex_to_xfl(field_value)
    elif field_type == "currency":
        return hex_to_currency(field_value)
    elif field_type == "xrpAddress":
        return hex_to_xrp_address(field_value)
    else:
        raise ValueError(f"Unknown type: {field_type}")


# Define the functions for decoding each type
def hex_to_uint8(hex_str: str) -> UInt8:
    return int(hex_str, 16)


def hex_to_uint16(hex_str: str) -> UInt16:
    return int(hex_str, 16)


def hex_to_uint32(hex_str: str) -> UInt32:
    return int(hex_str, 16)


def hex_to_uint64(hex_str: str) -> UInt64:
    return int(hex_str, 16)


def hex_to_uint224(hex_str: str) -> UInt224:
    return int(hex_str, 16)


def hex_to_var_string_length(hex_string, max_string_length):
    if max_string_length <= 2**8:
        # 1-byte length
        return int(hex_string[:2], 16)
    elif max_string_length <= 2**16:
        # 2-byte length
        return int(hex_string[:4], 16)
    raise ValueError("max_string_length exceeds 2 bytes")


def hex_to_var_string(hex_str: str, max_string_length: int) -> VarString:
    length = hex_to_var_string_length(hex_str, max_string_length)
    prefix_length = length_to_hex(length, max_string_length)
    content = hex_str[len(prefix_length) :]
    return bytes.fromhex(content).decode("utf-8")[:length]


def hex_to_xfl(hex_str: str) -> XFL:
    if hex_str == "0000000000000000":
        return 0
    value = flip_hex(hex_str)
    xfl = hex_to_uint64(value[:16])
    return float(to_string(xfl))


def hex_to_currency(hex_str: str) -> Currency:
    clean_hex = hex_str.replace("0", " ").strip().replace(" ", "0")
    value = hex_to_str(clean_hex)
    return value.replace("\0", "").strip()


def hex_to_xrp_address(hex_str: str) -> XRPAddress:
    value = encode_classic_address(bytes.fromhex(hex_str))
    return value[:40]
