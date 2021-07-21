# coding=utf-8
# !/usr/bin/python3

from textblob import TextBlob


def translate(message, language):
    if language is None:
        return message
    return str(TextBlob(message).translate(to=language))
