# coding: utf-8


from __future__ import annotations

import json
import pprint

from pydantic import BaseModel, Field, StrictStr


class ResetChatHistoryRequest(BaseModel):
    """
    重置对话
    """
    character_id: StrictStr = Field(..., alias="characterId", description="角色ID")
    user_id: StrictStr = Field(..., alias="userId", description="业务系统用户ID")
    __properties = ["characterId", "userId"]

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
    def from_json(cls, json_str: str) -> ResetChatHistoryRequest:
        """Create an instance of SysReminderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResetChatHistoryRequest:
        """Create an instance of SysReminderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResetChatHistoryRequest.parse_obj(obj)

        _obj = ResetChatHistoryRequest.parse_obj({
            "character_id": obj.get("characterId"),
            "user_id": obj.get("userId")
        })
        return _obj


