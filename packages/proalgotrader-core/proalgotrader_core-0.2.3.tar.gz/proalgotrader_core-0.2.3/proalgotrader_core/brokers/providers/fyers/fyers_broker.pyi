import abc
from _typeshed import Incomplete
from abc import ABC
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker
from proalgotrader_core.order import Order as Order
from proalgotrader_core.position import Position as Position
from proalgotrader_core.protocols.enums.order_type import OrderType as OrderType
from proalgotrader_core.protocols.enums.position_type import PositionType as PositionType
from proalgotrader_core.protocols.enums.product_type import ProductType as ProductType
from proalgotrader_core.token_managers.fyers_token_manager import FyersTokenManager as FyersTokenManager
from typing import Any, Dict

class FyersBroker(BaseBroker, ABC, metaclass=abc.ABCMeta):
    token_manager: Incomplete
    def __init__(self, api: Api, algo_session: AlgoSession) -> None: ...
    async def get_order_types(self) -> Dict[str, Any]: ...
    async def get_position_types(self) -> Dict[str, Any]: ...
    async def get_product_types(self) -> Dict[str, Any]: ...
    capital: Incomplete
    async def set_capital(self) -> None: ...
    async def place_order(self, *, broker_symbol: BrokerSymbol, quantities: int, market_type: str, product_type: str, order_type: str, position_type: str, position_id: str | None) -> Position: ...
    def get_average_enter_price(self, order: Order) -> float: ...
