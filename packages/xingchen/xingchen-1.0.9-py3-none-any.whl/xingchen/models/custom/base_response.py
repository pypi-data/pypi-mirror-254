# coding: utf-8

from __future__ import annotations

import json
import pprint

from pydantic import BaseModel, Field, StrictStr, StrictInt, StrictBool, conlist
from typing import Optional


class BaseResponse(BaseModel):
    request_id: Optional[StrictStr] = Field(None, alias="requestId")
    error_code: Optional[StrictInt] = Field(None, alias="errorCode")
    error_message: Optional[StrictStr] = Field(None, alias="errorMessage")
    error_name: Optional[StrictStr] = Field(None, alias="errorName")
    http_status_code: Optional[StrictInt] = Field(None, alias="httpStatusCode")

    success: Optional[StrictBool] = Field(None, alias="success")
    code: Optional[StrictInt] = Field(None, alias="code")
    message: Optional[StrictBool] = Field(None, alias="message")
    error_message_key: Optional[StrictStr] = Field(None, alias="errorMessageKey")

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
    def from_json(cls, json_str: str) -> BaseResponse:
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> BaseResponse | None:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaseResponse.parse_obj(obj)

        return BaseResponse.parse_obj({
            'request_id': obj.get('requestId'),
            'error_code': obj.get('errorCode'),
            'error_message': obj.get('errorMessage'),
            'error_name': obj.get('errorName'),
            'http_status_code': obj.get('httpStatusCode'),
            'code': obj.get('code'),
            'error_message_key': obj.get('errorMessageKey'),
            'success': obj.get('success')
        })
