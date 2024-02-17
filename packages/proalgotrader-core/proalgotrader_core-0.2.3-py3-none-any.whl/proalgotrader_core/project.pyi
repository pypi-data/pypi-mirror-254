from _typeshed import Incomplete
from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker import Broker as Broker
from proalgotrader_core.data_broker import DataBroker as DataBroker
from proalgotrader_core.github_repository import GithubRepository as GithubRepository
from typing import Any, Dict

class Project:
    id: Incomplete
    title: Incomplete
    description: Incomplete
    status: Incomplete
    broker: Incomplete
    data_broker: Incomplete
    github_repository: Incomplete
    def __init__(self, project_info: Dict[str, Any]) -> None: ...
    async def clone_repository(self, api: Api) -> None: ...
