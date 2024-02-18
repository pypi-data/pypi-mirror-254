#!/usr/bin/env python
# coding: utf-8

from xrpl.models.transactions.set_hook import HookGrant


class HookGrantAuthorize:
    def __init__(self, value: str):
        self.value = value

    @classmethod
    def from_value(cls, value: str):
        return cls(value)


class HookGrantEntries:
    def __init__(self, grants: list):
        self.grants = grants


class HookGrantHash:
    def __init__(self, value: str):
        self.value = value

    @classmethod
    def from_value(cls, value: str):
        return cls(value)


class HookGrantEntry:
    def __init__(self, hash: HookGrantHash, account: HookGrantAuthorize = None):
        self.hash = hash
        self.account = account

    def from_hex(self, hash: str, account: str):
        self.hash = HookGrantHash(hash)
        self.account = HookGrantAuthorize(account)

    def to_xrpl(self) -> HookGrant:
        hook_grant = HookGrant(HookHash=self.hash.value)
        if self.account and self.account.value:
            hook_grant["HookGrant"]["Authorize"] = self.account.value
        return hook_grant
