import warnings
from typing import Any

import requests
import logging

from ..util import get_dict
from .metadata import generate_metadata_dict

logger = logging.getLogger(__name__)


# Todo: Fix typing for this function (circular import)
def universal_format_log(
    log_config: "LogConfig",
    provider: "Providers",
    prompt: "Prompt",
    model: str,
    response: "Response",
    session_key: str = None,
    prompt_ref: dict = None,
    custom_metadata: dict = None,
    **kwargs,
) -> dict[str, str]:
    if not log_config:
        logger.info("No log config found. Define the log config in the log or client.")
        return {}
    if not log_config.api_key:
        # print("No api key found. Define the api key in the log config or client.")
        return {}

    body: dict[str, Any] = {
        "input": {
            # Todo: Fix typing for Providers enum (circular import)
            "prompt_ref": prompt_ref,
            "provider": provider.value if hasattr(provider, "value") else provider,
            "model": model,
            **prompt.to_dict(),
            **kwargs,
        },
        "output": get_dict(response),
        "metadata": generate_metadata_dict(),
    }

    if custom_metadata is not None:
        body["custom_metadata"] = custom_metadata

    try:
        headers = {"X-API-Key": log_config.api_key}
        request: requests.Response = requests.post(
            f"{log_config.endpoint}/logging/create/llm", headers=headers, json=body
        )
        request.raise_for_status()
        return request.json()
    except requests.exceptions.HTTPError as e:
        logger.info("HTTP", e)
    except requests.exceptions.ReadTimeout as e:
        logger.info("Read", e)
    except requests.exceptions.ConnectionError as e:
        logger.info("Connection", e)
    except requests.exceptions.RequestException as e:
        logger.info("Request", e)
