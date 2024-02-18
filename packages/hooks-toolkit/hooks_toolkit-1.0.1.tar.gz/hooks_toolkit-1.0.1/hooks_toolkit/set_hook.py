#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any

from xrpl.clients.sync_client import SyncClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import SetHook
from xrpl.models.transactions.set_hook import Hook
from xrpl.utils import calculate_hook_on
from xrpl.models.transactions import SetHookFlag

from hooks_toolkit.libs.xrpl_helpers.transaction import (
    get_transaction_fee,
    app_transaction,
)
from hooks_toolkit.utils import hex_namespace, read_hook_binary_hex_from_ns
from hooks_toolkit.types import SetHookParams


def create_hook_payload(
    params: SetHookParams,
) -> Hook:
    kwargs: Dict[str, Any] = {
        "hook_api_version": params.version,
        "hook_namespace": hex_namespace(params.namespace),
    }

    if params.create_file is not None:
        kwargs["create_code"] = read_hook_binary_hex_from_ns(params.create_file)

    if params.hook_on_array is not None:
        kwargs["hook_on"] = calculate_hook_on(params.hook_on_array)

    if params.hook_hash is not None:
        kwargs["hook_hash"] = params.hook_hash

    if params.flags is not None:
        kwargs["flags"] = params.flags

    if params.hook_parameters is not None:
        kwargs["hook_parameters"] = params.hook_parameters

    if params.hook_grants is not None:
        kwargs["hook_grants"] = params.hook_grants

    return Hook(**kwargs)


def set_hooks_v3(client: SyncClient, seed: str, hooks: List[Hook]):
    HOOK_ACCOUNT = Wallet(seed, 0)
    _tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
    )
    tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
        fee=get_transaction_fee(client, _tx),
    )

    app_transaction(client, tx, HOOK_ACCOUNT, hard_fail=True, count=2, delay_ms=1000)


def clear_all_hooks_v3(client: SyncClient, seed: str):
    HOOK_ACCOUNT = Wallet(seed, 0)
    hook = Hook(
        **{
            "create_code": "",
            "flags": [SetHookFlag.HSF_OVERRIDE, SetHookFlag.HSF_NS_DELETE],
        }
    )
    _tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=[hook, hook, hook, hook, hook, hook, hook, hook, hook, hook],
    )
    tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=[hook, hook, hook, hook, hook, hook, hook, hook, hook, hook],
        fee=get_transaction_fee(client, _tx),
    )

    app_transaction(client, tx, HOOK_ACCOUNT, hard_fail=True, count=2, delay_ms=1000)


def clear_hook_state_v3(client: SyncClient, seed: str, hooks: List[Hook]):
    HOOK_ACCOUNT = Wallet(seed, 0)
    _tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
    )
    tx = SetHook(
        account=HOOK_ACCOUNT.classic_address,
        hooks=hooks,
        fee=get_transaction_fee(client, _tx),
    )
    app_transaction(client, tx, HOOK_ACCOUNT, hard_fail=True, count=2, delay_ms=1000)
