from textblob import TextBlob


def translate_text(message, language="en"):
    if not language or language == "en":
        return message
    return str(TextBlob(message).translate(to=language))
