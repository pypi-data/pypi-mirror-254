#!/usr/bin/env python
# coding: utf-8

from typing import Any
from xrpl.clients import Client

from hooks_toolkit.libs.xrpl_helpers.transaction import app_transaction
from hooks_toolkit.types import SmartContractParams
from hooks_toolkit.libs.keylet_utils import ExecutionUtility


class Xrpld:
    @staticmethod
    def submit(client: Client, params: SmartContractParams) -> Any:
        # validate(built_tx)
        tx_response = app_transaction(
            client,
            params.tx,
            params.wallet,
            hard_fail=True,
            count=1,
            delay_ms=1000,
        )
        tx_result = tx_response.result.get("meta")["TransactionResult"]
        if tx_result == "tecHOOK_REJECTED":
            hook_executions = ExecutionUtility.get_hook_executions_from_meta(
                tx_response.result.get("meta"),
            )
            raise ValueError(hook_executions.executions[0].HookReturnString)
        return tx_response.result
