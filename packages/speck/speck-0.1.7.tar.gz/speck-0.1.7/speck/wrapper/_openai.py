from __future__ import annotations

import logging
import os
from typing import Any, Callable, Iterator

from openai import OpenAI as _OpenAI
from openai import AsyncOpenAI as _AsyncOpenAI
from openai import AzureOpenAI as _AzureOpenAI
from openai import AsyncAzureOpenAI as _AsyncAzureOpenAI
from openai import Stream as _Stream
from litellm import completion

from .. import ChatLogger, OpenAIResponse, ProvidersList, Speck
from .._client import BasePrompt
from ..chat.entities import (
    ChatConfig,
    LogConfig,
    OpenAIChatConfig,
    Prompt,
    Response,
    Stream,
)
from ..util._wrapper import wrap_method

logger = logging.getLogger(__name__)


def wrapper(original_method, *args, **kwargs):
    """
    Example of a wrapper function that can be used with add_method_wrapper.

    Args:
        original_method: The original method to be wrapped.
        *args, **kwargs: Arguments and keyword arguments for the original method.

    Returns:
        The result of the original method call.
    """
    logger.info(f"Before calling {original_method.__name__}")
    result = original_method(*args, **kwargs)
    logger.info(f"After calling {original_method.__name__}")
    return result


class OpenAIStream:
    # processor that has lambda which returns MessageDelta
    def __init__(
        self,
        config: OpenAIChatConfig,
        prompt: Prompt,
        iterator: Iterator[Any],
        kwargs: dict,
        processor: Callable[[Any], Any],
        speck_api_key: str,
        provider: str = "openai",
        prompt_ref: dict = None,
        custom_metadata: dict = None,
        _speck_client: Speck = None,
    ):
        self.config: OpenAIChatConfig = config
        self.prompt = prompt
        self.message: str = ""
        self._iterator = iterator
        self._kwargs = kwargs
        self._processor = processor
        self._has_logged = False
        self._closed = False
        self._last_item = None
        self.speck_api_key = speck_api_key
        self.provider = provider
        self.prompt_ref = prompt_ref
        self._speck_client = _speck_client
        self.custom_metadata = custom_metadata

    def _log(self):
        if not self._has_logged:
            self._has_logged = True

            kwargs = self._kwargs
            kwargs["prompt"] = self._kwargs.get("prompt", [])
            kwargs["model"] = self._kwargs.get("model", "N/A")
            # kwargs["response"] = Response(content=self.message, raw={}, closed=True)
            # ChatLogger.log(**kwargs)

            self.config.log_chat(
                log_config=LogConfig(api_key=self.speck_api_key, endpoint=self._speck_client.endpoint),
                prompt=self.prompt,
                response=Response(content=self.message, raw={}, closed=True),
                provider=self.provider,
                prompt_ref=self.prompt_ref,
                custom_metadata=self.custom_metadata,
            )

    def _process(self, item) -> Any:
        return self._processor(item)

    def __next__(self) -> Any:
        try:
            if self._closed:
                raise StopIteration

            item: Any = self._process(next(self._iterator))
            self._last_item = item
            if item.choices[0].delta.content:
                self.message += item.choices[0].delta.content
            return item
        except StopIteration:
            self._log()
            raise

    def __iter__(self) -> Iterator[Any]:
        return self

    def close(self):
        try:
            self._closed = True
            # todo: make this work for packages other than openai
            self._iterator.response.close()
        except AttributeError:
            pass

    async def __anext__(self) -> Any:
        try:
            if self._closed:
                raise StopAsyncIteration

            item: Any = self._process(await self._iterator.__anext__())
            self._last_item = item
            if item.choices[0].delta.content:
                self.message += item.choices[0].delta.content
            return item
        except StopAsyncIteration:
            self._log()
            raise

    def __aiter__(self) -> Iterator[Any]:
        return self


def preprocess_chat(**kwargs):
    model: str = kwargs.get("model", None)
    stream = kwargs.get("stream", False)
    messages = kwargs.get("messages", None)
    if isinstance(messages, Prompt):
        prompt = messages
        kwargs["messages"] = prompt.compose()
    else:
        prompt = Prompt.from_openai(messages)

    custom_metadata = kwargs.get("metadata", None)
    if "metadata" in kwargs:
        del kwargs["metadata"]

    config = OpenAIChatConfig(**kwargs)
    config = config.convert()

    return prompt, config, stream, model, custom_metadata, kwargs

