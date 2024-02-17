from _typeshed import Incomplete
from proalgotrader_core.algorithm import Algorithm as Algorithm
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.protocols.enums.position_type import PositionType as PositionType
from proalgotrader_core.protocols.enums.product_type import ProductType as ProductType
from proalgotrader_core.risk_reward import RiskReward as RiskReward
from typing import Any, Dict, Literal

class Position:
    id: Incomplete
    position_id: Incomplete
    market_type: Incomplete
    position_type: Incomplete
    order_type: Incomplete
    product_type: Incomplete
    quantities: Incomplete
    enter_price: Incomplete
    exit_price: Incomplete
    status: Incomplete
    tags: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    algorithm: Incomplete
    broker_symbol: Incomplete
    position_manager: Incomplete
    def __init__(self, position_info: Dict[str, Any], broker_symbol: BrokerSymbol, algorithm: Algorithm) -> None: ...
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
