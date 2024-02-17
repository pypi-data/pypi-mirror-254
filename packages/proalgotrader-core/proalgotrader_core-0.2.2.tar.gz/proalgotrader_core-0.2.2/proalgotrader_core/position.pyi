from datetime import datetime
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.protocols.enums.position_type import PositionType as PositionType
from proalgotrader_core.protocols.enums.product_type import ProductType as ProductType
from proalgotrader_core.risk_reward import RiskReward as RiskReward
from pydantic import BaseModel
from typing import Any, List, Literal

class Position(BaseModel):
    id: int
    position_id: str
    market_type: str
    position_type: str
    order_type: str
    product_type: str
    quantities: int
    enter_price: float
    exit_price: float | None
    status: Literal['open', 'closed']
    tags: List[str] | None
    created_at: datetime
    updated_at: datetime
    broker_symbol: BrokerSymbol
    class Config:
        arbitrary_types_allowed: bool
    algorithm: Any
    position_manager: Any
    @property
    def is_buy(self) -> bool: ...
    @property
    def is_sell(self) -> bool: ...
    @property
    def pnl(self) -> float: ...
    @property
    def pnl_percent(self) -> float: ...
    @property
    def should_square_off(self) -> bool: ...
    async def initialize(self) -> None: ...
    async def on_after_market_closed(self) -> None: ...
    async def exit(self) -> None: ...
    async def get_risk_reward(self, *, broker_symbol: BrokerSymbol, direction: Literal['long', 'short'], sl: float, tgt: float | None = None, tsl: float | None = None) -> RiskReward: ...
    async def next(self) -> None: ...
