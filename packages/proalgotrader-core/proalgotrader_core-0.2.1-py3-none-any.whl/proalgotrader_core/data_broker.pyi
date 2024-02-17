from pydantic import BaseModel
from typing import Any, Dict

class DataBroker(BaseModel):
    id: int
    broker_uid: str
    broker_title: str
    broker_name: str
    broker_config: Dict[str, Any]
