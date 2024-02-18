"""
Name: Fireworks
URL: https://fireworks.ai
Features:
- Chat Completion
- Completion (todo)
"""
from openai import AsyncOpenAI, OpenAI

from .openai import OpenAIConnector


class FireworksConnector(OpenAIConnector):
    def __init__(
        self,
        client: "BaseClient",
        api_key: str,
        log_config: "LogConfig" = None,
        **kwargs
    ):
        super().__init__(client=client, api_key=None, log_config=log_config)
        self.api_key = api_key
        self.client = OpenAI(
            base_url="https://api.fireworks.ai/inference/v1",
            api_key=self.api_key,
            **kwargs
        )
        self.async_client = AsyncOpenAI(
            base_url="https://api.fireworks.ai/inference/v1",
            api_key=self.api_key,
            **kwargs
        )
