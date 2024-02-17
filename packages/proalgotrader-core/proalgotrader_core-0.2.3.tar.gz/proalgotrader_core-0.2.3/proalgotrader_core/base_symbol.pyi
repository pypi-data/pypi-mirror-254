from _typeshed import Incomplete
from typing import Any, Dict, Literal

class BaseSymbol:
    id: Incomplete
    exchange: Incomplete
    key: Incomplete
    type: Incomplete
    lot_size: Incomplete
    strike_size: Incomplete
    weekly_expiry_day: Incomplete
    monthly_expiry_day: Incomplete
    def __init__(self, base_symbol_info: Dict[str, Any]) -> None: ...
    def get_expiry_day(self, expiry_period: Literal['weekly', 'monthly']) -> str: ...
