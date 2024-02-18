#!/usr/bin/env python
# coding: utf-8

from hooks_toolkit.libs.binary_models import BaseModel, UInt64, VarString


class TestModel(BaseModel):
    def __init__(
        self,
        update_time: UInt64 = None,
        updated_by: VarString = None,
        message: VarString = None,
    ):
        self.update_time = update_time
        self.updated_by = updated_by
        self.message = message
        super().__init__()

    @staticmethod
    def get_metadata():
        return [
            {"field": "update_time", "type": "uint64"},
            {"field": "update_by", "type": "varString", "maxStringLength": 32},
            {"field": "message", "type": "varString", "maxStringLength": 250},
        ]
