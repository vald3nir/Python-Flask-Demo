from src.apis.responses import response_failed, response_success
from src.apis.utils.translator import translate_text


def response_password_wrong(language):
    return response_failed({'message': translate_text('password wrong', language)})


def response_password_updated(language):
    return response_success({'message': translate_text('password updated', language)})
