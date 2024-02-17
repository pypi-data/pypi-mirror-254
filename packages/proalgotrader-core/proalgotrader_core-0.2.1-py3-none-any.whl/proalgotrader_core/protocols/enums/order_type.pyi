from enum import Enum

class OrderType(Enum):
    LIMIT_ORDER: str
    MARKET_ORDER: str
    STOP_ORDER: str
    STOP_LIMIT_ORDER: str