def chat_wrapper(self: OpenAIWrapper, original_method, *args, **kwargs):
    prompt, config, stream, model, custom_metadata, kwargs = preprocess_chat(**kwargs)
    # if model is not None and ":" in model:
    #     provider, model = model.split(":", 1)
    #     if provider in ProvidersList:
    #         config.provider = provider
    #         config.model = model
    #         # Todo: return in OpenAI format
    #         return self._speck_client.chat.create(prompt=prompt, config=config)
    logger.info(f"Call {original_method.__name__} with model {model}")
    provider = "fireworks" if self.base_url is not None and "fireworks" in str(self.base_url.raw.raw_host) else "openai"
    config.provider = provider

    if stream:
        stream = original_method(*args, **kwargs)
        # Todo: wrap the Stream class
        # Best current way to do this is to convert our Stream class to an OpenAI Stream class
        return OpenAIStream(
            config=config,
            prompt=prompt,
            iterator=stream,
            kwargs={
                "provider": provider,
            },
            processor=lambda a: a,
            speck_api_key=self._speck_api_key,
            provider=provider,
            prompt_ref=prompt.get_ref(),
            custom_metadata=custom_metadata,
            _speck_client=self._speck_client,
        )
    else:
        result = original_method(*args, **kwargs)
        config.log_chat(
            log_config=LogConfig(api_key=self._speck_api_key),
            prompt=prompt,
            response=OpenAIResponse(result),
            provider=provider,
            prompt_ref=prompt.get_ref(),
            custom_metadata=custom_metadata,
        )

        return result


async def async_chat_wrapper(self: AsyncOpenAIWrapper, original_method, *args, **kwargs):
    prompt, config, stream, model, custom_metadata, kwargs = preprocess_chat(**kwargs)
    # if model is not None and ":" in model:
    #     provider, model = model.split(":", 1)
    #     if provider in ProvidersList:
    #         config.provider = provider
    #         config.model = model
    #         # Todo: return in OpenAI format
    #         return self._speck_client.chat.create(prompt=prompt, config=config)
    logger.info(f"Call {original_method.__name__} with model {model}")
    provider = "fireworks" if self.base_url is not None and "fireworks" in str(self.base_url.raw.raw_host) else "openai"
    config.provider = provider

    if stream:
        stream = await original_method(*args, **kwargs)
        # Todo: wrap the Stream class
        # Best current way to do this is to convert our Stream class to an OpenAI Stream class
        return OpenAIStream(
            config=config,
            prompt=prompt,
            iterator=stream,
            kwargs={
                "provider": provider,
            },
            processor=lambda a: a,
            speck_api_key=self._speck_api_key,
            provider=provider,
            prompt_ref=prompt.get_ref(),
            custom_metadata=custom_metadata,
            _speck_client=self._speck_client,
        )
    else:
        result = await original_method(*args, **kwargs)
        config.log_chat(
            log_config=LogConfig(api_key=self._speck_api_key),
            prompt=prompt,
            response=OpenAIResponse(result),
            provider=provider,
            prompt_ref=prompt.get_ref(),
            custom_metadata=custom_metadata,
        )

        return result


def stream_next_wrapper(original_method, *args, **kwargs):
    logger.info(f"Before calling {original_method.__name__}")
    result = original_method(*args, **kwargs)
    logger.info(f"After calling {original_method.__name__}")
    return result


def stream_iter_wrapper(original_method, *args, **kwargs):
    logger.info(f"Before calling {original_method.__name__}")
    result = original_method(*args, **kwargs)
    logger.info(f"After calling {original_method.__name__}")
    return result


