from abc import ABC

from ..chat.entities import ChatLogger, LogConfig, Prompt, Response
from .providers import Providers


class IConnector(ABC):
    _client: "Speck"
    _log_config: "LogConfig"

    def __init__(
        self, client: "Speck", provider: Providers, log_config: "LogConfig" = None
    ):
        self._client = client
        self.provider = provider
        self._log_config = log_config

    # @abstractmethod
    # def process_message(self, messages: Messages, model: str) -> str:
    #     pass

    def _get_log_kwargs(self, prompt: Prompt, response: Response, **kwargs):
        return {
            "provider": self.provider,
            "model": kwargs.get("model"),
            "temperature": kwargs.get("temperature"),
            "stream": kwargs.get("stream", False),
            "prompt": prompt,
            "config": kwargs,
            "response": response,
        }

    def log(
        self, *, log_config: LogConfig, prompt: Prompt, response: Response, custom_metadata: dict = None, **kwargs
    ):
        # Todo: refactor to use config.log_chat !!!
        ChatLogger.log(
            log_config=log_config,
            custom_metadata=custom_metadata,
            **self._get_log_kwargs(prompt, response, **kwargs),
        )

    def __str__(self):
        return f"Client({self.provider.value})"
