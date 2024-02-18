import time

from numerous.grpc.spm_pb2 import RefreshRequest, Token
from numerous.grpc.spm_pb2_grpc import TokenManagerStub


class RefreshingAccessToken:
    _refresh_threshold = 8 * 60

    def __init__(self, token_manager: TokenManagerStub, refresh_token: str):
        self._token_manager = token_manager
        self._refresh_token = refresh_token
        self._access_token: str = ""
        self._last_refresh_timestamp = float("-inf")

    @property
    def value(self) -> str:
        self._refresh_if_need()
        return self._access_token

    def _refresh_if_need(self):
        now = time.monotonic()
        if now - self._last_refresh_timestamp >= self._refresh_threshold:
            self._access_token = self._token_manager.GetAccessToken(
                RefreshRequest(refresh_token=Token(val=self._refresh_token))
            ).val
            self._last_refresh_timestamp = now

    def __eq__(self, other):
        if isinstance(other, RefreshingAccessToken):
            return other._access_token == self._access_token
        else:
            return False
