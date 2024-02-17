from datetime import datetime
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from pydantic import BaseModel
from typing import Any, Literal

class Order(BaseModel):
    id: int
    order_id: str
    position_id: str | None
    market_type: str
    position_type: str
    order_type: str
    product_type: str
    quantities: int
    price: float
    status: Literal['pending', 'completed', 'rejected', 'failed']
    created_at: datetime
    updated_at: datetime
    broker_symbol: BrokerSymbol
    class Config:
        arbitrary_types_allowed: bool
    algorithm: Any
    @property
    def is_completed(self) -> bool: ...
    @property
    def is_pending(self) -> bool: ...
