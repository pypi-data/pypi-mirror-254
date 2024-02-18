from xrpl.asyncio.clients import AsyncWebsocketClient
from xrpl.models.requests import LedgerEntry
from xrpl.models.requests.ledger_entry import Hook, HookDefinition, HookState
from xrpl.models.requests.account_namespace import AccountNamespace


class StateUtility:
    @staticmethod
    async def get_hook(client: AsyncWebsocketClient, account: str) -> Hook:
        if not client.is_open():
            raise Exception("xrpl Client is not connected")
        hook_req = LedgerEntry(
            hook={
                "account": account,
            },
        )
        hook_res = await client.request(hook_req)
        return hook_res.result["node"]

    @staticmethod
    async def get_hook_definition(
        client: AsyncWebsocketClient, hash: str
    ) -> HookDefinition:
        if not client.is_open():
            raise Exception("xrpl Client is not connected")
        hook_def_request = LedgerEntry(
            hook_definition=hash,
        )
        hook_def_res = await client.request(hook_def_request)
        return hook_def_res.result["node"]

    @staticmethod
    async def get_hook_state_dir(
        client: AsyncWebsocketClient, account: str, namespace: str
    ):
        if not client.is_open():
            raise Exception("xrpl Client is not connected")
        response = await client.request(
            AccountNamespace(account=account, namespace_id=namespace)
        )
        return response.result["namespace_entries"]

    @staticmethod
    async def get_hook_state(
        client: AsyncWebsocketClient, account: str, key: str, namespace: str
    ) -> HookState:
        if not client.is_open():
            raise Exception("xrpl Client is not connected")
        hook_state_req = LedgerEntry(
            hook_state={
                "account": account,
                "key": key,
                "namespace_id": namespace,
            },
        )
        hook_state_resp = await client.request(hook_state_req)
        return hook_state_resp.result["node"]