class OpenAIWrapper(_OpenAI):
    _speck_api_key: str = None
    _speck_client: Speck = None
    prompt: BasePrompt

    def __init__(self, *args, **kwargs):
        if "speck_api_key" in kwargs:
            del kwargs["speck_api_key"]
        super().__init__(*args, **kwargs)

    def initialize_speck(
        self,
        api_key: str = None,
        speck_api_key: str = None,
        api_keys: dict[str, str] = {},
        debug: bool = False,
    ):
        """
        Deprecated. Replaced with:
        openai = OpenAI(..., speck_api_key=...)
        """
        self._speck_api_key = api_key or speck_api_key
        if "openai" not in api_keys:
            api_keys["openai"] = self.api_key
        if api_keys["openai"] is None:
            api_keys["openai"] = os.environ.get("OPENAI_API_KEY")

        self._speck_client = Speck(
            api_key=self._speck_api_key, api_keys=api_keys, debug=debug
        )

    def add_api_key(self, provider: str, api_key: str):
        self._speck_client.add_api_key(provider, api_key)

    def add_api_keys(self, api_keys: dict[str, str]):
        for provider, api_key in api_keys.items():
            self.add_api_key(provider, api_key)


class AzureOpenAIWrapper(_AzureOpenAI):
    _speck_api_key: str = None
    _speck_client: Speck = None
    prompt: BasePrompt

    def __init__(self, *args, **kwargs):
        if "speck_api_key" in kwargs:
            del kwargs["speck_api_key"]
        super().__init__(*args, **kwargs)

    def add_api_key(self, provider: str, api_key: str):
        self._speck_client.add_api_key(provider, api_key)

    def add_api_keys(self, api_keys: dict[str, str]):
        for provider, api_key in api_keys.items():
            self.add_api_key(provider, api_key)


class AsyncOpenAIWrapper(_AsyncOpenAI):
    _speck_api_key: str = None
    _speck_client: Speck = None
    prompt: BasePrompt

    def __init__(self, *args, **kwargs):
        if "speck_api_key" in kwargs:
            del kwargs["speck_api_key"]
        super().__init__(*args, **kwargs)

    def add_api_key(self, provider: str, api_key: str):
        self._speck_client.add_api_key(provider, api_key)

    def add_api_keys(self, api_keys: dict[str, str]):
        for provider, api_key in api_keys.items():
            self.add_api_key(provider, api_key)


class AsyncAzureOpenAIWrapper(_AsyncAzureOpenAI):
    _speck_api_key: str = None
    _speck_client: Speck = None
    prompt: BasePrompt

    def __init__(self, *args, **kwargs):
        if "speck_api_key" in kwargs:
            del kwargs["speck_api_key"]
        super().__init__(*args, **kwargs)

    def add_api_key(self, provider: str, api_key: str):
        self._speck_client.add_api_key(provider, api_key)

    def add_api_keys(self, api_keys: dict[str, str]):
        for provider, api_key in api_keys.items():
            self.add_api_key(provider, api_key)


def _wrapper_init(original_method, *args, **kwargs):
    logger.info(f"Initializing {original_method.__name__}")
    result = original_method(*args, **kwargs)
    logger.info(f"Adding method wrappers {original_method.__name__}")
    self = args[0]
    self._speck_api_key = kwargs.get("speck_api_key", None) or os.environ.get("SPECK_API_KEY", None)
    if "speck_api_key" in kwargs:
        del kwargs["speck_api_key"]

    self._speck_client = Speck(api_key=self._speck_api_key)
    self.prompt = BasePrompt(self._speck_client)

    def chat_wrapper_caller(*args, **kwargs):
        return chat_wrapper(self,*args, **kwargs)

    async def async_chat_wrapper_caller(*args, **kwargs):
        return await async_chat_wrapper(self, *args, **kwargs)

    is_sync = isinstance(self, OpenAIWrapper) or isinstance(self, AzureOpenAIWrapper)
    wrap_method(
        self.chat.completions,
        "create",
        chat_wrapper_caller if is_sync else async_chat_wrapper_caller,
    )
    logger.info(f"After calling {original_method.__name__}")
    return result


wrap_method(OpenAIWrapper, "__init__", _wrapper_init)
wrap_method(AsyncOpenAIWrapper, "__init__", _wrapper_init)
wrap_method(AzureOpenAIWrapper, "__init__", _wrapper_init)
wrap_method(AsyncAzureOpenAIWrapper, "__init__", _wrapper_init)

# add_method_kwarg(OpenAIWrapper, "__init__", "speck_log", 69)
