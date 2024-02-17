import abc
from abc import ABC
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.api import Api as Api
from proalgotrader_core.brokers.base_broker import BaseBroker as BaseBroker

class LiveBroker(BaseBroker, ABC, metaclass=abc.ABCMeta):
    def __init__(self, api: Api, algo_session: AlgoSession) -> None: ...
