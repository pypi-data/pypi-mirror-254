#!/usr/bin/env python
# coding: utf-8

from typing import List

from xrpl.asyncio.clients import AsyncWebsocketClient
from xrpl.models import TransactionMetadata
from xrpl.models.transactions.metadata import (
    HookExecution,
    HookExecutionFields,
    HookEmission,
    HookEmissionFields,
)
from xrpl.models.requests import Tx
from xrpl.utils.str_conversions import hex_to_str


class iHookExecution:
    def __init__(self, hook_execution: HookExecutionFields):
        self.HookAccount = hook_execution["HookAccount"]
        self.HookEmitCount = hook_execution["HookEmitCount"]
        self.HookExecutionIndex = hook_execution["HookExecutionIndex"]
        self.HookHash = hook_execution["HookHash"]
        self.HookInstructionCount = hook_execution["HookInstructionCount"]
        self.HookResult = hook_execution["HookResult"]
        self.HookReturnCode = hook_execution["HookReturnCode"]
        self.HookReturnString = hex_to_str(hook_execution["HookReturnString"]).replace(
            "\x00", ""
        )
        self.HookStateChangeCount = hook_execution["HookStateChangeCount"]
        self.Flags = hook_execution["Flags"]


class iHookEmission:
    def __init__(self, hook_emission: HookEmissionFields):
        self.EmittedTxnID = hook_emission["EmittedTxnID"]
        self.HookAccount = hook_emission["HookAccount"]
        self.HookHash = hook_emission["HookHash"]
        self.EmitNonce = hook_emission["EmitNonce"]


class iHookExecutions:
    def __init__(self, results: List[HookExecution]):
        self.executions = [iHookExecution(entry["HookExecution"]) for entry in results]


class iHookEmissions:
    def __init__(self, results: List[HookEmission]):
        self.txs = [iHookEmission(entry["HookEmission"]) for entry in results]


class ExecutionUtility:
    @staticmethod
    async def get_hook_executions_from_meta(meta: TransactionMetadata):
        if not meta["HookExecutions"]:
            raise Exception("No HookExecutions found")

        return iHookExecutions(meta["HookExecutions"])

    @staticmethod
    async def get_hook_executions_from_tx(client: AsyncWebsocketClient, hash: str):
        if not client.is_open():
            raise Exception("xrpl Client is not connected")

        tx_response = await client.request(Tx(transaction=hash))

        hook_executions = tx_response.result.get("meta", {}).get("HookExecutions")
        if not hook_executions:
            raise Exception("No HookExecutions found")

        return iHookExecutions(hook_executions)

    @staticmethod
    async def get_hook_emitted_txs_from_meta(meta: TransactionMetadata):
        if not meta["HookEmissions"]:
            raise Exception("No HookEmissions found")

        return iHookEmissions(meta["HookEmissions"])
