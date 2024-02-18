#!/usr/bin/env python
# coding: utf-8

import binascii
from typing import Any

from xrpl.utils import str_to_hex
from xrpl.core.addresscodec import decode_classic_address

from hooks_toolkit.utils import float_to_le_xfl


def encode_field(
    field_value: Any, field_type: str, max_string_length: int = None
) -> str:
    if field_type == "uint8":
        return uint8_to_hex(field_value)
    elif field_type == "uint32":
        return uint32_to_hex(field_value)
    elif field_type == "uint16":
        return uint16_to_hex(field_value)
    elif field_type == "uint64":
        return uint64_to_hex(field_value)
    elif field_type == "uint224":
        return uint224_to_hex(field_value)
    elif field_type == "hash256":
        return field_value
    elif field_type == "publicKey":
        return field_value
    elif field_type == "varString":
        if max_string_length is None:
            raise ValueError("maxStringLength is required for type varString")
        return var_string_to_hex(field_value, max_string_length)
    elif field_type == "xfl":
        return xfl_to_hex(field_value)
    elif field_type == "currency":
        return currency_to_hex(field_value)
    elif field_type == "xrpAddress":
        return xrp_address_to_hex(field_value)
    else:
        raise ValueError(f"Unknown type: {field_type}")


def uint8_to_hex(value: int) -> str:
    return value.to_bytes(1, byteorder="big").hex().upper()


def uint16_to_hex(value: int) -> str:
    return value.to_bytes(2, byteorder="big").hex().upper()


def uint32_to_hex(value: int) -> str:
    return value.to_bytes(4, byteorder="big").hex().upper()


def uint64_to_hex(value: int) -> str:
    return value.to_bytes(8, byteorder="big").hex().upper()


def uint224_to_hex(value: int) -> str:
    return value.to_bytes(28, byteorder="big").hex().upper()


def length_to_hex(value, max_string_length):
    if max_string_length <= 2**8:
        # 1-byte length
        return format(value, "02x")
    elif max_string_length <= 2**16:
        # 2-byte length
        return format(value, "04x")
    raise ValueError("max_string_length exceeds 2 bytes")


def var_string_to_hex(value: str, max_string_length: int) -> str:
    if len(value) > max_string_length:
        raise ValueError(
            f"String length {len(value)} exceeds max length of {max_string_length}"
        )
    prefix_length = length_to_hex(len(value), max_string_length)
    content = binascii.hexlify(value.encode("utf-8")).decode("utf-8")
    padded_content = content.ljust(max_string_length * 2, "0")
    return (prefix_length + padded_content).upper()


def xfl_to_hex(value: float) -> str:
    if value == 0:
        return "0000000000000000"
    return float_to_le_xfl(str(value))


def currency_to_hex(value: str) -> str:
    content = str_to_hex(value)
    return content.ljust(16, "0").rjust(40, "0").upper()


def xrp_address_to_hex(value: str) -> str:
    content = decode_classic_address(value)
    return binascii.hexlify(content).decode("utf-8").upper()
