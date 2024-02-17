from pydantic import BaseModel
from typing import Any, Dict

class Broker(BaseModel):
    id: int
    broker_uid: str
    broker_title: str
    broker_name: str
    broker_config: Dict[str, Any]
