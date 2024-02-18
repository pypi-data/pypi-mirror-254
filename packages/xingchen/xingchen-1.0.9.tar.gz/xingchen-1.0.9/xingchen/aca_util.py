from xingchen.models import ChatReqParams, BaseChatRequestAcaChatExtParam, Input

api_router_map = {
    '/v2/api/chat/send': 'aca-chat-send',
    '/v2/api/character/create': 'aca-character-create',
    '/v2/api/character/update': 'aca-character-update',
    '/v2/api/character/details': 'aca-character-details',
    '/v2/api/character/delete': 'aca-character-delete',
    '/v2/api/character/search': 'aca-character-search',
    '/v2/api/character/createOrUpdateVersion': 'aca-character-version-mgmt',
    '/v2/api/character/versions': 'aca-character-versions',
    '/v2/api/character/newversion/recommend': 'aca-character-version-recommend',
    '/v2/api/chat/message/histories': 'aca-message-history',
    '/v2/api/chat/rating': 'aca-message-rating',
    '/v2/api/chat/reminder': 'aca-chat-reminder',
    '/v2/api/chat/reset': 'aca-chat-reset',
}


def get_service_router(path, async_req):
    if not path:
        return None
    if path.__eq__('/v2/api/chat/send') and async_req:
        return 'aca-chat-send-sse'
    return api_router_map.get(path)


def convert_chat_params(chat_req_params: ChatReqParams):
    bot_profile = chat_req_params.bot_profile
    parameters = chat_req_params.model_parameters
    user_profile = chat_req_params.user_profile
    scenario = chat_req_params.scenario
    messages = chat_req_params.messages
    sample_messages = chat_req_params.sample_messages
    model_name = parameters.model_name if parameters is not None else None
    functions = chat_req_params.functions
    plugins = chat_req_params.plugins
    function_choice = chat_req_params.function_choice
    context = chat_req_params.context

    aca = {
        'botProfile': bot_profile,
        'userProfile': user_profile,
        'sampleMessages': sample_messages,
        'scenario': scenario,
        'functionList': functions,
        'pluginList': plugins,
        'functionChoice': function_choice,
        'context': context
    }

    return BaseChatRequestAcaChatExtParam(
        model=model_name,
        input=Input(
            prompt='|<system>|',
            messages=messages,
            aca=aca
        ),
        parameters=parameters
    )
