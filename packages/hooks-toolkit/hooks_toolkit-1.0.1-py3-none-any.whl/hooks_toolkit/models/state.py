from xrpl.models.requests.ledger_entry import HookState
from xrpl.utils.str_conversions import hex_to_str, str_to_hex


class iHookState:
    def __init__(self, entry: HookState):
        self.entry = iHookStateEntry(entry)


class iHookStateData:
    def __init__(self, data: str):
        self.data = data

    @staticmethod
    def from_value(value: str):
        return iHookStateData(hex_to_str(value))

    def hex(self):
        return str_to_hex(self.data)


class iHookStateEntry:
    def __init__(self, hook_state: HookState):
        self.key = iHookStateKey.from_value(hook_state["HookStateKey"])
        self.data = iHookStateData.from_value(hook_state["HookStateData"])


class iHookStateKey:
    def __init__(self, key: str):
        self.key = key

    @staticmethod
    def from_value(value: str):
        return iHookStateKey(hex_to_str(value))

    def hex(self):
        return str_to_hex(self.key)
