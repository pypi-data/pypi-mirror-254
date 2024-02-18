from typing import Tuple, Union

from .chat.client import IChatClient
from .chat.entities import (
    ChatConfig,
    ChatConfigTypes,
    LogConfig,
    Prompt,
    PromptTypes,
    Response,
    ResponseTypes,
    PromptContext,
)
from .connections._litellm import LiteLLMConnector
from .connections.anthropic import AnthropicConnector
from .connections.fireworks import FireworksConnector
from .connections.openai import OpenAIConnector
from .connections.openai_azure import AzureOpenAIConnector
from .connections.replicate import ReplicateConnector
from .logs.app import app


# Todo: Add BaseClient
# Todo: Add AsyncResource, SyncResource
class BaseClient:
    api_key: Union[str, None]
    api_keys: dict[str, str]
    endpoint: Union[str, None]
    azure_openai_config: dict[str, str]
    debug: bool = False
    ws_endpoint: str

    def __init__(self, debug: bool = False, ws_endpoint: str = None):
        self.debug = debug
        self.ws_endpoint = ws_endpoint or "wss://api.getspeck.ai/debug/ws"
        self.azure_openai_config = {}
        self.prompt = BasePrompt(self)

    def add_api_key(self, provider: str, api_key: str):
        self.api_keys[provider] = api_key

    def add_azure_openai_config(self, azure_endpoint: str, api_version: str):
        self.azure_openai_config = {
            "azure_endpoint": azure_endpoint,
            "api_version": api_version,
        }

    def to_dict(self):
        return {
            "api_key": self.api_key,
            "api_keys": self.api_keys,
            "endpoint": self.endpoint,
            "azure_openai_config": self.azure_openai_config,
            "debug": self.debug,
        }


class Resource:
    pass


class AsyncResource(Resource):
    pass


class SyncResource(Resource):
    pass


