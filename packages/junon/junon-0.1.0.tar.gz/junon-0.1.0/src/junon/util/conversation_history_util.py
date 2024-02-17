import os
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import json
import tiktoken
from openai.types.chat.chat_completion_message import FunctionCall
from tiktoken import Encoding

_TIKTOKEN_ENCODING_MODEL_NAME: str = 'cl100k_base'
_TIKTOKEN_ENCODING_MODEL: Optional[Encoding] = None


@dataclass
class Message:
    timestamp: str
    role: str
    content: str
    name: Optional[str] = None
    function_call: Optional[FunctionCall] = None
    token_count: Optional[int] = None

    @classmethod
    def from_dict(cls, d: dict):
        return Message(
            timestamp=datetime.now().isoformat(),
            role=d['role'],
            content=d['content'],
            name=d.get('name'),
            function_call=d.get('function_call'),
        )

    def to_api_argument(self) -> dict:
        if self.name:  # function
            return dict(
                role=self.role,
                content=self.content,
                name=self.name,
            )
        elif self.function_call and self.function_call.name:  # function call
            return dict(
                role=self.role,
                content=self.content or "",
                function_call=dict(
                    name=self.function_call.name,
                    arguments=self.function_call.arguments
                )
            )
        else:
            return dict(
                role=self.role,
                content=self.content,
            )

    @classmethod
    def list_to_api_argument(cls, messages: List) -> List[dict]:
        return [message.to_api_argument() for message in messages]

    def count_token(self):
        if not self.token_count:
            message_json = json.dumps(self.to_api_argument())
            encoded = get_tiktoken_encoding().encode(message_json)
            self.token_count = len(encoded)
        return self.token_count


def encode_custom_class(obj):
    if isinstance(obj, FunctionCall):
        return obj.__dict__  # または {'field1': obj.field1, 'field2': obj.field2}
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


def decode_custom_class(json_dict):
    if "name" in json_dict and "arguments" in json_dict:
        return FunctionCall(**json_dict)
    return json_dict


def save(messages: List[Message], filename: str):
    """
    Save a list of Message objects to a JSON file.

    :param messages: List of Message objects.
    :param filename: Name of the file where data will be saved.
    """
    with open(filename, 'w') as file:
        json.dump(
            [message.__dict__ for message in messages],
            file,
            indent=4,
            default=encode_custom_class,
            ensure_ascii=False
        )


def load(filename: str) -> List[Message]:
    """
    Load Message objects from a JSON file.

    :param filename: Name of the file to load data from.
    :return: A list of Message objects.
    """
    if not os.path.exists(filename):
        return list()
    with open(filename, 'r') as file:
        data = json.load(file, object_hook=decode_custom_class)
        return [Message(**item) for item in data]


def to_dict(messages: List[Message]) -> List[dict]:
    """
    Convert a list of Message objects to a list of dictionaries.
    :param messages:
    :return:
    """
    return [dict(role=message.role, content=message.content) for message in messages]


def get_token_count(messages: List[Message]) -> int:
    """
    Count the number of tokens in a list of Message objects.
    :param messages:
    :return:
    """
    return sum(message.count_token() for message in messages)

def set_tiktoken_encoding_model_name(model_name: str):
    global _TIKTOKEN_ENCODING_MODEL_NAME, _TIKTOKEN_ENCODING_MODEL
    if _TIKTOKEN_ENCODING_MODEL_NAME == model_name:
        return
    _TIKTOKEN_ENCODING_MODEL = None
    _TIKTOKEN_ENCODING_MODEL_NAME = model_name


def get_tiktoken_encoding():
    # "cl100k_base"
    global _TIKTOKEN_ENCODING_MODEL
    if not _TIKTOKEN_ENCODING_MODEL:
        _TIKTOKEN_ENCODING_MODEL = tiktoken.get_encoding(_TIKTOKEN_ENCODING_MODEL_NAME)
    return _TIKTOKEN_ENCODING_MODEL
