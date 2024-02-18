from __future__ import annotations

import re
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Iterator, Literal, Optional, Tuple, Union
import requests

from openai._types import NotGiven

# from dataclasses import dataclass
from pydantic import BaseModel, Extra

from ..chat.logger import ChatLogger
from ..util._live_debug import run_debug_websocket

NOT_GIVEN = None


class MissingVariables(ValueError):
    variables: list[str]
    id: str | None

    def __init__(self, variables: list[str], id: str | None):
        self.variables = variables
        self.id = id

    def __str__(self):
        return f"Missing variables {self.variables} for prompt \"{self.id}\""


class PromptNotFound(ValueError):
    id: str

    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return f"Prompt \"{self.id}\" not found."


class DuplicatePromptId(ValueError):
    id: str

    def __init__(self, id: str):
        self.id = id

    def __str__(self):
        return f"Prompt \"{self.id}\" already exists."


class PromptContext:
    api_key: str
    endpoint: str
    context_id: str
    path: str
    prompts: dict[str, Prompt]

    def __init__(self, api_key: str, endpoint: str, path: str):
        self.api_key = api_key
        self.endpoint = endpoint or "https://api.getspeck.ai"
        self.path = path
        self.prompts = {}
        self.context_id = uuid.uuid4().hex

    def add_prompt(self, id: str, prompt: Prompt):
        if id in self.prompts:
            raise DuplicatePromptId(id)
        self.prompts[id] = prompt

    def upload(self):
        if self.api_key:
            headers = {"X-API-Key": self.api_key}
            body = self.to_dict()

            response = requests.post(f"{self.endpoint}/logging/create/prompt", headers=headers, json=body)
            response.raise_for_status()
            return response.json()

    def get_key(self):
        return {
            "context_id": self.context_id,
            "path": self.path,
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.upload()

    def to_dict(self):
        return {
            "context_id": self.context_id,
            "path": self.path,
            "prompts": {
                name: prompt.to_dict() for name, prompt in self.prompts.items()
            },
            "metadata": {
                "timestamp": int(datetime.now().timestamp()),
            }
        }


class Value:
    type: Type
    value: Any = None

    class Type(Enum):
        ANY = "any"

    def __init__(self, type: Type, value: Any):
        self.type = type
        self.value = value


class Message:
    role: MessageRole
    content: str
    condition: Union[str, None] = None

    def __init__(
        self,
        role: MessageRole,
        content: str,
        condition: Union[str, None] = None,
    ):
        self.role = role
        self.content = content
        self.condition = condition

    def to_dict(self):
        if self.condition:
            return {
                "role": self.role,
                "content": self.content,
                "condition": self.condition,
            }
        else:
            return {"role": self.role, "content": self.content}

    def __str__(self):
        return f"Message(role={self.role}, content={self.content}, condition={self.condition})"


class SafeDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"  # Returns the key in curly braces as a string


class PromptChild:
    prompt: Prompt = None
    role: str = None
    content: str = None
    inherit_variables: bool = True

    @property
    def is_prompt(self):
        return self.prompt is not None

    def __init__(self, prompt: Prompt = None, content: str = None, role: str = None, inherit_variables: bool = True):
        self.prompt = prompt
        self.role = role
        self.content = content
        self.inherit_variables = inherit_variables

    def get_ref(self):
        if self.content is not None:
            return {
                "role": self.role,
                "content": self.content,
                "inherit_variables": self.inherit_variables,
            }

        return {
            "prompt": self.prompt.get_ref(),
            "inherit_variables": self.inherit_variables,
        }

class Prompt(str):
    id: Union[str, None] = None
    messages: list[Message]
    variable_declarations: Union[dict[str, Value]] = None
    variables: Union[dict[str, Any], None] = None
    config: Union[dict[str, str], None] = None
    _context: PromptContext = None
    _children: list[PromptChild] = []

    def get_children_messages(self):
        if self._children is None:
            return None
        ret = []
        for child in self._children:
            if child.is_prompt:
                if child.inherit_variables:
                    raise NotImplementedError("Inheriting variables not supported yet.")
                ret += child.prompt.compose()
            else:
                ret.append(
                    {
                        "role": child.role,
                        "content": Prompt._format_map(
                            child.content, self.variables, self.variable_declarations
                        ) if child.inherit_variables else child.content,
                    }
                )

        return ret

    def to_dict(self):
        messages = [msg.to_dict() for msg in self.messages]

        children_messages = self.get_children_messages()
        if children_messages:
            messages += children_messages

        return {
            "messages": messages,
            "variables": self.variables,
            "variable_declarations": [{"name": name, "type": value.type.value if isinstance(value.type, Value.Type) else value.type, "value": value.value} for name, value in (self.variable_declarations or {}).items()],
            "config": self.config,
            "id": self.id,
        }

    def get_ref(self):
        data = {
            **(self._context.get_key() if self._context else {}),
            "id": self.id,
            "variables": self.variables,
        }

        if self._children:
            data["children"] = [child.get_ref() for child in self._children]

        return data

    def __init__(
        self,
        messages: PromptTypes,
        variables: Union[dict[str, str], None] = None,
        config: Union[dict[str, str], None] = None,
        id: Union[str, None] = None,
        context: PromptContext = None,
        variable_declarations: Union[dict[str, Value], None] = None,
        children: list[PromptChild] = None,
    ):
        if isinstance(messages, str):
            messages = [Message(role="user", content=messages)]
        elif isinstance(messages, Message):
            messages = [messages]
        elif isinstance(messages, list):
            if all(isinstance(message, Message) for message in messages):
                pass
            elif all(isinstance(message, dict) for message in messages):
                messages = [
                    Message(role=message["role"], content=message["content"])
                    for message in messages
                ]
            else:
                raise ValueError(
                    f"Invalid type for messages: {type(messages)}\n{messages}"
                )

        self.messages = messages
        self.variables = variables
        self.config = config
        self.id = id
        self._context = context
        self.variable_declarations = variable_declarations
        self._children = children
        super().__init__()

    @classmethod
    def create(
        cls,
        messages: PromptTypes,
        variables: dict[str, str] = None,
        id: Union[str, None] = None,
        config: Union[dict[str, Any], None] = None,
    ) -> "Prompt":
        if isinstance(messages, cls):
            # Todo: clone object and add variables
            return messages
        return cls(messages=messages, variables=variables, id=id, config=config)

    @classmethod
    def _read(cls, lines: str, id: str = None, context: PromptContext = None) -> "Prompt":
        # Todo: add config parsing
        config = {}
        messages = []
        variable_declarations = {}

        current_min_spaces = 0
        current_section = None
        current_message = []
        condition = None

        def add_message():
            nonlocal current_message, current_min_spaces, condition, current_section
            if current_section:  # current_message:
                if current_section != "variables" and not current_section.startswith("/") and current_section != "config":
                    messages.append(
                        Message(
                            role=current_section,
                            content="\n".join(
                                [m[current_min_spaces:] for m in current_message]
                            ),
                            condition=condition,
                        )
                    )
                current_message = []
                current_min_spaces = 0
                condition = None

        for line in lines.split("\n"):
            line = line.rstrip("\r")
            if line.startswith("<"):
                line = line.strip()
                add_message()
                current_section = line[1:-1]
                if "if " in current_section:
                    if_index = current_section.index("if ")
                    condition = current_section[if_index + 2 :]
                    current_section = current_section[: if_index - 1]
                else:
                    condition = None
            elif current_section == "config" and "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
            elif current_section == "variables":
                var_value = None
                if "=" in line:
                    line, var_value = line.split("=", 1)
                    line = line.strip()
                    var_value = var_value.strip()

                var_type = Value.Type.ANY
                if ":" in line:
                    line, var_type = line.split(":", 1)
                    line = line.strip()
                    var_type = var_type.strip()

                key = line.strip()
                variable_declarations[key] = Value(type=var_type, value=var_value)
            elif (
                current_section is not None
                and current_section in ["system", "user", "assistant", "if", "else"]
                or "add " in current_section
            ):
                min_spaces = len(line) - len(line.lstrip())
                if 0 < min_spaces < current_min_spaces or current_min_spaces == 0:
                    current_min_spaces = min_spaces
                current_message.append(line)

        add_message()
        return cls(messages=messages, id=id, context=context, variable_declarations=variable_declarations, config=config)

    @classmethod
    def read_all(cls, path: str, context: PromptContext = None) -> dict[str, "Prompt"]:
        with open(path, "r") as f:
            return cls.reads_all(f.read(), context=context)

    @classmethod
    def read(cls, path: str, id: Union[str, None] = None, context: PromptContext = None, **kwargs) -> "Prompt":
        with open(path, "r") as f:
            return cls.reads(f.read(), id=id, context=context, **kwargs)

    @classmethod
    def reads(cls, text: str, id: Union[str, None] = None, context: PromptContext = None, **kwargs) -> "Prompt":
        name = id or kwargs.get("name")
        if name is not None:
            prompts = cls.reads_all(text, context=context)
            return prompts[name]
        else:
            return cls._read(text, id=name)

    @classmethod
    def parse(cls, text: str, context: PromptContext = None) -> dict[str, "Prompt"]:
        return cls.reads_all(text, context=context)

    @classmethod
    def reads_all(cls, text: str, context: PromptContext = None) -> dict[str, "Prompt"]:
        if context is None:
            context = PromptContext(path=text.split("\n")[0], api_key=None, endpoint=None)

        prompts = {}
        lines = []
        current_prompt_name = None
        current_min_spaces = -1

        for line in text.split("\n"):
            line = line.rstrip("\n").rstrip("\r")
            if line.lstrip().startswith("<"):
                min_spaces = len(line) - len(line.lstrip())
                stripped_line = line.strip()

                if stripped_line.startswith("<prompt") and min_spaces == 0:
                    if current_prompt_name:
                        prompts[current_prompt_name] = cls._read(
                            "\n".join([m[current_min_spaces:] for m in lines]),
                            id=current_prompt_name,
                            context=context,
                        )

                    current_min_spaces = -1
                    lines = []
                    temp_prompt_name = stripped_line[8:-1].strip()
                    if "id=" in temp_prompt_name:
                        temp_prompt_name, id = temp_prompt_name.split("id=")
                        current_prompt_name = id.strip("\"' ")
                    else:
                        current_prompt_name = temp_prompt_name
                elif stripped_line.startswith("</prompt>") and min_spaces == 0:
                    prompts[current_prompt_name] = cls._read(
                        "\n".join([m[current_min_spaces:] for m in lines]),
                        id=current_prompt_name,
                        context=context,
                    )
                    current_prompt_name = None
                    current_min_spaces = -1
                    lines = []
                else:
                    lines.append(line)
                    if current_min_spaces == -1 or min_spaces < current_min_spaces:
                        current_min_spaces = min_spaces
            else:
                lines.append(line)

        for id, prompt in prompts.items():
            context.add_prompt(id, prompt)

        return prompts

    def _file(self):
        file = []
        if len(self.variable_declarations or {}) > 0:
            file.append("<variables>")
            for name, value in self.variable_declarations.items():
                type: str = value.type.value if isinstance(value.type, Value.Type) else value.type

                if value.value is None:
                    file.append(f"    {name}: {type}")
                else:
                    file.append(f"    {name}: {type} = {value.value}")

        for message in self.messages:
            if message.condition is not None:
                file.append(f"<{message.role} if {message.condition}>")
            else:
                file.append(f"<{message.role}>")

            if len(message.content) > 0:
                for line in message.content.split("\n"):
                    file.append(" " * 4 + line)
        return "\n".join(file)

    @classmethod
    def write(cls, prompt: Union["Prompt", dict[str, "Prompt"]], path: str):
        with open(path, "w") as f:
            if isinstance(prompt, dict):
                content = ""
                for name, prompt in prompt.items():
                    content += f'<prompt id="{name}">\n'
                    content += "\n".join(
                        [" " * 4 + line for line in prompt._file().split("\n")]
                    )
                    content += "\n</prompt>\n\n"
                f.write(content.strip())
            else:
                f.write(prompt._file())

    def __new__(
        cls,
        messages: PromptTypes,
        **kwargs,
    ):
        # Todo: Handle string, Message, and list[Message]
        instance = super(Prompt, cls).__new__(cls, str(messages))
        return instance

    @classmethod
    def from_openai(cls, messages: list[dict[str, str]]):
        return cls(
            messages=[
                Message(role=message["role"], content=message["content"])
                for message in messages
            ]
        )

    def _check_condition(self, condition: str):
        if condition is None:
            return False

        condition = condition.strip()
        if condition.startswith("not"):
            return not self._check_condition(condition[3:])
        if condition.startswith("!"):
            return not self._check_condition(condition[1:])

        def check_declarations():
            if self.variable_declarations is None:
                return False

            var_name = condition.strip(" {}")
            if var_name not in self.variable_declarations:
                return False

            value = self.variable_declarations[var_name].value
            return (
                value == "true"
                or value == "True"
                or value == "1"
                or value == 1
                or value == True
            )

        def check_variables():
            if self.variables is None:
                return check_declarations()

            var_name = condition.strip(" {}")
            if var_name not in self.variables:
                return check_declarations()

            value = self.variables[var_name]
            return (
                value == "true"
                or value == "True"
                or value == "1"
                or value == 1
                or value == True
            )

        return check_variables()

    @staticmethod
    def _format_map(text: str, variables: dict[str, str], variable_declarations: dict[str, Value]):
        pattern = r"\{[^{}]*\}"
        matches = list(re.finditer(pattern, text))
        for match in reversed(matches):
            start, end = match.span()
            var_text = text[start + 1 : end - 1]
            if variables is not None and var_text in variables:
                # Todo: Promptfiles better variable type parsing
                text = text[:start] + str(variables[var_text]) + text[end:]
            elif variable_declarations is not None and var_text in variable_declarations:
                text = text[:start] + str(variable_declarations[var_text].value) + text[end:]

        return text  # string.format_map(SafeDict(variables or {}))

    def _convert_expression(self, expression: str) -> str:
        """In (A ? B : C), B and C can be expressions"""
        expression = expression.strip()

        if expression.startswith('"') and expression.endswith('"'):
            return Prompt._format_map(
                expression[1:-1].replace("\\n", "\n").replace("\\t", "\t"),
                self.variables,
                self.variable_declarations,
            )
        else:
            return Prompt._format_map("{" + expression + "}", self.variables, self.variable_declarations)

    def _format_message(self, message: Message, override_role: Union[str, None] = None):
        # Check for variables with {...: prompt} and replace with prompt
        pattern = r"\{[^{}]*\}"  # Pattern to match {anything: prompt}

        text = message.content
        matches = list(re.finditer(pattern, text))
        # Replace matches from the end to keep indexes correct
        for match in reversed(matches):
            start, end = match.span()
            var_text = text[start + 1 : end - 1]
            # Adds support for ternary operators and conditions
            if "?" in var_text:
                condition, values = var_text.split("?")
                left, right = values.split(":")
                if self._check_condition(condition):
                    text = text[:start] + self._convert_expression(left) + text[end:]
                else:
                    text = text[:start] + self._convert_expression(right) + text[end:]
            # text = text[:start] + "{hi}" + text[end:]

        return {
            "role": override_role if override_role is not None else message.role,
            "content": Prompt._format_map(text, self.variables, self.variable_declarations),
        }

    def compose(self, override_prompt: Prompt = None) -> list[dict[str, str]]:
        var_declarations = (self.variable_declarations if override_prompt is None else override_prompt.variable_declarations) or {}
        required_variables = set(var for var, value in var_declarations.items() if value.value is None)
        defined_variables = set(self.variables or {})

        prev_role, prev_condition = None, False
        ret: list[dict[str, str]] = []

        def add_prompt(name: str):
            if self._context and name in self._context.prompts:
                for sub_msg in self.compose(
                    override_prompt=self._context.prompts[name]
                ):
                    if sub_msg["role"] == "system":
                        raise NotImplementedError("System prompt not supported yet.")
                    else:
                        ret.append(sub_msg)
            else:
                raise PromptNotFound(name)

        for message in (
            self.messages if override_prompt is None else override_prompt.messages
        ):
            add = False  # Java-like variable scoping
            if message.condition is not None:
                add = self._check_condition(message.condition)
                prev_role, prev_condition = "if", add
            elif message.role == "else":
                if not prev_condition:
                    if message.role.startswith("else add "):
                        id = message.role[9:].strip()
                        if "id=" in id:
                            id = id.split("id=")[1].strip("\"' ")
                        add_prompt(id)
                    else:
                        ret.append(
                            self._format_message(message, override_role=prev_role)
                        )
                prev_role, prev_condition = "else", True
                continue
            else:
                add = True
                prev_role = message.role

            if add:
                if message.role.startswith("add "):
                    id = message.role[4:].strip()
                    if "id=" in id:
                        id = id.split("id=")[1].strip("\"' ")
                    add_prompt(id)
                else:
                    ret.append(self._format_message(message))

        children_messages = (override_prompt or self).get_children_messages()
        if children_messages:
            ret += children_messages

        if len(required_variables - defined_variables) > 0:
            raise MissingVariables(variables=list(required_variables - defined_variables), id=(override_prompt or self).id)

        return ret

    def add(self, *args, role: str = None, content: str = None, prompt: Prompt = None, inherit_variables=False) -> Prompt:
        if len(args) > 0:
            raise NotImplementedError("Use [role, content] or [prompt] args instead")
        new_prompt = self.__class__(
            messages=self.messages,
            variables=self.variables,
            id=self.id,
            config=self.config,
            variable_declarations=self.variable_declarations,
            context=self._context,
            children=(self._children or []),
        )

        if role is not None or content is not None:
            new_prompt._children.append(PromptChild(role=role, content=content))

        if prompt is not None:
            new_prompt._children.append(PromptChild(prompt=prompt, inherit_variables=inherit_variables))

        return new_prompt

    @staticmethod
    def _apply_variables(
        messages: list[Message], variables: dict[str, str], variable_declarations: dict[str, Value]
    ) -> list[Message]:
        return [
            Message(
                role=message.role,
                content=Prompt._format_map(message.content, variables, variable_declarations),
                condition=message.condition,
            )
            for message in messages
        ]

    def _check_duplicate_keys(self, other_variables: dict[str, str]) -> dict[str, str]:
        duplicate_keys = set((self.variables or {}).keys()).intersection(
            set((other_variables or {}).keys())
        )
        return {
            key: self.variables[key]
            for key in duplicate_keys
            if self.variables[key] != other_variables[key]
        }

    def _remove_duplicate_keys_from_messages(
        self, other_variables: dict[str, str]
    ) -> list[Message]:
        messages = self.messages
        applied_variables = self._check_duplicate_keys(other_variables)
        if len(applied_variables) > 0:
            messages = self._apply_variables(self.messages, applied_variables, None)

        return messages

    def format(self, *args, **kwargs) -> Prompt:
        # return self.__class__(
        #     messages=[
        #         Message(
        #             role=message.role, content=message.content.format(*args, **kwargs)
        #         )
        #         for message in self.messages
        #     ]
        # )

        messages = self._remove_duplicate_keys_from_messages(kwargs)
        return self.__class__(
            id=self.id,
            messages=[
                Message(
                    role=message.role,
                    content=message.content,
                    condition=message.condition,
                )
                for message in messages
            ],
            variables={**SafeDict(self.variables or {}), **kwargs},
            context=self._context,
            config=self.config,
            variable_declarations=self.variable_declarations,
            children=self._children,
        )

    def __add__(self, other):
        if isinstance(other, Message):
            return self.__class__(
                messages=self.messages + [other], variables={**(self.variables or {})}
            )
        elif isinstance(other, Prompt):
            # Check if there are duplicate keys
            messages = self._remove_duplicate_keys_from_messages(other.variables or {})

            return self.__class__(
                messages=messages + other.messages,
                variables={
                    **SafeDict(self.variables or {}),
                    **SafeDict(other.variables or {}),
                },
            )
        else:
            raise NotImplementedError

    def __str__(self):
        return (
            "Prompt(\n"
            + (
                "\n".join(
                    [f"{message.role}: {message.content}" for message in self.messages]
                )
                + "\n"
                + str(self.variables or {})
            )
            + "\n)"
        )


class Response(BaseModel):
    content: Union[str, None]
    prompt_tokens: Union[int, None] = None
    completion_tokens: Union[int, None] = None
    raw: Union[dict, None] = None

    def __init__(
        self,
        content: Union[str, None],
        closed: bool = False,
        prompt_tokens: Union[int, None] = None,
        completion_tokens: Union[int, None] = None,
        raw: Union[dict, None] = None,
        **kwargs,
    ):
        super().__init__(
            content=content,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            raw=raw,
        )
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create(cls, response: ResponseTypes) -> "Response":
        if isinstance(response, cls):
            return response
        elif isinstance(response, str):
            return cls(content=response)
        else:
            raise NotImplementedError

    def __str__(self):
        return f"Response(content={self.content}, prompt_tokens={self.prompt_tokens}, completion_tokens={self.completion_tokens}, raw={self.raw})"


class MessageChunk(BaseModel):
    content: Union[str, None]

    def encode(self, encoding: str = "utf-8"):
        content = self.content or ""
        return content.encode(encoding)


class Stream:
    # processor that has lambda which returns MessageDelta
    def __init__(
        self,
        client: "Speck",
        iterator: Iterator[Any],
        kwargs: dict,
        log_config: "LogConfig",
        processor: Callable[[Any], MessageChunk],
        custom_metadata: dict = None,
    ):
        self._client = client
        self.message: str = ""
        self.tokens: int = 0
        self._iterator = iterator
        self._kwargs = kwargs
        self._processor = processor
        self._has_logged = False
        self._closed = False
        self._log_config = log_config
        self.custom_metadata = custom_metadata

    def _log(self):
        if not self._has_logged:
            self._has_logged = True

            kwargs = self._kwargs
            kwargs["prompt"] = self._kwargs.get("prompt", [])
            kwargs["temperature"] = self._kwargs.get("temperature", "N/A")
            kwargs["model"] = self._kwargs.get("model", "N/A")
            kwargs["response"] = Response(
                content=self.message, raw={}, closed=True, completion_tokens=self.tokens
            )

            # Todo: add prompt_tokens using tiktoken
            ChatLogger.log(log_config=self._log_config, custom_metadata=self.custom_metadata, **kwargs)

    def _process(self, item) -> MessageChunk:
        return self._processor(item)

    def __next__(self) -> MessageChunk:
        try:
            if self._closed:
                raise StopIteration

            # next_item = None
            # while next_item is None:
            next_item = next(self._iterator)

            item: MessageChunk = self._process(next_item)
            if item.content:
                self.message += item.content
            self.tokens += 1
            return item
        except StopIteration:
            self._log()
            raise

    def __iter__(self) -> Iterator[MessageChunk]:
        return self

    def close(self):
        try:
            self._closed = True
            # todo: make this work for packages other than openai
            self._iterator.response.close()
        except AttributeError:
            pass


class LogConfig(BaseModel):
    api_key: Union[str, None] = None
    endpoint: str = "https://api.getspeck.ai"

    class Config:
        extra = "allow"


class ChatConfig:
    # Todo: add typed params here
    # Todo: Create conversions to other formats
    def __init__(
        self,
        *,
        provider: str = None,
        model: OpenAIModel,
        stream: bool = False,
        _log: bool = True,
        temperature: Union[Optional[float], NotGiven] = NOT_GIVEN,
        max_tokens: Union[Optional[int], NotGiven] = NOT_GIVEN,
        top_p: Union[Optional[float], NotGiven] = NOT_GIVEN,
        frequency_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN,
        presence_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN,
        chat_args: dict[str, str] = {},
        **config_kwargs,
    ):
        if "log_config" in config_kwargs:
            del config_kwargs["log_config"]

        self.provider = provider
        self.model = model
        self.stream = stream
        self._log = _log
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.chat_args = chat_args | config_kwargs
        # If this is modified, update to_dict too

    def to_dict(self):
        return {
            "provider": self.provider,
            "model": str(self.model),  # Assuming model can be represented as a string
            "stream": self.stream,
            "_log": self._log,
            "temperature": self._convert_optional(self.temperature),
            "max_tokens": self._convert_optional(self.max_tokens),
            "top_p": self._convert_optional(self.top_p),
            "frequency_penalty": self._convert_optional(self.frequency_penalty),
            "presence_penalty": self._convert_optional(self.presence_penalty),
            "chat_args": self.chat_args,
        }

    def _convert_optional(self, value):
        return None if isinstance(value, NotGiven) else value

    @classmethod
    def create(cls, config: ChatConfigTypes, kwargs: dict = None) -> "ChatConfig":
        if isinstance(config, cls):
            if kwargs is not None:
                return cls(**{**config.__dict__, **kwargs})
            else:
                return config
        elif isinstance(config, dict):
            return cls(**config)
        elif kwargs:
            return cls(**kwargs)
        else:
            raise NotImplementedError

    def get(self, key: str, default: Any = None) -> Any:
        return getattr(self, key, default)

    def convert(self, provider: str = "speck") -> "ChatConfig":
        """
        Convert to another config format
        """
        if provider == "openai":
            return OpenAIChatConfig(
                model=self.model,
                stream=self.stream,
                _log=self._log,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
                **self.chat_args,
            )

        return self

    def log_chat(
        self,
        *,
        log_config: LogConfig,
        prompt: Prompt,
        response: Response,
        provider: str = "speck",
        prompt_ref: dict = None,
        custom_metadata: dict = None,
    ):
        config = self.convert()
        ChatLogger.log(
            log_config=log_config,
            provider=provider,
            model=str(config.model),
            prompt=prompt,
            response=response,
            prompt_ref=prompt_ref,
            custom_metadata=custom_metadata,
            **config.chat_args,
        )

    def encode(self, encoding: str = "utf-8"):
        return self.__str__().encode(encoding)

    def __str__(self):
        return f"ChatConfig(provider={self.provider}, model={self.model}, stream={self.stream}, _log={self._log}, temperature={self.temperature}, max_tokens={self.max_tokens}, top_p={self.top_p}, frequency_penalty={self.frequency_penalty}, presence_penalty={self.presence_penalty}, chat_args={self.chat_args})"


class OpenAIChatConfig(ChatConfig):
    def __init__(
        self,
        model: OpenAIModel,
        provider: str = "openai",
        stream: bool = False,
        _log: bool = True,
        temperature: Union[Optional[float], NotGiven] = NOT_GIVEN,
        max_tokens: Union[Optional[int], NotGiven] = NOT_GIVEN,
        top_p: Union[Optional[float], NotGiven] = NOT_GIVEN,
        frequency_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN,
        presence_penalty: Union[Optional[float], NotGiven] = NOT_GIVEN,
        **config_kwargs,
    ):
        self.provider = provider
        self.model = model
        self.stream = stream
        self._log = _log
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.chat_args = config_kwargs

    def convert(self, provider: str = "speck") -> ChatConfig:
        """
        Maps config to universal format then converts to another config format
        """
        universal_config = ChatConfig(
            model=self.model,
            stream=self.stream,
            _log=self._log,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            **self.chat_args,
        )

        return universal_config.convert(provider=provider)


class IChatClient(ABC):
    def debug_chat(
        self, prompt: "Prompt", config: "ChatConfig"
    ) -> ("Prompt", "ChatConfig"):
        data = run_debug_websocket(self._client, self, prompt, config)

        if data.get("prompt") and data.get("config"):
            prompt = Prompt(**data["prompt"])
            config = ChatConfig(**data["config"])

        return prompt, config

    @abstractmethod
    def chat(
        self,
        prompt: PromptTypes,
        config: Union[ChatConfig, NotGiven] = NOT_GIVEN,
        **config_kwargs,
    ) -> Union[Response, Stream]:
        pass

    @abstractmethod
    async def achat(
        self,
        prompt: PromptTypes,
        config: Union[ChatConfig, NotGiven] = NOT_GIVEN,
        **config_kwargs,
    ) -> Union[Response, Stream]:
        pass


PromptTypes = Union[str, Message, list[Message], list[dict[str, str]]]
ResponseTypes = Union[Response, str]
ChatConfigTypes = Union[ChatConfig, dict[str, str]]

MessageRole = Union[Literal["system", "user", "assistant"], str]
OpenAIModel = Union[Literal["gpt-4", "gpt-3.5", "gpt-3.5-turbo"], str]