class Logger(SyncResource):  # App logger
    def __init__(self, client: BaseClient):
        self.client = client

    def log(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.log(*args, **kwargs)

    def info(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.debug(*args, **kwargs)

    def warning(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.critical(*args, **kwargs)

    def exception(self, *args, **kwargs):
        kwargs["endpoint"] = self.client.endpoint
        app.exception(*args, **kwargs)


def _create_connector(
    client: BaseClient, prompt: PromptTypes, config: ChatConfig = None, **config_kwargs
) -> IChatClient:
    if config is None:
        config = ChatConfig(**config_kwargs)
        # Todo: convert to default config based on class param
    elif len(config_kwargs) > 0:
        # Set config_kwargs as config attributes
        for key, value in config_kwargs.items():
            setattr(config, key, value)

    if config.provider is None:
        # Try to extract provider by getting string before : in model
        if ":" in config.model:
            provider_str, model_str = config.model.split(":", 1)
            config.provider = provider_str
            config.model = model_str
        else:
            raise ValueError("Provider must be specified in config or as a class param")

    provider = config.provider.lower()
    if client.api_keys.get(provider) is None and config.provider != "litellm":
        raise ValueError(f"An API key for {config.provider} is required")

    log_config = LogConfig(
        api_key=config_kwargs.get("_speck_access_token") or client.api_key,
        endpoint=client.endpoint or "https://api.getspeck.ai",
    )
    if "_speck_access_token" in config_kwargs:
        del config_kwargs["_speck_access_token"]

    if provider == "fireworks":
        connector = FireworksConnector(
            client=client,
            api_key=client.api_keys["fireworks"].strip(),
            log_config=log_config,
        )
        return connector
    if provider == "openai":
        connector = OpenAIConnector(
            client=client,
            api_key=client.api_keys["openai"].strip(),
            log_config=log_config,
        )
        return connector
    if provider == "azure-openai":
        connector = AzureOpenAIConnector(
            client=client,
            api_key=client.api_keys["azure-openai"].strip(),
            log_config=log_config,
            **client.azure_openai_config,
        )
        return connector
    if provider == "replicate":
        connector = ReplicateConnector(
            client=client,
            api_key=client.api_keys["replicate"].strip(),
            log_config=log_config,
        )
        return connector
    if provider == "anthropic":
        connector = AnthropicConnector(
            client=client,
            api_key=client.api_keys["anthropic"].strip(),
            log_config=log_config,
        )
        return connector
    if provider == "litellm":
        connector = LiteLLMConnector(
            client=client,
            api_key="",
            log_config=log_config,
        )
        return connector

    # raise ValueError("Provider not found")
    connector = LiteLLMConnector(
        client=client,
        api_key="",
        log_config=log_config,
    )
    return connector


class BasePrompt(SyncResource):
    client: BaseClient

    def __init__(self, client: BaseClient):
        self.client = client

    def _create_context(self, path: str):
        return PromptContext(api_key=self.client.api_key, endpoint=self.client.endpoint, path=path)

    # Deprecated
    # def read_prompt(self, path: str, id: Union[str, None] = None):
    #     with self._create_context() as context:
    #         prompt = Prompt.read(path, id, context=context)
    #     return prompt

    def read_prompts(self, path: str) -> dict[str, Prompt]:
        with self._create_context(path=path) as context:
            prompts = Prompt.read_all(path, context=context)
        return prompts

    def from_string(self, text: str, override: bool = False):
        with self._create_context(path=text.split("\n")[0]) as context:
            prompts = Prompt.reads_all(text, context=context)
        return prompts


class BaseChat(SyncResource):
    client: BaseClient

    def __init__(self, client: BaseClient):
        self.client = client

    def _create_connector(
        self, prompt: PromptTypes, config, **config_kwargs
    ) -> (Prompt, ChatConfig, IChatClient, Union[str, None]):
        _access_token = config_kwargs.get("_speck_access_token")
        if config_kwargs is not None and "_speck_access_token" in config_kwargs:
            del config_kwargs["_speck_access_token"]

        prompt = Prompt.create(prompt)
        config = ChatConfig.create(config, config_kwargs)
        connector = _create_connector(
            self.client, prompt, config, _speck_access_token=_access_token
        )

        if self.client.debug:
            # Create a socket connection to the server
            prompt, config = connector.debug_chat(prompt, config)

        return prompt, config, connector


class Chat(BaseChat):
    def __init__(self, client: BaseClient):
        super().__init__(client)

    def create(
        self, *, prompt: PromptTypes, config: ChatConfig = None, **config_kwargs
    ):
        prompt, config, connector = self._create_connector(
            prompt, config, **config_kwargs
        )
        return connector.chat(prompt=prompt, config=config)

    def log(
        self, messages: PromptTypes, config: ChatConfigTypes, response: ResponseTypes, custom_metadata: dict = None
    ):
        prompt = Prompt.create(messages)
        config = ChatConfig.create(config)
        response = Response.create(response)
        config.log_chat(log_config=LogConfig(api_key=self.client.api_key, endpoint=self.client.endpoint), prompt=prompt, response=response, custom_metadata=custom_metadata)


class AsyncChat(BaseChat):
    def __init__(self, client: BaseClient):
        super().__init__(client)

    async def create(
        self, *, prompt: PromptTypes, config: ChatConfig = None, **config_kwargs
    ):
        prompt, config, connector = self._create_connector(
            prompt, config, **config_kwargs
        )
        return await connector.achat(prompt, config)

    def log(
        self,
        log_config: LogConfig,
        messages: Prompt,
        config: ChatConfig,
        response: Response,
        custom_metadata: dict = None,
    ):
        config.log_chat(log_config=log_config, prompt=messages, response=response, custom_metadata=custom_metadata)


class Speck(BaseClient):
    def __init__(
        self,
        api_key: Union[str, None] = None,
        api_keys: dict[str, str] = {},
        endpoint: str = "https://api.getspeck.ai",
        debug: bool = False,
        **kwargs,
    ):
        super().__init__(debug=debug, **kwargs)
        self.api_key = api_key.strip() if api_key is not None else None
        self.api_keys = api_keys
        self.endpoint = endpoint

        self.chat = Chat(self)
        self.logger = Logger(self)


class AsyncSpeck(BaseClient):
    def __init__(
        self,
        api_key: Union[str, None] = None,
        api_keys: dict[str, str] = {},
        endpoint: Union[str, None] = "https://api.getspeck.ai",
        debug: bool = False,
        **kwargs,
    ):
        super().__init__(debug=debug, **kwargs)
        self.api_key = api_key.strip() if api_key is not None else None
        self.api_keys = api_keys
        self.endpoint = endpoint

        self.chat = AsyncChat(self)
        self.logger = Logger(self)


Client = Speck
AsyncClient = AsyncSpeck
