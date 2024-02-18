"""
Name: Anthropic
URL: https://anthropic.ai/
Features:
- Chat
"""
import json
from typing import Union

import httpx
import requests

from ..chat.entities import (
    NOT_GIVEN,
    ChatConfig,
    IChatClient,
    LogConfig,
    MessageChunk,
    Prompt,
    Response,
    Stream,
)
from .connector import IConnector
from .providers import Providers


def _process_chunk(obj) -> MessageChunk:
    return MessageChunk(content=obj["completion"])


class AnthropicStream:
    def __init__(self, iterator):
        self.iterator = iterator
        self.closed = False

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.closed:
                raise StopIteration

            obj = next(self.iterator)
            line = obj.decode("utf-8")
            if line.startswith("data: "):
                data = json.loads(line[6:])
                if data.get("stop_reason") is not None:
                    self.closed = True
                if data.get("completion") is not None:
                    return data
            else:
                continue


class AnthropicResponse(Response):
    def __init__(self, obj):
        content = obj["completion"]
        super().__init__(
            content=content,
            prompt_tokens=None,
            completion_tokens=None,
            raw=obj,
        )


class AnthropicConnector(IConnector, IChatClient):
    def __init__(
        self,
        api_key: str = None,
        client: "Speck" = None,
        log_config: "LogConfig" = None,
    ):
        super().__init__(
            client=client, provider=Providers.Anthropic, log_config=log_config
        )
        if api_key is not None:
            self.api_key = api_key
            self.url = "https://api.anthropic.com/v1/complete"

    def _convert_messages_to_prompt(self, prompt: Prompt) -> str:
        res = ""
        messages = prompt.compose()
        if messages[0]["role"] == "system":
            res = "System: " + messages[0]["content"] + "\n\n"
        for msg in messages:
            if msg["role"] == "system":
                continue
            res += (
                f"{'Human' if msg['role'] == 'user' else 'Assistant'}: "
                + msg["content"]
                + "\n\n"
            )
        res += "Assistant:"
        return res

    def _process_kwargs(self, prompt: Prompt, config: ChatConfig, **config_kwargs):
        if config is NOT_GIVEN:
            config = ChatConfig(**config_kwargs)
            # Todo: convert to default config based on class param

        # Remove all None values
        all_kwargs = {k: v for k, v in vars(config).items() if v is not None}

        input = self._convert_messages_to_prompt(prompt)

        headers = {
            "anthropic-version": config.get("anthropic_version", "2023-06-01"),
            "content-type": "application/json",
            "x-api-key": self.api_key,
        }

        data = {
            "model": config.model,
            "prompt": input,
            "max_tokens_to_sample": config.max_tokens or 100,
            "stream": config.stream,
            "temperature": config.temperature,
            **config.chat_args,
        }

        blocked_kwargs = ["provider", "_log", "chat_args", "stream", "max_tokens"]

        for k, v in all_kwargs.items():
            if k not in data and k not in blocked_kwargs:
                data[k] = v

        return headers, data, all_kwargs

    def chat(
        self, prompt: Prompt, config: ChatConfig = NOT_GIVEN, **config_kwargs
    ) -> Union[AnthropicResponse, Stream]:
        headers, data, all_kwargs = self._process_kwargs(
            prompt, config, **config_kwargs
        )

        response = requests.post(
            self.url, headers=headers, data=json.dumps(data), stream=config.stream
        )

        if config.stream:
            return Stream(
                client=self._client,
                iterator=AnthropicStream(response.iter_lines()),
                log_config=self._log_config,
                kwargs=self._get_log_kwargs(prompt, None, **all_kwargs),
                processor=_process_chunk,
            )
        else:
            output = response.json()
            if config._log:
                self.log(
                    log_config=self._log_config,
                    prompt=prompt,
                    response=AnthropicResponse(output),
                    **all_kwargs,
                )
                # Todo: set config= as param

            return AnthropicResponse(output)

    async def achat(
        self, prompt: Prompt, config: ChatConfig = NOT_GIVEN, **config_kwargs
    ) -> Union[AnthropicResponse, Stream]:
        headers, data, all_kwargs = self._process_kwargs(
            prompt, config, **config_kwargs
        )

        with httpx.AsyncClient() as client:
            response = await client.post(
                self.url, headers=headers, data=json.dumps(data), stream=config.stream
            )

            if config.stream:
                return Stream(
                    client=self._client,
                    iterator=AnthropicStream(response.iter_lines()),
                    log_config=self._log_config,
                    kwargs=self._get_log_kwargs(prompt, None, **all_kwargs),
                    processor=_process_chunk,
                )
            else:
                output = response.json()
                if config._log:
                    self.log(
                        log_config=self._log_config,
                        prompt=prompt,
                        response=AnthropicResponse(output),
                        **all_kwargs,
                    )
                    # Todo: set config= as param

                return AnthropicResponse(output)
