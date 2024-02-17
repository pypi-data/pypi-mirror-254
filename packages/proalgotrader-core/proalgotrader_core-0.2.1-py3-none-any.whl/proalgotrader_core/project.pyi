from proalgotrader_core.api import Api as Api
from proalgotrader_core.broker import Broker as Broker
from proalgotrader_core.data_broker import DataBroker as DataBroker
from proalgotrader_core.github_repository import GithubRepository as GithubRepository
from pydantic import BaseModel

class Project(BaseModel):
    id: int
    title: str
    description: str
    status: str
    broker: Broker
    data_broker: DataBroker
    github_repository: GithubRepository
    async def clone_repository(self, api: Api) -> None: ...
