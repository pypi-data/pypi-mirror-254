import abc
from _typeshed import Incomplete
from abc import ABC
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker
from proalgotrader_core.order import Order as Order

class PaperBroker(BaseBroker, ABC, metaclass=abc.ABCMeta):
    def __init__(self, api: Api, algo_session: AlgoSession) -> None: ...
    capital: Incomplete
    async def set_capital(self) -> None: ...
    async def place_order(self, *, broker_symbol: BrokerSymbol, quantities: int, market_type: str, product_type: str, order_type: str, position_type: str, position_id: str | None) -> None: ...
    def get_average_enter_price(self, order: Order) -> float: ...
