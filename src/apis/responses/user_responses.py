from src.apis.responses import response_success, response_failed
from src.apis.utils.translator import translate_text


def response_user_created(language):
    return response_success({'message': translate_text('user created', language)})


def response_new_user_created(language):
    return response_success({'message': translate_text('user created successfully', language)})


def response_user_updated(language):
    return response_success({'message': translate_text('user updated successfully', language)})


def response_user_not_found(language):
    return response_failed({'message': translate_text('user not found', language)})


def response_list_all_users(users):
    return response_success({"users": users})


def response_user_api_fail(language):
    return response_failed({'message': translate_text('user api failed', language)})
