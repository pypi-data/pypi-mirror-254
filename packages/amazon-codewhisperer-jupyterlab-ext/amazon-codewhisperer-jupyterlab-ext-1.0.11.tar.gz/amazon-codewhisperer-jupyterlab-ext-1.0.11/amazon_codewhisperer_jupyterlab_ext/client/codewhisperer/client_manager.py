import logging
from abc import ABC, abstractmethod
from pathlib import Path
from aiobotocore.session import get_session
from botocore.exceptions import ClientError, ConnectTimeoutError
from amazon_codewhisperer_jupyterlab_ext.utils import generate_succeeded_service_response, \
    generate_client_error_codewhisperer_service_response, generate_connect_error_codewhisperer_service_response


# Interface for managing lifecycles of different sdk clients.
class CodeWhispererClientManager(ABC):
    _instance = None

    READ_TIMEOUT_IN_SEC = 15
    CONNECT_TIMEOUT_IN_SEC = 5

    def __init__(self):
        self.session = get_session()
        session_folder = f"{Path(__file__).parent.parent}/service_models"
        self.session.get_component('data_loader').search_paths.append(session_folder)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @abstractmethod
    def get_client(self):
        pass

    @abstractmethod
    async def invoke_recommendations(self, request, opt_out):
        pass

    async def generate_recommendations(self, recommendation_request, opt_out):
        try:
            recommendation_response = await self.invoke_recommendations(recommendation_request, opt_out)
            return generate_succeeded_service_response(recommendation_response)
        except ClientError as e:
            return generate_client_error_codewhisperer_service_response(e)
        except ConnectTimeoutError as e:
            logging.warning(f"Cannot access CodeWhisperer service: {e}")
            return generate_connect_error_codewhisperer_service_response(e)
