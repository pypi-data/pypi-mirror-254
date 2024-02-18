#!/usr/bin/env python
# coding: utf-8

from hooks_toolkit.libs.binary_models import BaseModel, XFL, Currency, XRPAddress


class AmountModel(BaseModel):
    def __init__(
        self,
        value: XFL = None,
        currency: Currency = None,
        issuer: XRPAddress = None,
    ):
        self.value = value
        self.currency = currency
        self.issuer = issuer
        super().__init__()

    @staticmethod
    def get_metadata():
        return [
            {"field": "value", "type": "xfl"},
            {"field": "currency", "type": "currency"},
            {"field": "issuer", "type": "xrpAddress"},
        ]
