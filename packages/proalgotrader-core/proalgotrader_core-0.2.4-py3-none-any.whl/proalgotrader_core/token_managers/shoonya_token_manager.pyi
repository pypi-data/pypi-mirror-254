from _typeshed import Incomplete
from proalgotrader_core.helpers.get_totp import get_totp as get_totp
from proalgotrader_core.token_managers.base_token_manager import BaseTokenManager as BaseTokenManager

class ShoonyaTokenManager(BaseTokenManager):
    token: Incomplete
    user_id: Incomplete
    password: Incomplete
    totp_key: Incomplete
    vendor_code: Incomplete
    api_secret: Incomplete
    imei: Incomplete
    api: Incomplete
    def __init__(self, user_id: str, password: str, totp_key: str, vendor_code: str, api_secret: str, imei: str) -> None: ...
    def set_token(self, token: str) -> None: ...
    def get_token(self) -> str: ...
