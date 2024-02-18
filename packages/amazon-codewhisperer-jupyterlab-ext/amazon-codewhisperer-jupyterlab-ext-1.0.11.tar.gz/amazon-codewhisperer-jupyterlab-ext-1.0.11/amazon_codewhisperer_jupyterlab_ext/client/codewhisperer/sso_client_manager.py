from abc import ABC
from botocore import UNSIGNED
from botocore import client
from amazon_codewhisperer_jupyterlab_ext.client.codewhisperer.client_manager import CodeWhispererClientManager
from amazon_codewhisperer_jupyterlab_ext.constants import (
    REQUEST_OPTOUT_HEADER_NAME,
    RTS_PROD_ENDPOINT,
    RTS_PROD_REGION,
    BEARER
)


class CodeWhispererSsoClientManager(CodeWhispererClientManager, ABC):
    _initialized = False

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._bearer_token = ""
        self._opt_out = False
        self.cfg = client.Config(
            connect_timeout=self.CONNECT_TIMEOUT_IN_SEC,
            read_timeout=self.READ_TIMEOUT_IN_SEC,
            retries={"total_max_attempts": 2},
            tcp_keepalive=True,
            signature_version=UNSIGNED
        )
        super().__init__()

    def _add_header(self, request, **kwargs):
        request.headers.add_header("Authorization", "Bearer " + self._bearer_token)
        request.headers.add_header(REQUEST_OPTOUT_HEADER_NAME, f"{self._opt_out}")

    def get_client(self):
        return self.session.create_client(
            service_name=BEARER,
            endpoint_url=RTS_PROD_ENDPOINT,
            region_name=RTS_PROD_REGION,
            verify=False,
            config=self.cfg
        )

    async def invoke_recommendations(self, request, opt_out):
        self._opt_out = opt_out
        async with self.get_client() as sso_client:
            sso_client.meta.events.register_first("before-sign.*.*", self._add_header)
            return await sso_client.generate_completions(**request)

    def set_bearer_token(self, token):
        self._bearer_token = token
