#!/usr/bin/env python
# coding: utf-8

import dataclasses
from typing import List, Optional

from xrpl.models.transactions import (
    Transaction,
    SetHookFlag,
)
from xrpl.models.transactions.set_hook import HookParameter, HookGrant
from xrpl.wallet import Wallet


@dataclasses.dataclass
class SmartContractParams:
    wallet: Wallet
    tx: Transaction


@dataclasses.dataclass
class SetHookParams:
    namespace: str
    version: Optional[int] = None
    hook_hash: Optional[str] = None
    create_file: Optional[str] = None
    flags: Optional[List[SetHookFlag]] = None
    hook_on_array: Optional[List[SetHookFlag]] = None
    hook_parameters: Optional[List[HookParameter]] = None
    hook_grants: Optional[List[HookGrant]] = None
