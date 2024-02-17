from pydantic import BaseModel
from typing import Literal

class BaseSymbol(BaseModel):
    id: int
    exchange: str
    key: str
    type: str
    lot_size: int
    strike_size: int
    weekly_expiry_day: str | None
    monthly_expiry_day: str | None
    def get_expiry_day(self, expiry_period: Literal['weekly', 'monthly']) -> str: ...
