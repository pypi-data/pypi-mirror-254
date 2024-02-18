"""
Name: OpenAI Azure
URL:
Features:
"""
from openai import AsyncAzureOpenAI, AzureOpenAI

from .openai import OpenAIConnector


class AzureOpenAIConnector(OpenAIConnector):
    def __init__(
        self,
        client: "BaseClient",
        api_key: str,
        azure_endpoint: str,
        api_version: str,
        log_config: "LogConfig" = None,
        **kwargs
    ):
        super().__init__(client=client, api_key=None, log_config=log_config)
        self.client = AzureOpenAI(
            api_key=api_key,
            azure_endpoint=azure_endpoint,
            api_version=api_version,
            **kwargs
        )
        self.async_client = AsyncAzureOpenAI(
            api_key=api_key,
            azure_endpoint=azure_endpoint,
            api_version=api_version,
            **kwargs
        )
        self.api_key = api_key
        self.azure_endpoint = azure_endpoint
        self.api_version = api_version
