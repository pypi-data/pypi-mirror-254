# coding: utf-8

from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr


class ChatContext(BaseModel):
    use_chat_history: Optional[bool] = Field(None, alias="useChatHistory", description="是否使用平台对话历史，默认是")
    is_regenerate: Optional[bool] = Field(None, alias="isRegenerate", description="""
    是否重新生成
    true: 重新生成
    - 如果使用平台对话历史
        - messages 会被忽略
        - queryId 不能为空
    - 如果不使用平台历史
        - 可以不传 queryId, messages 和 随机因子 parameter.seed 需要用户提供
    """)
    query_id: Optional[StrictStr] = Field(None, alias="queryId", description="重新生成且使用平台历史时，该值必传，不使用平台历史时，该值可以不传")
    answer_id: Optional[StrictStr] = Field(None, alias="answerId", description="若 answerId 不为空，认为是重新生成后的新一轮对话，该 answerId 为最后轮对话中多个回复中的一条消息ID")
    __properties = ["useChatHistory", "isRegenerate", "queryId", "answerId"]

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
    def from_json(cls, json_str: str) -> ChatContext:
        """Create an instance of Context from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChatContext:
        """Create an instance of Context from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChatContext.parse_obj(obj)

        _obj = ChatContext.parse_obj({
            "use_chat_history": obj.get("useChatHistory"),
            "is_regenerate": obj.get("isRegenerate"),
            "query_id": obj.get("queryId"),
            "answer_id": obj.get("answerId"),
        })
        return _obj


