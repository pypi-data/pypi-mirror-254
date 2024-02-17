from _typeshed import Incomplete
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.position import Position as Position
from typing import Literal

class RiskReward:
    position: Incomplete
    broker_symbol: Incomplete
    symbol_name: Incomplete
    symbol_price: Incomplete
    direction: Incomplete
    sl: Incomplete
    tgt: Incomplete
    tsl: Incomplete
    stoploss: Incomplete
    target: Incomplete
    trailed_stoplosses: Incomplete
    def __init__(self, *, position: Position, broker_symbol: BrokerSymbol, symbol_name: str, symbol_price: float, direction: Literal['long', 'short'], sl: float, tgt: float | None = None, tsl: float | None = None) -> None: ...
    @property
    def ltp(self) -> float: ...
    @property
    def trailed_stoploss(self) -> float: ...
    async def next(self) -> None: ...
