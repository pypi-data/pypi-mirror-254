from __future__ import annotations
from enum import Enum
from typing import Dict, List, Any

from pydantic import BaseModel, Field

import pprint
import re  # noqa: F401
import json


class Function(BaseModel):
    name: str = Field(..., title="function名", description="function名")
    description: str = Field(..., title="function描述", description="function描述")
    parameters: Dict = Field(..., title="function参数定义", description="function参数定义，json schema格式")

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Function:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Function:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Function.parse_obj(obj)

        _obj = Function.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "parameters": obj.get("parameters")
        })
        return _obj


class FunctionChoiceType(Enum):
    none = "none"
    auto = "auto"
    specific = "specific"


class FunctionChoice(BaseModel):
    type: FunctionChoiceType = Field(..., title="function调用策略", description="function调用策略")
    names: List[str] = Field(None, title="指定的 function 名", description="调用策略为specific时指定的function名，目前只生效第一个")

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FunctionChoice:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FunctionChoice:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FunctionChoice.parse_obj(obj)

        _obj = FunctionChoice.parse_obj({
            "type": obj.get("type"),
            "names": obj.get("names")
        })
        return _obj


class PlanningApiInfo(BaseModel):
    api_name: str = Field(..., alias="apiName", description="fc名称")
    parameters: Dict = Field({})

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PlanningApiInfo:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlanningApiInfo:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlanningApiInfo.parse_obj(obj)

        _obj = PlanningApiInfo.parse_obj({
            "api_name": obj.get("apiName"),
            "parameters": obj.get("parameters")
        })
        return _obj


class FunctionCall(BaseModel):
    thought: str = Field(...)
    api_call_list: List[PlanningApiInfo] = Field([], alias="apiCallList", description="API调用列表")

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FunctionCall:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FunctionCall:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FunctionCall.parse_obj(obj)

        _obj = FunctionCall.parse_obj({
            "thought": obj.get("thought"),
            "api_call_list": [PlanningApiInfo.from_dict(_item) for _item in obj.get("apiCallList")] if obj.get("apiCallList") is not None else None,

        })
        return _obj


class Plugin(BaseModel):
    name: str = Field(..., title="插件名", description="插件名")
    ext: Dict = Field(None, title="插件参数", description="插件参数")

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Plugin:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Plugin:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Plugin.parse_obj(obj)

        _obj = Plugin.parse_obj({
            "name": obj.get("thought"),
            "ext": obj.get("ext")

        })
        return _obj
