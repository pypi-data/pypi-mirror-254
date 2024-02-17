from proalgotrader_core.base_symbol import BaseSymbol as BaseSymbol
from proalgotrader_core.protocols.enums.segment_type import SegmentType as SegmentType
from proalgotrader_core.tick import Tick as Tick
from pydantic import BaseModel
from typing import Any

class BrokerSymbol(BaseModel):
    id: int
    market_type: str
    segment_type: str
    expiry_period: str | None
    expiry_date: str | None
    strike_price: int | None
    option_type: str | None
    symbol_name: str | None
    symbol_token: str | int | None
    exchange_token: str | int | None
    data_token: str | int | None
    base_symbol: BaseSymbol
    class Config:
        arbitrary_types_allowed: bool
    algorithm: Any
    tick: Tick
    @property
    def can_trade(self) -> bool: ...
    def initialize(self, algorithm: Any) -> None: ...
    def on_tick(self, tick: Tick) -> None: ...
