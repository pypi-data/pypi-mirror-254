import abc
from _typeshed import Incomplete
from abc import ABC
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker_symbol import BrokerSymbol as BrokerSymbol
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker
from proalgotrader_core.protocols.enums.market_type import MarketType as MarketType
from proalgotrader_core.protocols.enums.order_type import OrderType as OrderType
from proalgotrader_core.protocols.enums.position_type import PositionType as PositionType
from proalgotrader_core.protocols.enums.product_type import ProductType as ProductType
from proalgotrader_core.token_managers.angel_one_token_manager import AngelOneTokenManager as AngelOneTokenManager

class AngelOneBroker(BaseBroker, ABC, metaclass=abc.ABCMeta):
    token_manager: Incomplete
    def __init__(self, api: Api, algo_session: AlgoSession) -> None: ...
    capital: Incomplete
    async def set_capital(self) -> None: ...
    async def place_order(self, *, broker_symbol: BrokerSymbol, quantities: int, market_type: MarketType, product_type: ProductType, order_type: OrderType, position_type: PositionType, position_id: str | None): ...
