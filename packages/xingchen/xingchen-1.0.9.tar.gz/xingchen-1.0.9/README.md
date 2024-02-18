# [通义星尘](https://tongyi.aliyun.com/xingchen) Python SDK

- API 版本: v2
- Package 版本: 1.0.5

## 运行环境

Python 3.7+

## 安装/使用

### 安装

```sh
pip install xingchen==1.0.5
```

## 使用

认证信息可在[通义星尘/接入管理](https://tongyi.aliyun.com/xingchen/accessManagement)官网创建。

```python

import unittest

from xingchen import Configuration, ApiClient, ChatApiSub, ChatReqParams, CharacterKey, Message, UserProfile, \
    ModelParameters


def build_chat_param():
    return ChatReqParams(
        bot_profile=CharacterKey(
            character_id="c39797a35ad243f1a85baaa6e1ec37e0",
            version=1
        ),
        model_parameters=ModelParameters(
            top_p=0.8,    
            temperature=0.8,
            seed=1683806810
        ),
        messages=[
            Message(
                name='小明',
                role='user',
                content='你叫什么名字？'
            ),
            Message(
                name='小婉',
                role='assistant',
                content='我叫小婉啊。'
            ),
            Message(
                name='小明',
                role='user',
                content='你今年多大?'
            ),
            Message(
                name='小婉',
                role='assistant',
                content='我今年17岁了。'
            ),
            Message(
                name='小明',
                role='user',
                content='可以详细介绍浙江有哪些好玩的地方吗？'
            )
        ],
        user_profile=UserProfile(
            user_id='123456789',
            user_name='小明'
        )
    )


class Test(unittest.TestCase):

    @staticmethod
    def init_client():
        configuration = Configuration(
            host="https://nlp.aliyuncs.com"
        )
        configuration.access_token = "{API-KEY}"
        with ApiClient(configuration) as api_client:
            api_instance = ChatApiSub(api_client)
        return api_instance

    # 非流式回复
    def test_chat_sync(self):
        api = self.init_client()
        chat_param = build_chat_param()
        res = api.chat(chat_param)
        print(res.to_str())

    # 流式回复
    def test_chat_async(self):
        # 用户对话
        api = self.init_client()
        chat_param = build_chat_param()
        chat_param.streaming = True
        responses = api.chat(chat_param)
        for res in responses:
            print(res)


```

## [API文档](https://tongyi.aliyun.com/xingchen/document/interface_description)

请求地址 *https://nlp.aliyuncs.com*

Class | Method | HTTP request | 描述
------------ | ------------- | ------------- | -------------
*CharacterApiSub* | [**character_details**](docs/CharacterApiSub.md#character_details) | **GET** /v2/api/character/details | 角色详情
*CharacterApiSub* | [**character_details1**](docs/CharacterApiSub.md#character_details1) | **GET** /v1/api/character/details | 角色详情
*CharacterApiSub* | [**create**](docs/CharacterApiSub.md#create) | **POST** /v1/api/character/create | 创建角色
*CharacterApiSub* | [**create1**](docs/CharacterApiSub.md#create1) | **POST** /v2/api/character/create | 创建角色
*CharacterApiSub* | [**create_or_update_version**](docs/CharacterApiSub.md#create_or_update_version) | **PUT** /v1/api/character/createOrUpdateVersion | 创建或更新角色版本
*CharacterApiSub* | [**create_or_update_version1**](docs/CharacterApiSub.md#create_or_update_version1) | **PUT** /v2/api/character/createOrUpdateVersion | 创建或更新角色版本
*CharacterApiSub* | [**delete**](docs/CharacterApiSub.md#delete) | **DELETE** /v1/api/character/delete | 删除角色
*CharacterApiSub* | [**delete1**](docs/CharacterApiSub.md#delete1) | **DELETE** /v2/api/character/delete | 删除角色
*CharacterApiSub* | [**list_character_versions**](docs/CharacterApiSub.md#list_character_versions) | **GET** /v1/api/character/versions/{characterId} | 角色版本列表
*CharacterApiSub* | [**list_character_versions1**](docs/CharacterApiSub.md#list_character_versions1) | **GET** /v2/api/character/versions/{characterId} | 角色版本列表
*CharacterApiSub* | [**recommend_character_version**](docs/CharacterApiSub.md#recommend_character_version) | **GET** /v2/api/character/newversion/recommend/{characterId} | 角色版本列表
*CharacterApiSub* | [**recommend_character_version1**](docs/CharacterApiSub.md#recommend_character_version1) | **GET** /v1/api/character/newversion/recommend/{characterId} | 角色版本列表
*CharacterApiSub* | [**search**](docs/CharacterApiSub.md#search) | **POST** /v2/api/character/search | 查询角色
*CharacterApiSub* | [**search1**](docs/CharacterApiSub.md#search1) | **POST** /v1/api/character/search | 查询角色
*CharacterApiSub* | [**update**](docs/CharacterApiSub.md#update) | **PUT** /v2/api/character/update | 更新角色信息
*CharacterApiSub* | [**update1**](docs/CharacterApiSub.md#update1) | **PUT** /v1/api/character/update | 更新角色信息
*ChatApiSub* | [**chat**](docs/ChatApiSub.md#chat) | **POST** /v1/api/chat/send | 用户对话
*ChatApiSub* | [**chat_v2**](docs/ChatApiSub.md#chat_v2) | **POST** /v2/api/chat/send | 用户对话v2
*ChatApiSub* | [**custom_chat**](docs/ChatApiSub.md#custom_chat) | **POST** /v2/api/chat/generate | 用户对话
*ChatApiSub* | [**custom_chat1**](docs/ChatApiSub.md#custom_chat1) | **POST** /v1/api/chat/generate | 用户对话
*ChatMessageApiSub* | [**chat_histories**](docs/ChatMessageApiSub.md#chat_histories) | **POST** /v1/api/chat/message/histories | 对话历史
*ChatMessageApiSub* | [**chat_histories1**](docs/ChatMessageApiSub.md#chat_histories1) | **POST** /v2/api/chat/message/histories | 对话历史
*ChatMessageApiSub* | [**chat_histories2**](docs/ChatMessageApiSub.md#chat_histories2) | **GET** /v1/api/chat/history/{characterId} | 对话历史
*ChatMessageApiSub* | [**chat_histories3**](docs/ChatMessageApiSub.md#chat_histories3) | **GET** /v2/api/chat/history/{characterId} | 对话历史
*ChatMessageApiSub* | [**rate_message**](docs/ChatMessageApiSub.md#rate_message) | **POST** /v2/api/chat/rating | 消息评分
*ChatMessageApiSub* | [**rate_message1**](docs/ChatMessageApiSub.md#rate_message1) | **POST** /v1/api/chat/rating | 消息评分
*ChatMessageApiSub* | [**sys_reminder**](docs/ChatMessageApiSub.md#sys_reminder) | **POST** /v1/api/chat/reminder | 
*ChatMessageApiSub* | [**sys_reminder1**](docs/ChatMessageApiSub.md#sys_reminder1) | **POST** /v2/api/chat/reminder | 


## 请求/响应参数对象

 - [AdvancedSettings](docs/AdvancedSettings.md)
 - [BaseChatRequest](docs/BaseChatRequest.md)
 - [BaseChatRequestAcaChatExtParam](docs/BaseChatRequestAcaChatExtParam.md)
 - [CharacterAdvancedConfig](docs/CharacterAdvancedConfig.md)
 - [CharacterCreateDTO](docs/CharacterCreateDTO.md)
 - [CharacterDTO](docs/CharacterDTO.md)
 - [CharacterKey](docs/CharacterKey.md)
 - [CharacterPermissionConfig](docs/CharacterPermissionConfig.md)
 - [CharacterQueryDTO](docs/CharacterQueryDTO.md)
 - [CharacterQueryWhere](docs/CharacterQueryWhere.md)
 - [CharacterUpdateDTO](docs/CharacterUpdateDTO.md)
 - [CharacterVersionCreateOrUpdateDTO](docs/CharacterVersionCreateOrUpdateDTO.md)
 - [ChatHistoryQueryDTO](docs/ChatHistoryQueryDTO.md)
 - [ChatHistoryQueryWhere](docs/ChatHistoryQueryWhere.md)
 - [ChatMessageDTO](docs/ChatMessageDTO.md)
 - [ChatReqParams](docs/ChatReqParams.md)
 - [ChatRoomUserDTO](docs/ChatRoomUserDTO.md)
 - [Context](docs/Context.md)
 - [FileInfoVO](docs/FileInfoVO.md)
 - [GatewayContext](docs/GatewayContext.md)
 - [GatewayIssuedParams](docs/GatewayIssuedParams.md)
 - [Input](docs/Input.md)
 - [Message](docs/Message.md)
 - [MessageRatingRequest](docs/MessageRatingRequest.md)
 - [Meta](docs/Meta.md)
 - [ModelParameter](docs/ModelParameter.md)
 - [ModelParameters](docs/ModelParameters.md)
 - [PageResultCharacterDTO](docs/PageResultCharacterDTO.md)
 - [PageResultChatMessageDTO](docs/PageResultChatMessageDTO.md)
 - [Repository](docs/Repository.md)
 - [RepositoryInfo](docs/RepositoryInfo.md)
 - [ResultDTOBoolean](docs/ResultDTOBoolean.md)
 - [ResultDTOCharacterDTO](docs/ResultDTOCharacterDTO.md)
 - [ResultDTOCharacterKey](docs/ResultDTOCharacterKey.md)
 - [ResultDTOListCharacterDTO](docs/ResultDTOListCharacterDTO.md)
 - [ResultDTOPageResultCharacterDTO](docs/ResultDTOPageResultCharacterDTO.md)
 - [ResultDTOPageResultChatMessageDTO](docs/ResultDTOPageResultChatMessageDTO.md)
 - [Scenario](docs/Scenario.md)
 - [SysReminderRequest](docs/SysReminderRequest.md)
 - [UserProfile](docs/UserProfile.md)

# 打包与发布

## 打包

```shell
# 安装打包工具
python3 -m pip install --user --upgrade setuptools wheel

# 打包命令，以下会在dist目录下生成一个tar.gz的源码包和一个.whl的Wheel包
python3 setup.py sdist bdist_wheel
```

## 发布

可将包发布到内网和外网PyPI仓库，往外发发布前需要走[数据对外披露流程](https://df.alibaba-inc.com/#/pia/lc)。

### 内网发布

1. 获取上传key
登陆：https://opsx.alibaba-inc.com/web/scm/package/pypi, 点击获取获取上传密钥获取key

2. 配置~/.pypirc
```shell
[distutils]
index-servers = aliyun-pypi

[aliyun-pypi]
repository: http://opsx.vip.tbsite.net/aliyun-pypi/simple/
username: xxx #第一步获取的账号
password: xxx #第一步获取的密钥
```

3. 上传

```commandline
twine check $pkg_path  # 上传前检查
twine upload -r aliyun-pypi $pkg_path --verbose # 上传
```

4. 查看包上传情况
查看 http://yum.tbsite.net/aliyun-pypi/simple/{{package_name}} 进行查看
在页面 https://opsx.alibaba-inc.com/web/scm/package/pypi 搜索包名进行查看

### 外网发布
1. 注册[PyPI](https://pypi.org/account/register/)账号
2. 通过账号绑定邮件进行账号激活
3. 激活2FA，通过安装 Authenticator 应用，扫描TOTP二维码，生成6位验证码，通过该验证码可以激活2FA
4. 生成 API TOKEN
5. 配置 ～/.pypirc
```shell
[distutils]
index-servers = pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__ 
password = pypi-xxx #步骤4生成到API TOKEN
```
6. 发布
```commandline
twine upload dist/*
```

7. 验证
```commandline
pip install {包名}=={版本名} -i https://www.pypi.org/simple/
```

## 版本变更

### 1.0.9
- 对话接口，添加重新生成逻辑，相关参数 `chat_req_params.context`
- 对话接口，添加是否使用平台对话历史 `chat_req_params.context.use_chat_history_`
- 对话接口，添加function call逻辑，参数 `chat_req_params.functions`
- 新增重置对话接口，`ChatMessageApiSub.reset_chat_history`

### 1.0.8
- 对话接口，模型设置添加增量输出开关 `parameters.incrementalOutput`

### 1.0.7
- 添加助手类对话接口，对话请求添加 `type=assistant` 配置

### 1.0.6
- 对话请求头参数添加 X-AcA-SSE=enable/disable 来开启/关闭SSE对话

### 1.0.5
- 支持自定义角色对话

### 1.0.1
- 请求host切换到大模型网关 `https://nlp.aliyuncs.com`

### 1.0.0
- 支持对色对话（流式、非流式）
- 支持角色管理
- 支持对话历史查询、消息评价和系统消息推送