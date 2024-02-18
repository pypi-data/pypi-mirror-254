#!/usr/bin/env python
# coding: utf-8

from xrpl.models.transactions.transaction import HookParameter
from xrpl.utils.str_conversions import hex_to_str, str_to_hex


class iHookParamName:
    def __init__(self, value: str, is_hex: bool = False):
        self.value = value
        self.is_hex = is_hex

    @staticmethod
    def from_hex(hex_value: str):
        return iHookParamName(hex_to_str(hex_value))

    def to_hex(self):
        return str_to_hex(self.value)


class iHookParamValue:
    def __init__(self, value: str, is_hex: bool = False):
        self.value = value
        self.is_hex = is_hex

    @staticmethod
    def from_hex(hex_value: str):
        return iHookParamValue(hex_to_str(hex_value))

    def to_hex(self):
        return str_to_hex(self.value)


class iHookParamEntry:
    def __init__(self, name: iHookParamName, value: iHookParamValue):
        self.name = name
        self.value = value

    def from_hex(self, name: str, value: str):
        self.name = iHookParamName.from_hex(name)
        self.value = iHookParamValue.from_hex(value)

    def to_xrpl(self):
        return HookParameter(
            hook_parameter_name=self.name.to_hex()
            if not self.name.is_hex
            else self.name.value,
            hook_parameter_value=self.value.to_hex()
            if not self.value.is_hex
            else self.value.value,
        )


class iHookParamEntries:
    def __init__(self, parameters: list[iHookParamEntry]):
        self.parameters = parameters
