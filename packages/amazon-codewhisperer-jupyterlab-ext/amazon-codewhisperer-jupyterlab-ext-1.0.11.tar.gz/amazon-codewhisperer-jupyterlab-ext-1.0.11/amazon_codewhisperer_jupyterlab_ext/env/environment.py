import json
import os

import aiohttp
from aiohttp import ClientTimeout
from packaging.version import Version
from amazon_codewhisperer_jupyterlab_ext.constants import CURRENT_VERSION, CODEWHISPERER_PYPI_JSON_URL, \
    NEW_VERSION_USER_MESSAGE, CONSUMER_ENV_KEY, CONSUMER_ENV_VALUE_GLUE_STUDIO, CONSUMER_ENV_VALUE_EMR_STUDIO


class Environment:
    SM_STUDIO = "SageMaker Studio"
    JUPYTER_OSS = "Jupyter OSS"
    GLUE_STUDIO_NOTEBOOK = "Glue Studio Notebook"
    EMR_STUDIO_WORKSPACE = "EMR Studio Workspace"

    @staticmethod
    async def get_update_notification():
        try:
            # Glue Studio environment doesn't want any update and update notification
            if Environment.is_glue_studio():
                return "", ""

            # EMR Studio environment doesn't want any update and update notification
            if Environment.is_emr_studio():
                return "", ""

            # Get the URL from environment variable or fall back to default
            url = os.environ.get("JSON_URL", CODEWHISPERER_PYPI_JSON_URL)

            # Download the JSON data
            async with aiohttp.ClientSession() as session:
                # Define the timeout duration (in seconds)
                timeout_duration = 2  # Timeout after 2 seconds

                # Create a ClientTimeout object
                timeout = ClientTimeout(total=timeout_duration)

                async with session.get(url, timeout=timeout) as response:
                    response.raise_for_status()
                    data = await response.json()

            # Get the latest version and launch date #TODO: Write a test case for this functionality- Get the latest version
            keys = data["releases"].keys()
            filtered_versions = [version for version in keys if version.startswith('1.')]
            version_to_tuple = lambda version_str: tuple(map(int, version_str.split('.')))
            latest_version  = '.'.join(map(str, max((version_to_tuple(version) for version in filtered_versions)))) 

            # Compare the current version with the latest version
            if Version(latest_version) > Version(CURRENT_VERSION):
                return NEW_VERSION_USER_MESSAGE.format(latest_version), latest_version
            else:
                return "", ""
        except Exception as e:
            print(f"Error: {e}")
            return "", ""
    
    @staticmethod
    def get_environment():
        env = Environment.JUPYTER_OSS
        try:
            if Environment.is_glue_studio():
                return Environment.GLUE_STUDIO_NOTEBOOK
            
            if Environment.is_emr_studio():
                return Environment.EMR_STUDIO_WORKSPACE

            with open('/opt/ml/metadata/resource-metadata.json', 'r') as f:
                data = json.load(f)
                if 'ResourceArn' in data:
                    env = Environment.SM_STUDIO
        except Exception as e:
            # Default to Builder ID / Jupyter OSS for all errors
            pass
        return env

    @staticmethod
    def is_glue_studio():
        return CONSUMER_ENV_KEY in os.environ and os.environ.get(CONSUMER_ENV_KEY) == CONSUMER_ENV_VALUE_GLUE_STUDIO

    @staticmethod
    def is_emr_studio():
        return CONSUMER_ENV_KEY in os.environ and os.environ.get(CONSUMER_ENV_KEY) == CONSUMER_ENV_VALUE_EMR_STUDIO

    @staticmethod
    def is_sm_studio():
        return Environment.get_environment() == Environment.SM_STUDIO
   