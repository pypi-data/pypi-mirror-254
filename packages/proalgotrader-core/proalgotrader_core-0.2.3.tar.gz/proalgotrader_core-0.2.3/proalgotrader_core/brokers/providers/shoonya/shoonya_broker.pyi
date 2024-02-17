import abc
from _typeshed import Incomplete
from abc import ABC
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker
from proalgotrader_core.token_managers.shoonya_token_manager import ShoonyaTokenManager as ShoonyaTokenManager

class ShoonyaBroker(BaseBroker, ABC, metaclass=abc.ABCMeta):
    token_manager: Incomplete
    def __init__(self, api: Api, algo_session: AlgoSession) -> None: ...
    capital: Incomplete
    async def set_capital(self) -> None: ...
    async def place_order(self, *, broker_symbol: BrokerSymbol, quantities: int, market_type: str, product_type: str, order_type: str, position_type: str, position_id: str | None): ...
