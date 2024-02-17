import abc
from abc import ABC
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker
from proalgotrader_core.brokers.live.live_broker import LiveBroker as LiveBroker
from proalgotrader_core.brokers.paper.paper_broker import PaperBroker as PaperBroker
from proalgotrader_core.brokers.providers.angel_one.angel_one_broker import AngelOneBroker as AngelOneBroker
from proalgotrader_core.brokers.providers.fyers.fyers_broker import FyersBroker as FyersBroker
from proalgotrader_core.brokers.providers.shoonya.shoonya_broker import ShoonyaBroker as ShoonyaBroker

class BrokerManager(BaseBroker, ABC, metaclass=abc.ABCMeta):
    def __new__(cls, api: Api, algo_session: AlgoSession) -> BrokerManager: ...
