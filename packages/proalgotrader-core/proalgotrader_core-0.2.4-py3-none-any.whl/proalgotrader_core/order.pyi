from _typeshed import Incomplete
from proalgotrader_core.algorithm import Algorithm as Algorithm
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from typing import Any, Dict

class Order:
    id: Incomplete
    order_id: Incomplete
    position_id: Incomplete
    market_type: Incomplete
    position_type: Incomplete
    order_type: Incomplete
    product_type: Incomplete
    quantities: Incomplete
    price: Incomplete
    status: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    algorithm: Incomplete
    broker_symbol: Incomplete
    def __init__(self, order_info: Dict[str, Any], broker_symbol: BrokerSymbol, algorithm: Algorithm) -> None: ...
    async def initialize(self) -> None: ...
    @property
    def is_completed(self) -> bool: ...
    @property
    def is_pending(self) -> bool: ...
