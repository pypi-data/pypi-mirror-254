#!/usr/bin/env python
# coding: utf-8

from typing import List

from xrpl.clients import Client
from xrpl.wallet import Wallet
from xrpl.models.amounts import IssuedCurrencyAmount

from hooks_toolkit.libs.xrpl_helpers.tools import (
    Account,
    ICXRP,
    balance,
    fund,
    account_set,
    limit,
    trust,
    pay,
)


def fund_system(
    client: Client,
    wallet: Wallet,
    ic: IssuedCurrencyAmount,
    native_balance: int,
    ic_limit: int,
    ic_balance: int,
) -> None:
    user_accounts = [
        "alice",
        "bob",
        "carol",
        "dave",
        "elsa",
        "frank",
        "grace",
        "heidi",
        "ivan",
        "judy",
    ]
    user_wallets: List[Account] = [Account(acct) for acct in user_accounts]
    hook_accounts = [
        "hook1",
        "hook2",
        "hook3",
        "hook4",
        "hook5",
    ]
    hook_wallets: List[Account] = [Account(hacct) for hacct in hook_accounts]

    USD = ic

    gw: Account = Account("gw")
    if balance(client, gw.wallet.classic_address) == 0:
        fund(client, wallet, ICXRP(native_balance), gw.wallet.classic_address)
        account_set(client, gw.wallet)

    needs_funding = []
    needs_lines = []
    needs_ic = []

    for acct in user_wallets:
        if balance(client, acct.wallet.classic_address) < (native_balance / 2):
            needs_funding.append(acct.wallet.classic_address)
        if limit(client, acct.wallet.classic_address, USD) < (ic_limit / 2):
            needs_lines.append(acct.wallet)
        if balance(client, acct.wallet.classic_address, USD) < (ic_balance / 2):
            needs_ic.append(acct.wallet.classic_address)

    for hacct in hook_wallets:
        if balance(client, hacct.wallet.classic_address) < (native_balance / 2):
            needs_funding.append(hacct.wallet.classic_address)

    print(f"FUNDING: {len(needs_funding)}")
    print(f"TRUSTING: {len(needs_lines)}")
    print(f"PAYING: {len(needs_ic)}")

    fund(client, wallet, ICXRP(native_balance), *needs_funding)
    trust(client, USD.set(ic_limit), *needs_lines)
    pay(client, USD.set(ic_balance), gw.wallet, *needs_ic)
