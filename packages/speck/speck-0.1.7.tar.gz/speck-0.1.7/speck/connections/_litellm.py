from typing import Union

from litellm import acompletion, completion

from ..chat.entities import NOT_GIVEN, ChatConfig, Prompt, Stream
from ..util._filter import no_filter_kwargs

"""
Name: OpenAI Azure
URL:
Features:
"""
from openai import AsyncAzureOpenAI, AzureOpenAI

from .openai import OpenAIConnector, OpenAIResponse, _process_chunk


class LiteLLMClient:
    def __init__(self, method):
        self.method = method
        self.chat = self.Chat(self)

    class Chat:
        def __init__(self, client):
            self.client = client
            self.completions = self.Completions(self.client)

        class Completions:
            def __init__(self, client):
                self.client = client

            def create(self, *args, **kwargs):
                return self.client.method(*args, **kwargs)


class LiteLLMConnector(OpenAIConnector):
    def __init__(
        self,
        client: "BaseClient",
        api_key: str,
        log_config: "LogConfig" = None,
        **kwargs
    ):
        super().__init__(client=client, api_key=None, log_config=log_config)
        self.client = LiteLLMClient(method=completion, **kwargs)
        self.async_client = LiteLLMClient(method=acompletion, **kwargs)
        # self.api_key = api_key

    def chat(
        self, prompt: Prompt, config: ChatConfig = NOT_GIVEN, **config_kwargs
    ) -> Union[OpenAIResponse, Stream]:
        input, all_kwargs = self._process_kwargs(prompt, config, **config_kwargs)

        if config.stream:
            output_stream = self.client.chat.completions.create(
                messages=input,
                **no_filter_kwargs(completion, all_kwargs, self.EXCLUDED_PARAMS),
            )

            return Stream(
                client=self._client,
                iterator=output_stream,
                log_config=self._log_config,
                kwargs=self._get_log_kwargs(prompt, None, **all_kwargs),
                processor=_process_chunk,
            )
        else:
            output = self.client.chat.completions.create(
                messages=input,
                **no_filter_kwargs(completion, all_kwargs, self.EXCLUDED_PARAMS),
            )

            if config._log:
                self.log(
                    log_config=self._log_config,
                    prompt=prompt,
                    response=OpenAIResponse(output),
                    **all_kwargs,
                )
                # Todo: set config= as param

        return OpenAIResponse(output)

    async def achat(
        self, prompt: Prompt, config: ChatConfig = NOT_GIVEN, **config_kwargs
    ) -> Union[OpenAIResponse, Stream]:
        input, all_kwargs = self._process_kwargs(prompt, config, **config_kwargs)

        if config.stream:
            output_stream = await self.async_client.chat.completions.create(
                messages=input,
                **no_filter_kwargs(acompletion, all_kwargs, self.EXCLUDED_PARAMS),
            )

            # Todo: async iterator support
            return Stream(
                client=self._client,
                iterator=output_stream,
                log_config=self._log_config,
                kwargs=self._get_log_kwargs(prompt, None, **all_kwargs),
                processor=_process_chunk,
            )
        else:
            output = await self.async_client.chat.completions.create(
                messages=input,
                **no_filter_kwargs(acompletion, all_kwargs, self.EXCLUDED_PARAMS),
            )

            if config._log:
                self.log(
                    log_config=self._log_config,
                    prompt=prompt,
                    response=OpenAIResponse(output),
                    **all_kwargs,
                )
                # Todo: set config= as param

        return OpenAIResponse(output)
