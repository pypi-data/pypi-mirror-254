import pandas as pd
from _typeshed import Incomplete
from datetime import date, datetime, time, timedelta
from proalgotrader_core.helpers.get_data_path import get_data_path as get_data_path
from proalgotrader_core.helpers.get_trading_days import get_trading_days as get_trading_days
from proalgotrader_core.project import Project as Project
from typing import Any, Dict, Literal, Tuple

class AlgoSession:
    id: Incomplete
    key: Incomplete
    secret: Incomplete
    mode: Incomplete
    tz: Incomplete
    project: Incomplete
    capital: int
    tz_info: Incomplete
    market_start_time: Incomplete
    market_end_time: Incomplete
    market_start_datetime: Incomplete
    market_end_datetime: Incomplete
    resample_days: Incomplete
    warmup_days: Incomplete
    data_path: Incomplete
    trading_days: Incomplete
    def __init__(self, algo_session_info: Dict[str, Any]) -> None: ...
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
