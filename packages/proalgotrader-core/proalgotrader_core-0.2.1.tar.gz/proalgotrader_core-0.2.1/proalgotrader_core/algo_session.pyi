import pandas as pd
import pytz
from datetime import date, datetime, time, timedelta
from pathlib import Path
from proalgotrader_core.helpers.get_data_path import get_data_path as get_data_path
from proalgotrader_core.helpers.get_trading_days import get_trading_days as get_trading_days
from proalgotrader_core.project import Project as Project
from pydantic import BaseModel
from typing import Any, Dict, Literal, Tuple

class AlgoSession(BaseModel):
    id: int
    key: str
    secret: str
    mode: Literal['Paper', 'Live']
    tz: str
    project: Project
    class Config:
        arbitrary_types_allowed: bool
    tz_info: pytz.timezone
    capital: float
    market_start_time: time
    market_end_time: time
    market_start_datetime: datetime
    market_end_datetime: datetime
    resample_days: Dict[str, str]
    warmup_days: Dict[timedelta, int]
    data_path: Path
    trading_days: pd.DataFrame
    def model_post_init(self, __context: Any) -> None: ...
    @property
    def current_datetime(self) -> datetime: ...
    @property
    def current_timestamp(self) -> int: ...
    @property
    def current_date(self) -> date: ...
    @property
    def current_time(self) -> time: ...
    def get_market_status(self) -> str: ...
    async def validate_market_status(self) -> None: ...
    def get_expires(self, expiry_period: Literal['weekly', 'monthly'], expiry_day: str) -> pd.DataFrame: ...
    def get_warmups_days(self, timeframe: timedelta) -> int: ...
    def fetch_ranges(self, timeframe: timedelta) -> Tuple[int, int]: ...
    def get_current_candle(self, timeframe: timedelta) -> datetime: ...
