from _typeshed import Incomplete
from proalgotrader_core.algo_session import AlgoSession as AlgoSession
from proalgotrader_core.algorithm import Algorithm as Algorithm
from proalgotrader_core.api import Api as Api
from proalgotrader_core.args_manager import ArgsManager as ArgsManager
from proalgotrader_core.broker_manager import BrokerManager as BrokerManager
from proalgotrader_core.chart_manager import ChartManager as ChartManager

class Application:
    algorithm: Incomplete
    chart_manager: Incomplete
    broker_manager: Incomplete
    algo_session: Incomplete
    api: Incomplete
    args_manager: Incomplete
    def __init__(self) -> None: ...
    async def start(self) -> None: ...
    async def boot(self) -> None: ...
    async def run(self) -> None: ...
