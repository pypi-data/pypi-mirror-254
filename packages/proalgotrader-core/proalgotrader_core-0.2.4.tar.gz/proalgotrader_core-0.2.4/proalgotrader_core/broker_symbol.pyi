from _typeshed import Incomplete
from proalgotrader_core.algorithm import Algorithm as Algorithm
from proalgotrader_core.base_symbol import BaseSymbol as BaseSymbol
from proalgotrader_core.protocols.enums.segment_type import SegmentType as SegmentType
from proalgotrader_core.tick import Tick as Tick
from typing import Any, Dict

class BrokerSymbol:
    id: Incomplete
    market_type: Incomplete
    segment_type: Incomplete
    expiry_period: Incomplete
    expiry_date: Incomplete
    strike_price: Incomplete
    option_type: Incomplete
    symbol_name: Incomplete
    symbol_token: Incomplete
    exchange_token: Incomplete
    data_token: Incomplete
    base_symbol: Incomplete
    algorithm: Incomplete
    tick: Incomplete
    def __init__(self, broker_symbol_info: Dict[str, Any], algorithm: Algorithm) -> None: ...
    @property
    def can_trade(self) -> bool: ...
    def on_tick(self, tick: Tick) -> None: ...
