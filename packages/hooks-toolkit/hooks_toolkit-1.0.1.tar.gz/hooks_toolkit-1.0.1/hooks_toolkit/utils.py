#!/usr/bin/env python
# coding: utf-8

import hashlib
import struct


def get_xrp_balance(client, wallet):
    request = {"command": "account_info", "account": wallet.classic_address}
    response = client.request(request)
    return response["result"]["account_data"]["Balance"]


def make_xfl(exponent, mantissa):
    # convert types as needed
    if not isinstance(exponent, int):
        exponent = int(exponent)

    if not isinstance(mantissa, int):
        mantissa = int(mantissa)

    # canonical zero
    if mantissa == 0:
        return 0

    # normalize
    is_negative = mantissa < 0
    if is_negative:
        mantissa *= -1

    while mantissa > 9999999999999999:
        mantissa //= 10
        exponent += 1
    while mantissa < 1000000000000000:
        mantissa *= 10
        exponent -= 1

    # canonical zero on mantissa underflow
    if mantissa == 0:
        return 0

    # under and overflows
    if exponent > 80 or exponent < -96:
        return -1  # note this is an "invalid" XFL used to propagate errors

    exponent += 97

    xfl = 1 if not is_negative else 0
    xfl <<= 8
    xfl |= exponent
    xfl <<= 54
    xfl |= mantissa

    return xfl


def get_exponent(xfl):
    if xfl < 0:
        raise ValueError("Invalid XFL")
    if xfl == 0:
        return 0
    return ((xfl >> 54) & 0xFF) - 97


def get_mantissa(xfl):
    if xfl < 0:
        raise ValueError("Invalid XFL")
    if xfl == 0:
        return 0
    return xfl - ((xfl >> 54) << 54)


def is_negative(xfl):
    if xfl < 0:
        raise ValueError("Invalid XFL")
    if xfl == 0:
        return False
    return ((xfl >> 62) & 1) == 0


def to_string(xfl):
    if xfl < 0:
        raise ValueError("Invalid XFL")
    if xfl == 0:
        return "<zero>"
    return (
        ("-" if is_negative(xfl) else "+")
        + str(get_mantissa(xfl))
        + "E"
        + str(get_exponent(xfl))
    )


def float_to_xfl(fl):
    e = 0
    d = str(float(fl)).lower()
    s = d.split("e")
    if len(s) == 2:
        e = int(s[1])
        d = s[0]
    s = d.split(".")
    if len(s) == 2:
        d = d.replace(".", "")
        e -= len(s[1])
    else:
        d = str(0)

    return make_xfl(e, d)


def float_to_be_xfl(fl):
    xfl = float_to_xfl(fl)
    return hex(xfl)[2:].upper()


def float_to_le_xfl(fl):
    xfl = float_to_xfl(fl)
    return flip_be_le(xfl)


def flip_be_le(endian):
    hex_string = hex(endian)[2:].upper()
    flipped_hex = ""
    for i in range(len(hex_string) - 2, -1, -2):
        flipped_hex += hex_string[i : i + 2]
    return flipped_hex


def flip_hex(hex_string):
    flipped_hex = ""
    for i in range(len(hex_string) - 2, -1, -2):
        flipped_hex += hex_string[i : i + 2]
    return flipped_hex


def flip_endian(n):
    # convert the number to a byte array
    arr = struct.pack(">I", n)

    # swap the data in the array
    arr = bytearray(arr)
    arr[0], arr[3] = arr[3], arr[0]
    arr[1], arr[2] = arr[2], arr[1]

    # perform bit-shifting and OR to get flipped Endian
    flipped_endian = struct.unpack("<I", arr)[0]

    return flipped_endian


def int_to_hex(integer, byte_length):
    hex_string = hex(integer)[2:].zfill(byte_length * 2)
    return hex_string


def read_hook_binary_hex_from_ns(filename: str):
    with open(f"build/{filename}.wasm", "rb") as file:
        wasm = file.read()
    return wasm.hex().upper()


def hex_namespace(hook_namespace_seed: str):
    return hashlib.sha256(hook_namespace_seed.encode()).hexdigest().upper()


def generate_hash(data_bytes: bytes):
    hash_ = hashlib.sha512(data_bytes).digest()
    return hash_[:32].hex().upper()


def pad_hex_string(input_, target_length=64):
    padded_string = input_.zfill(target_length)
    return padded_string
