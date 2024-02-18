# coding: utf-8
from __future__ import annotations

import json
import pprint

from pydantic import BaseModel, Field, StrictStr, StrictInt, conlist
from typing import Optional

from xingchen.models import Message, Context
from xingchen.models.custom.base_response import BaseResponse


class Choice(BaseModel):
    stop_reason: Optional[StrictStr] = Field(None, alias="stopReason")
    messages: Optional[conlist(Message)] = Field(None, alias="messages")
    __properties = ["stopReason", "messages"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self):
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Choice:
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> Choice:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Choice.parse_obj(obj)

        return Choice.parse_obj({
            'stop_reason': obj.get('stopReason'),
            'messages': obj.get('messages')
        })


class Usage(BaseModel):
    user_tokens: Optional[StrictInt] = Field(None, alias="userTokens")
    input_tokens: Optional[StrictInt] = Field(None, alias="inputTokens")
    output_tokens: Optional[StrictInt] = Field(None, alias="outputTokens")

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self):
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Usage:
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> Usage:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Usage.parse_obj(obj)

        return Usage.parse_obj({
            'user_tokens': obj.get('userTokens'),
            'input_tokens': obj.get('inputTokens'),
            'output_tokens': obj.get('outputTokens')
        })


class ChatResult(BaseModel):
    choices: Optional[conlist(Choice)] = Field(None, alias="choices")
    usage: Optional[Usage] = Field(None, alias="usage")
    context: Optional[Context] = Field(None, alias="context")

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self):
        return self.dict(by_alias=True, exclude={}, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> ChatResult:
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> ChatResult:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChatResult.parse_obj(obj)

        return ChatResult.parse_obj({
            'choices': obj.get('choices'),
            'usage': obj.get('usage'),
            'context': obj.get('context')
        })


class ChatResponse(BaseResponse):
    data: Optional[ChatResult] = Field(None, alias="chatResult")

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        return pprint.pformat(self.dict(by_alias=False, exclude_none=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self):
        return self.dict(by_alias=False, exclude={}, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> ChatResponse:
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> ChatResponse | None:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChatResponse.parse_obj(obj)

        return ChatResponse.parse_obj({
            'request_id': obj.get('requestId'),
            'error_code': obj.get('errorCode'),
            'error_message': obj.get('errorMessage'),
            'error_name': obj.get('errorName'),
            'http_status_code': obj.get('httpStatusCode'),
            'code': obj.get('code'),
            'error_message_key': obj.get('errorMessageKey'),
            'success': obj.get('success'),
            'data': obj.get('data')
        })