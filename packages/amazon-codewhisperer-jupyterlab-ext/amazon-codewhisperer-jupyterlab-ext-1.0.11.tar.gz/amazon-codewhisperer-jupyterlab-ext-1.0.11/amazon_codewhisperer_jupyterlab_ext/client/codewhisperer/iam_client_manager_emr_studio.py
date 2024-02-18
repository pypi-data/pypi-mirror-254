from abc import ABC
import logging
from amazon_codewhisperer_jupyterlab_ext.client.codewhisperer.client_manager import CodeWhispererClientManager
from amazon_codewhisperer_jupyterlab_ext.constants import (
    REQUEST_OPTOUT_HEADER_NAME,
    RTS_PROD_ENDPOINT,
    RTS_PROD_REGION,
    SIGV4
)

logging.basicConfig(format="%(levelname)s: %(message)s")


class CodeWhispererIamEMRStudioClientManager(CodeWhispererClientManager, ABC):

    def __init__(self):
        super().__init__()
        self._editor_id = ""
        self._cookie = ""

    def _add_header(self, request, **kwargs):
        request.headers.add_header("editor-id", self._editor_id)
        request.headers.add_header("cookie", self._cookie)
        request.headers.add_header("x-target-aws-service", "codewhisperer")

    def get_client(self):
        # EMR Studio actually uses FAS credential stored in the proxy server at localhost:7777.
        # Since boto3.Session.client requires aws credential as mandatory parameter, dummy credential was used here.
        return self.session.create_client(
            aws_access_key_id="xxx",
            aws_secret_access_key="xxx",
            aws_session_token="xxx",
            service_name=SIGV4,
            endpoint_url="http://localhost:7777",
            region_name=RTS_PROD_REGION,
            verify=False,
        )

    async def invoke_recommendations(self, request, opt_out):
        async with self.get_client() as iam_client:
            iam_client.meta.events.register_first("before-sign.*.*", self._add_header)
            return iam_client.generate_recommendations(**request)

    def set_header_values(self, requestHeaders):
        # editor_id is used by proxy server to pick up the associated FAS token 
        self._editor_id = requestHeaders.get("Editorid")
        # Cookie is used by proxy server to validate the request and pick up additional session data in collaboration case
        self._cookie = requestHeaders.get("Cookie")
    
