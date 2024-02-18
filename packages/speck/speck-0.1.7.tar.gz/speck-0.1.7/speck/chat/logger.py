from typing import Any

from ..logs.logger import universal_format_log


class ChatLogger:
    @staticmethod
    def log(log_config: "LogConfig", prompt: Any, model: str, response: Any, prompt_ref: dict = None, custom_metadata: dict = None, **kwargs):
        universal_format_log(
            log_config=log_config,
            prompt=prompt,
            model=model,
            response=response,
            prompt_ref=prompt_ref,
            custom_metadata=custom_metadata,
            **kwargs,
        )
